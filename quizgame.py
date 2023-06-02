import random
random_num=random.randint(0,6)
random_numupdate=random_num

print()
print()
# option choice
print("1 show question")
print("2 Show marks")
print("3 Run Game")
print()
choice=int(input("selet your option (1 or 2 or 3) :"))

#option one 
if choice==1:
    try:
        file=open("questions.txt","r")
        for line in file:
            print(line)
        file.close()

    except:
        print("Error reading file")
    print()
    input("press enter to close")

    
# option two
elif choice==2:
    try:
        score_pad=open("scores.txt")
        for line in score_pad:
            print(line)
        score_pad.close()
    except:
        print("Error Reading File")
    print()   
    input("press enter to close")
    

#option three
elif choice==3:

    print()

    name=input("Enter your Name :")
    print()
    print("lets Play game")
    print()
    
    questions=(
        

        "Which Apollo mission was the first one to land on the Moon?",
        "Which of the following bones is not in the leg?",
        "How many planets make up our Solar System?",
        "What is the primary addictive substance found in tobacco?",
        "disease primarily affects which part of the human body?",
        "The asteroid belt is located between which two planets?",
        "The medical term for the belly button is which of the following?"
        )
    
    options = (("A. Apollo 9",
                "B. Apollo 10",
                "C. Apollo 11",
                "D. Apollo 13"),

               ("A. Patella",
                "B. Tibia",
                "C. Fibula",
                "D. Radius"),

               ("A. 8",
                "B. 7",
                "C. 6",
                "D. 4"),

               ("A. Nicotine",
                "B. Cathinone",
                "C. Ephedrine",
                "D. Glaucine"),

               ("A. Lungs",
                "B. Brain",
                "C. Skin",
                "D. Heart"),

               ("A. Jupiter and Saturn",
                "B. Mercury and Venus",
                "C. Mars and Jupiter",
                "D. Earth and Mars"),

               ("A. Umbilicus",
                "B. Nevus",
                "C. Nares",
                "D. Paxillus")
               )
    
    answers =("C","D","A","A","B","C","A")
    
    guesses=[]
    score = 0
    question_num =random_num
    answersheet=[] 
    
    
    for x in range(0,4):
        
        print("--------------")
        print(questions[random_numupdate])
        for opt in (options[random_numupdate]):
            print(opt)

        #print(options[random_numupdate])
        print()
        guess = input("Enter (A,B,C,D):").upper()
        guesses.append(guess)
        answersheet.append(answers[random_numupdate])
        if guess ==answers[random_numupdate]:
            score+=1
            print("CORRECT!")
        
        else:
            print("INCORRECT!")
            print(f"{answers[random_numupdate]} is the correct answer")
        
    # genarate numer as a random
        random_num=random.randint(0,6)
        if random_num==random_numupdate:
            random_num=random.randint(0,6)
        random_numupdate=random_num
        
    
      
    print("--------------")
    print("     RESULT   ")
    print("--------------")
    
    
    print("answers:",end="")
    for answer in answersheet:
        print(answer,end="")
    print()
    
    print()
    
    print("Guesses:",end="")
    for guess in guesses:
        print(guess,end="")
    print()
    
    score = int(score/4*100)
    print(f"Your score is: {score}%")

    file2=open("scores.txt","a")
    file2.write("{}-{}% \n".format(name,score))

    print()
    input("press enter to close")


    
    





