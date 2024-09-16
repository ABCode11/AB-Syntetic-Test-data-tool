import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from faker import Faker
import pandas as pd
import random

class SyntheticDataGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Synthetic Test Data Generator")
        self.faker = Faker()
       
        self.create_widgets()

    def create_widgets(self):
        # Data Type Selection
        ttk.Label(self.master, text="Data Type:").grid(row=0, column=0, padx=5, pady=5)
        self.data_type = ttk.Combobox(self.master, values=["Personal", "Financial", "Product"])
        self.data_type.grid(row=0, column=1, padx=5, pady=5)
        self.data_type.set("Personal")

        # Field Configuration
        ttk.Label(self.master, text="Fields:").grid(row=1, column=0, padx=5, pady=5)
        self.fields_frame = ttk.Frame(self.master)
        self.fields_frame.grid(row=1, column=1, padx=5, pady=5)
        self.fields = []
        self.add_field()

        ttk.Button(self.master, text="Add Field", command=self.add_field).grid(row=2, column=1, padx=5, pady=5)

        # Record Count
        ttk.Label(self.master, text="Record Count:").grid(row=3, column=0, padx=5, pady=5)
        self.record_count = ttk.Entry(self.master)
        self.record_count.grid(row=3, column=1, padx=5, pady=5)
        self.record_count.insert(0, "100")

        # Generate Button
        ttk.Button(self.master, text="Generate Data", command=self.generate_data).grid(row=4, column=1, padx=5, pady=5)

    def add_field(self):
        field_frame = ttk.Frame(self.fields_frame)
        field_frame.pack(fill=tk.X)

        field_name = ttk.Entry(field_frame, width=20)
        field_name.pack(side=tk.LEFT, padx=2)
        field_name.insert(0, f"Field{len(self.fields)+1}")

        field_type = ttk.Combobox(field_frame, values=["Name", "Email", "Phone", "Date", "Number"], width=10)
        field_type.pack(side=tk.LEFT, padx=2)
        field_type.set("Name")

        self.fields.append((field_name, field_type))

    def generate_data(self):
        try:
            count = int(self.record_count.get())
            data = []

            for _ in range(count):
                record = {}
                for name_widget, type_widget in self.fields:
                    field_name = name_widget.get()
                    field_type = type_widget.get()
                   
                    if field_type == "Name":
                        record[field_name] = self.faker.name()
                    elif field_type == "Email":
                        record[field_name] = self.faker.email()
                    elif field_type == "Phone":
                        record[field_name] = self.faker.phone_number()
                    elif field_type == "Date":
                        record[field_name] = self.faker.date()
                    elif field_type == "Number":
                        record[field_name] = random.randint(1, 1000)

                data.append(record)

            df = pd.DataFrame(data)
            file_path = filedialog.asksaveasfilename(defaultextension=".csv")
            if file_path:
                df.to_csv(file_path, index=False)
                messagebox.showinfo("Success", f"Data saved to {file_path}")
            else:
                messagebox.showwarning("Cancelled", "Data generation cancelled")

        except ValueError:
            messagebox.showerror("Error", "Invalid record count")

if __name__ == "__main__":
    root = tk.Tk()
    app = SyntheticDataGenerator(root)
    root.mainloop() 