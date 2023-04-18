import random
import colorama
import json
import requests  # Make a request to a web page, and print the response text

from colorama import Fore, Back, Style
colorama.init(autoreset=True)  # return to default colour after each time


def start_game():
    print(Back.MAGENTA + "=================================================")
    print("|                                               |")
    print(Style.BRIGHT + "|              Flickers Smarticles              |")
    print("|               Movie Trivia Game               |")
    print("|                                               |")
    print("|  Do you know your Tom Cruise from Brad Pitt?  |")
    print("| Answer 20 questions. Select from 1, 2, 3, or 4|")
    print("|                                               |")
    print( Back.MAGENTA +"=================================================")
    print()
    print()
    
    # from opentdb api, category: entertainment
    # film, 20 questions, multiple choice
    API_URL = "https://opentdb.com/api.php?amount=20&category=11&type=multiple"

    # get data from the API
    response = requests.get(API_URL)
    data = json.loads(response.text)

    # create variable to store quiz questions
    questions = data["results"]

    # score is zero at the start, score equals number of correct answers
    correct_answer = 0

    # for each question in the random 20 questions in the api, show question
    # show 3 incorrect answers and 1 correct answer
    # ask player to enter their choice
    for question in questions:
        # remove ugly text that comes in from the api for apostrophes
        print(Style.BRIGHT + Back.MAGENTA + question["question"].replace(
            "&quot;", "'").replace("&#039;", "'").replace(
                "&ldquo;", "'").replace(",&rdquo;", "'").replace(
                    "&amp;", "'"))
        print("Select your answer from the following 4 options:")

        # assign 3 incorrect answers and 1 correct answer into a variable 
        # shuffle them so that the answer is not always the same option
        all_answers = question["incorrect_answers"]
        all_answers.append(question["correct_answer"])
        random.shuffle(all_answers)

        for i, answer in enumerate(all_answers):
            # remove ugly text that comes in from the api for apostrophes
            print(f"{i + 1}. {answer}".replace("&quot;", "'").replace(
                "&#039;", "'").replace("&ldquo;", "'").replace(
                    ",&rdquo;", "'").replace("&amp;", "'").replace(
                        "&egrave;", "e").replace("&hellip;", "..."))

        # player selects an answer: 1,2,3,4
        user_answer = (input("What\'s your answer? Select 1,2,3 or 4: "))

        while True:
            if user_answer not in ['1', '2', '3', '4']:
                user_answer = (input(
                    "You can only enter 1, 2, 3 or 4. Try again: "))
                continue
            else:
                break

        user_input = int(user_answer)
        if all_answers[user_input - 1] == question["correct_answer"]:
            print(Fore.GREEN + "Correct, well done!\n\n")
            correct_answer += 1
        else:
            print(Fore.RED + "Sorry, incorrect.\n\n")

    print(Back.MAGENTA + "GAME OVER!")
    print(
        f"You got {correct_answer} out of {len(questions)} questions correct.")
    print()
    play_again = input("Play again? Y / N: ").lower()

    while True:
        if play_again not in ["y", "n"]:
            play_again = input(
                "Not a valid answer. Play again? Y / N: ").lower()
            continue
        else:
            if play_again == "y":
                start_game()
            else:
                print(Back.MAGENTA + "Goodbye")
                print()
                print()
            break


start_game()
