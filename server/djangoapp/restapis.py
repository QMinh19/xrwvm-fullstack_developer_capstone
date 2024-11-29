# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    """
    Sends a GET request to the specified endpoint with optional query parameters.
    """
    params = urlencode(kwargs)  # Properly encode parameters
    request_url = f"{backend_url}{endpoint}?{params}" if params else f"{backend_url}{endpoint}"
    print(f"GET from {request_url}")

    try:
        # Call the GET method of the requests library
        response = requests.get(request_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()  # Return the parsed JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request: {e}")
        return None
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
def post_review(data_dict):
# Add code for posting review
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")