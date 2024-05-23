from typing import List
from expense import Expense

def main():
    print("Get ready to calculate your expenses!!")
    expense_file_path = "expenses.csv"
    budget = 2000
    summarise_exp(expense_file_path, budget)

def get_user_exp():
    print("Gathering user expenses")
    expense_name = input("Enter the expense name: ")
    expense_amount = float(input("Enter the expense amount: "))

    expense_category = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]

    expense_paymode = [
        "Cash",
        "Credit Card",
        "Debit Card"
    ]

    while True:
        print("Select category:")
        for i, category_name in enumerate(expense_category):
            print(f"{i + 1} {category_name}")

        print("Select payment type:")
        for j, paytype in enumerate(expense_paymode):
            print(f"{j + 1} {paytype}")

        value_range = f"[1-{len(expense_category)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        paytype_range = f"[1-{len(expense_paymode)}]"
        selected_paymethod = int(input(f"Enter a payment category {paytype_range}: ")) - 1

        if (selected_index in range(len(expense_category))) and (selected_paymethod in range(len(expense_paymode))):
            selected_category = expense_category[selected_index]
            selected_method = expense_paymode[selected_paymethod]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount, paymode=selected_method
            )
            return new_expense
        else:
            print("Oh no, please enter a valid option")

def save_exp_to_file(expense: Expense, expense_file_path):
    print(f"Saving the expenses details: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category},{expense.paymode}\n")

def summarise_exp(expense_file_path, budget):
    print("Summary of your expenses")
    expenses: List[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category, expense_paymode = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
                paymode=expense_paymode,
            )
            expenses.append(line_expense)
            print(line_expense)

    amount_by_category = {}
    count_by_paymode = {"Cash": 0, "Credit Card": 0, "Debit Card": 0}

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

        if expense.paymode in count_by_paymode:
            count_by_paymode[expense.paymode] += 1

    print("Expense By category:")
    for key, amount in amount_by_category.items():
        print(f"{key}: ${amount:.2f}")

    print("Amount by category:", amount_by_category)
    print("Count by payment method:", count_by_paymode)

    total_spent = sum([x.amount for x in expenses])
    print(f"You have spent ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Budget remaining ${remaining_budget:.2f} this month!")

if __name__ == "__main__":
    main()
