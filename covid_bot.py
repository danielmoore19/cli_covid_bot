import greeting
import bot_engine

flag=True
print("Greetings! I am a chatbot, and I will try to answer your questions about COVID-19. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response not in ['bye','shutdown','exit', 'quit']):
        if(user_response=='thanks' or user_response=='thank you'):
            flag=False
            print("Chatbot : My pleasure! Take care, and wash your hands!")
        else:
            if(welcome(user_response)!=None):
                print("Chatbot : "+welcome(user_response))
            else:
                print("Chatbot : ",end="")
                print(COVID2bot(user_response))
    else:
        flag=False
        print("Chatbot: Stay safe, and wash your hands!!! ")