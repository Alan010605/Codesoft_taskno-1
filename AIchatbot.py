
def chatbot():
    print("AI Chatbot: Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("AI Chatbot: Hi there! How can I assist you?")
        elif "your name" in user_input:
            print("AI Chatbot: I’m your friendly chatbot.")
        elif "bye" in user_input:
            print("AI Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("AI Chatbot: Sorry, I didn’t understand that.")

chatbot()
