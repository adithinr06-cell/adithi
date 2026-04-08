import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required data (only first time)
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Natural Language Processing is a fascinating field of Artificial Intelligence."

# Tokenization (splitting text into words)
words = word_tokenize(text)
print("Tokenized Words:", words)

# Removing stopwords (common words like 'is', 'a', 'the')
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

print("After Removing Stopwords:", filtered_words)