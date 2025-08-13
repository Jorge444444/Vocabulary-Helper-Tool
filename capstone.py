from wordhoard import Definitions
from wordhoard import Synonyms
from wordhoard import Antonyms





def mainMenu():
    print("Welcome to a vocabulary helper tool\n")
    print("1. Find information of a word")
    print("2. View Favorites")
    print('3. View stats')
    print('(Other input ends the interaction)')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        get_translation()
    if choice == 2:
        view_fav()
        mainMenu()
    if choice == 3:
        view_stats()
        mainMenu()
    
    

        

def get_translation():
    global word
    word = input("Please enter a word:")
    definition = Definitions(search_string=word)
    definition_results = definition.find_definitions()

    if definition_results:
        print(f'Here is the information on the word: {word.capitalize()}\n')
        print("Definitions:")

        for index, value in enumerate(definition_results):
            print(f"{index + 1} - {value}\n")

        print("Synonyms:")

        synonym = Synonyms(search_string= word)
        synonym_results = synonym.find_synonyms()
        synonym_set = set(synonym_results)
        print(', '.join(synonym_set))
        print('\n')

        print("Antonyms")

        antonym = Antonyms(search_string= word)
        antonym_results = antonym.find_antonyms()
        antonym_set = set(antonym_results)
        print(', '.join(antonym_set))
        print('\n')

        stats()

        print("1. Go back to main menu")
        print("2. Find another word")
        print("3. save word")
        after_get_translation = int(input("What would you like to do next?"))
        if after_get_translation == 1:
            mainMenu()
        elif after_get_translation == 2:
            get_translation()
        elif after_get_translation == 3:
            save_word()



def save_word():

    f = open("Favorites.txt", "a")
    f.write(word)
    f.write("\n")
    f.close

    f = open("Favorites.txt", "r")
    favorite_list = []
    for line in f:        
        favorite_list.append(line)
    favorite_set = set(favorite_list)
    f.close

    f = open("Favorites.txt", "w")
    for fav in favorite_set:
        f.write(fav)
    f.close

    f = open("Favorites.txt", "r")
    print(f.read())
    f.close

def del_word():

    f = open("Favorites.txt", "r")
    favorite_list = []
    for line in f:        
        favorite_list.append(line)
    
    for fav in favorite_list[:]:
        if fav.strip() == word:
            favorite_list.remove(fav)
            


    f = open("Favorites.txt", "w")
    for fav in favorite_list:
        f.write(fav)
    f.close
    
    f = open("Favorites.txt", "r")
    print(f.read())
    f.close

def view_fav():
    f = open("Favorites.txt", "r")
    favorite_list = []
    for line in f:        
        favorite_list.append(line)
    
    print("Here are your favorites: ")
    for index, value in enumerate(favorite_list):
            print(f"{index + 1} - {value}\n")
    


        

def stats():
    s = open("stats.txt","r")
    counter = s.readline().strip()
    counter = int(counter) + 1
    f = open("stats.txt", "w")
    f.write(str(counter))
    
def view_stats():
    s = open("stats.txt","r")
    print("Total lookups:")
    print(s.readline().strip())




def main ():
    mainMenu()

    


main()
    