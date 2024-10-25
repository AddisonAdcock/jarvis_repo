Sure, here is a simple example of how you might access a news API using Python. This example uses the Requests library to access the News API:

```python
import requests
import json

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=your_api_key"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]
    for news in articles:
        print(news["title"])

get_news()
```
Please replace "your_api_key" with your actual News API key.