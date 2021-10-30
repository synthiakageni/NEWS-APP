from flask import render_template
from app import app
from .request import get_news
from .request import get_news, get_news_articles
# Views
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title)
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    general_news = get_news('general')
    sports_news = get_news('sports')
    entertainment_news = get_news('entertainment')
    health_news = get_news('health')
    business_news = get_news('business')
    tech_news = get_news('technology')
    science_news = get_news('science')
    title = 'Welcome to the best News website'
    return render_template('index.html', title = title, general = general_news, sports = sports_news, entertainment = entertainment_news,   health = health_news, business = business_news, technology = tech_news, science = science_news)

    
