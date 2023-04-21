# FLICKERS SMARTICLES

Flickers Smarticles is a movie trivia quiz game for the movie fans. It covers a range of difficulties to cater from the most novice to the most die-hard fans of the Hollywood blockbuster movie industry. The questions are interesting, fun, and even educational.

The brand Flickers Smarticles is a play on the words: Flicker being an expression for the flickering images of the old movies, and a way of describing types of movies, such as Chick Flicks for romantic comedies; and Smarticles is a play on the word Smart, implying that the game players are smart movie fans paying attention to the details in films. 

Flickers Smarticles

![Responsive Views](documentation/images/am-i-responsive.png)

## UX

Game is designed using Python default view in black screen. 


## Features

The game is based on the opentdb.com open API for trivia game questions. The API created for this game speficially pulls 20 randomly selected questions each time the game starts, along with 3 incorrect and 1 correct answer. The quiz questions are different in each game, and the order of the multiple choice answers are re-shuffled in each game to ensure the answer is not always the same option. This prevents the game from becoming too easy and repetitive. 

The game validates player's answer inputs and only accepts the answer in the valid input type. It also offers replayability by offering the player to start a new game at the end of one. Each correct answer counts towards a score of one which creates a sense of achievement as the player will try to increase their score each time. 

### Game Flow

Below is the flowchart of the main process of this Python program. It shows the entire cycle of the game and the planning process.

![Game Flow](documentation/images/game-flow-diagram.png)
 
### Existing Features

- **OpenTDB Game API**

    - The game is based on Open TDB game trivia database API to ensure that the question base is not small and repetitive and continuously gets updated by public contributions. The answer options come available through the API with over 4,000 questions.
    
