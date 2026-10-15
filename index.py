#Start code here
import random
print("HANGMAN")
print("By Python3")



hangman_pics = ['''
    +---+
        |
        |
        |                           
       ===''', '''
       +---+
       0   |
           |
           |
          ===''', '''
       +---+
       0   |
       |   |
           |
          ===''', '''
       +---+
       0   |
       |   |
      /    |
          ===''', '''
       +---+
       0   |
       |   |
      /|   |
          ===''', '''
       +---+
       0   |
       ||  |
      /|   |
          ===''', '''
       +---+
       0   |
      /||  |
      /|   |
          ===''']
word_list = ["dog", "eleve", "python", "anniversaire", "bonjour", "food"]
word1 = random.choice(word_list)

print("_ " * len(word1))

ans = ["_ "] * len(word1)

word = ["c", "i", "n", "e", "m", "a"]

hang_var = -1


    
while True:
    
    user_guess = input("Guess the letters: ")

    if user_guess in word1:
        for i in range(len(word1)):
            if word1[i] == user_guess:
                ans[i] = user_guess
        print(*ans)
    elif user_guess == word1:
        print("Congratulations!!!")
            
        
    if user_guess not in word1:
        hang_var = hang_var + 1
        print(hangman_pics[hang_var])
        
        if hang_var == 6:
            print("You have no more lives left!")
            break

    if "_ " not in ans:
        print("Congratulations!")
        break
    












