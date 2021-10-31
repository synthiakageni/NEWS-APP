from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news
from .request import get_news, get_news_articles,search_article
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
    
    title = 'Home - Welcome to The best News Website Online'

    search_article = request.args.get('news_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
     return render_template('index.html', title = title, general = general_news, sports = sports_news, entertainment = entertainment_news,   health = health_news, business = business_news, technology = tech_news, science = science_news)

@app.route('/articles/<id>')
def articles(id):
    '''
    View article function that returns the articles in a source
    '''
    articles = get_news_articles(id)
    return render_template('articles.html', id = id, articles = articles)
@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',article = searched_articles)
   