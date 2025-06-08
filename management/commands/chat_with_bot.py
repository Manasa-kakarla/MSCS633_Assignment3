from django.core.management.base import BaseCommand
from chat.bot import chatbot

class Command(BaseCommand):
    help = 'Chat with ChatterBot in terminal'

    def handle(self, *args, **kwargs):
        print("Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Bot: Goodbye!")
                break
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")

