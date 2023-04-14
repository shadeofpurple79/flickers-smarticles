import random

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)  #return to default colour after each time

import json
import requests # Make a request to a web page, and print the response text


def start_game():
    # from opentdb api, category: entertainment 
    # - film, 20 questions, multiple choice
    API_URL = "https://opentdb.com/api.php?amount=20&category=11&type=multiple"

    # get data from the API
    response = requests.get(API_URL)
    data = json.loads(response.text)

    # create variable to store quiz questions
    questions = data["results"]
    # print(data) - testing to show that the questions and answers are coming through the api
    
    # score is zero at the start, score equals number of correct answers
    correct_answer = 0  
    # player should only enter answer options 1-2-3-4
    # answer_choices = [1, 2, 3, 4]

    # for each question in the random 20 questions in the api, show the question, 
    # show 3 incorrect answers and 1 correct answer, 
    # ask player to enter their choice
    for question in questions: 
        # remove ugly text that comes in from the api for apostrophes 
        print(Style.BRIGHT + Back.MAGENTA + question["question"].replace("&quot;", "'").replace("&#039;", "'").replace("&ldquo;", "'").replace(",&rdquo;", "'").replace("&amp;", "'")) 
        print("Select your answer from the following 4 options:") 

        # assign 3 incorrect answers and 1 correct answer into a variable and shuffle them so that the answer is not always the same option
        all_answers = question["incorrect_answers"]
        all_answers.append(question["correct_answer"])
        random.shuffle(all_answers)

        for i, answer in enumerate(all_answers):
            print(f"{i + 1}. {answer}".replace("&quot;", "'").replace("&#039;", "'").replace("&ldquo;", "'").replace(",&rdquo;", "'").replace("&amp;", "'"))

        # player selects an answer: 1,2,3,4 
        user_answer = (input("What\'s your answer? Select 1,2,3 or 4: "))

        # answer_count = 0
        # answer_limit = 3 # can only enter 3 times for one question
        # out_of_try = False
        
        while True: 
            if user_answer not in ['1', '2', '3', '4']:
            # answer_count < answer_limit:
                user_answer = (input("You can only enter 1, 2, 3 or 4. Try again: "))
                # answer_count += 1
                continue
            else:
                # out_of_try = True
                break
        
        # if out_of_try:
        #     print("Sorry, too many invalid answers. ")
        # else: 
        user_input = int(user_answer)
        if all_answers[user_input - 1] == question["correct_answer"]:
            print(Fore.GREEN + "Correct, well done!\n\n")
            correct_answer += 1
        else:
            print(Fore.RED + "Sorry, incorrect.\n\n")
            print()  # Add a blank line between questions

    print(Back.MAGENTA + "GAME OVER!")
    print(f"You got {correct_answer} out of {len(questions)} questions correct.")
    
    play_again = input("Play again? Y / N: ").lower()
    
    while True: 
        if play_again not in ["y", "n"]:
            play_again = input("Not a valid answer. Play again? Y / N: ").lower()
            continue
        else:
            break

    # if play_again == "y":
    #     start_game()
    # else play_again == "n":
    #     print(Back.MAGENTA + "Goodbye") 
    #     print()
    #     print()
        
start_game()



# CODING CHECKLIST

# RUN PROGRAM BUTTON

# show game intro at the start

# function start_game - DONE start_game
# 	pull new 20 questions and answer choices from the API link - DONE
# 	reset the score = 0 - DONE
# 	question_number = 0
# 	choices = [1-2-3-4] - DONE
# 	clear the screen

# 	for question i to 20 - DONE

# 		show_question [i] - DONE 
# 		question_number + 1 - DONE
# 		i + 1 - DONE
#       shuffle the order of incorrect answers and correct answer - DONE
# 		show 3 incorrect answers - DONE
# 		show 1 correct answer - DONE
# 		show 1-2-3-4 next to each answer option - DONE

# 		input answer - DONE
# 		while input answer is not included in choices - DONE
# 			print error message, input only 1-2-3-4 - DONE
# 		otherwise check if input answer is correct or wrong - DONE
# 			if it's correct - DONE
# 				print correct - DONE
# 				score + 1 - DONE
# 			if it's wrong - DONE
# 				print incorrect - DONE
# 		back to show_question - DONE

# 	when i = 20 end quiz  - DONE

# print score + message - DONE
# input question play again? y/n - DONE
# 	if y - DONE
# 		function start_game - DONE
# 	if n - DONE
# 		print goodbye + end game - DONE
# 	if other - DONE
# 		input question play again? y/n - DONE
	


# bug remove unwanted code from all answer choices and replace with apostrophe


# FIXED BUGS
# bug - correct answer is always the same number 4 - fixed by assigning all incorrect plus 1 correct answer into a variable and shuffling all of them
# user answer must be an int, otherwise it shows as incorrect answer - FIXED
# bug - validation not working, not throwing an error when answer is other than 1234. Fixed by using a while loop with continue and break commands
# if any other number is entered, it gives an error, but doesn't accept any further answers. Fixed by adding continue and break to while loop.
# if any character other than a number is entered, it breaks and ends the game. Fixed by removing integer from input, and assigning the answer into a new variable that converts the answer into an integer. 
#  play again y/n. if answer is invalid, program ends, it doesn't accept any new answers. Fixed by replacing if loop with a while continue break loop. 




# # BINNED CODE

############### fix 1
 # len() function returns the number of items in an object, 20 questions
        # print all 3 incorrect answers and 1 correct answer
        # for i in range(len(question["incorrect_answers"])):  
        #     random.shuffle(question['incorrect_answers'])
        #     print(f"{i+1}. {(question['incorrect_answers'][i])}")
        # print(f"{len(question['incorrect_answers'])+1}. {question['correct_answer']}")
############### end of fix 1


############### fix 2
        # if user_answer == len(question["incorrect_answers"]) + 1:
        #     print(Fore.GREEN + "Correct, well done!\n\n")
        #     print()  # Add a blank line between questions
        #     correct_answer += 1 #increase score by 1 for each correct answer
        # else:
        #     print(Fore.RED + "Sorry, incorrect.\n\n")
############### END OF fix 2


# def validate_choice(user_answer, answer_choices):
        #     try:
        #         if user_answer not in answer_choices:
        #             user_answer = (input("You can only enter 1, 2, 3 or 4. Try again: "))
        #             # raise ValueError
        #     except ValueError:
        #         print(red(LINE))
        #         print(red(CENT(f'Error: "{user_answer}" is not valid! Enter 1 or 2 or 3 or 4')))
        #         return False
        #     return True



 # again = input("Play again? Y / N")
    #     if again = "y":
    #         start_game()
    #     elif again = "n":
    #         print(Back.MAGENTA + "Goodbye")
    #         break 
    #     else:
    #         input("Not a valid answer. Play again? Y/N")
  


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


    

# while not (user_answer == 1 or user_answer == 2 or user_answer == 3 or user_answer == 4):

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


