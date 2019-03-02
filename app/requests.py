import urllib.request,json
from .models import Quote

# Getting the news base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url ='http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_news_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        # results = None
        #
        # if get_response['quotes']:
        #     results_list = get_news_response['quotes']
        #     results = process_results(results_list)
        return get_response

# def process_results(quotes_list):
#     '''
#     Function  that processes the news result and transform them to a list of Objects
#
#     Args:
#         news_list: A list of dictionaries that contain news details
#
#     Returns :
#         news_results: A list of news objects
#     '''
#     quotes_results = []
#     for quote in quotes_list:
#         id = quote.get('id')
#         author = quote.get('author')
#         quote = quote.get('quote')
#         permalink = quote.get('permalink')
#
#         if id:
#             quotes_object = Quote(id,author,quote,permalink)
#             quotes_results.append(quotes_object)
#
#     return quotes_results
