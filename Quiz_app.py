score =0
def ask_question(question,answer):
    global score
    user = input(question +" ")
    if user.lower() == answer.lower():
        print("crt")
        score += 1
    else:
        print("wrong")
name = input("enter your good name ? ")
ask_question("What is the capital of France?", "Paris")
ask_question("What is the capital of Germany?", "Berlin")
ask_question("What is the capital of Italy?", "Rome")
ask_question("What is the capital of Spain?", "Madrid")
ask_question("What is the capital of Japan?", "Tokyo")
ask_question("What is the capital of Canada?", "Ottawa")
ask_question("What is the capital of Australia?", "Canberra")
ask_question("What is the capital of India?", "New Delhi")
ask_question("What is the capital of Brazil?", "Brasília")
ask_question("What is the capital of Russia?", "Moscow")
print("Thank you!!"," ",name)
print("Your point is",score)
if score >=7 :
    print("Excellent")
elif score >= 4:
    print("Good")    
else:
    print("fail")               