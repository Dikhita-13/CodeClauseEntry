import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    [r"how are you", ["I'm a bot, but I'm doing great! How about you?", "Feeling chatty today!"]],
    [r"what is your name", ["I'm a simple chatbot created using NLTK."]],
    [r"(.*) your name", ["I go by ChatBot, what's yours?"]],
    [r"what can you do", ["I can chat with you, answer simple questions, and keep you entertained!"]],
    [r"tell me a joke", ["Why don't programmers like nature? Because it has too many bugs!", "Why do Java developers wear glasses? Because they don’t C#!"]],
    [r"favorite color", ["I like blue, just like the sky!", "I like green, like fresh code!"]],
    [r"what is love", ["Love is a complex emotion that I, as a bot, am still trying to understand."]],
    [r"who created you", ["I was created by a talented developer using Python and NLTK!"]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "See you soon!"]],
    [r"what's your favorite food", ["I don't eat, but I hear pizza is amazing!", "Code is my fuel!"]],
    [r"do you like music", ["Yes! I enjoy listening to binary beats!", "Music is great! What's your favorite song?"]],
    [r"who is the president of the USA", ["As of my last update, it's Joe Biden."]],
    [r"what is AI", ["AI stands for Artificial Intelligence, which enables machines to think and learn!"]],
    [r"do you sleep", ["Nope! I’m always awake to chat with you."]],
    [r"can you do math", ["Yes! Try asking me a simple math problem."]],
    [r"what's the capital of France", ["Paris is the capital of France."]],
    [r"how old are you", ["I'm as old as the code that runs me!"]],
    [r"what is your purpose", ["My purpose is to chat with you and make your day better!"]],
    [r"(.*)", ["Sorry, I don't understand that.", "Can you rephrase it?"]]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("")
        if user_input.lower() == "bye":
            print("Goodbye! Have a great day!")
            break
        else:
            print(chatbot.respond(user_input))

if __name__ == "__main__":
    start_chat()
