def show_menu():
    print("1. Ask questions")
    print("2. add a question")
    print("3. Exit Game")
    
    option = input("enter option: ")
    return option
print (show_menu())

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You selected 'Ask questions'")
            ask_questions()
        elif option == "2":
            print("you selected 'Add a question'")
            add_question()
        elif option == "3":
            print("TTFN")
            break
        else:
            print("Invalid Option")
        print("")


def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("Ok then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()
    
def ask_questions():
    questions = []
    answers = []
    
    file = open("questions.txt", "r")
    lines = file.read().splitlines()
    lines = enumerate(lines)
    
    for i, text in lines:
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)

    file.close()
    
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)
    
    score = 0
    
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        print(len(guess))
        print(len(answer))
        if guess == answer:
            score +=1
            print("right")
            print(score)
        else:
            print("wrong")
            
    print("you got {0} correct out of {1}".format(score, number_of_questions))
    
game_loop()