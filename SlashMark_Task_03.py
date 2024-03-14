#!/usr/bin/env python
# coding: utf-8

# In[23]:


import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0")
        self.style.configure("TButton", background="#4caf50", foreground="white")

        self.numPasswords_label = ttk.Label(master, text="Number of passwords:", font=("Helvetica", 12))
        self.numPasswords_label.pack(pady=(20, 5))

        self.numPasswords_entry = ttk.Entry(master, font=("Helvetica", 12))
        self.numPasswords_entry.pack(pady=5)

        self.generate_button = ttk.Button(master, text="Generate Passwords", command=self.generate_passwords)
        self.generate_button.pack(pady=10)

        self.output_frame = ttk.Frame(master)
        self.output_frame.pack(pady=10)

        self.passwords_label = ttk.Label(self.output_frame, text="Generated Passwords:", font=("Helvetica", 12))
        self.passwords_label.pack()

        self.passwords_text = tk.Text(self.output_frame, height=8, width=40, font=("Helvetica", 11))
        self.passwords_text.pack()

    def generate_password(self, pwlength, min_uppercase=1, min_lowercase=1, min_number=1, min_symbol=0, exclude_similar=True):
        char_sets = {
            "uppercase": string.ascii_uppercase,
            "lowercase": string.ascii_lowercase,
            "numbers": string.digits,
            "symbols": string.punctuation
        }
        similar_chars = {"0": "O", "1": "l", "5": "S", "B": "8"}
        used_sets = []
        password = ""

        for char_set, min_count in [("uppercase", min_uppercase), ("lowercase", min_lowercase),
                                    ("numbers", min_number), ("symbols", min_symbol)]:
            if min_count > 0:
                used_sets.append(char_set)
                char_pool = char_sets[char_set]
                if exclude_similar and char_set in similar_chars.keys():
                    char_pool = [char for char in char_pool if char not in similar_chars[char_set]]
                password += random.choice(char_pool)

        remaining_length = pwlength - len(password)
        allowed_sets = list(char_sets.keys()) if min_symbol > 0 else ["uppercase", "lowercase", "numbers"]
        for _ in range(remaining_length):
            char_set = random.choice(allowed_sets)
            char_pool = char_sets[char_set]
            if exclude_similar and char_set in similar_chars.keys():
                char_pool = [char for char in char_pool if char not in similar_chars[char_set]]
            password += random.choice(char_pool)

        password_list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)

        return password

    def generate_passwords(self):
        self.passwords_text.delete('1.0', tk.END)
        try:
            num_passwords = int(self.numPasswords_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        if num_passwords <= 0:
            messagebox.showerror("Error", "Number of passwords must be greater than 0.")
            return

        for i in range(num_passwords):
            length = random.randint(10, 16)  # Random length between 10 and 16
            min_uppercase = random.randint(1, 3)
            min_lowercase = random.randint(1, 3)
            min_number = random.randint(1, 3)
            min_symbol = random.randint(0, 2)
            exclude_similar = random.choice([True, False])

            password = self.generate_password(length, min_uppercase, min_lowercase, min_number, min_symbol, exclude_similar)
            self.passwords_text.insert(tk.END, f"Password {i+1}: {password}\n")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




