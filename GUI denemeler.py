import tkinter as tk
from tkinter import ttk, messagebox
import json
import matplotlib.pyplot as plt

# Global variables and constants
HUF_TO_EUR_RATE = 0.002562  # Updated to today's rate
expenses = []
modifying_index = None


def save_expenses():
    """Saves the expenses list to a JSON file."""
    try:
        with open("expenses.json", "w") as f:
            json.dump(expenses, f, indent=4)
    except IOError:
        messagebox.showerror("Error", "Could not save data to file.")


def load_expenses():
    """Loads expenses from a JSON file."""
    global expenses
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
            messagebox.showinfo("Data Loaded", "Expenses have been loaded from file.")
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist yet
    except IOError:
        messagebox.showerror("Error", "Could not read data from file.")
    update_expense_list()
    update_total()


def add_expense():
    """Adds a new expense from the GUI inputs."""
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()

        if not category or not description:
            messagebox.showerror("Input Error", "Category and Description cannot be empty.")
            return

        expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })

        save_expenses()
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        update_expense_list()
        update_total()
        messagebox.showinfo("Success", "Expense added successfully.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the amount.")


def delete_expense():
    """Deletes the selected expense from the list."""
    selected_index = expense_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Selection Error", "Please select an expense to delete.")
        return

    index = selected_index[0]
    response = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this expense?")
    if response:
        expenses.pop(index)
        save_expenses()
        update_expense_list()
        update_total()
        delete_button.pack_forget()
        modify_button.pack_forget()


def modify_expense():
    """Prepares the UI to modify the selected expense."""
    global modifying_index
    selected_index = expense_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Selection Error", "Please select an expense to modify.")
        return

    modifying_index = selected_index[0]
    expense_to_modify = expenses[modifying_index]

    amount_entry.delete(0, tk.END)
    amount_entry.insert(0, str(expense_to_modify["amount"]))
    category_entry.delete(0, tk.END)
    category_entry.insert(0, expense_to_modify["category"])
    description_entry.delete(0, tk.END)
    description_entry.insert(0, expense_to_modify["description"])

    add_button.config(text="Save Changes", command=save_modified_expense)


def save_modified_expense():
    """Saves the changes made during a modification."""
    global modifying_index
    try:
        new_amount = float(amount_entry.get())
        new_category = category_entry.get()
        new_description = description_entry.get()

        if not new_category or not new_description:
            messagebox.showerror("Input Error", "Category and Description cannot be empty.")
            return

        expenses[modifying_index] = {
            "amount": new_amount,
            "category": new_category,
            "description": new_description
        }

        save_expenses()
        modifying_index = None

        # Reset the UI to add mode
        add_button.config(text="Add Expense", command=add_expense)
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)

        update_expense_list()
        update_total()
        messagebox.showinfo("Success", "Expense updated successfully.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the amount.")


def update_expense_list():
    """Refreshes the Listbox with the current expenses."""
    expense_listbox.delete(0, tk.END)
    if expenses:
        for exp in expenses:
            display_text = f"{exp['amount']:.2f} HUF - {exp['category']} - {exp['description']}"
            expense_listbox.insert(tk.END, display_text)


def update_total():
    """Calculates and updates the total expense label in HUF and EUR."""
    total_huf = sum(exp["amount"] for exp in expenses)
    total_label.config(text=f"Total Spent: {total_huf:.2f} HUF")

    total_eur = total_huf * HUF_TO_EUR_RATE
    total_eur_label.config(text=f"Total in EUR: {total_eur:.2f} EUR")


def on_list_select(event):
    """Shows/hides the delete and modify buttons based on selection."""
    if expense_listbox.curselection():
        delete_button.pack(side=tk.LEFT, padx=5)
        modify_button.pack(side=tk.LEFT, padx=5)
    else:
        delete_button.pack_forget()
        modify_button.pack_forget()


def show_expense_chart():
    """Generates and displays a pie chart of expenses by category."""
    if not expenses:
        messagebox.showinfo("No Data", "No expenses recorded to create a chart.")
        return

    category_totals = {}
    for exp in expenses:
        category = exp["category"].capitalize()
        amount = exp["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title("Expense Breakdown by Category")
    plt.ylabel('')

    plt.show()


def filter_expenses(event):
    """Filters the listbox based on the search query."""
    query = search_entry.get().lower()
    expense_listbox.delete(0, tk.END)

    if not query:
        update_expense_list()
        return

    filtered_expenses = [
        exp for exp in expenses
        if query in exp["category"].lower() or query in exp["description"].lower()
    ]

    for exp in filtered_expenses:
        display_text = f"{exp['amount']:.2f} HUF - {exp['category']} - {exp['description']}"
        expense_listbox.insert(tk.END, display_text)


# --- GUI Setup ---
root = tk.Tk()
root.title("Expense Tracker")
# root.iconbitmap('icon.ico')  # Uncomment this line and specify your icon file

input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
display_frame = ttk.Frame(root, padding="10")
display_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

# --- Input Widgets ---
ttk.Label(input_frame, text="Amount:").grid(row=0, column=0, sticky=tk.W)
amount_entry = ttk.Entry(input_frame, width=20)
amount_entry.grid(row=0, column=1)

ttk.Label(input_frame, text="Category:").grid(row=1, column=0, sticky=tk.W)
category_entry = ttk.Entry(input_frame, width=20)
category_entry.grid(row=1, column=1)

ttk.Label(input_frame, text="Description:").grid(row=2, column=0, sticky=tk.W)
description_entry = ttk.Entry(input_frame, width=20)
description_entry.grid(row=2, column=1)

add_button = ttk.Button(input_frame, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

ttk.Label(input_frame, text="Search:").grid(row=4, column=0, sticky=tk.W, pady=(10, 0))
search_entry = ttk.Entry(input_frame, width=20)
search_entry.grid(row=4, column=1, pady=(10, 0))
search_entry.bind("<KeyRelease>", filter_expenses)

# --- Display Widgets ---
expense_listbox = tk.Listbox(display_frame, height=10, width=50)
expense_listbox.pack(pady=10)
expense_listbox.bind('<<ListboxSelect>>', on_list_select)

action_button_frame = ttk.Frame(display_frame)
action_button_frame.pack(pady=5)

delete_button = ttk.Button(action_button_frame, text="Delete", command=delete_expense)
modify_button = ttk.Button(action_button_frame, text="Modify", command=modify_expense)
show_chart_button = ttk.Button(action_button_frame, text="Show Chart", command=show_expense_chart)

delete_button.pack_forget()
modify_button.pack_forget()
show_chart_button.pack(side=tk.LEFT, padx=5)

total_label = ttk.Label(display_frame, text="Total Spent: 0.00 HUF", font=("Helvetica", 12, "bold"))
total_label.pack(pady=5)
total_eur_label = ttk.Label(display_frame, text="Total in EUR: 0.00 EUR", font=("Helvetica", 10))
total_eur_label.pack(pady=5)

# --- Final Code Execution ---
load_expenses()
root.mainloop()