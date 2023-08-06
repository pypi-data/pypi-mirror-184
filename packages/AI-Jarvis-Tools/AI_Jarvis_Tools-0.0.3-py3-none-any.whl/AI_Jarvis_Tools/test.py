from Jarvis import QNA
from Jarvis import Brain

def main():
    while True:
        query=input("You:- ")
        query = query.lower()
        if "what is" in query or "how" in query:
            replay = QNA.Questions_Answers(query)
            print(replay)
        elif "exit"==query or "exit()"==query or "q"==query:
            exit()
        else:
            replay = Brain.ChatBot_Brain(query)
            print(replay)