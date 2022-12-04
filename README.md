# Python Insurance Calculator.

![Opening message](/images/application-start-up.png)

Welcome to the Insurance Calculator application. This application is built using only Python.
it is designed to provide the user with a realistic insurance quote depending on what details
the user enters. 

There is three vehicle categorys which are cars, vans and motorbikes.
With each category starting with a seperate base price.

Live link to the application can be found here: [Python Insurance Calculator](https://python-insurance-calculator.herokuapp.com/)

## Target Audience

 * This application is for people who may want to get an insurance quote.

# Features

## Existing Features

* The user is presented with a welcome message and instructed to proceed for an isurance quote.

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
   * option 3 for motorbikes.
 
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

![Premium breakdown](/images/premium-breakdown.png)

* Also the user will be given an insurance premium breakdown of all the increases or decreases depending on the information entered, followed by the total premium price.

![Total premium](/images/total-premium.png)

## Future Features

* I would like to add a google sheet to store and retrieve insurance quotes when there is time to do so.

* I would also like to add more categorys like home insurance and other vehicle categorys.

## Design

![Total premium](/images/lucid-chart.png)

* My starting point on this project was to design a flow chart to give me a clear understanding of how i may approach it.

## User stories

* As a user I would like to have a clear understanding of what is being presented to me.

* As a user I would like the instructions to be easy to follow.

* As a user i would like to see where my insurance premium increased and why.

* As a user i would also like to see where my insurance premium decreased and why.

## Users Expect

* As a young person i expect my premium to be expensive.

* As a driver of an old vehicle i expect an increase on my total premium.

* As driver with many penalty points i expect an increase on my total premium.

* As a driver with many years no claim bonus i expect a decrease on my total premium.

* As a driver if my vehicle engine size is small i expect a decrease on my total premium on the other hand if my engine size is large i expect an increase on my total premium

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

* Not neccesarily a bug but when i started the project i was having some difficulty in passing parameters and arguments to different functions , this was because i had the functions placed outside the class objects and once i moved the functions inside the appropriate classes things became a lot more clear to me regarding the flow of the application.

* I also found that validating user input one by one was making my functions untidy and longer than they needed to be, so I created validator function for each case and assigned each input to its corosponding validator function. 
