import requests
import json
import urllib.parse
import os 
from dotenv import load_dotenv
import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

load_dotenv()
COVID_API_KEY = os.environ['COVID_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']


with open('states.json') as fp:
    SUPPORTED_STATES = json.load(fp)

def fetch_stats(county=None, state=None):
    if state:
        url = f"https://api.covidactnow.org/v2/states.json?apiKey={COVID_API_KEY}"
        r = requests.get(url)
        data = r.json()
        state = get_state_code(state)
        if state:
            for i in data:
                if state.lower() in i["state"].lower():
                    return i
    else:
        url = f"https://api.covidactnow.org/v2/counties.json?apiKey={COVID_API_KEY}"
        r = requests.get(url)
        data = r.json()
        for i in data:
            if county.lower() in i["county"].lower():
                return i
    return {}


def get_state_code(state):
    for key, value in SUPPORTED_STATES.items():
        if state in value.lower():
            return key 
    return ''

def get_stats(data):
    doc = nlp(data)
    location = ''
    for X in doc.ents:
        if X.label_ == 'GPE':
            location = X.text 
            break 
    if location == '':
        return 'Please enter the state or county of USA you want statistics of. '
    
    state_code = get_state_code(location)
    if state_code == '':
        stats_data = fetch_stats(county=location)
    else:
        stats_data = fetch_stats(state=location)
    
    if stats_data:
        location_name = location
        confirmed = stats_data["actuals"]['cases'] if stats_data["actuals"]['cases'] else 'N/A'
        deaths = stats_data["actuals"]['deaths'] if  stats_data["actuals"]['deaths'] else 'N/A'
        new_cases = stats_data["actuals"]['newCases'] if stats_data["actuals"]['newCases'] else 'N/A'
        vacc_completed = stats_data['actuals']['vaccinationsCompleted'] if stats_data['actuals']['vaccinationsCompleted'] else 'N/A'
        source = stats_data['annotations']['cases']['sources'][0] if stats_data['annotations']['cases']['sources'][0] else 'N/A'
    
        result =(f"For location {location_name}, here are the stats:\n\n"
            f"- total cases confirmed: {confirmed}\n"
            f"- total deaths: {deaths}\n"
            f"- new cases: {new_cases}\n"
            f"- vaccinations completed: {vacc_completed}\n"
            f"- source: {source}\n")
    
    else:
        result=  'Please enter the state or county of USA you want statistics of. '

    return result


def fetch_news():
    url = "http://newsapi.org/v2/top-headlines"
    payload = {
        "apiKey": NEWS_API_KEY,
        "country": "US",
        "q": "covid",
    }
    response = requests.get(url, params=payload)

    return response.json().get("articles", [])

def get_news(data):
    news_data = fetch_news()[:3]
    result = [f"Here are the top 3 news articles on covid: "]
    result += [(f"Title: {i.get('title', 'No title?. Report this.')}\n\n"
                f"Link: {i.get('url', 'No URL?. Report this.')}") 
                for i in news_data]
    
    return result

def regulations(data):
    doc = nlp(data)
    location = ''
    for X in doc.ents:
        if X.label_ == 'GPE':
            location = X.text 
            break 
    return f'You can find your location specific regulations here:\n https://www.google.com/search?q=covid+regulations+{location}'

    
# print(get_stats('stats of washington state'))

# print(get_news('give me covid news'))