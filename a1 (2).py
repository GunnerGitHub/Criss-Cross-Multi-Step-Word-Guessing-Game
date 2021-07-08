"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Gunit Singh}} ({{s4642570}})"
__email__ = "gunit.singh@uqconnect.edu.au"
__date__ = "4/09/2020"



# Write your code here (i.e. functions)
def select_word_at_random(word_select):
    """Given the word select is either “FIXED” or “ARBITRARY" this function
    will return a string randomly selected from WORDS FIXED.txt or WORDS ARBITRARY.txt
    If word select is anything else, it will return none.
    Parameter:
        word_select (string): input which determines whether string returned is from
        from WORDS FIXED.txt or WORDS ARBITRARY.txt.

    Return:
        word (str): A string randomly selected from WORDS FIXED.txt or WORDS ARBITRARY
    """
    
    if word_select=='FIXED' or word_select=='ARBITRARY':
            wordlist=load_words(word_select)
            random_word_index=random_index(wordlist)
            word=wordlist[random_word_index]
            return word
    else:
            return None


def create_guess_line(guess_no, word_length):
    """This function returns the string representing the display corresponding
        to the guess number integer, guess no.

    Parameters:
        guess_no (int): An integer representing how many guesses the player has made
        word_length (int): An integer representing the length of the word being guessed by the player

    Return:
        display (str): A string representing the guess line
    """
  
    display='Guess ' + str(guess_no)+'|'
    asterisk_pos_start = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]
    asterisk_pos_end = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]

    for loop_counter in range(word_length):
        if asterisk_pos_start<=loop_counter <=asterisk_pos_end:
            display+=' * |'
        else:
            display+=' - |'
    return display


def top_numbers_display(word_length):
    """Creates a number line at the top to represent the character to be guessed

    Parameters:
        word_length (int): An integer representing the length of the word being guessed by the player

    Return:
        Prints the numberline which fits at top of display_guess_matrix
    """
    number=1
    print('      ', end='')
    while number<=word_length:
        print(' | ', end='')
        print(str(number), end='')
        number+=1
    print(' |')
    print(WALL_HORIZONTAL*(word_length*4+9))
    
          
def display_guess_matrix(guess_no, word_length, scores):
    """Prints the progress of the game, including all line strings for guesses up to guess_no
        with the corresponding scores

    Parameters:
    guess_no (int): An integer representing how many guesses the player has made
        word_length (int): An integer representing the length of the word being guessed by the player
        scores (tuple): A tuple representing all the scores of the guess up to current guess

    Return None:
        Prints progress of the game and the current guess line.
    """

    top_numbers_display(word_length)
    
    current_guess=1
    while current_guess<guess_no:
        display=create_guess_line(current_guess, word_length)
        print(display, end='')
        print('   '+str(scores[-1+current_guess])+' Points')
        print(WALL_HORIZONTAL*(word_length*4+9))
        current_guess+=1
    display=create_guess_line(current_guess, word_length)
    print(display)
    print(WALL_HORIZONTAL*(word_length*4+9))


def compute_value_for_guess(word, start_index, end_index, guess):
        """Returns score for specific guess

        Parameters:
            word (str): Represents the word the player has to guess
            start_index (int): Start of a substring that slices the word
            end_index (int): The end of the substring (included) that slices the word.

        Return:
            points (int): An integer representing the score for the guess.
        """
        
        points=0
        given_guess = word[start_index: end_index+1]
        index_of_guess=0
        while index_of_guess<=len(guess)-1:
            if guess[index_of_guess] in VOWELS and guess[index_of_guess]==word[start_index+index_of_guess]:
                points+=14
            elif guess[index_of_guess] in CONSONANTS and guess[index_of_guess]==word[start_index+index_of_guess]:
                points+=12
            elif guess[index_of_guess] in given_guess and guess[index_of_guess]!=word[start_index+index_of_guess]: 
                points+=5
            index_of_guess+=1
        return points





def main():
    """
    Handles top-level interaction with user.
    """
    # Write the code for your main function here
    game_on=0
    print(WELCOME)
    starting=input(INPUT_ACTION)
    while True:
        if starting=='h':
            print(HELP)
            game_on+=1
            break
                        
        elif starting=='s':
            game_on+=1
            break

        elif starting=='q':
            game_on=0
            break

        else:
            print(INVALID)
            starting=input(INPUT_ACTION)
    
    if game_on!=0:
        selection=input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
        word=select_word_at_random(selection)
        print('Now try and guess the word, step by step!!')

        word_length=len(word)
        """Run the game now"""
        
        scores=()
        guess_no=1
        while guess_no<word_length:              
            display_guess_matrix(guess_no, word_length, scores)
            start_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][0]
            end_index = GUESS_INDEX_TUPLE[word_length-6][guess_no-1][1]
            guess=input('Now enter Guess '+str(guess_no)+': ')
            while True:
                if guess.isalpha() and len(guess)==(end_index+1-start_index):
                    break
                else:
                    guess=input('Now enter Guess '+str(guess_no)+': ')
            scores+=(compute_value_for_guess(word, start_index, end_index, guess),)
            guess_no+=1

        display_guess_matrix(guess_no, word_length, scores)
        final_guess=input('Now enter your final guess. i.e. guess the whole word: ')
        if final_guess==word:
            print('You have guessed the word correctly. Congratulations.')
        else:
            print('Your guess was wrong. The correct word was "'+word+'"')



if __name__ == "__main__":
    main()
