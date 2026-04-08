# Text Extractor (No external libraries)

def extract_emails(text):
    words = text.split()
    emails = []
    for word in words:
        if "@" in word and "." in word:
            emails.append(word.strip(".,!?"))
    return emails


def extract_phone_numbers(text):
    words = text.split()
    phones = []
    for word in words:
        if word.isdigit() and (10 <= len(word) <= 12):
            phones.append(word)
    return phones


def extract_urls(text):
    words = text.split()
    urls = []
    for word in words:
        if word.startswith("http") or word.startswith("www"):
            urls.append(word.strip(".,!?"))
    return urls


def extract_numbers(text):
    words = text.split()
    numbers = []
    for word in words:
        if word.isdigit():
            numbers.append(word)
    return numbers


def extract_keywords(text):
    stopwords = ["is", "a", "the", "and", "in", "on", "at", "to", "for", "of"]
    
    # Clean text
    text = text.lower()
    punctuation = ".,!?;:"
    for p in punctuation:
        text = text.replace(p, "")
    
    words = text.split()
    
    keywords = []
    for word in words:
        if word not in stopwords:
            keywords.append(word)
    
    return keywords


# -------- MAIN PROGRAM --------
text = input("Enter your text:\n")

print("\n--- Extracted Information ---")

print("Emails:", extract_emails(text))
print("Phone Numbers:", extract_phone_numbers(text))
print("URLs:", extract_urls(text))
print("Numbers:", extract_numbers(text))
print("Keywords:", extract_keywords(text))