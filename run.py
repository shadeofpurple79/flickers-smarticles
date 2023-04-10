import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) #return to default colour after each time

import json
import requests #Make a request to a web page, and print the response text

# from opentdb api, category: entertainment - film, 20 questions, multiple choice
API_URL = "https://opentdb.com/api.php?amount=20&category=11&type=multiple"

# get data from the API
response = requests.get(API_URL)
data = json.loads(response.text)

# create variable to store quiz questions
questions = data["results"]

# print(data)

correct_answers = 0 #score is zero at the start, score equals number of correct answers
for question in questions: #for each question in the random 20 questions in the api
    print(Style.BRIGHT + Back.MAGENTA + question["question"].replace("&quot;", "'").replace("&#039;", "'")) #print a random question to the player, remove ugly text that comes in from the api for apostrophes
    print("Select your answer from the following 4 options:") #print the answers for the question to the player
    for i in range(len(question["incorrect_answers"])): #len() function returns the number of items in an object, 20 questions, 
        print(f"{i+1}. {question['incorrect_answers'][i]}")
    print(f"{len(question['incorrect_answers'])+1}. {question['correct_answer']}")
    # user_answer = ""
    user_answer = int(input("What\'s your answer? Select 1,2,3 or 4: ")) #player selects an answer: 1,2,3, or 4 for each question
    # while not (user_answer == 1 or user_answer == 2 or user_answer == 3 or user_answer == 4):
        # user_answer = int(input("You can only enter 1, 2, 3 or 4. Try again: "))
    if user_answer == len(question["incorrect_answers"]) + 1:
        print(Fore.GREEN + "Correct, well done!\n\n")
        correct_answers += 1 #increase score by 1 for each correct answer
    else:
        print(Fore.RED + "Sorry, incorrect.\n\n")
print(Back.MAGENTA + "GAME OVER!")
print(f"You got {correct_answers} out of {len(questions)} questions correct.")

    #EXCEPTION 1 TO HANDLE: player enters numbers outside of 1234
    #EXCEPTION 2 TO HANDLE: player enters non-integer

    # while True: 
    #     user_answer = ""
    #     try:
    #         user_answer = int(input("What\'s your answer? Select 1,2,3 or 4: ")) #player selects an answer: 1,2,3, or 4 for each question
    #         if user_answer == len(question["incorrect_answers"]) + 1:
    #             print(Fore.GREEN + "Correct, well done!\n\n")
    #             correct_answers += 1 #increase score by 1 for each correct answer
    #         else:
    #             print(Fore.RED + "Sorry, incorrect.\n\n")
    #     except ValueError: 
    #         user_answer = int(input("You can only enter 1, 2, 3 or 4. Try again: "))





# show game intro at the start

 



# question number is zero



    # from 1 to 20
    # select 1 random question
    # show the selected question, 4 answer options
    # increase question number by 1 out of 20
    
        # function to validate answer
            # while input is not A or B or C or D; and a or b or c or d
            # print message invalid answer, enter A B C D, ask for input
            # when input is A or B or C or D; and a or b or c or d; go to unfciont to check answer

# function to check answer
    # 
