<br/>
<h1 align="center">Lab Exercises Questions</h1>

## Tuples, Lists, Sets, Dictionaries

1. [Given a list of tuples, create a Python function that takes the list as input and returns a dictionary where the keys are student names and the values are their average scores. Utilize tuple unpacking and list comprehension.](./Exercise/1.py)

2. [Create a Python function that takes a list of integers as input and returns a list of all unique combinations of two numbers that sum to a prime number. Utilize list comprehension.](./Exercise/2.py)

3. [Write a Python function that takes two sets as input and returns a new set containing elements that are common to both sets. Use set operations to achieve this.](./Exercise/3.py)

4. [Create a Python function that takes two dictionaries as input and returns a new dictionary containing the merged key-value pairs. If there are common keys, sum the corresponding values. Utilize dictionary comprehension.](./Exercise/4.py)

## Control Flow, Functions and Strings:

5. [Create a Python program that calculates a student's final grade based on the following criteria](./Exercise/5.py):

<ol>Assign weights to different components: 40% for exams, 30% for assignments, and 30% for participation.

If the student's overall score is 90 or above, assign the grade "A."

If the overall score is between 80 and 89, assign the grade "B."

If the overall score is between 70 and 79, assign the grade "C."

If the overall score is between 60 and 69, assign the grade "D."

If the overall score is below 60, assign the grade "F."

Additionally, consider the following conditions:

If a student has scored below 40 on any individual component (exam, assignment, or participation), automatically assign the grade "F" regardless of the overall score.

If a student's participation score is 0, even if the overall score is above 60, assign the grade "F."</ol>

6. [Study and implement the string manipulation functions. Write a Python function named title_case that takes a sentence as input and returns a new sentence where each word is capitalized, except for common words (e.g., "and," "the," "in") which are lowercase, unless they appear at the beginning of the sentence. Use list comprehension to achieve this.](./Exercise/6.py)

7. [You have a simple Python program for email validation that uses the validate_email_address library to check if an email address is valid. The program also prints an informative error message if the email is considered invalid. Now, you want to further enhance this program by incorporating additional checks and providing user feedback.](./Exercise/7.py)

<ol>a) Include an additional check to verify that the email domain has valid DNS records.

b) Provide user-friendly error messages for different validation scenarios (e.g., invalid format, invalid domain, invalid mailbox).

c) Allow the user to input an email address and test your enhanced validation program.</ol>

## Classes and objects:

9. [Create a Python class named Student to represent a student. The class should have the following attributes: name, roll_number, grade, and marks (a dictionary where keys are subject names and values are corresponding marks). Implement the following methods](./Exercise/9.py):

<ol>a) _ _init_ _: Initializes a new student with the provided information.

b) calculate_average: Calculates and returns the average marks of the student.

c) get_grade: Assigns a grade based on the average marks and returns it.

d) display_info: Displays the student's information, including name, roll number, and average marks.</ol>

10. [Create Python classes for a Library Management System. Design a Book class with attributes like title, author, ISBN, and availability. Develop a Library class to manage books, allowing addition, display, borrowing, and returning. Implement a Member class for library members with attributes such as member ID, name, and a list of borrowed books. Lastly, create a LibrarySystem class to register members, display member lists, and facilitate book transactions (borrowing and returning).](./Exercise/10.py)

## Operator Overloading

11. [Design a Python class named BankAccount to represent a simple bank account. The class should include the following attributes: account_number, account_holder, and balance. Implement the following methods and operator overloading functionalities](./Exercise/11.py):

<ol>
a)  _ _init_ _: Initializes a new bank account with the provided account number, account holder's name, and initial balance.

b) deposit: Accepts an amount and adds it to the account balance.

c) withdraw: Accepts an amount and subtracts it from the account balance if sufficient funds are available. Ensure that the withdrawal operation properly handles cases where the account balance becomes negative.

d) get_balance: Returns the current balance of the account.

e) display_account_info: Displays the account information, including account number, account holder's name, and current balance.

f) Overload the + operator to allow adding two BankAccount objects. The result should be a new BankAccount object with an updated balance.

g) Overload the - operator to allow subtracting the balance of one BankAccount object from another. The result should be a new BankAccount object with an updated balance.

