from flask import render_template
from app import app
from .request import get_news
from .request import get_news, get_news_articles
# Views

@app.route('/')
def index():
    '''
    function that returns the index page and its data 
    '''
    #Get popular news
    general_news = get_news('general')
    sports_news = get_news('sports')
    entertainment_news = get_news('entertainment')
    health_news = get_news('health')
    business_news = get_news('business')
    tech_news = get_news('technology')
    science_news = get_news('science')
    
    
    
    title = 'Your Trusted News Sources'
    return render_template('index.html', title = title, general = general_news, sports = sports_news, entertainment = entertainment_news,   health = health_news, business = business_news, technology = tech_news, science = science_news)

@app.route('/articles/<id>')
def articles(id):
    '''
    View article function that returns the articles in a source
    '''
    articles = get_news_articles(id)
    return render_template('articles.html', id = id, articles = articles)