import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext, font
import os

# Function to load recipes from file
def load_recipes():
    if not os.path.exists("recipes.txt"):
        with open("recipes.txt", "w") as file:
            file.write("{}")
        return {}
    
    with open("recipes.txt", "r") as file:
        content = file.read()
        return eval(content) if content else {}

# Function to save recipes to file
def save_recipes(recipes):
    with open("recipes.txt", "w") as file:
        file.write(str(recipes))

# Function to add a recipe
def add_recipe(name, ingredients, instructions, recipes):
    recipes[name] = {'Ingredients': ingredients, 'Instructions': instructions}
    save_recipes(recipes)
    messagebox.showinfo("Success", f"Recipe for {name} added successfully!")

# Function to display a recipe
def view_recipe(name, recipes):
    recipe = recipes.get(name)
    if recipe:
        messagebox.showinfo(name, f"Ingredients: {', '.join(recipe['Ingredients'])}\\nInstructions: {recipe['Instructions']}")
    else:
        messagebox.showerror("Error", "Recipe not found.")

# Function to view all recipes
def view_all_recipes(recipes):
    if recipes:
        results = ""
        for name, recipe in recipes.items():
            results += f"Recipe: {name}\\nIngredients: {', '.join(recipe['Ingredients'])}\\nInstructions: {recipe['Instructions']}\\n\\n"
        
        scrolled_text = scrolledtext.ScrolledText(root, width=40, height=10)
        scrolled_text.insert(tk.INSERT, results)
        scrolled_text.pack()
    else:
        messagebox.showinfo("View Recipes", "No recipes available.")

# Function to search for recipes
def search_recipe(keyword, recipes):
    found = False
    results = ""
    for name, recipe in recipes.items():
        if keyword.lower() in name.lower() or keyword.lower() in ' '.join(recipe['Ingredients']).lower() or keyword.lower() in recipe['Instructions'].lower():
            results += f"Recipe: {name}\\nIngredients: {', '.join(recipe['Ingredients'])}\\nInstructions: {recipe['Instructions']}\\n\\n"
            found = True
    if found:
        scrolled_text = scrolledtext.ScrolledText(root, width=40, height=10)
        scrolled_text.insert(tk.INSERT, results)
        scrolled_text.pack()
    else:
        messagebox.showinfo("Search Results", "No recipes found for the given keyword.")

# Tkinter UI Functions
def add_recipe_ui():
    name = simpledialog.askstring("Add Recipe", "Enter the recipe name:")
    if name:
        ingredients = simpledialog.askstring("Add Recipe", "Enter the ingredients (comma-separated):").split(',')
        instructions = simpledialog.askstring("Add Recipe", "Enter the instructions:")
        add_recipe(name, ingredients, instructions, recipes)

def view_recipes_ui():
    view_all_recipes(recipes)

def search_recipes_ui():
    keyword = simpledialog.askstring("Search Recipe", "Enter a keyword to search for a recipe:")
    if keyword:
        search_recipe(keyword, recipes)

# Load recipes
recipes = load_recipes()

# Main Window Setup
root = tk.Tk()
root.title("Recipe Organizer")
root.geometry("500x400") # Adjust window size
root.configure(bg="#f0f0f0") # Set background color

# Custom Fonts
title_font = font.Font(family="Helvetica", size=12, weight="bold")
button_font = font.Font(family="Helvetica", size=10)

# Add buttons for Add, View, Search, Exit
add_button = tk.Button(root, text="Add Recipe", command=add_recipe_ui, font=button_font, bg="#4caf50", fg="white", pady=5, width=20)
add_button.pack(pady=10, padx=20)

view_button = tk.Button(root, text="View Recipes", command=view_recipes_ui, font=button_font, bg="#2196f3", fg="white", pady=5, width=20)
view_button.pack(pady=10, padx=20)

search_button = tk.Button(root, text="Search Recipes", command=search_recipes_ui, font=button_font, bg="#ff9800", fg="white", pady=5, width=20)
search_button.pack(pady=10, padx=20)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=button_font, bg="#f44336", fg="white", pady=5, width=20)
exit_button.pack(pady=10, padx=20)

root.mainloop()
