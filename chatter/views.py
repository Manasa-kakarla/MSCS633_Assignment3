# Import necessary modules
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize the chatbot
chatbot = ChatBot('ChatterBot')

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def home(request):
    """Render the home page."""
    return render(request, 'index.html')

def get_response(request):
    """Handle user input and generate a bot response."""
    # Get the user input from the POST request
    user_input = request.POST.get('user_input')

    # Generate the response from the chatbot
    bot_response = chatbot.get_response(user_input)

    # Render the response on the template
    return render(request, 'index.html', {'user_input': user_input, 'bot_response': bot_response})