h) Overload the == operator to compare two BankAccount objects based on their account numbers.
</ol>

## Inheritance and polymorphism:

12. [Imagine you're building a system for a transportation company to manage different vehicles. Develop the following setup that allows flexible management of different vehicle types within the transportation company, adhering to object-oriented design principles.](./Exercise/12.py)

<ol>a) Start with a base class called Vehicle, which has attributes like make, model, year, and fuel_type.

b) Create a derived class Car inheriting from Vehicle with additional attributes such as num_doors, num_passengers, and car_type.

c) Extend further with a Truck class inheriting from Vehicle, adding attributes like payload_capacity and four_wheel_drive. Design an ElectricCar class inheriting from Car with attributes specific to electric cars like battery_capacity and charging_time.

d) Implement a Motorcycle class inheriting from Vehicle with attributes like num_wheels, has_sidecar, and motorcycle_type.

e) To showcase polymorphism, create a function that takes a list of vehicles and calls their display_info methods.</ol>

## File Handling:

13. [Create a program that reads a log file containing various entries with timestamps, messages, and severity levels. Implement a file handling mechanism to read the log file, extract relevant information, and perform analytics such as finding the total number of entries, counting entries with a specific severity level, and calculating the average time gap between entries.](./Exercise/13.py)

14. [Design a program that works with a CSV file containing data about employees in a company. The CSV file should have columns like employee ID, name, department, and salary. Implement file handling to read the CSV file, perform operations such as finding the highest-paid employee, sorting employees by department, and calculating the average salary for each department.](./Exercise/14.py)

## Exception Handling:

15. [Create a simple calculator program that takes user input for two numbers and an operation (addition, subtraction, multiplication, division). Implement exception handling to catch errors such as division by zero, invalid input for numbers or operations, and any other potential issues. The program should gracefully handle these exceptions and provide informative error messages.](./Exercise/15.py)

16. [Develop a program that reads data from an external source (e.g., a file or user input) and performs some numerical calculations on the data. Implement exception handling to handle potential errors, such as non-numeric data in the input, missing data, or unexpected formats. Ensure that the program continues to execute smoothly even when faced with these exceptions, providing feedback to the user about the encountered issues.](./Exercise/16.py)

## Data Analysis with NumPy, Pandas, and Matplotlib

17. [Imagine you are working with a dataset that contains information about sales transactions for an e-commerce company. The dataset has the following columns: 'Transaction_ID', 'Product_Name', 'Quantity', 'Price_per_Unit', 'Customer_ID', and 'Date'. Design exercises using NumPy, Pandas, and Matplotlib to analyze this dataset](./Exercise/17.py):

<ol>a) Data Loading and Exploration:

- Load the dataset into a Pandas DataFrame.

- Use descriptive statistics functions from both NumPy and Pandas to gain insights into the dataset's basic characteristics.

- Display the first few rows of the dataset to understand its structure.

b) Data Cleaning and Manipulation:

- Check for missing values in the dataset and decide on an appropriate strategy to handle them.

- Convert the 'Date' column to a datetime object using Pandas.

- Create a new column 'Total_Price' by multiplying 'Quantity' and 'Price_per_Unit' columns.

c) Data Visualization:

- Use Matplotlib to create a bar chart showing the total sales for each product.

- Create a line chart to visualize the trend in sales over time (use the 'Date' column).

- Generate a scatter plot to explore the relationship between 'Quantity' and 'Total_Price'.

d) Advanced Analysis:

- Utilize NumPy to calculate the correlation coefficient between 'Quantity' and 'Total_Price'.

- Use Pandas to group the data by 'Customer_ID' and find the average total spending per customer.

- Identify and visualize the top 5 products by total sales.</ol>

## Networking and GUI:

18. [Write a Python program to implement a simple chat application using both TCP and UDP. The application should consist of a server and multiple clients that can exchange messages.](./Exercise/18.py)

19. [Create a Python program using Tkinter to build a graphical interface for a two-player Tic-Tac-Toe game.](./Exercise/19.py)

<ol>a) Design the GUI to display a 3x3 grid where players can click to make their moves (X or O).<br/>b) Implement logic to check for a winning condition or a draw and display the result on the GUI.</ol>