"""
Develop an elementary chatbot for any suitable customer interaction
application.
"""

#=============================
#Basic Emergency Chatbot
#=============================

intents = {
    "police":["theft", "fight", "crime"],
    "fire":["fire", "smoke", "blast"],
    "ambulance":["injury", "accident", "medical"],
    "electricity":["power cut", "no electricity"],
    "water":["no water", "leakage"]
}

helplines = {
    "police":100,
    "fire":101,
    "ambulance":102,
    "electricity":103,
    "water":104
}

def detect_intent(text):
    text = text.lower()
    for dept, words in intents.items():
        for word in words:
            if word in text:
                return dept
    return None

print("Emergency Chatbot")
print("Type 'exit' to stop\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Stay safe. Goodbye.")
        break

    dept = detect_intent(user_input)

    if dept:
        print(f"Bot: {dept.capitalize()} emergency detected.")
        print(f"Helpline Number: {helplines[dept]}\n")
    else:
        print("Bot: Could not understand. Please describe emergency.\n")
    