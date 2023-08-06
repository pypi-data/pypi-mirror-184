Intro = '''
Application Name:- Jarvis
Developer Name:- RISHABH-SAHIL 
'''
Intro = '''
Application Name:- Jarvis
Developer Name:- RISHABH-SAHIL 
'''

# ----------------------Modules Name----------------------
import openai
from dotenv import load_dotenv

def ChatBot_Brain(question,chat_log=None):
    try:
        fileopen = open("Data\Api.txt","r") # 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
        API = fileopen.read()
        fileopen.close()
        openai.api_key = API
        load_dotenv()
        completion = openai.Completion()
        FileLog = open("DataBase\\chat_log.txt","r")
        chat_log_template = FileLog.read()
        FileLog.close()

        if chat_log is None:
            chat_log = chat_log_template
        
        prompt = f'{chat_log} You : {question}\nJarvis : '
        response = completion.create(
            model = "text-davinci-002",
            prompt=prompt,
            temperature = 0.5,
            max_tokens = 60,
            top_p = 0.3,
            frequency_penalty = 0.5,
            presence_penalty = 0)
        answer = response.choices[0].text.strip()
        chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
        FileLog = open("DataBase\\chat_log.txt","w")
        FileLog.write(chat_log_template_update)
        FileLog.close()
        return answer
    except:
        import os
        # Create a folder
        os.makedirs("DataBase")
        os.makedirs("Data")
        # Open a file
        f = open("DataBase\\chat_log.txt", "w")
        first='''Jarvis: My Name is Jarvis'''
        # Write to the file
        f.write(str(first))

        # Close the file
        f.close()
        f = open("Data\\Api.txt", "w")
        # Write to the file
        f.write('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')

        # Close the file
        f.close()



# while True:
#     query = input(">> ")
#     replay = ChatBot_Brain(query)
#     print(replay)
