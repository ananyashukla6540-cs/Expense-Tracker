def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category}\n")

    print("Expense Added Successfully!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            data = file.readlines()

            if len(data) == 0:
                print("No expenses found!")
            else:
                print("\nAll Expenses:")
                for expense in data:
                    print(expense.strip())

    except FileNotFoundError:
        print("No expenses found!")


def total_expenses():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                total += float(amount)

        print(f"\nTotal Expenses: ₹{total}")

    except FileNotFoundError:
        print("No expenses found!")


def delete_expense():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        if len(expenses) == 0:
            print("No expenses found!")
            return

        print("\nExpenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense.strip()}")

        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            expenses.pop(choice - 1)

            with open("expenses.txt", "w") as file:
                file.writelines(expenses)

            print("Expense deleted successfully!")
        else:
            print("Invalid expense number!")

    except FileNotFoundError:
        print("No expenses found!")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")