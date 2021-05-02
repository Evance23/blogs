import requests,json

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/quotes/41')
    if response.status_code == 200:
        quote = response.json()
        return quote
