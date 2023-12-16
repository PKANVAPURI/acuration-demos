from bs4 import BeautifulSoup
import re

def clean_html_and_extract_text(html_text):
    # Parse the HTML document using BeautifulSoup
    soup = BeautifulSoup(html_text, 'html.parser')

    # Extract text content without HTML tags
    text = soup.get_text(separator='\n')  # Preserve newlines

    # Remove special characters and extra whitespaces
    text = re.sub(r'[^\w\s\n]', '', text)  # Remove special characters except for whitespace and newline

    # Normalize the text (convert to lowercase, for example)
    text = text.lower()

    return text

