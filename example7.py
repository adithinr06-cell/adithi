# Sample text
text = "Natural Language Processing is a fascinating field of Artificial Intelligence."

# Convert to lowercase
text = text.lower()

# Remove punctuation
punctuation = ".,!?;:"
for p in punctuation:
    text = text.replace(p, "")

# Tokenization (split into words)
words = text.split()

print("Tokenized Words:", words)

# Define simple stopwords list
stopwords = ["is", "a", "the", "of", "and", "in", "to", "for"]

# Remove stopwords
filtered_words = []
for word in words:
    if word not in stopwords:
        filtered_words.append(word)

print("After Removing Stopwords:", filtered_words)