import tkinter as tk
from tkinter import ttk, messagebox
import json
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import os
import datetime

# Global variables and constants
HUF_TO_EUR_RATE = 0.002562
expenses = []
modifying_index = None

# List of users for the Combobox
users = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# List of categories for the Combobox
categories = ["Food", "Transportation", "Tips", "Gift", "SIM Card", "Office Equipment", "Else"]

# Currency rates relative to 1 HUF (Hungarian Forint)
CURRENCY_RATES = {
    "HUF": 1.0,
    "EUR": 380.0,
    "USD": 350.0,
    "HKD": 45.0,
    "IDR": 0.022
}


def convert_to_huf(amount, currency):
    """Converts a given amount to HUF based on the currency rates."""
    rate = CURRENCY_RATES.get(currency, 1.0)
    if currency == "HUF":
        return amount
    else:
        return amount * rate


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
            # Add date field for old entries if it doesn't exist
            for exp in expenses:
                if "date" not in exp:
                    exp["date"] = "N/A"
            messagebox.showinfo("Data Loaded", "Expenses have been loaded from file.")
    except FileNotFoundError:
        pass
    except IOError:
        messagebox.showerror("Error", "Could not read data from file.")
    update_expense_list()
    update_total()


def get_category_from_input():
    """Gets the category from the Combobox."""
    return category_combobox.get()


def add_expense():
    """Adds a new expense from the GUI inputs."""
    try:
        amount = float(amount_entry.get())
        category = get_category_from_input()
        description = description_entry.get()
        user = user_combobox.get()
        currency = currency_combobox.get()
        date = date_entry.get()

        if not category or not description or not user or not currency or not date:
            messagebox.showerror("Input Error", "All fields must be filled.")
            return

        expenses.append({
            "amount": amount,
            "currency": currency,
            "category": category,
            "description": description,
            "user": user,
            "date": date
        })

        save_expenses()
        amount_entry.delete(0, tk.END)
        category_combobox.set('')
        description_entry.delete(0, tk.END)
        user_combobox.set('')
        currency_combobox.set('HUF')
        date_entry.delete(0, tk.END)
        date_entry.insert(0, datetime.date.today().strftime('%Y-%m-%d'))
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
    description_entry.delete(0, tk.END)
    description_entry.insert(0, expense_to_modify["description"])
    user_combobox.set(expense_to_modify.get("user", ""))
    currency_combobox.set(expense_to_modify.get("currency", "HUF"))
    date_entry.delete(0, tk.END)
    date_entry.insert(0, expense_to_modify.get("date", datetime.date.today().strftime('%Y-%m-%d')))

    # Set category correctly
    category = expense_to_modify["category"]
    if category in categories:
        category_combobox.set(category)
        category_combobox.config(state="readonly")
    else:
        category_combobox.set(category)
        category_combobox.config(state="normal")

    add_button.config(text="Save Changes", command=save_modified_expense)


def save_modified_expense():
    """Saves the changes made during a modification."""
    global modifying_index
    try:
        new_amount = float(amount_entry.get())
        new_category = get_category_from_input()
        new_description = description_entry.get()
        new_user = user_combobox.get()
        new_currency = currency_combobox.get()
        new_date = date_entry.get()

        if not new_category or not new_description or not new_user or not new_currency or not new_date:
            messagebox.showerror("Input Error", "All fields must be filled.")
            return

        expenses[modifying_index] = {
            "amount": new_amount,
            "currency": new_currency,
            "category": new_category,
            "description": new_description,
            "user": new_user,
            "date": new_date
        }

        save_expenses()
        modifying_index = None

        # Reset the UI to add mode
        add_button.config(text="Add Expense", command=add_expense)
        amount_entry.delete(0, tk.END)
        category_combobox.set('')
        category_combobox.config(state="readonly")
        description_entry.delete(0, tk.END)
        user_combobox.set('')
        currency_combobox.set('HUF')
        date_entry.delete(0, tk.END)
        date_entry.insert(0, datetime.date.today().strftime('%Y-%m-%d'))

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
            user = exp.get("user", "Unknown")
            currency = exp.get("currency", "HUF")
            amount = exp.get("amount", 0)
            date = exp.get("date", "N/A")
            display_text = f"{date} | {amount:.2f} {currency} - {exp['category']} - {exp['description']} - by {user}"
            expense_listbox.insert(tk.END, display_text)


