import tkinter as tk
from tkinter import StringVar, ttk
import yaml
import unicodedata

# Function to remove diacritics from Greek characters
def remove_diacritics(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

# Load the YAML lexicon
with open('lexemes.yaml', 'r', encoding='utf-8') as file:
    lexicon = yaml.safe_load(file)

# Dictionary to convert QWERTY input to Greek letters
similar_letters = {
    'a': ['α', 'ά', 'ἀ', 'ἁ', 'ἂ', 'ἃ', 'ἄ', 'ἅ', 'ἆ', 'ἇ'],
    'b': ['β'],
    'c': ['ς'],
    'g': ['γ'],
    'd': ['δ'],
    'e': ['ε', 'έ', 'ἐ', 'ἑ', 'ἒ', 'ἓ', 'ἔ', 'ἕ'],
    'z': ['ζ'],
    'h': ['η', 'ή', 'ἠ', 'ἡ', 'ἢ', 'ἣ', 'ἤ', 'ἥ', 'ἦ', 'ἧ'],
    'th': ['θ'],
    'i': ['ι', 'ί', 'ἰ', 'ἱ', 'ἲ', 'ἳ', 'ἴ', 'ἵ', 'ἶ', 'ἷ'],
    'k': ['κ'],
    'l': ['λ'],
    'm': ['μ'],
    'n': ['ν'],
    'x': ['ξ'],
    'o': ['ο', 'ό', 'ὀ', 'ὁ', 'ὂ', 'ὃ', 'ὄ', 'ὅ'],
    'p': ['π'],
    'r': ['ρ', 'ῤ', 'ῥ'],
    's': ['σ'],
    't': ['τ'],
    'u': ['υ', 'ύ', 'ὑ', 'ὕ', 'ὒ', 'ὓ', 'ὖ', 'ὗ'],
    'ph': ['φ'],
    'ch': ['χ'],
    'ps': ['ψ'],
    'w': ['ω', 'ώ', 'ὠ', 'ὡ', 'ὢ', 'ὣ', 'ὤ', 'ὥ', 'ὦ', 'ὧ']
}

# Function to convert QWERTY input to Greek
def convert_qwerty_to_greek(word):
    greek_word = word
    # Handle digraphs first (like "th" for θ, "ph" for φ)
    for qwerty_char, greek_chars in [('th', 'θ'), ('ph', 'φ'), ('ch', 'χ'), ('ps', 'ψ')]:
        greek_word = greek_word.replace(qwerty_char, greek_chars)
    
    # Then handle single letter replacements
    for qwerty_char, greek_chars in similar_letters.items():
        if qwerty_char in greek_word:
            # Replace with the first Greek equivalent
            greek_word = greek_word.replace(qwerty_char, greek_chars[0])
    
    return greek_word

# Search function to handle both QWERTY input and diacritic normalization
def search_word_combined(word):
    # Convert QWERTY to Greek
    greek_word = convert_qwerty_to_greek(word)
    
    # Remove diacritics from the input
    normalized_input = remove_diacritics(greek_word)
    
    matches = []
    for lemma, data in lexicon.items():
        normalized_lemma = remove_diacritics(lemma)
        if normalized_input in normalized_lemma:  # Search using the normalized input
            matches.append((lemma, data))
    
    return matches

# Callback for search
def search_and_display():
    word = greek_input.get()
    result_list.delete(0, tk.END)
    
    results = search_word_combined(word)
    
    if results:
        for lemma, data in results:
            result_list.insert(tk.END, f"Word: {lemma}")
            # Display only glossary
            if 'gloss' in data:
                result_list.insert(tk.END, f"Meaning: {data['gloss']}")
            # Insert an empty line for spacing
            result_list.insert(tk.END, "")  # This creates a blank line between results
    else:
        result_list.insert(tk.END, "No match found.")



# GUI Setup
root = tk.Tk()
root.title("Curly Sigma - Greek Translator")

# Greek Word Input Field
greek_input = StringVar()
input_label = tk.Label(root, text="Enter Greek Word:")
input_label.pack(pady=5)
input_entry = tk.Entry(root, textvariable=greek_input, font=('Arial', 16))
input_entry.pack(pady=5)

# Dropdown Menu for Grammatical Form
form_var = StringVar(value="All Forms")
forms = ["All Forms", "Noun", "Verb", "Adjective", "Adverb"] 
form_label = tk.Label(root, text="Select Grammatical Form:")
form_label.pack(pady=5)
form_dropdown = ttk.Combobox(root, textvariable=form_var, values=forms, state="readonly")
form_dropdown.pack(pady=5)

# Search Button
search_button = tk.Button(root, text="Search", command=search_and_display)
search_button.pack(pady=5)

# Listbox to Display Results
result_list = tk.Listbox(root, width=50, height=10)
result_list.pack(pady=10)

# Virtual Keyboard Frame
keyboard_frame = tk.Frame(root)
keyboard_frame.pack(pady=5)

# Updated Greek alphabet split into 4 rows (lowercase, uppercase, special characters)
rows = [
    ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ'],
    ['ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω'],
    ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ'],
    ['Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
]

# Add special characters buttons with comments
special_buttons = [
    ('ς', '     Curly Sigma - Greek Translator')
]

# Function to add Greek alphabet buttons to the GUI
def create_keyboard(frame, rows):
    for row in rows:
        row_frame = tk.Frame(frame)
        row_frame.pack()
        for char in row:
            button = tk.Button(row_frame, text=char, command=lambda c=char: insert_char(c), width=3)
            button.pack(side=tk.LEFT, padx=1)

# Add the alphabet and special characters to the virtual keyboard
create_keyboard(keyboard_frame, rows)

# Create a separate row for special characters
special_frame = tk.Frame(root)
special_frame.pack(pady=5)


# Create buttons with comments
for char, comment in special_buttons:
    row = tk.Frame(special_frame)
    row.pack(pady=2)
    button = tk.Button(row, text=char, command=lambda c=char: insert_char(c), width=3)
    button.pack(side=tk.LEFT, padx=1)
    label = tk.Label(row, text=comment, font=('Arial', 10))
    label.pack(side=tk.LEFT, padx=5)


# Insert character from virtual keyboard
def insert_char(char):
    current_text = greek_input.get()
    new_text = current_text + char
    greek_input.set(new_text)
    
    # Move the cursor to the right (end of the text)
    input_entry.icursor(tk.END)

# Run the app
root.mainloop()
