def guess():

    secret_word = "james bond"
    guess = ""

    while guess != secret_word:
        guess = input("please enter your guess: ")
        if guess != secret_word:
            print("wrong guess , try again")
    
    print("Yay correct guess , you guessed" , secret_word , "correctly" )
guess()