[API_URL https://opentdb.com/api.php?amount=20&category=11&type=multiple](https://opentdb.com/api.php?amount=20&category=11&type=multiple) 

![Open TDB Trivia Database API](documentation/images/opentdb-trivia.png)

- **Game Score**

    - Player earns 1 point for each correct answer out of 20 questions answered. 

![Scores](documentation/images/game-score.png)

- **Reshuffle Order of Answer Choices**

    - OpenTDB API provides 3 incorrect and 1 correct answer options for each question. However, the incorrect answers come through in the same order each time. For this reason, Flickers Smarticles game re-shuffles the order of the multiple choice answer options each time the question is displayed to the player. This reduces the predictability and ensures that the player must read answer options each time. 

![Reshuffle Answers](documentation/images/reshuffle-answers.png)

- **Removal of Unicodes from the API** 

    - Open TDB questions and answers are full of unicodes that appear illegible to the player. These are mostly apostrophes, such as `\&quot;` `\&#039;` `\&ldquo;` `\,&rdquo;` `\&amp;;` but also the French letter e with accent (`\&egrave;`) and the three dots for ellipsis (`\&hellip;`). These are replaced using the .replace in Python before they're displayed to the player. 

![Unicodes](documentation/images/bad-characters.png)

- **Numbered List for Multiple Choice Options**

    - Prefixes in the form of 1-2-3-4 is added to the beginning of each multiple choice answer to make it easy for the player to enter their answer. 

![API Multiple Choices](documentation/images/api-multiple-choice.png)
![Numbered List Multiple Choices](documentation/images/numbered-multiple-choice.png)

- **Use of Colours**

    - To make the questions and answers more legible and the correct and incorrect answer announcements more interesting, use of colours have been utilised. 

![Colours](documentation/images/colours-text.png)

- **Input Validation**

    - Player is requested to enter one of 1-2-3-4 as an answer choice to the multiple choice questions. If the input is anything other than these four numbers, a while loop has been implemented that keeps asking the player to enter the correct type of input. This validation includes any letters, special characters and also any number outside of 1-2-3-4. 

![Colours](documentation/images/input-choices.png)

- **Replayability**

    - Player is prompted to play again once the game is completed. requested to enter one of 1-2-3-4 as an answer choice to the multiple choice questions. If the input is anything other than these four numbers, a while loop has been implemented that keeps asking the player to enter the correct type of input. This validation includes any letters, special characters and also any number outside of 1-2-3-4. 

![Colours](documentation/images/game-over.png)

### Future Features

- Select Level of Difficulty 
    - The API allows for categorisation of questions according to level of difficulty. This game can incorporate that and offer it as an option to the player. The player can select their level or difficulty at the start of the game. 
- Game Progression 
    - The game could start from an easy level and allow the player to progress to higher levels with increased difficulty as they complete previous levels.
- Save Past Scores 
    - Player's past scores and all time best scores could be saved and be available upon subsequent visits. 
- Registration and Login 
    - Player could register a game account and login to see their past scores and games.

## Tools & Technologies Used

- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Open TDB](https://opentdb.com/api_config.php) used as a database of trivia questions in the film category.

### Classes & Functions

The primary functions used on this application are:

- `def start_game()`
    - Starts the game, shows questions and answer options and checks player inputs 

- `clear()`
    - Clears the terminal to show a clean screen

### Imports

I've used the following Python packages and/or external imported packages.

- `json`: used for converting the python dictionary into a JSON string that can be written into a file
- `requests`: used to make a request to a web page and print the response text
- `colorama`: used for including color in the terminal
- `random`: used to get a random choice from a list
- `os`: used to clear the screen


## Testing

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

## Code Validation

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | URL | Screenshot | Notes |
| ---- | ------ | ------- | -------- |
| PP3 *run.py* file | [Pep8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/shadeofpurple79/flickers-smarticles/main/run.py) | ![Screenshot pep8](documentation/images/pep8-validation.png) | No errors found|

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Screenshot | Notes |
| ---- | ---------- | ----- |
| Home | ![screenshot](documentation/images/lighthouse-report.png) | No issues |

## Bugs

Bugs are documented under Github Issues page. 

### GitHub **Issues**

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/shadeofpurple79/flickers-smarticles/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [1) correct answer is always the same number 4 ](https://github.com/shadeofpurple79/flickers-smarticles/issues/1) | Closed |
| [2) user answer must be an int, otherwise it shows as incorrect answer](https://github.com/shadeofpurple79/flickers-smarticles/issues/2) | Closed |
| [3) not throwing an error when answer is other than 1-2-3-4](https://github.com/shadeofpurple79/flickers-smarticles/issues/3) | Closed |
| [4) after error, doesn't accept any further answers](https://github.com/shadeofpurple79/flickers-smarticles/issues/4) | Closed |
| [5) Game breaks when any character other than a number is entered](https://github.com/shadeofpurple79/flickers-smarticles/issues/5) | Closed |
| [6) Game breaks if answer is invalid when play again? y/n is asked](https://github.com/shadeofpurple79/flickers-smarticles/issues/6) | Closed |
| [7) Bad characters still appearing in answer choices](https://github.com/shadeofpurple79/flickers-smarticles/issues/7) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/shadeofpurple79/flickers-smarticles/issues).

There are no open issues. 

## Unfixed Bugs

There are no remaining bugs that I am aware of. 

All apostrophe characters found so far in the API have been replaced. 

During the testing of the game, about 500 questions and their answer options have been checked and all ascii characters have been cleaned up. These are: 

- `\&quot;`
- `\&#039;`
- `\&ldquo;`
- `\&rdquo;`
- `\&amp;`
- `\&rsquo;`

However occasionally new ascii characters still come up. I couldn't find a way to review the entire question database to see if any other variation of apostrophe has been used in the Open TDB database.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://flickers-smarticles.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/shadeofpurple79/flickers-smarticles) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/shadeofpurple79/flickers-smarticles.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/shadeofpurple79/flickers-smarticles)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/shadeofpurple79/flickers-smarticles)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

I've used a lot of resources to help me understand how Python works and how to create a basic simple quiz game:

| Source | Notes |
| --- | --- |
| [Tim Nelson's Markdown Builder](https://traveltimn.github.io/markdown-builder/) | tool to help generate the Markdown files |
| [Open Trivia Database](https://opentdb.com/api_config.php) | provides a free JSON API for use in programming projects |
| [Learn Python - Full Course for Beginners [Tutorial] FreeCodeCamp.org](https://www.youtube.com/watch?v=rfscVS0vtbw) | helped me understand Python better |
| [Learn Python](https://learnpython.com/) | learn how to use Python |

### Content

I've used code snippets and adjusted to my requirements from the following resources:

| Source | Notes |
| --- | --- |
| [Creating A Basic Trivia Game In Python](https://medium.com/@webmind-solutions/creating-a-basic-trivia-game-in-python-using-apis-89a45ac1877) | useful article about using Open TDB |
| [Create a QUIZ GAME with Python](https://youtu.be/zehwgTB0vV8) | useful video showing steps for creating a Python game |
| [Python Quiz Game](https://youtu.be/yriw5Zh406s) |  useful video showing steps for creating a Python game |
| [Adding Color to Your Python Project](https://www.youtube.com/watch?v=u51Zjlnui4Y ) | Colorama Tutorial |
| [Fetching Questions](https://www.commudle.com/labs/gui-quiz-application-using-tkinter-and-open-trivia-db/steps/150352) | article about fetching questions from Open Trivia DB API |
| [Python String replace() Method](https://www.w3schools.com/python/ref_string_replace.asp) | used in replacing ugly apostrophe code | 
| [A Guide to Formatting with f-strings in Python](http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf) | used in constructing print statements using variables | 

### Acknowledgements

- I would like to thank my Mentor at Code Institute, [Tim Nelson](https://github.com/TravelTimN) for going out of his way to help me improve my code and encourabge me that I can do this. 