def update_total():
    """Calculates and updates the total expense label in HUF and EUR."""
    total_huf = sum(convert_to_huf(exp["amount"], exp.get("currency", "HUF")) for exp in expenses)
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
        category = exp.get("category", "Unknown").capitalize()
        amount_huf = convert_to_huf(exp.get("amount", 0), exp.get("currency", "HUF"))
        category_totals[category] = category_totals.get(category, 0) + amount_huf

    categories_chart = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories_chart, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
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
        if query in exp.get("category", "").lower() or query in exp["description"].lower() or query in exp.get("user",
                                                                                                               "").lower() or query in exp.get(
            "date", "").lower()
    ]

    for exp in filtered_expenses:
        user = exp.get("user", "Unknown")
        currency = exp.get("currency", "HUF")
        amount = exp.get("amount", 0)
        date = exp.get("date", "N/A")
        display_text = f"{date} | {amount:.2f} {currency} - {exp['category']} - {exp['description']} - by {user}"
        expense_listbox.insert(tk.END, display_text)


def save_and_print_report():
    """Generates a PDF report for the selected user and opens it."""
    selected_user = user_combobox.get()
    if not selected_user:
        messagebox.showerror("Selection Error", "Please select a user to generate a report.")
        return

    user_expenses = [exp for exp in expenses if exp.get("user") == selected_user]
    if not user_expenses:
        messagebox.showinfo("No Data", f"No expenses found for {selected_user}.")
        return

    # PDF generation logic
    file_name = f"expense_report_{selected_user}_{datetime.date.today()}.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    story = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    body_style = styles['Normal']
    body_style.spaceAfter = 12

    # Title
    title_text = f"Expense Report for {selected_user}"
    story.append(Paragraph(title_text, title_style))
    story.append(Spacer(1, 12))

    # Date
    story.append(Paragraph(f"Date: {datetime.date.today()}", body_style))
    story.append(Spacer(1, 12))

    # Table of expenses
    table_data = [['Date', 'Amount (HUF)', 'Original Amount', 'Currency', 'Category', 'Description']]

    total_huf_report = 0
    for exp in user_expenses:
        amount_huf = convert_to_huf(exp.get("amount", 0), exp.get("currency", "HUF"))
        table_data.append([
            exp.get("date", "N/A"),
            f"{amount_huf:.2f}",
            f"{exp['amount']:.2f}",
            exp.get("currency", "HUF"),
            exp['category'],
            exp['description']
        ])
        total_huf_report += amount_huf

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ])

    expense_table = Table(table_data)
    expense_table.setStyle(table_style)
    story.append(expense_table)
    story.append(Spacer(1, 12))

    # Total
    total_eur = total_huf_report * HUF_TO_EUR_RATE
    story.append(Paragraph(f"Total Expenses for {selected_user}: {total_huf_report:.2f} HUF", body_style))
    story.append(Paragraph(f"Total in EUR: {total_eur:.2f} EUR", body_style))
    story.append(Spacer(1, 24))

    # Signature lines
    signature_data = [
        [f'Employee Name: {selected_user}', 'Approval Name: _______________'],
        ['Signature: __________________', 'Signature: __________________']
    ]
    signature_table_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('BOX', (0, 0), (0, -1), 1, colors.black),  # employee box
        ('BOX', (1, 0), (1, -1), 1, colors.black),  # approver box
        ('LEFTPADDING', (0, 0), (1, -1), 10),
        ('RIGHTPADDING', (0, 0), (1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (1, -1), 10),
    ])

    signature_table = Table(signature_data, colWidths=[2.5 * 100, 2.5 * 100])
    signature_table.setStyle(signature_table_style)
    story.append(signature_table)

    # Build the PDF
    doc.build(story)
    messagebox.showinfo("Report Generated", f"PDF report saved as '{file_name}'.")

    # Automatically open the PDF
    os.startfile(file_name)


