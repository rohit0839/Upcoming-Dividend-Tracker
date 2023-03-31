from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
   
    # Set the RSS feed URL
    rss_url = 'https://feeds.feedburner.com/nseindia/ca'
    
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)
    
    # Filtering to include only dividend corporate actions
    keyword = 'DIVIDEND'
    filtered_items = []
    for item in feed.entries:
        if keyword in item.description.upper():
            filtered_items.append(item)

    # Render the template with the feed items
    return render_template('index.html', feed_items=filtered_items)

if __name__ == '__main__':  
   app.run()
