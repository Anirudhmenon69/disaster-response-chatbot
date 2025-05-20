def respond_to_input(user_input):
    responses = {
        "hello": "Hello! How can I help you during this disaster?",
        "help": "Please provide your location and the kind of assistance you need.",
        "evacuate": "If you need to evacuate, follow the nearest safe route marked on your map."
    }
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "Sorry, I didn't understand. Can you please rephrase?"

if __name__ == "__main__":
    print("Disaster Response Chatbot running...")
    while True:
        user_text = input("You: ")
        if user_text.lower() in ['exit', 'quit']:
            print("Chatbot exiting. Stay safe!")
            break
        print("Bot:", respond_to_input(user_text))