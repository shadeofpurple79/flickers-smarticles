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

- **Removal of Bad Characters from the API**

    - Open TDB questions and answers are full of bad characters that appear illegible to the player. These are mostly apostrophes, such as &quot;, &#039;, &ldquo;, ,&rdquo;, &amp;; but also the French letter e with accent (&egrave;), and the three dots for ellipsis (&hellip;). These are replaced using the .replace in Python before they're displayed to the player. 

![Bad Characters](documentation/images/bad-characters.png)

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
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.

### Classes & Functions

The program uses classes as a blueprint for the project's objects (OOP). This allows for the object to be reusable.

```python
class Person:
    """ Insert docstring comments here """
    def __init__(self, name, age, health, inventory):
        self.name = name
        self.age = age
        self.health = health
        self.inventory = inventory
```

The primary functions used on this application are:

- `def start_game()`
    - Starts the game, shows questions and answer options and checks player inputs 

### Imports

I've used the following Python packages and/or external imported packages.

- `json`: used for converting the python dictionary into a JSON string that can be written into a file
- `requests`: used to make a request to a web page and print the response text
- `colorama`: used for including color in the terminal
- `random`: used to get a random choice from a list

## Testing

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

## Code Validation

Use the space to discuss code validation for any of your own code files (where applicable).
You are not required to validate external libraries/frameworks, such as imported Bootstrap, Materialize, Font Awesome, etc.

**IMPORTANT**: You must provide a screenshot for each file you validate.

**PRO TIP**: Always validate the live site pages, not your local code. There could be subtle/hidden differences.

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

    | File | CI URL | Raw URL | Combined |
    | ---- | ------ | ------- | -------- |
    | PP3 *run.py* file | `https://pep8ci.herokuapp.com/` | `https://raw.githubusercontent.com/shadeofpurple79/flickers-smarticles/main/run.py` | https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/shadeofpurple79/flickers-smarticles/main/run.py |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Screenshot | Notes |
| ---- | ---------- | ----- |
| Home | ![screenshot](documentation/images/lighthouse-report.png) | No issues |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |


Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

## Bugs

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

For JavaScript and Python applications, it's best to screenshot the errors to include them as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/shadeofpurple79/flickers-smarticles/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/shadeofpurple79/flickers-smarticles/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/shadeofpurple79/flickers-smarticles/issues/1) | Closed |


# bug - correct answer is always the same number 4 - fixed by assigning all incorrect plus 1 correct answer into a variable and shuffling all of them
# user answer must be an int, otherwise it shows as incorrect answer - FIXED
# bug - validation not working, not throwing an error when answer is other than 1234. Fixed by using a while loop with continue and break commands
# if any other number is entered, it gives an error, but doesn't accept any further answers. Fixed by adding continue and break to while loop.
# if any character other than a number is entered, it breaks and ends the game. Fixed by removing integer from input, and assigning the answer into a new variable that converts the answer into an integer. 
# play again y/n. if answer is invalid, program ends, it doesn't accept any new answers. Fixed by replacing if loop with a while continue break loop and adding a nested if loop within.  
# bug remove unwanted code from all answer choices and replace with apostrophe

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/shadeofpurple79/flickers-smarticles/issues).

No open issues. 

## Unfixed Bugs

There are no remaining bugs that I am aware of.

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
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
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

### Local VS Deployment

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

## Credits

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

### Content

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!



| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.