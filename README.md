# Deployment Instructions

## Local Development:
1. Create virtual environment: `python -m venv venv`
2. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Create templates folder and add index.html
5. Run: `python app.py`

## Heroku Deployment:
1. Create Procfile: `web: gunicorn app:app`
2. git init && git add . && git commit -m "Initial commit"
3. heroku create your-app-name
4. git push heroku main

## Docker Deployment:
# Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

## Features Included:

### Core Functionality:
✅ Enhanced Hacker News scraper (based on your original code)
✅ Generic website scraper with configurable CSS selectors
✅ Real-time data preview in table format
✅ Pandas DataFrame integration for data processing
✅ Export functionality (CSV, JSON)
✅ Modern, responsive UI with glass morphism design
✅ Error handling and loading states

### Advanced Features:
✅ Dynamic configuration based on scrape type
✅ CSS selector validation and helpers
✅ Data summarization and statistics
✅ Pagination for large datasets
✅ Mobile-responsive design
✅ Real-time feedback and progress indicators

### Configuration Options for Users:
- Hacker News: Pages to scrape, minimum vote threshold
- Generic sites: URL, max items, custom CSS selectors for any data field
- Export formats and download functionality
- Real-time data preview with search and filtering

### Technical Features:
- Session management for data persistence
- Rate limiting and error recovery
- Robust error handling
- Modern async/await patterns
- Responsive design with Tailwind CSS
- Alpine.js for reactive UI components