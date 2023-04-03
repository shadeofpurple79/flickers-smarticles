import json
import requests

# category: entertainmewnt - film, 20 questions, multiple choice, from opentdb api
api_url = "https://opentdb.com/api.php?amount=20&category=11&type=multiple"

# get data from the API
response = requests.get(api_url)
data = json.loads(response.text)

# create variable to store quiz questions
questions = data["results"]
