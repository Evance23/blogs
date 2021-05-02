import urllib.request,json
import requests
import .models import Blog

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config["QUOTES_API_BASE_URL"]

    

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/quotes/41')
    if response.status_code == 200:
        quote = response.json()
        return quote
