import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')  # Only needed once; comment out after first run

# Define the target URL and keywords with corresponding filenames
target_url = 'https://www.cnn.com/2024/04/28/politics/cnn-poll-trump-biden-matchup/index.html'
keywords_to_files = {
    'trump': 'trump.txt',
    'biden': 'biden.txt',
    'election': 'election.txt'
}

# Fetch the web page
response = requests.get(target_url)
response.raise_for_status()  # Check for request errors
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the paragraphs from the specific class
paragraphs = soup.find_all('p', class_='paragraph inline-placeholder')

# Get combined text from the paragraphs
text = ' '.join(p.get_text(strip=True) for p in paragraphs)

# Tokenize the text into sentences
sentences = nltk.tokenize.sent_tokenize(text)

# Function to find sentences containing the keyword and write to file
def find_sentences_and_write(sentences, keyword, filename):
    keyword = keyword.lower()
    with open(filename, 'w') as file:  # 'w' to write anew each time the script runs
        for sentence in sentences:
            if keyword in sentence.lower():
                file.write(sentence + "\n\n")  # Write the sentence to the file

# Process each keyword and associated file
for keyword, filename in keywords_to_files.items():
    find_sentences_and_write(sentences, keyword, filename)

print("Relevant sentences have been successfully written to their respective files.")
