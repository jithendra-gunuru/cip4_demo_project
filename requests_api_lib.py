import requests

API_KEY = ""
API_BASE_URL = ""

def search_articles(search_term):
    params = {
        "q" : search_term,
        "api-key": API_KEY
    }
    response = requests.get(API_BASE_URL, params)
    return response.json()

def display_results(search_results):
    #print(search_results)
    docs = search_results["response"]["docs"]
    for doc in docs:
        articles_web_url = doc["web_url"]
        articles_headline= doc["headline"]["main"]
        print(articles_headline + "(" + articles_web_url + ")")

while True:
    search_term = input("your search term: ")
    search_results = search_articles(search_term)
    display_results(search_results)
    print("")                                                                 