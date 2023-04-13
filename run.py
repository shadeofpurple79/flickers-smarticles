import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True) #return to default colour after each time

import json
import requests #Make a request to a web page, and print the response text


def start_game():
    # from opentdb api, category: entertainment - film, 20 questions, multiple choice
    API_URL = "https://opentdb.com/api.php?amount=20&category=11&type=multiple"

    # get data from the API
    response = requests.get(API_URL)
    data = json.loads(response.text)

    # create variable to store quiz questions
    questions = data["results"]

    # print(data)
    # clear()
    correct_answers = 0 #score is zero at the start, score equals number of correct answers 
    choices = ["1", "2", "3", "4"]
    for question in questions: #for each question in the random 20 questions in the api
        print(Style.BRIGHT + Back.MAGENTA + question["question"].replace("&quot;", "'").replace("&#039;", "'").replace("&ldquo;", "'").replace(",&rdquo;", "'")) #print a random question to the player, remove ugly text that comes in from the api for apostrophes
        print("Select your answer from the following 4 options:") #print the answers for the question to the player
        for i in range(len(question["incorrect_answers"])): #len() function returns the number of items in an object, 20 questions, 
            print(f"{i+1}. {question['incorrect_answers'][i]}")
        print(f"{len(question['incorrect_answers'])+1}. {question['correct_answer']}")
        user_answer = (input("What\'s your answer? Select 1,2,3 or 4: ")) #player selects an answer: 1,2,3, or 4 for each question
        # while not (user_answer == 1 or user_answer == 2 or user_answer == 3 or user_answer == 4):
            
        def validate_choice(user_answer, choices):
            try:
                if user_answer not in choices:
                    user_answer = (input("You can only enter 1, 2, 3 or 4. Try again: "))
                    # raise ValueError
            except ValueError:
                print(red(LINE))
                print(red(CENT(f'Error: "{user_answer}" is not valid! Enter 1 or 2 or 3 or 4')))
                return False
            return True

        
        if user_answer == len(question["incorrect_answers"]) + 1:
            print(Fore.GREEN + "Correct, well done!\n\n")
            print()  # Add a blank line between questions
            correct_answers += 1 #increase score by 1 for each correct answer
        else:
            print(Fore.RED + "Sorry, incorrect.\n\n")
            print()  # Add a blank line between questions
    print(Back.MAGENTA + "GAME OVER!")
    print(f"You got {correct_answers} out of {len(questions)} questions correct.")
    again = input("Play again? Y / N")
        if again = "y":
            start_game()
        elif again = "n":
            print(Back.MAGENTA + "Goodbye")
            break 
        else:
            input("Not a valid answer. Play again? Y/N")
            

start_game()

# CODING CHECKLIST

# RUN PROGRAM BUTTON

# function start_game
# 	pull new 20 questions and answer choices from the API link
# 	reset the score = 0
# 	question_number = 0
# 	choices = [1-2-3-4]
# 	clear the screen

# 	for question i to 20

# 		show_question [i]
# 		question_number + 1
# 		i + 1
# 		show 3 incorrect answers
# 		show 1 correct answer
# 		show 1-2-3-4 next to each answer option

# 		input answer
# 		while input answer is not included in choices 
# 			print error message, input only 1-2-3-4
# 		otherwise check if input answer is correct or wrong
# 			if it's correct
# 				print correct
# 				score + 1
# 			if it's wrong
# 				print incorrect
# 		back to show_question

# 	when i = 20 end quiz 

# print score + message
# input question play again? y/n
# 	if y
# 		function start_game
# 	if n
# 		print goodbye + end game
# 	if other
# 		input question play again? y/n
	
		
# # 
# 
# 
# 
# 
# 
# 
# 
# 
# 


# function to validate user answer
# def validate_choice(user_answer, choices):
#     try:
#         if user_answer not in choices:
#             raise ValueError
#     except ValueError:
#         print(red(LINE))
#         print(red(CENT(f'Error: "{user_answer}" is not valid! Enter 1 or 2 or 3 or 4')))
#         return False
#     return True


    #EXCEPTION 1 TO HANDLE: player enters numbers outside of 1234
    #EXCEPTION 2 TO HANDLE: player enters non-integer
    # bug remove unwanted code from all answer choices and replace with apostrophe
    # bug validation not working, not throwing an error when answer is other than 1234

    # while True: 
    #     user_answer = ""
    #     try:
    #         user_answer = int(input("What\'s your answer? Select 1,2,3 or 4: ")) #player selects an answer: 1,2,3, or 4 for each question
    #         choices = 
                # if user error not in choices 
    #           if user_answer == len(question["incorrect_answers"]) + 1:
    #             print(Fore.GREEN + "Correct, well done!\n\n")
    #             correct_answers += 1 #increase score by 1 for each correct answer
    #         else:
    #             print(Fore.RED + "Sorry, incorrect.\n\n")
    #     except ValueError: 
    #         user_answer = int(input("You can only enter 1, 2, 3 or 4. Try again: "))


# show game intro at the start