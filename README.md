# Flask Web Scraper 🕷️

A powerful, user-friendly web scraping application built with Flask that allows you to extract data from websites with ease. Features both specialized Hacker News scraping and generic website scraping with customizable CSS selectors.

![Flask Web Scraper](https://img.shields.io/badge/Flask-2.3.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### Core Functionality
- **🔥 Hacker News Scraper**: Enhanced scraper based on original code with vote filtering
- **🌐 Generic Website Scraper**: Configurable CSS selectors for any website
- **📊 Real-time Data Preview**: Interactive table format with pagination
- **🐼 Pandas Integration**: Advanced data processing capabilities
- **📁 Export Options**: CSV and JSON export functionality
- **💎 Modern UI**: Glass morphism design with responsive layout
- **⚡ Real-time Feedback**: Loading states and progress indicators

### Advanced Features
- **🎯 Dynamic Configuration**: Adapts based on scraping type
- **✅ CSS Selector Validation**: Built-in helpers and validation
- **📈 Data Analysis**: Automatic summarization and statistics
- **📱 Mobile Responsive**: Works seamlessly on all devices
- **🔄 Session Management**: Persistent data for exports
- **🛡️ Error Handling**: Robust error recovery and user feedback
- **🎨 Interactive Elements**: Hover effects and smooth animations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-web-scraper.git
   cd flask-web-scraper
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/macOS
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create templates folder** (if not present)
   ```bash
   mkdir templates
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
Flask==2.3.0
requests==2.31.0
beautifulsoup4==4.12.0
pandas==2.0.0
lxml==4.9.0
gunicorn==20.1.0
```

## 🎯 Usage Guide

### Hacker News Scraping

1. **Select Hacker News mode** (default)
2. **Configure parameters:**
   - **Pages**: Number of pages to scrape (1-10)
   - **Minimum Votes**: Filter stories below vote threshold
3. **Click "Start Scraping"**
4. **View results** in the interactive table
5. **Export data** as CSV or JSON

**Example Output:**
```json
{
  "title": "Revolutionary AI Breakthrough",
  "link": "https://example.com/article",
  "votes": 250,
  "comments": 45,
  "author": "tech_user",
  "scraped_at": "2024-01-15 10:30:45"
}
```

### Generic Website Scraping

1. **Select "Custom Website" mode**
2. **Enter target URL**
3. **Configure CSS selectors:**
   - **Container**: Main wrapper for each item (e.g., `.article`, `.post`)
   - **Title**: Article title selector (e.g., `h2`, `.headline`)
   - **Link**: URL selector (href will be extracted)
   - **Description**: Summary/excerpt selector
   - **Custom Fields**: Add any additional fields

4. **Set maximum items** to scrape
5. **Click "Start Scraping"**
6. **Review and export results**

**CSS Selector Examples:**
```css
/* Container */
.article, .post, div.item

/* Title */
h1, h2, .title, .headline

/* Links */
a.read-more, .post-link

/* Content */
.summary, .excerpt, p.description
```

## 🏗️ Project Structure

```
flask-web-scraper/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore           # Git ignore rules
├── Procfile             # Heroku deployment config
├── Dockerfile           # Docker configuration
│
├── templates/
│   └── index.html       # Main HTML template
│
└── static/              # Static assets (if any)
    ├── css/
    ├── js/
    └── images/
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file for configuration:

```env
SECRET_KEY=your-super-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True
```

### Scraper Settings

Modify these constants in `app.py`:

```python
# Default settings
DEFAULT_PAGES = 2
DEFAULT_MIN_VOTES = 99
DEFAULT_MAX_ITEMS = 50
REQUEST_TIMEOUT = 15
MAX_PAGES = 10
```

## 🚀 Deployment

### Heroku Deployment

1. **Create Procfile:**
   ```
   web: gunicorn app:app
   ```

2. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Docker Deployment

1. **Build image:**
   ```bash
   docker build -t flask-scraper .
   ```

2. **Run container:**
   ```bash
   docker run -p 5000:5000 flask-scraper
   ```

### Traditional Server

Use any WSGI server like Gunicorn:
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## 🛠️ API Reference

### Scraping Endpoint

**POST** `/scrape`

**Request Body:**
```json
{
  "scrape_type": "hackernews|generic",
  "pages": 2,
  "min_votes": 99,
  "url": "https://example.com",
  "max_items": 50,
  "css_selectors": {
    "container": ".article",
    "title": "h2",
    "link_href": "a"
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": [...],
  "total_items": 25,
  "columns": ["title", "link", "votes"],
  "summary": {
    "scraped_at": "2024-01-15 10:30:45",
    "total_items": 25,
    "scrape_type": "hackernews"
  }
}
```

### Export Endpoints

- **GET** `/export/csv` - Download CSV format
- **GET** `/export/json` - Download JSON format

## 🧪 Testing

### Manual Testing Checklist

- [ ] Hacker News scraping with different vote thresholds
- [ ] Generic website scraping with various selectors
- [ ] CSV export functionality
- [ ] JSON export functionality
- [ ] Mobile responsiveness
- [ ] Error handling (invalid URLs, network issues)
- [ ] Large dataset handling

### Test Sites for Generic Scraping

1. **News Sites**: BBC, Reuters, TechCrunch
2. **Blogs**: Medium articles, WordPress sites
3. **E-commerce**: Product listings (respect robots.txt)
4. **Forums**: Reddit, Stack Overflow

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

1. **Fork the repository**
2. **Create feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make changes and test thoroughly**
4. **Commit with clear messages:**
   ```bash
   git commit -m "Add: New CSS selector validation"
   ```

5. **Push to branch:**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Create Pull Request**

### Contribution Guidelines

- **Code Style**: Follow PEP 8 for Python, use meaningful variable names
- **Documentation**: Update README and add docstrings
- **Testing**: Test your changes thoroughly
- **Security**: Never commit secrets or API keys

### Areas for Contribution

#### 🎯 High Priority
- [ ] Unit tests with pytest
- [ ] Rate limiting and request throttling
- [ ] Database storage for scraped data
- [ ] User authentication and personal dashboards
- [ ] Scheduled scraping with cron jobs

#### 🔧 Medium Priority
- [ ] Support for JavaScript-rendered sites (Selenium)
- [ ] Advanced filtering and search functionality
- [ ] Data visualization with charts
- [ ] API documentation with Swagger
- [ ] Webhook notifications

#### 🎨 Enhancement Ideas
- [ ] Dark/light theme toggle
- [ ] Scraping templates for popular sites
- [ ] Bulk URL processing
- [ ] Data comparison between scrapes
- [ ] Browser extension for quick scraping

### Bug Reports

When reporting bugs, include:

1. **Environment details** (OS, Python version, browser)
2. **Steps to reproduce**
3. **Expected vs actual behavior**
4. **Screenshots** (if applicable)
5. **Error logs/console output**

## 📚 Advanced Usage

### Custom CSS Selectors Guide

#### Basic Selectors
```css
/* Element */
div, p, h1

/* Class */
.article, .post, .content

/* ID */
#main-content

/* Attribute */
[data-testid="article"]
```

#### Advanced Selectors
```css
/* Descendant */
.article p

/* Child */
.article > h2

/* Nth-child */
.post:nth-child(2)

/* Contains text */
a[href*="article"]
```

### Handling Dynamic Content

For sites with JavaScript-rendered content, consider:

1. **Selenium WebDriver** integration
2. **Requests-HTML** for basic JS support
3. **API endpoints** if available

### Performance Optimization

1. **Use session reuse** for multiple requests
2. **Implement caching** for repeated scrapes
3. **Add delays** to respect server load
4. **Use connection pooling**

## 🐛 Troubleshooting

### Common Issues

**Issue**: "Connection timeout"
**Solution**: Check internet connection, try different user agent

**Issue**: "No data found"
**Solution**: Verify CSS selectors with browser dev tools

**Issue**: "Template error with integers"
**Solution**: This is fixed in the latest version

**Issue**: "Export not working"
**Solution**: Ensure you've scraped data first

### Debug Mode

Enable debug mode for detailed error messages:
```python
app.run(debug=True)
```

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 Flask Web Scraper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- **Beautiful Soup** for HTML parsing
- **Flask** for the web framework
- **Pandas** for data manipulation
- **Bootstrap** for responsive design
- **Font Awesome** for icons
- **Hacker News** for inspiration

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/flask-web-scraper/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/flask-web-scraper/discussions)
- **Email**: your.email@example.com

## 🔮 Roadmap

### Version 2.0 (Planned)
- [ ] User authentication system
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] RESTful API with authentication
- [ ] Scheduling system for automated scraping
- [ ] Advanced data visualization

### Version 2.5 (Future)
- [ ] Machine learning for content extraction
- [ ] Multi-language support
- [ ] Cloud deployment templates (AWS, GCP, Azure)
- [ ] Performance monitoring dashboard

---

**⭐ Star this repository if it helped you!**

**🔄 Fork it to contribute or customize for your needs**

Built with ❤️ by the community