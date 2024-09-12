# Curly Sigma - Greek Translator

This is a Tkinter-based desktop application designed to help users search for Greek words, their meanings, and grammatical forms. The app allows users to input Greek words either through a QWERTY keyboard or a virtual Greek keyboard provided in the interface. It also provides a flexible search system that handles both direct Greek input and transliterations from QWERTY input.

## Features

- **QWERTY to Greek Conversion**: Automatically convert transliterations from a QWERTY keyboard into the corresponding Greek letters.
- **Diacritic Handling**: Search functionality normalizes input by removing diacritics, making it easier to find words regardless of their specific accents.
- **Virtual Greek Keyboard**: Provides a set of buttons to input Greek letters directly, including special characters.
- **Search Filters**: Allows users to filter results by grammatical form, such as nouns, verbs, adjectives, and adverbs.
- **Search Results Display**: Displays matched Greek words along with their full-citation forms and glosses.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/alanmaizon/curly-sigma.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd curly-sigma
   ```
3. **Install Dependencies**:
   Make sure you have Python installed, then install the required libraries:
   ```bash
   pip install pyyaml
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

## Usage

1. **Enter Greek Words**:
   - You can type in Greek words directly if you have a Greek keyboard layout enabled.
   - Alternatively, you can use the QWERTY keyboard to type transliterations. The app will convert these into Greek letters.

2. **Use the Virtual Keyboard**:
   - Click on the Greek letters provided in the virtual keyboard to enter them into the search field.
   - Special characters are accompanied by comments to help you understand their usage.

3. **Filter by Grammatical Form**:
   - Use the dropdown menu to select a specific grammatical form (e.g., Noun, Verb) if you wish to filter the search results.

4. **Search**:
   - Click the "Search" button to find matching Greek words in the lexicon.
   - The results, including the word's full-citation form and gloss, will be displayed in the results list.

5. **Review Results**:
   - The results are displayed with a blank line between each entry for easy readability.

## Lexicon Data

The app uses a YAML file (`lexemes.yaml`) as its lexicon. This file contains Greek words, their full-citation forms, glosses, and other relevant data. Make sure to update this file if you wish to expand the dictionary.

## Customization

- **Adding More Characters**: You can extend the `similar_letters` dictionary in the code to include more transliteration rules.
- **Updating the Lexicon**: Modify `lexemes.yaml` to add or edit Greek words and their corresponding data.

## Contributing

Feel free to submit issues, fork the repository, and make pull requests. Contributions are welcome!

## Acknowledgements

This app was developed using Python's Tkinter library and YAML for data management. Special thanks to all contributors and open-source projects that made this possible.

---
