import random
from datetime import datetime
import re

def simple_chatbot(user_input):
    greetings = ['hello', 'hi', 'hy', 'hey', 'greetings']
    farewell_responses = ['Goodbye! Have a great day.', 'See you later!', 'Take care!']
    greeting_responses = ['Hello! How can I help you today?', 'Hi there! What can I do for you?', 'Hey! Need any assistance?']
    time_related_queries = ['time', 'current time', 'what time is it']
    joke_queries = ['tell me a joke', 'make me laugh', 'joke']
    weather_queries = ['weather', 'current weather', 'forecast']
    calculation_pattern = re.compile(r'\b(\d+)\s*([-+*/])\s*(\d+)\b')
    fun_fact_queries = ['fun fact', 'tell me a fact', 'interesting fact']
    small_talk = {
        'how are you': 'I am fine, thank you!',
        'what is your name': 'I am a chatbot.',
        'who created you': 'I was created by Pankaj',
        'what do you do': 'I chat with people and try to help them.',
        'do you like music': "I don't have preferences, but I can suggest songs if you want.",
        'default': "I'm sorry, I don't understand that. Can you please rephrase?"
    }
    motivational_quotes = [
        'Believe you can and you\'re halfway there.',
        'The only way to do great work is to love what you do.',
        'You are stronger than you think.',
        "Don't watch the clock; do what it does. Keep going."
    ]
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        'Why did the scarecrow win an award? Because he was outstanding in his field!',
        "Why don't skeletons fight each other? They don't have the guts."
    ]
    fun_facts = [
        'Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.',
        'A day on Venus is longer than a year on Venus.',
        'Octopuses have three hearts.'
    ]

    # Convert user input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()

    # Check for greetings and farewells
    if any(word in user_input_lower for word in greetings):
        return random.choice(greeting_responses)

    if any(word in user_input_lower for word in farewell_responses):
        return random.choice(farewell_responses)
    
    if any(word in user_input_lower for word in time_related_queries):
        current_time = datetime.now().strftime('%H:%M:%S')
        return f'The current time is {current_time}.'
    
    if any(word in user_input_lower for word in joke_queries):
        return random.choice(jokes)
    
    if any(word in user_input_lower for word in weather_queries):
        return "I can't check the weather right now, but you can check a weather website or app for the latest updates."

    if any(word in user_input_lower for word in fun_fact_queries):
        return random.choice(fun_facts)
    
    # Check for specific responses
    for pattern, response in small_talk.items():
        if pattern in user_input_lower:
            return response

    # Check for math calculations
    match = calculation_pattern.search(user_input_lower)
    if match:
        num1, operator, num2 = match.groups()
        num1, num2 = int(num1), int(num2)
        if operator == '+':
            return f'The result is {num1 + num2}.'
        elif operator == '-':
            return f'The result is {num1 - num2}.'
        elif operator == '*':
            return f'The result is {num1 * num2}.'
        elif operator == '/':
            return f'The result is {num1 / num2}.'
    
    # Return a random motivational quote
    if 'motivate me' in user_input_lower or 'inspire me' in user_input_lower:
        return random.choice(motivational_quotes)

    # If no specific patterns match, return a default response
    return small_talk['default']

# Simple loop to interact with the chatbot
user_name = input('Hello! What is your name? ')
print(f'Chatbot: Nice to meet you, {user_name}! Type "exit" to end the chat.')

while True:
    user_input = input(f'{user_name}: ')
    
    # Exit the loop if the user enters 'exit'
    if user_input.lower() == 'exit':
        print('Chatbot: Goodbye!')
        break
    
    # Get the chatbot's response
    chatbot_response = simple_chatbot(user_input)
    
    # Print the response
    print('Chatbot:', chatbot_response)
