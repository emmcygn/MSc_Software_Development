#Import the relevant modules and classes

from expense import Expense
import calendar
import datetime

# Define classes to add styles to the text below:

def green(text):
        return f"\033[92m{text}\033[00m"
    
def red(text):
        return f"\033[91m{text}\033[00m"
    
def gold(text):
        return f"\033[93m{text}\033[00m"
    
def print_bold(text):
        return("\033[1m" + text + "\033[0m")

# Define the main function

def main():
    print(f"🚀 You are now running the Expense Tracker 🚀")
    print()
    expense_file_path = "expenses.csv"
    budget = 1000.00

# get user input for expense
    
    expense = get_user_expense()

# Write their expense to a file 
    
    save_expense_to_file(expense, expense_file_path)

# Read a file and summarise expenses
    
    summarise_expenses(expense_file_path, budget)
 
print()

# Define a function to get user input for expense

def get_user_expense():
    expense_name = input("⭕ What is the expense name? ")

    while True:
        try:
            expense_amount = float(input("💰 What is the expense amount: £"))
            break  # Exit the loop if conversion to float is successful
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Define a list of expense categories

    expense_categories = [
        "🍔 Eating Out", 
        "🏠 Home",
        "🚃 Travel",
        "🎢 Entertainment",
        "👖 Other",
    ]

# Print the expense categories

    while True:
        print("📁 Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
        print()  # Add an extra line for better formatting
        
        value_range = f"[1 - {len(expense_categories)}]"

        while True:
            try:
                selected_index = int(input(f"📁 Enter a category number {value_range}: ")) - 1
                if selected_index in range(len(expense_categories)):
                    selected_category = expense_categories[selected_index]
                    break  # Exit the loop if the input is valid
                else:
                    print("Invalid Category. Please Try Again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Create a new expense object

        new_expense = Expense(
            name=expense_name, category=selected_category, amount=expense_amount
        )
        return new_expense

# Define a function to save the expense to a file

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"💾 Saving User Expense to File: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.category},{expense.name},{expense.amount}\n")

    print() # Add an extra line for better formatting

# Define a function to read a file and summarise expenses

def summarise_expenses(expense_file_path, budget):
    print(f"📊 Summarising Expenses")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_category, expense_name, expense_amount = line.strip().split(",")
            print(expense_category, expense_name, expense_amount)
            line_expense = Expense(
                category=expense_category, name=expense_name, amount=float(expense_amount)
            )
            expenses.append(line_expense)
    
    print()

# Summarise expenses by category

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount 
        else:
            amount_by_category[key] = expense.amount 

    print("📌 Expenses Summary:")
    
# Print the expenses summary
    
    for key, amount in amount_by_category.items():
        print()
        print(f"     {key}: £{amount:.2f}")

# Print the total expenses and remaining budget

    total_expenses = sum(x.amount for x in expenses)
    print(green(f"📀 You have spent £{total_expenses:.2f} this month"))

# Print the remaining budget

    remaining_budget = budget - total_expenses
    print(green(f"💹 Your remaining budget is £{remaining_budget:.2f}"))
    if remaining_budget < 0:
        print("You are over budget!")

# Print the average daily spend

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    average_daily_spend = remaining_budget / remaining_days
    print(green(f"📋 You can spend £{average_daily_spend:.2f} per day for the rest of the month"))
    print("     There are {} days remaining in the month".format(remaining_days))

# Ask the user if they would like to add to the expense tracker

    rerun = input(gold("Would you like to add to the expense tracker? (yes/no): ").lower())
    
    if rerun == "yes":
        print()
        main()  # Rerun the application
    else:
        print()
        print(red("Exiting the application."))

# Define the main function

if __name__ == "__main__":
    main()

