import re
print("Hi, I am the smartBot, How can I help you !")
user_input = input("you : ")
if re.search ("Hi", user_input , re.IGNORECASE) :
    print("Bot : Hello User !")
elif re.search("How are you" , user_input ,re.IGNORECASE) :
    print("Bot : I am fine ! How you doing !")
else : print("Sorry! Didn't get you , Please repeat again")
