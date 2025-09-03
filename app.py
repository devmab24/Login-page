from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, session, send_file
from bs4 import BeautifulSoup
import pandas as pd
import json
import io
import csv
from urllib.parse import urljoin, urlparse
import re
from datetime import datetime
import logging

import requests

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def scrape_hacker_news(self, pages=2, min_votes=99):
        """Enhanced Hacker News scraper based on your original code"""
        all_links = []
        all_subtext = []
        
        for page in range(1, pages + 1):
            try:
                if page == 1:
                    url = 'https://news.ycombinator.com/news'
                else:
                    url = f'https://news.ycombinator.com/news?p={page}'
                
                res = self.session.get(url, timeout=10)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, 'html.parser')
                
                links = soup.select('.titleline > a')
                subtext = soup.select('.subtext')
                
                all_links.extend(links)
                all_subtext.extend(subtext)
                
            except Exception as e:
                logger.error(f"Error scraping page {page}: {str(e)}")
                continue
        
        return self.create_custom_hn(all_links, all_subtext, min_votes)
    
    def create_custom_hn(self, links, subtext, min_votes):
        """Process Hacker News data"""
        hn = []
        for idx, item in enumerate(links):
            if idx >= len(subtext):
                break
                
            title = item.getText().strip()
            href = item.get('href', '')
            
            # Make relative URLs absolute
            if href.startswith('item?'):
                href = f'https://news.ycombinator.com/{href}'
            elif not href.startswith('http'):
                href = urljoin('https://news.ycombinator.com/', href)
            
            vote_elem = subtext[idx].select('.score')
            points = 0
            if vote_elem:
                try:
                    points = int(vote_elem[0].getText().replace(' points', '').replace(' point', ''))
                except ValueError:
                    points = 0
            
            comments_elem = subtext[idx].select('a[href*="item?id="]')
            comments = 0
            if comments_elem:
                comment_text = comments_elem[-1].getText()
                if 'comment' in comment_text:
                    try:
                        comments = int(re.findall(r'\d+', comment_text)[0])
                    except (IndexError, ValueError):
                        comments = 0
            
            author_elem = subtext[idx].select('.hnuser')
            author = author_elem[0].getText() if author_elem else 'Unknown'
            
            if points >= min_votes:
                hn.append({
                    'title': title,
                    'link': href,
                    'votes': points,
                    'comments': comments,
                    'author': author,
                    'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
        
        return sorted(hn, key=lambda k: k['votes'], reverse=True)
    
    def scrape_generic_website(self, url, css_selectors, max_items=50):
        """Generic website scraper with configurable CSS selectors"""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            results = []
            elements = soup.select(css_selectors.get('container', 'body'))[:max_items]
            
            for idx, element in enumerate(elements):
                item = {'index': idx + 1}
                
                for field, selector in css_selectors.items():
                    if field == 'container':
                        continue
                    
                    try:
                        if field.endswith('_href'):
                            # Extract href attribute
                            elem = element.select_one(selector)
                            if elem and elem.get('href'):
                                item[field] = urljoin(url, elem.get('href'))
                            else:
                                item[field] = ''
                        else:
                            # Extract text content
                            elem = element.select_one(selector)
                            item[field] = elem.get_text().strip() if elem else ''
                    except Exception as e:
                        item[field] = f'Error: {str(e)}'
                
                item['scraped_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                results.append(item)
            
            return results
            
        except Exception as e:
            raise Exception(f"Failed to scrape {url}: {str(e)}")

scraper = WebScraper()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.get_json()
        scrape_type = data.get('scrape_type', 'hackernews')
        
        if scrape_type == 'hackernews':
            pages = int(data.get('pages', 2))
            min_votes = int(data.get('min_votes', 99))
            
            results = scraper.scrape_hacker_news(pages=pages, min_votes=min_votes)
            
        elif scrape_type == 'generic':
            url = data.get('url')
            css_selectors = data.get('css_selectors', {})
            max_items = int(data.get('max_items', 50))
            
            if not url:
                return jsonify({'error': 'URL is required for generic scraping'}), 400
            
            results = scraper.scrape_generic_website(url, css_selectors, max_items)
        
        else:
            return jsonify({'error': 'Invalid scrape type'}), 400
        
        # Convert to DataFrame for analysis
        df = pd.DataFrame(results)
        
        # Prepare response data
        response_data = {
            'success': True,
            'data': results,
            'total_items': len(results),
            'columns': list(df.columns) if not df.empty else [],
            'summary': {
                'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'total_items': len(results),
                'scrape_type': scrape_type
            }
        }
        
        if scrape_type == 'hackernews' and results:
            response_data['summary'].update({
                'avg_votes': round(sum(item['votes'] for item in results) / len(results), 1),
                'max_votes': max(item['votes'] for item in results),
                'min_votes': min(item['votes'] for item in results)
            })
        
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"Scraping error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/export/<format>')
def export_data(format):
    """Export last scraped data in specified format"""
    try:
        # Get data from session
        results = session.get('last_results', [])
        if not results:
            flash('No data to export. Please scrape some data first.', 'error')
            return redirect(url_for('index'))
        
        df = pd.DataFrame(results)
        
        if format == 'csv':
            output = io.StringIO()
            df.to_csv(output, index=False)
            output.seek(0)
            
            return send_file(
                io.BytesIO(output.getvalue().encode()),
                mimetype='text/csv',
                as_attachment=True,
                download_name=f'scraped_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
            )
        
        elif format == 'json':
            output = io.StringIO()
            df.to_json(output, orient='records', indent=2)
            output.seek(0)
            
            return send_file(
                io.BytesIO(output.getvalue().encode()),
                mimetype='application/json',
                as_attachment=True,
                download_name=f'scraped_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            )
        
        else:
            flash('Unsupported export format', 'error')
            return redirect(url_for('index'))
            
    except Exception as e:
        flash(f'Export failed: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)