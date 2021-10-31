class News:
    '''
    News class that defines the news objects
    '''
    
    def __init__(self, id, name, description, url, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.country = country
        