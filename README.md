# Python Insurance Calculator.

![Opening message](/images/application-start-up.png)

Welcome to the Insurance Calculator application. This application is built using only Python.
It is designed to provide the user with a realistic insurance quote depending on what details
the user enters. 

There is three vehicle categories which are cars, vans and motorbikes.
With each category starting with a seperate base price.

Live link to the application can be found here: [Python Insurance Calculator](https://python-insurance-calculator.herokuapp.com/)

Link to my repository on GitHub can be found [here](https://github.com/Dean85e/portfolio-project-3)

## Target Audience

 * This application is for people who may want to get an insurance quote.

# Features

## Existing Features

* The user is presented with a welcome message and instructed to proceed for an insurance quote.

![Personal details](/images/personal-detail.png)

* The program will then ask the user to enter a series of some personal details such as:
  * First name.
  * Second name.
  * Age.
  * Address.
  * No claim bonus.
  * Penalty points.
 
 ![Vehicle selection](/images/vehicle-select.png)

 * The user will then be given a choice of vehicle to select:
   
   * Option 1 for cars.
   * Option 2 for vans.
   * Option 3 for motorbikes.
 
 ![Vehicle information](/images/vehicle-info.png)
 
 * Once the user has selected a vehicle category the program will then ask 
 a series of questions about the vehicle such as:
   
   * The make of the vehicle.
   * The model of the vehicle.
   * The year of the vehicle.
   * The engine size in cubic capacity.

* The program will then calculate the insurance premium with the information the user has provided.

![Information feedback](/images/info-feedback.png)

* The user will be presented with all the details they have provided.

![Premium breakdown](/images/premium_breakdown.png)

* Also the user will be given an insurance premium breakdown of all the increases or decreases depending on the information entered, followed by the total premium price.

![Total premium](/images/total-premium.png)

## Future Features

* I would like to add a google sheet to store and retrieve insurance quotes when there is time to do so.

* I would also like to add more categories like home insurance and other vehicle categories.

## Design

![Total premium](/images/lucid-chart.png)

* My starting point on this project was to design a flow chart to give me a clear understanding of how I may approach it.

## User stories

* As a user I would like to have a clear understanding of what is being presented to me.

* As a user I would like the instructions to be easy to follow.

* As a user I would like to see where my insurance premium increased and why.

* As a user I would also like to see where my insurance premium decreased and why.

## Users Expect

* As a young person I expect my premium to be expensive.

* As a driver of an old vehicle I expect an increase on my total premium.

* As driver with many penalty points I expect an increase on my total premium.

* As a driver with many years no claim bonus I expect a decrease on my total premium.

* As a driver if my vehicle engine size is small I expect a decrease on my total premium on the other hand if my engine size is large I expect an increase on my total premium

# Testing

## Validator Testing

* I can confirm this project code passed through the CI Python Linter with no issues.

![Total premium](/images/py-validation.png)

## Application Testing

* I can confirm that the input validation is working on each input question.

* I can confirm that the program adds and subtracts from the base premium as expected depending on which data the user inputs.

* Testing input validation on First Name. 

![First name blank](/images/f-name-blank.png)


![First name number](/images/f-name-num.png)

* Testing input validation on Last Name.

![Last name blank](/images/l-name-blank.png)

![Last name number](/images/l-name-num.png)

* Testing input validation on Address.

![Address blank](/images/address-blank.png)

![Address number](/images/address-num.png)

![Address string](/images/address-str.png)

* Testing input validation on Age.

![Age blank](/images/age-blank.png)

![Age](/images/age-num.png)

![Age string](/images/age-str.png)

* Testing input validation on No Claim Bonus.

![No claim blank](/images/ncb-blank.png)

![No claim string](/images/ncb-str.png)

![No claim wrong int](/images/ncb-wrong-int.png)

* Testing input validation on Vehicle Menu.

![Menu select string](/images/vehicle-select-str.png)

![Menu select wrong int](/images/vehicle-select-wrong-int.png)

* Testing input validation on Vehicle Make.

![vehicle make int](/images/make-int.png)

* Testing input validation on Vehicle Model.

![model int](/images/model-int.png)

* Testing input validation on Vehicle Year.

![year blank](/images/year-blank.png)

![year string](/images/year-str.png)

* Testing input validation on Engine Capacity.

![CC blank](/images/cc-blank.png)

![CC string](/images/cc-str.png)

![CC wrong int](/images/cc-wrong-int.png)

# Bugs 

## Solved Bugs 

![Bug](/images/input-error.png)


* Upon testing I discovered if an empty string or a single character (char) was entered in any of inputs using the range() method the program would crash to fix this I used the .strip method to make sure the user could not enter an empty string by setting valid_input to False , for the single character I checked if the user has entered a string and if so set valid_input to False.

![Bug solution](/images/validation-bug.png)

* This has fixed the issue.

* I also found that the string input questions would accept special characters to fix this I used the .isalpha method.

![Bug solution](/images/special-char.png)

* This issue is now resolved.

* Not neccesarily a bug but when I started the project I was having some difficulty in passing parameters and arguments to different functions , This was because I had the functions placed outside the class objects and once I moved the functions inside the appropriate classes things became a lot more clear to me regarding the flow of the application.

* I also found that validating user input one by one was making my functions untidy and longer than they needed to be, so I created validator function for each case and assigned each input to its corresponding validator function.


## Unfixed Bugs

* No unfixed Bugs.

## Deployment

The following are the steps I went through to deploy my live site:

* The site was deployed using Heroku. The steps to deploy are as follows:

  1. Go to Heroku
  2. Go to 'New' and select 'Create a new app'
  3. Input your app name and create app.
  4. Navigate to 'Settings'
  5. Install the needed buildpacks. Select Python and install and then node.js and 
     install and then click save. They must be in this order.
  6. Navigate to the 'Deploy' section.
  7. Connect to GitHub, search for your repo and confirm.
  8. Choose branch to deploy.
  9. Your app should now be available to see. You can choose whether to have your app 
     automatically redeploy with every push or to keep it manual.

* To Fork the repository:

  * On GitHub.com, navigate to the repository.
  * In the top-right corner of the page, click Fork.
  * Select an owner for the forked repository.
  * By default, forks are named the same as their parent repositories. You can change 
    the name of the fork to distinguish it further.
  *  Optionally, add a description of your fork.
  * Choose whether to copy only the default branch or all branches to the new fork.
  * Click Create fork.

* To Clone the repository:

  * On GitHub.com, navigate to the repository.
  * Above the list of files, click the Code button.
  * Copy the URL for the repository.
  * Open Git Bash.
  * Change the current working directory to the location where you want the cloned 
    directory.
  * Type git clone, and then paste the URL you copied earlier.
  * Press Enter. Your local clone will be created.

## Credits 
  Throughout the building process I faced many challenges, here are the resources that I found very helpful. 
  
  * This Youtube channel is an excellent source of information, In particular it helped me bolster my understanding of the concepts of classes and instance objects. [Link Here](https://www.youtube.com/@johnphilipjones)

  * The .strip method was inspired by this thread on [Stackoverflow](https://stackoverflow.com/questions/51764409/how-to-prevent-user-from-inputting-spaces-nothing-in-python)

  * I found the Object Orientated Programming tutorial on youtube very helpful with [Tech With Tim](https://www.youtube.com/watch?v=JeznW_7DlB0&t=12s)

  * Some inspiration for the input validation was taken from here [Youtube](https://www.youtube.com/watch?v=LUWyA3m_-r0)

  * The .isalpha method was taken from here [Youtube](https://www.youtube.com/watch?v=HanqlqLzdnU)

  I also found many helpful threads online regarding the Python __init__ Function links to these threads can be found below:

  * [w3schools](https://www.w3schools.com/python/gloss_python_class_init.asp)

  * [geeksforgeeks.org](https://www.geeksforgeeks.org/__init__-in-python/)

  * [AskPython](https://www.askpython.com/python/oops/init-method)

## Languages used 

 * Python

## Technologies used

 * Github 

 * Gitpod

 * Heroku

 * Code Institute template

 ## Links 

  Live link to the application can be found here: [Python Insurance Calculator](https://python-insurance-calculator.herokuapp.com/)

  Link to my repository on GitHub can be found [here](https://github.com/Dean85e/portfolio-project-3)