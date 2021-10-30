import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Kanye West Used Cars From Wyoming Going Up for Auction - TMZ','Kanye West former fleet from his Wyoming ranch is on the auction block','"https://imagez.tmz.com/image/5a/16by9/2021/10/28/5af2e450cbf44b55af7195506259d84d_xl.jpg"',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()