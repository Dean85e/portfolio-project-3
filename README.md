# Python Insurance Calculator.
![Opening message](/images/application-start-up.png)

Welcome to the Insurance Calculator application. This application is built using only Python.
it is designed to provide the user with a realistic insurance quote depending on what details
the user enters. 

There is three vehicle categorys which are cars, vans and motorbikes.

Live link to the application can be found here: [Python Insurance Calculator](https://python-insurance-calculator.herokuapp.com/)
## Target Audience
 * This application is for people who may want to get an isnsurance quote.
# Features

## Existing Features

* The user is presented with a welcome message and instructed to proceed for an isurance quote.
![Personal details](/images/personal_detail.png)
* The program will then ask the user to enter a series of some personal details such as:
  * First name.
  * Second name.
  * Age.
  * Address.
  * No claim bonus.
  * Penalty points.
 ![Vehicle selection](/images/vehicle_select.png)
 * The user will then be given a choice of vehicle to select:
   
   * Option 1 for cars.
   * Option 2 for vans.
   * option 3 for motorbikes.
 ![Vehicle information](/images/vehicle_info.png)
 * Once the user has selected a vehicle category the program will then ask 
 a series of questions about the vehicle such as:
   
   * The make of the vehicle.
   * The model of the vehicle.
   * The year of the vehicle.
   * The engine size in cubic capacity.

* The program will then calculate the insurance premium with the information the user has provided.
![Information feedback](/images/info_feedback.png)

* The user will be presented with all the details they have provided.
![Premium breakdown](/images/premium_breakdown.png)
* Also the user will be given an insurance premium breakdown of all the increases or decreases depending on the information entered, followed by the total premium price.
![Total premium](/images/total_premium.png)

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

# Testing

## Validator Testing

* I can confirm this project code passed through the CI Python Linter with no issues.

![Total premium](/images/py-validation.png)
## Application Testing

* I can confirm that the input validation is working on each input question.

* I can confirm that the program adds and subtracts from the base premium as expected depending on which data the user inputs.