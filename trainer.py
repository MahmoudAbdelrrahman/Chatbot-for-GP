from chatbot import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "./knowledge/electricity.yml",
    "./knowledge/plumbing.yml",
    "./knowledge/moving.yml"

)



def brain(user_input):
    response = chatbot.get_response(user_input)
    return response




