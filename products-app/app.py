import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3 

class Product:
    db_name = 'database.db'
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')
        
        # Creating a frame container
        frame = LabelFrame(self.wind, text = 'Register a new product')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = 20)
        
        # Name input
        Label(frame, text = 'Name:').grid(row = 1, column = 0, pady = 5, padx = 5)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1, padx = 10)
        
        # Price input
        Label(frame, text = 'Price:').grid(row = 2, column = 0, pady = 5, padx = 5)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1, padx = 10)
        
        # Button add product
        ttk.Button(frame, text = 'Save product', command = self.add_product).grid(row = 3, columnspan = 2, pady = 5, padx = 5)
        
        # Output messages
        self.message = Label(frame, text = '', fg = 'red')
        self.message.grid(row = 4, column = 0, columnspan = 2, sticky = W + E)
        
        # Table
        self.tree = ttk.Treeview(height = 10, column = 2)
        self.tree.grid(row = 5, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Price', anchor = CENTER)
        
        self.get_products()
    
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_products(self):
        # Cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Quering data    
        query = 'SELECT * FROM product'
        db_rows = self.run_query(query)
        # Filling table
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])
    
    def validation(self):
        return (len(self.name.get()) != 0) and (len(self.price.get()) != 0)
    
    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} added successfully.'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
            
        else:
            self.message['text'] = 'Name and price are required.'
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
