from flask import Flask, request, jsonify
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Using an in-memory cache to optimize API performance and costs
translation_cache = {}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    
    # Simple, efficient caching logic
    cache_key = f"{data['source']}_{data['target']}_{text}"
    if cache_key in translation_cache:
        return jsonify({'result': translation_cache[cache_key]})

    # External API Call logic
    payload = {'q': text, 'source': data['source'], 'target': data['target'], 'key': os.getenv('API_KEY')}
    response = requests.post('https://translation.googleapis.com/language/translate/v2', data=payload)
    
    if response.status_code == 200:
        result = response.json()['data']['translations'][0]['translatedText']
        translation_cache[cache_key] = result
        return jsonify({'result': result})
    return jsonify({'error': 'Service Unavailable'}), 500

if __name__ == '__main__':
    app.run(port=5000)