def on_category_select(event):
    """Changes the state of the Combobox to allow or prevent manual entry."""
    if category_combobox.get() == "Else":
        category_combobox.config(state="normal")
    else:
        category_combobox.config(state="readonly")


# --- GUI Setup ---
root = tk.Tk()
root.title("Expense Tracker")
# root.iconbitmap('icon.ico')

input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
display_frame = ttk.Frame(root, padding="10")
display_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

# --- Input Widgets ---
ttk.Label(input_frame, text="Amount:").grid(row=0, column=0, sticky=tk.W)
amount_entry = ttk.Entry(input_frame, width=15)
amount_entry.grid(row=0, column=1, sticky=tk.W)

ttk.Label(input_frame, text="Currency:").grid(row=0, column=2, sticky=tk.W, padx=(10, 0))
currency_combobox = ttk.Combobox(input_frame, values=list(CURRENCY_RATES.keys()), width=7)
currency_combobox.grid(row=0, column=3, sticky=tk.W)
currency_combobox.set('HUF')
currency_combobox.config(state="readonly")

ttk.Label(input_frame, text="Category:").grid(row=1, column=0, sticky=tk.W)
category_combobox = ttk.Combobox(input_frame, values=categories, width=17)
category_combobox.config(state="readonly")
category_combobox.grid(row=1, column=1, columnspan=2, sticky=tk.W, pady=(5, 0))
category_combobox.bind("<<ComboboxSelected>>", on_category_select)

ttk.Label(input_frame, text="Description:").grid(row=2, column=0, sticky=tk.W)
description_entry = ttk.Entry(input_frame, width=20)
description_entry.grid(row=2, column=1, columnspan=2, sticky=tk.W, pady=(5, 0))

ttk.Label(input_frame, text="User:").grid(row=3, column=0, sticky=tk.W)
user_combobox = ttk.Combobox(input_frame, values=users, width=17)
user_combobox.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=(5, 0))

ttk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=4, column=0, sticky=tk.W)
date_entry = ttk.Entry(input_frame, width=20)
date_entry.grid(row=4, column=1, columnspan=2, sticky=tk.W)
date_entry.insert(0, datetime.date.today().strftime('%Y-%m-%d'))

add_button = ttk.Button(input_frame, text="Add Expense", command=add_expense)
add_button.grid(row=5, column=0, columnspan=4, pady=10)

ttk.Label(input_frame, text="Search:").grid(row=6, column=0, sticky=tk.W, pady=(10, 0))
search_entry = ttk.Entry(input_frame, width=20)
search_entry.grid(row=6, column=1, columnspan=2, pady=(10, 0))
search_entry.bind("<KeyRelease>", filter_expenses)

# --- Display Widgets ---
expense_listbox = tk.Listbox(display_frame, height=10, width=60)
expense_listbox.pack(pady=10)
expense_listbox.bind('<<ListboxSelect>>', on_list_select)

action_button_frame = ttk.Frame(display_frame)
action_button_frame.pack(pady=5)

delete_button = ttk.Button(action_button_frame, text="Delete", command=delete_expense)
modify_button = ttk.Button(action_button_frame, text="Modify", command=modify_expense)
show_chart_button = ttk.Button(action_button_frame, text="Show Chart", command=show_expense_chart)
save_pdf_button = ttk.Button(action_button_frame, text="Save & Print Report", command=save_and_print_report)

delete_button.pack_forget()
modify_button.pack_forget()
show_chart_button.pack(side=tk.LEFT, padx=5)
save_pdf_button.pack(side=tk.LEFT, padx=5)

total_label = ttk.Label(display_frame, text="Total Spent: 0.00 HUF", font=("Helvetica", 12, "bold"))
total_label.pack(pady=5)
total_eur_label = ttk.Label(display_frame, text="Total in EUR: 0.00 EUR", font=("Helvetica", 10))
total_eur_label.pack(pady=5)

# --- Final Code Execution ---
# load_expenses()
root.mainloop()