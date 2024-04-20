questions = {
    "What is the capital of Russia?":"C",
    "What is the capital of Italy?":"B",
    "What is the capital of USA?":"A",
    "What is the capital of UK?":"D",
    "What is the capital of Germany?":"C",
    "What is the capital of France?":"D",
}
options = [["A: Saint Petersburg","B: Yekaterinburg","C: Moscow","D: Kazan"],
           ["A: Milan","B: Rome","C: Bologna","D: Florence"],
           ["A: Washington DC","B: New York","C: Los Angeles","D: Chicago"],
           ["A: Oxford","B: Liverpool","C: Cambridge","D: London"],
           ["A: Munich","B: Frankfurt","C: Berlin","D: Stuttgart"],
           ["A: Marselle","B: Lyon","C: Strasbourg","D: Paris"]]

def final_score(score, guesses):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Answers: ",end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ",end=" ")
    for i in guesses:
        print(i,end="")
    print()
    score1 = str((score/len(questions))*100)
    print("Your score: "+score1+"%")

def score_check(guess, answer):
        if guess == answer:
            print("CORRECT!")
            return 1
        else:
            print("WRONG!")
            return 0
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for i in questions:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(question_num, end=". ")
        print(i)
        for key in options[question_num-1]:
            print(key)
        guess = input("A, B, C, D ").upper()
        guesses.append(guess)
        correct_guesses += score_check(guess, questions.get(i))
        question_num += 1
    final_score(correct_guesses,guesses)


new_game()