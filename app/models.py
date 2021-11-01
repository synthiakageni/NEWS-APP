class News:
    '''
    News class that defines the news objects
    '''
    
    def h(self, id, name, description, url, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.country = country
class Articles:
    '''
    class that defines the behaviour of the articles
    '''
    def __init__(self, title, description, urlToImage, publishedAt, author, url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.author = author
        self.url = url        
                   