import matplotlib.pyplot as plt
import openpyxl
from datetime import datetime

# Data storage
expenses = []
budget_limit = 0

# Function to set budget
def set_budget():
    global budget_limit
    try:
        budget_limit = float(input("Enter your budget limit: "))
        print(f"✅ Budget set to {budget_limit}")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# Function to add expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")

        expenses.append({"date": date, "category": category, "amount": amount, "description": description})
        print("✅ Expense added successfully!")

        check_budget()

    except ValueError:
        print("❌ Invalid input. Amount must be a number.")

# Function to check budget alert
def check_budget():
    total = sum(exp["amount"] for exp in expenses)
    if budget_limit > 0 and total > budget_limit:
        print(f"⚠️ ALERT: You have exceeded your budget of {budget_limit}! Current total: {total}")

# Function to view expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
    print("---------------------")

# Function to filter expenses
def filter_expenses():
    choice = input("Filter by (1) Category or (2) Date? ")
    if choice == "1":
        category = input("Enter category: ")
        filtered = [exp for exp in expenses if exp["category"].lower() == category.lower()]
    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")
        filtered = [exp for exp in expenses if exp["date"] == date]
    else:
        print("❌ Invalid choice.")
        return

    if filtered:
        for exp in filtered:
            print(f"{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")
    else:
        print("No matching expenses found.")

# Function to export expenses to Excel
def export_excel():
    if not expenses:
        print("❌ No expenses to export.")
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Date", "Category", "Amount", "Description"])

    for exp in expenses:
        ws.append([exp["date"], exp["category"], exp["amount"], exp["description"]])

    filename = f"expenses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(filename)
    print(f"✅ Expenses exported to {filename}")

# Function to plot expenses
def plot_expenses():
    if not expenses:
        print("❌ No expenses to plot.")
        return

    categories = {}
    for exp in expenses:
        categories[exp["category"]] = categories.get(exp["category"], 0) + exp["amount"]

    plt.figure(figsize=(6, 6))
    plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.show()

# Menu
def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Filter Expenses")
        print("5. Export to Excel")
        print("6. Show Chart")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            set_budget()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            filter_expenses()
        elif choice == "5":
            export_excel()
        elif choice == "6":
            plot_expenses()
        elif choice == "7":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice, try again.")

# Run program
if __name__ == "__main__":
    menu()
