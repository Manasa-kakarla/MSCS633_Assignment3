from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Command(BaseCommand):
    help = 'Start chatbot in terminal'

    def handle(self, *args, **options):
        chatbot = ChatBot("Terminal Bot")

        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train("chatterbot.corpus.english")

        self.stdout.write(self.style.SUCCESS("Chatbot is ready! Type 'exit' to quit."))

        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                break
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")

