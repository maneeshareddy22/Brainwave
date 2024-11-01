import tkinter as tk
from tkinter import messagebox

# Hardcoded users for login authentication
users = {
    "admin": "password123",
    "user1": "pass456"
}

# In-memory inventory storage
inventory = {}

# Function to add a product to the inventory
def add_product(name, quantity, price):
    inventory[name] = {"quantity": quantity, "price": price}
    messagebox.showinfo("Success", f"Product '{name}' added!")
    display_products()

# Function to delete a product from the inventory
def delete_product(name):
    if name in inventory:
        del inventory[name]
        messagebox.showinfo("Success", f"Product '{name}' deleted!")
        display_products()
    else:
        messagebox.showerror("Error", "Product not found in inventory.")

# Function to show low stock alerts
def low_stock_alert():
    low_stock = [name for name, data in inventory.items() if data["quantity"] < 5]
    if low_stock:
        messagebox.showwarning("Low Stock Alert", f"Low stock on: {', '.join(low_stock)}")
    else:
        messagebox.showinfo("Stock Status", "All products are sufficiently stocked.")

# GUI Application Class
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("600x400")

        # Authentication Frame
        self.auth_frame = tk.Frame(self.root)
        tk.Label(self.auth_frame, text="Username").pack()
        self.username_entry = tk.Entry(self.auth_frame)
        self.username_entry.pack()
        tk.Label(self.auth_frame, text="Password").pack()
        self.password_entry = tk.Entry(self.auth_frame, show="*")
        self.password_entry.pack()
        tk.Button(self.auth_frame, text="Login", command=self.authenticate).pack()
        self.auth_frame.pack()

        # Inventory Frame (initially hidden)
        self.inventory_frame = tk.Frame(self.root)
        tk.Label(self.inventory_frame, text="Product Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.inventory_frame)
        self.name_entry.grid(row=0, column=1)
        
        tk.Label(self.inventory_frame, text="Quantity").grid(row=1, column=0)
        self.quantity_entry = tk.Entry(self.inventory_frame)
        self.quantity_entry.grid(row=1, column=1)
        
        tk.Label(self.inventory_frame, text="Price").grid(row=2, column=0)
        self.price_entry = tk.Entry(self.inventory_frame)
        self.price_entry.grid(row=2, column=1)
        
        tk.Button(self.inventory_frame, text="Add Product", command=self.add_product).grid(row=3, column=0, columnspan=2)
        tk.Button(self.inventory_frame, text="Delete Product", command=self.delete_selected_product).grid(row=4, column=0, columnspan=2)
        tk.Button(self.inventory_frame, text="Low Stock Alert", command=low_stock_alert).grid(row=5, column=0, columnspan=2)

        # Product List Display
        self.product_listbox = tk.Listbox(self.inventory_frame, width=50)
        self.product_listbox.grid(row=6, column=0, columnspan=2)
        self.product_listbox.bind("<Double-1>", self.select_product)

    # Authentication function
    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if users.get(username) == password:
            messagebox.showinfo("Success", "Login successful")
            self.auth_frame.pack_forget()
            self.inventory_frame.pack()
            display_products()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    # Function to add product using entries
    def add_product(self):
        name = self.name_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            price = float(self.price_entry.get())
            if quantity < 0 or price < 0:
                raise ValueError
            add_product(name, quantity, price)
        except ValueError:
            messagebox.showerror("Error", "Quantity and price must be valid numbers")

    # Function to select a product for editing
    def select_product(self, event):
        selected_item = self.product_listbox.get(self.product_listbox.curselection())
        name = selected_item.split(":")[0].strip()
        product = inventory.get(name)
        if product:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, name)
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(tk.END, product["quantity"])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(tk.END, product["price"])

    # Function to delete selected product
    def delete_selected_product(self):
        try:
            selected_item = self.product_listbox.get(self.product_listbox.curselection())
            name = selected_item.split(":")[0].strip()
            delete_product(name)
        except tk.TclError:
            messagebox.showerror("Error", "No product selected for deletion")

# Function to display products in the listbox
def display_products():
    inventory_app.product_listbox.delete(0, tk.END)
    for name, data in inventory.items():
        inventory_app.product_listbox.insert(tk.END, f"{name}: {data['quantity']} units - ${data['price']:.2f} each")

# Main section to run the application
if __name__ == "__main__":
    root = tk.Tk()
    inventory_app = InventoryApp(root)
    root.mainloop()
