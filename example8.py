# Simple Sentiment Analysis (No external libraries)

# Predefined word lists
positive_words = [
    "happy", "good", "great", "excellent", "awesome", "love", "nice", "amazing", "wonderful", "fantastic"
]

negative_words = [
    "sad", "bad", "terrible", "awful", "hate", "worst", "angry", "upset", "depressed", "pain"
]

# Take input from user
text = input("Enter a sentence: ")

# Preprocess text
text = text.lower()

# Remove punctuation
punctuation = ".,!?;:"
for p in punctuation:
    text = text.replace(p, "")

# Tokenize
words = text.split()

# Initialize counters
pos_count = 0
neg_count = 0

# Count sentiment words
for word in words:
    if word in positive_words:
        pos_count += 1
    elif word in negative_words:
        neg_count += 1

# Decide sentiment
if pos_count > neg_count:
    print("Sentiment: Positive 😊")
elif neg_count > pos_count:
    print("Sentiment: Negative (Sad) 😔")
else:
    print("Sentiment: Neutral 😐")