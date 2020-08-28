import greeting
import bot_engine

flag1 = flag=True
flag2 = flag=False
def chat_bot():
    flag1
    print("Greetings! I am a chatbot, and I will try to answer your questions \
          about COVID-19. When you are done asking questions, just reply no!")
    while(flag1):
        user_response = input()
        user_response = user_response.lower()
        if(user_response not in ['bye','shutdown','exit', 'quit']):
            if(user_response=='thanks' or user_response=='thank you'):
                flag2
                print("Chatbot : My pleasure! Take care, and wash your hands!")
            else:
                if(greeting.welcome(user_response)!=None):
                    print("Chatbot : "+greeting.welcome(user_response))
                else:
                    print("Chatbot : ",end="")
                    print(bot_engine.COVID2bot(user_response))
        else:
            flag2
            print("Chatbot: Stay safe, and wash your hands!!! ")