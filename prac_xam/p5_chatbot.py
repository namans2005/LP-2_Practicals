print("------------------------------------------------------")
print("chatbot: Hello! Welcome to Customer Support.")
print("Chatbot: How can I help you?")
print("Type: order, return, contact, or exit")
print("------------------------------------------------------")
def chatbot():
    while True:
        user = input("You: ").lower()
        if user == "order":
            print("Chatbot: Your order is being processed.")
        elif user == "return":
            print("Chatbot: You can return products within 30 days.")
        elif user == "contact":
            print("Chatbot: Call us at 112.")
        elif user == "refund":
            print("chatbot:your amount credited in your account within 2 days. ")
        elif user == "delivery":
            print("chatbot:delivery are procced within a week.")
        elif user == "payment":
            print("chatbot:We accepted credit cards, UPI , cash ")
        elif user == "exit":
            print("Chatbot:Thank you! Have a nice day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand. Please try again.")
chatbot()