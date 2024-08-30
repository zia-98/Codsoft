import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x500")

        # Create a main frame
        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a frame for adding contacts
        self.add_contact_frame = tk.LabelFrame(self.main_frame, text="Add New Contact", padx=10, pady=10)
        self.add_contact_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Labels and Entry fields for adding contacts
        self.name_label = tk.Label(self.add_contact_frame, text="Name:")
        self.name_entry = tk.Entry(self.add_contact_frame, width=40)
        self.phone_label = tk.Label(self.add_contact_frame, text="Phone Number:")
        self.phone_entry = tk.Entry(self.add_contact_frame, width=40)
        self.email_label = tk.Label(self.add_contact_frame, text="Email:")
        self.email_entry = tk.Entry(self.add_contact_frame, width=40)
        self.address_label = tk.Label(self.add_contact_frame, text="Address:")
        self.address_entry = tk.Entry(self.add_contact_frame, width=40)

        # Button for adding contacts
        self.add_button = tk.Button(self.add_contact_frame, text="Add Contact", command=self.add_contact, width=20)

        # Place widgets in the add_contact_frame
        self.name_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.phone_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        self.email_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        self.address_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Create a frame for contact list and actions
        self.list_frame = tk.LabelFrame(self.main_frame, text="Contacts", padx=10, pady=10)
        self.list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Listbox to display contact list
        self.contact_list = tk.Listbox(self.list_frame, width=60, height=10)
        self.contact_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.contact_list.bind('<<ListboxSelect>>', self.on_contact_select)

        # Scrollbars for the listbox
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contact_list.yview)

        # Buttons for viewing, searching, updating, and deleting contacts
        self.view_button = tk.Button(self.main_frame, text="View Contact List", command=self.view_contacts, width=20)
        self.search_button = tk.Button(self.main_frame, text="Search Contact", command=self.search_contact, width=20)
        self.update_button = tk.Button(self.main_frame, text="Update Contact", command=self.edit_contact, width=20)
        self.delete_button = tk.Button(self.main_frame, text="Delete Contact", command=self.delete_contact, width=20)

        # Place buttons in the main frame
        self.view_button.grid(row=2, column=0, pady=5)
        self.search_button.grid(row=3, column=0, pady=5)
        self.update_button.grid(row=4, column=0, pady=5)
        self.delete_button.grid(row=5, column=0, pady=5)

        # Create a frame for displaying contact details
        self.details_frame = tk.LabelFrame(self.main_frame, text="Contact Details", padx=10, pady=10)
        self.details_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Labels for displaying contact details
        self.details_name_label = tk.Label(self.details_frame, text="Name:")
        self.details_phone_label = tk.Label(self.details_frame, text="Phone Number:")
        self.details_email_label = tk.Label(self.details_frame, text="Email:")
        self.details_address_label = tk.Label(self.details_frame, text="Address:")

        # Display fields for contact details
        self.details_name = tk.Label(self.details_frame, text="")
        self.details_phone = tk.Label(self.details_frame, text="")
        self.details_email = tk.Label(self.details_frame, text="")
        self.details_address = tk.Label(self.details_frame, text="")

        # Place widgets in the details_frame
        self.details_name_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.details_name.grid(row=0, column=1, padx=5, pady=5)
        self.details_phone_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.details_phone.grid(row=1, column=1, padx=5, pady=5)
        self.details_email_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.details_email.grid(row=2, column=1, padx=5, pady=5)
        self.details_address_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.details_address.grid(row=3, column=1, padx=5, pady=5)

        # Initialize contact list
        self.contacts = []

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            self.contact_list.insert(tk.END, name)
            self.clear_fields()
            self.show_message("Contact Added", f"{name} has been added successfully!")
        else:
            self.show_message("Input Error", "Name and Phone Number are required!")

    def view_contacts(self):
        self.contact_list.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_list.insert(tk.END, contact["name"])

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter contact name:")
        if search_term:
            self.contact_list.delete(0, tk.END)
            for contact in self.contacts:
                if search_term.lower() in contact["name"].lower():
                    self.contact_list.insert(tk.END, contact["name"])
                    break
            else:
                self.show_message("Search Result", "No contact found with that name!")

    def edit_contact(self):
        selected_index = self.contact_list.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            self.open_edit_dialog(index, contact)

    def open_edit_dialog(self, index, contact):
        edit_dialog = Toplevel(self.root)
        edit_dialog.title("Edit Contact")
        edit_dialog.geometry("300x250")

        # Labels and Entry fields for editing contacts
        tk.Label(edit_dialog, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        name_entry = tk.Entry(edit_dialog, width=30)
        name_entry.insert(0, contact["name"])
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(edit_dialog, text="Phone Number:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        phone_entry = tk.Entry(edit_dialog, width=30)
        phone_entry.insert(0, contact["phone"])
        phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(edit_dialog, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        email_entry = tk.Entry(edit_dialog, width=30)
        email_entry.insert(0, contact["email"])
        email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(edit_dialog, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        address_entry = tk.Entry(edit_dialog, width=30)
        address_entry.insert(0, contact["address"])
        address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Save button
        save_button = tk.Button(edit_dialog, text="Save", command=lambda: self.save_contact(index, name_entry, phone_entry, email_entry, address_entry, edit_dialog))
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_contact(self, index, name_entry, phone_entry, email_entry, address_entry, dialog):
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone:
            self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            self.view_contacts()
            dialog.destroy()
            self.show_message("Contact Updated", f"{name} has been updated successfully!")
        else:
            self.show_message("Input Error", "Name and Phone Number are required!")

    def delete_contact(self):
        selected_index = self.contact_list.curselection()
        if selected_index:
            index = selected_index[0]
            name = self.contacts[index]["name"]
            confirm = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {name}?")
            if confirm:
                del self.contacts[index]
                self.contact_list.delete(index)
                self.clear_fields()
                self.show_message("Contact Deleted", f"{name} has been deleted successfully!")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def on_contact_select(self, event):
        selected_index = self.contact_list.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            self.update_details_frame(contact)

    def update_details_frame(self, contact):
        self.details_name.config(text=contact["name"])
        self.details_phone.config(text=contact["phone"])
        self.details_email.config(text=contact["email"])
        self.details_address.config(text=contact["address"])

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    contact_manager = ContactManager(root)
    root.mainloop()
