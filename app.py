import requests
import time
import xml.etree.ElementTree as ET
from flask import Flask, render_template

app = Flask(__name__)

# Set the RSS feed URL
url = 'https://archives.nseindia.com/content/RSS/Corporate_action.xml'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

@app.route('/')
def index():
    
    response = requests.get(url, headers=headers)
    time.sleep(10)
    xml_content = response.content
    root = ET.fromstring(xml_content)
    
    filtered_items = []
    items = root.findall('.//item')
    keyword = 'DIVIDEND'
    
    # Filtering to only include dividend as corporate action
    
    for item in items:
        description = item.find('description').text
        if keyword in description:
            title = item.find('title').text
            filtered_items.append((title.replace('\n',''), description))

    # Render the template with the feed items
    return render_template('index.html', feed_items=filtered_items)

if __name__ == '__main__':  
   app.run()
