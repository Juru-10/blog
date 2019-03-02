import urllib.request,json
from .models import Quote

# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url,arti_url
    base_url = app.config['NEWS_API_BASE_URL']

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_news_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        results = None

        if get_response['quotes']:
            results_list = get_news_response['quotes']
            results = process_results(results_list)


    return results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        language = news_item.get('language')
        country = news_item.get('country')

        if id:
            news_object = News(id,name,description,url,language,country)
            news_results.append(news_object)

    return news_results

def get_newsd(name):
    '''
    Function that gets the json response to our url request
    '''
    get_arti_url = 'https://newsapi.org/v2/everything?sources={}&apiKey=d51bd896c92448e786bb80dc54e08fca'.format(name)
    print(get_arti_url)
    with urllib.request.urlopen(get_arti_url) as url:
        get_arti_data = url.read()
        get_arti_response = json.loads(get_arti_data)

        arti_results_list = None
        # arti_results = None

        if get_arti_response['articles']:
            arti_results_list = process_arti(get_arti_response['articles'])
            # arti_results_list
        print(arti_results_list)

        return arti_results_list

def process_arti(arti_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        arti_list: A list of dictionaries that contain articles details

    Returns :
        arti_results: A list of articles objects
    '''
    arti_results = []

    for arti_item in arti_list:
        id = arti_item.get('id')
        source = arti_item.get('source')
        title = arti_item.get('title')
        poster = arti_item.get('urlToImage')
        description = arti_item.get('description')
        publishedAt = arti_item.get('publishedAt')
        content = arti_item.get('content')
        url = arti_item.get('url')

        # if poster:
        arti_object = Arti(id,source,title,poster,description,publishedAt,content,url)
        arti_results.append(arti_object)

    return arti_results


def search_news(news_title):
    search_news_url = 'https://newsapi.org/v2/sources?category&apiKey={}&query={}'.format(api_key,news_title)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)

    return search_news_results
