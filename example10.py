# Sentence Type Classifier (No external libraries)

def classify_sentence(sentence):
    s = sentence.strip()

    # Lists for basic NLP detection
    question_words = ["what", "why", "how", "when", "where", "who", "which", "whom", "whose"]
    imperative_starters = ["please", "do", "don't", "kindly", "let", "go", "stop", "give", "take", "open", "close", "bring"]

    # Convert to lowercase for checking
    lower_s = s.lower()
    words = lower_s.split()

    # 1. Exclamatory
    if s.endswith("!"):
        return "Exclamatory 😲"

    # 2. Interrogative
    if s.endswith("?") or (words and words[0] in question_words):
        return "Interrogative (Question) ❓"

    # 3. Imperative
    if words and (words[0] in imperative_starters or words[0].endswith("!")):
        return "Imperative (Command/Request) 🗣️"

    # 4. Default → Declarative
    return "Declarative (Statement) 📄"


# -------- MAIN PROGRAM --------
sentence = input("Enter a sentence:\n")

result = classify_sentence(sentence)

print("\nSentence Type:", result)