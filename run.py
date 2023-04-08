import json
import requests

# category: entertainmewnt - film, 20 questions, multiple choice, from opentdb api
api_url = "https://opentdb.com/api.php?amount=20&category=11&type=multiple"

# get data from the API
response = requests.get(api_url)
data = json.loads(response.text)

# create variable to store quiz questions
questions = data["results"]

print(data)

# show game intro at the start

# get 20 random questions 
# get the answer options
# get the correct answer for each question

# question number is zero
# score is zero

# function to ask question 
    # from 1 to 20
    # select 1 random question
    # show the selected question, 4 answer options
    # increase question number by 1 out of 20
    # ask player to input their answer
        # function to validate answer
            # while input is not A or B or C or D; and a or b or c or d
            # print message invalid answer, enter A B C D, ask for input
            # when input is A or B or C or D; and a or b or c or d; go to unfciont to check answer

# function to check answer
    # 
