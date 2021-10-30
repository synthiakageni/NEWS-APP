from app import app
import urllib.request,json
from .models import news,articles


News = news.News

# Getting api key
apiKey = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        country = news_item.get('country')
        vote_count = news_item.get('vote_count')

        if url:
            news_object = News( id, name, description, url, country,vote_count)
            news_results.append(news_object)
        
    return news_results  
def get_news_articles(id):
    get_news_articles_url = base_url.format(id, apiKey)
    
    with urllib.request.urlopen(get_news_articles_url ) as url:
        news_articles_data = url.read()
        news_articles_response = json.loads(news_articles_data)
        
        articles_results = None
        if news_articles_response['articles']:
            articles_results_list = news_articles_response['articles']
            articles_results = process_articles(articles_results_list)
            
    return articles_results   
 
def process_articles(articles_list):
    '''
    method for processing the response
    '''
    articles_results = []
    for article_item in articles_list:
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item['description']
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
            # (self, title, description, urlToImage, publishedAt, author, url):
            if urlToImage:
                articles_object = articles(title, description, urlToImage, publishedAt, author,url)
                articles_results.append(articles_object)
            
    return articles_results
                    