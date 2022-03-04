import random

f = open('WordList.txt','r')
lines = f.readlines()
starting_word_list = []
for line in lines:
    if len(line) is 5 or 6:
        line = line.replace("\n","")
        starting_word_list.append(line)
possible_words = []

correct_letters = [0,0,0,0,0]
misplaced_letters = [[],[],[],[],[]]
letters_word_must_contain = []
incorrect_letters = []

def reset():
    global correct_letters
    global misplaced_letters
    global letters_word_must_contain
    global incorrect_letters
    correct_letters = [0,0,0,0,0]
    misplaced_letters = [[],[],[],[],[]]
    letters_word_must_contain = []
    incorrect_letters = []
    possible_words.clear()
    for word in starting_word_list:
        possible_words.append(word)


def add_guess():
    print('Enter your next word:')
    guess = input()
    guess_impl(guess)
    
    
def guess_impl(guess, display_words=True):
    guess = guess.replace(" ", "")
    for i in range(5):
        if guess[i+5] == '0':
            correct_letters[i] = guess[i]
        elif guess[i+5] == '1':
            misplaced_letters[i].append(guess[i])
            letters_word_must_contain.append(guess[i])
        elif guess[i+5] == '2':
            incorrect_letters.append(guess[i])
            
    possible_words.clear()
    for word in starting_word_list:
        is_valid = True
        for letter in incorrect_letters:
            if letter in word and letter not in correct_letters:
                is_valid = False
        for letter in letters_word_must_contain:
            if letter in word:
                pass
            else:
                is_valid = False
        for i in range(5):
            if correct_letters[i] is not 0 and correct_letters[i] is not word[i]:
                is_valid = False
            for letter in misplaced_letters[i]:
                if letter is word[i]:
                    is_valid = False
        
        if is_valid:
            possible_words.append(word)
    
    if display_words:
        print('Remaining words are:')
        print(len(possible_words))
        print(possible_words)

def player_game():
    reset()
    while len(possible_words) is not 1:
        add_guess()

def ai_game(count, display_logs, starter_word = ""):
    sum_of_turns = 0.0
    for j in range(count):
        reset()
        turn = 0
        target_word = starting_word_list[random.randint(0, len(starting_word_list) - 1)]
        guess = ""
        if display_logs:
            print("Target word: " + str(target_word))
        while len(possible_words) is not 1:
            turn += 1
            if display_logs:
                print("Turn: " + str(turn))
            guess = possible_words[random.randint(0, len(possible_words) - 1)] 
            if turn is 1 and starter_word is not "":
                guess = starter_word                     
            result = " "
            for i in range(5):
                if target_word[i] is guess[i]:
                    result += "0"
                elif guess[i] in target_word:
                    result += "1"
                else:
                    result += "2"
            if display_logs:
                print(guess + result)
            guess_impl(guess + result, False)
        print("Guessed " + guess + " in " + str(turn) + " turns")
        sum_of_turns += turn
    print("Mean average turns: " +  str(sum_of_turns / count))
    

ai_game(100, False, "crane")