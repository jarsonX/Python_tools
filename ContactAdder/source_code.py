import os
import csv
import tkinter as tk

# Create Tkinter window
window = tk.Tk()
window.title("Contacts App")

# Define function to save data to CSV file
def save_contact():
    # Get user input
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    telephone = telephone_entry.get()

    # Create path to desktop and CSV file
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    filename = os.path.join(desktop, 'contacts.csv')

    # Write data to CSV file
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Check if file is empty, if yes add header to csv
        if os.stat(filename).st_size == 0:
            writer.writerow(['First Name', 'Last Name', 'Telephone'])
        writer.writerow([first_name, last_name, telephone])

    # Reset input fields
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    telephone_entry.delete(0, tk.END)

    # Show success message
    success_label.config(text="Contact saved successfully")

# Create input fields and labels
first_name_label = tk.Label(window, text="First Name:")
first_name_entry = tk.Entry(window)
last_name_label = tk.Label(window, text="Last Name:")
last_name_entry = tk.Entry(window)
telephone_label = tk.Label(window, text="Telephone:")
telephone_entry = tk.Entry(window)

# Create save button
save_button = tk.Button(window, text="Save", command=save_contact)

# Create success label
success_label = tk.Label(window, fg="green")

# Add input fields, labels, and save button to window
first_name_label.grid(row=0, column=0)
first_name_entry.grid(row=0, column=1)
last_name_label.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
telephone_label.grid(row=2, column=0)
telephone_entry.grid(row=2, column=1)
save_button.grid(row=3, column=0, columnspan=2)
success_label.grid(row=4, column=0, columnspan=2)

# Run Tkinter window
window.mainloop()
