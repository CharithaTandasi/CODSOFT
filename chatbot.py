
import re
def bot(user_input):
    user_input = user_input.lower() 


    if re.search(r'\b(hello|hi)\b', user_input):
        return "Hi there! What can I do for you?"
    
    if re.search(r'\bhow are you\b' ,user_input):
        return "great!what about you"
    
    if re.search(r'\bwho are you\b', user_input):
        return "i am a chatbot created to be at your service"

    if re.search(r'\bbye\b', user_input):
        return "Goodbye! Have a great day!"

    if re.search(r'\bhelp\b', user_input):
        return "I can assist you with various tasks. Just let me know what you need help with."
    
    if re.search(r'\b(what can u do |about yourself)\b', user_input):
        return "i am able to respond to your quries."
    
    if re.search(r'\b(joke|funny story)\b', user_input):
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    
    if re.search(r'\b(fact|something you know| something intresting)\b' , user_input):
        return "sure thing, did you know that glass balls bounce higher than rubber balls...?"
    
    
    

    return "I'm sorry, I don't understand. Please try asking something else."


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    answer= bot(user_input)
    print("Chatbot:", answer)
               