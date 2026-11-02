import re
import random


responses = {
    "hello": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you."
    ],

    "name": [
        "I am a simple Python chatbot.",
        "My name is AI Bot."
    ],

    "how are you": [
        "I am fine. How are you?",
        "I am doing great!"
    ],

    "college": [
        "College is a place for learning.",
        "Keep studying and achieve your goals!"
    ],

    "bye": [
        "Goodbye! Have a nice day.",
        "See you again!"
    ]
}


def chatbot(user_input):

    text = user_input.lower()

    if re.search(r"\b(hello|hi|hey)\b", text):
        return random.choice(responses["hello"])

    elif "your name" in text or "who are you" in text:
        return random.choice(responses["name"])

    elif "how are you" in text:
        return random.choice(responses["how are you"])

    elif "college" in text:
        return random.choice(responses["college"])

    elif re.search(r"\b(bye|goodbye)\b", text):
        return random.choice(responses["bye"])

    else:
        return "Sorry, I don't understand. Please try again."


print("AI Chatbot Started!")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ")

    response = chatbot(user)

    print("Bot:", response)

    if re.search(r"\b(bye|goodbye)\b", user.lower()):
        break