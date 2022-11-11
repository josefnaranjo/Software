from game import Game
from gameInv import GameInv
from gameInv_Dict import GameInventoryDict
from dictionaryLinkedList import LinkedListDict
from gameInv_Hash import GameInventoryHash
from dictionaryHash import HashDict
from gameInv_Sort import GameInventorySort
from dictionarySortedList import SortedListDict

import time
import random
game_inv = GameInv()
gameInv_Dict = GameInventoryDict()
new_game = Game()
gameInv_Hash = GameInventoryHash()
hash = HashDict()
gameInv_Sort = GameInventorySort()


class Function: 
    import csv
    # Loads file into the list.
    @staticmethod
    def load_file():
      game_inv.create_inventory("vgList.csv")
      print("\nFile loaded...")

    # Searches a video game that matches the title entered
    # by the user.
    @staticmethod
    def search_title():
      print("\nEnter the video game title you're looking for: ")
      title = input()
      # Searches for a game by title.
      game = game_inv.search_title(title.upper())
      # If the game is not in the csv file, then 'Game not found' will pop up
      # on the console.
      if game is None:
          print("Game not found...")
      # If the game is in the file, though, all the information in regard to that
      # game will be shown on the console.
      else:
          print("\nDetails: ", game)

    # Searches video games of the chosen genre.
    @staticmethod
    def search_genre():
      print("\nEnter the genre you're most interested in: ")
      input_genre = input()
      # Searches for games by genre.
      list_genre = game_inv.search_genre(input_genre.upper())
      # If games are not found in the csv file, then 'Game not found' will pop up
      # on the console.
      if len(list_genre) == 0:
          print("Genre not found...")
      # If games of that genre are found in the file, then those games will be shown on the console.
      else:
        # loop through the list of games and print every single game.
          count = 1
          print("\n* Here's the list of games that match the " + input_genre.upper() + " genre:\n")
          for genre in list_genre:
            print("#" + str(count) + "-> " + str(genre) + "\n")
            count += 1

    # Searches games that match the chosen platform.
    @staticmethod
    def search_platform():
      print("\nEnter the platform you want to see games for: ")
      input_platform = input()
      # Searches for games by platform.
      list_platform = game_inv.search_platform(input_platform.upper())
      # If games are not found in the csv file, then 'Game not found' will pop up
      # on the console.
      if len(list_platform) == 0:
          print("Platform not found...")
      # If games created by that platform are found in the file, then those games will be shown on the console.
      else:
        # loop through the list of games and print every single game.
          count = 1
          print("\n* Here's the list of games that match the " + input_platform.upper() + " platform:\n")
          for platform in list_platform:
            print("#" + str(count) + "-> " + str(platform) + "\n")
            count += 1

    # Searches games that match the entered studio.
    @staticmethod
    def search_studio():
      print("\nEnter the name of the studio: ")
      input_studio = input()
      # Searches for games by studio.
      list_studio = game_inv.search_studio(input_studio.upper())
      # If games are not found in the csv file, then 'Game not found' will pop up
      # on the console.
      if len(list_studio) == 0:
          print("Studio not found...")
      # If games created by that studio are found in the file, then those games will be shown on the console.
      else:
        # loop through the list of games and print every single game.
          count = 1
          print("\n* Here's the list of games that were developed by " + input_studio.upper() + ":\n")
          for studio in list_studio:
            print("#" + str(count) + "-> " + str(studio) + "\n")
            count += 1

    # Searches games that match the year entered by the user.
    @staticmethod
    def search_year():
      print("\nEnter the year you're looking for: ")
      input_year = input()
      # Searches for games by year.
      list_year = game_inv.search_year_released(input_year)
      # If games released in that year are not found in the csv file, then 'Game not found' will pop up
      # on the console.
      if len(list_year) == 0:
          print("Year not found...")
      # If games released in that year are found in the file, then those games will be shown on the console.

      else:
        # loop through the list of games and print every single game.
          count = 1
          print("\n* Here's the list of games released in " + input_year + ":\n")
          for year in list_year:
            print("#" + str(count) + "-> " + str(year) + "\n")
            count += 1

    # Adds a new video game into the system.
    @staticmethod
    def add_game():
      print("\n.: Adding a new video game :.")
      title = input("\n+ Enter title of the game: ")
      genre = input("+ Enter genre:")
      studio = input("+ Enter studio: ")
      year = int(input("+ Enter year: "))
      #platform = []
      platform1 = input("+ Enter platform 1:")
      platform2 = input("+ Enter platform 2 or .:")
      platform3 = input("+ Enter platform 3 or .:")
      #platform.append(platform1.upper())
      #platform.append(platform2.upper())
      #platform.append(platform3.upper())
      game_inv.add_game(title.upper(), genre.upper(), studio.upper(), year, platform1.upper(), platform2.upper(), platform3.upper())
      if game_inv:
        print("\nGame added successfully")

    # Shows all the video games in the file.
    @staticmethod
    def show_list():
      print("\n.: Video games in file :.\n")
      print(game_inv)

    # Modifies the platforms of a video game.
    @staticmethod
    def modif_game():
      print("\n(!!!) You can only modify platforms (!!!)\n")
      title = input("> Enter game title you wish to modify: ")
      #platform = []
      platform1 = input("> Enter platform 1:")
      platform2 = input("> Enter platform 2 or '.':")
      platform3 = input("> Enter platform 3 or '.':")
      #platform.append(platform1.upper())
      #platform.append(platform2.upper())
      #platform.append(platform3.upper())
      game = game_inv.mod_game(title.upper(), platform1.upper(), platform2.upper(), platform3.upper())
      if game:
        print("\nGame modified successfully.")

    # Deletes an entry from the list.
    @staticmethod
    def del_game():
      game_title= input("\n- Enter name of the game: ")
      flag = game_inv.del_game(game_title.upper())
      if flag:
        print("\nGame deleted successfully.")
      else:
        print("\nGame not found...")

  # Once you exit the program, all the changes are saved
  # in the .csv file.
    @staticmethod
    def write_back():
      game_inv.write_back("vgList.csv")
      print("\n*** File updated.***")
      
class Function_Dict:  # Using a dictionary
  import csv
  
  @staticmethod
  def load_file():
    #print("\nEnter the name of the inventory file: ")
    #file_name = str(input())
    gameInv_Dict.create_inventory("vgList.csv")
    print("\nFile loaded**\n")

  @staticmethod
  def search_title():

    print("\nEnter the video game title you're looking for: ")
    input_title = input()
    # Searches for a game by title.
    game = gameInv_Dict.search_title(input_title.upper())
    # If the game is not in the csv file, then 'Game not found' will pop up
    # on the console.
    if game is None:
        print("\nGame not found...")
    # If the game is in the file, though, all the information in regard to that
    # game will be shown on the console.
    else:
      print("\nGame info: " + str(game))

  @staticmethod
  def search_genre():

    print("\nEnter the genre you're most interested in: ")
    input_genre = input()
    # Searches for games by genre.
    list_genre = gameInv_Dict.search_genre(input_genre.upper())
    # If games are not found in the csv file, then 'Game not found' will pop up
    # on the console.
    if len(list_genre) == 0:
        print("Game not found...")
    # If games of that genre are found in the file, then those games will be shown on the console.
    else:
      # loop through the list of games and print every single game.
        print("\nHere's the list of games that match the chosen genre:\n")
        for genre in list_genre:
          print(genre)

  @staticmethod
  def search_platform():

      print("\nEnter the platform you want to see games for: ")
      input_platform = input()
      # Searches for games by platform.
      list_platform = gameInv_Dict.search_platform(input_platform.upper())
      # If games are not found in the csv file, then 'Game not found' will pop up
      # on the console.
      if len(list_platform) == 0:
          print("Game not found...")
      # If games created by that platform are found in the file, then those games will be shown on the console.
      else:
        # loop through the list of games and print every single game.
          print("\nHere's the list of games that match the chosen platform:\n")
          for platform in list_platform:
            print(platform)

  @staticmethod
  def search_studio():

    print("\nEnter the name of the studio: ")
    input_studio = input()
    # Searches for games by studio.
    list_studio = gameInv_Dict.search_studio(input_studio.upper())
    # If games are not found in the csv file, then 'Game not found' will pop up
    # on the console.
    if len(list_studio) == 0:
        print("Game not found...")
    # If games created by that studio are found in the file, then those games will be shown on the console.
    else:
      # loop through the list of games and print every single game.
        print("\nHere's the list of games that match the chosen studio:\n")
        for studio in list_studio:
          print(studio)

  @staticmethod
  def search_year():

    print("\nEnter the year you're looking for: ")
    input_year = input()
    # Searches for games by year.
    list_year = gameInv_Dict.search_year_released(input_year)
    # If games released in that year are not found in the csv file, then 'Game not found' will pop up
    # on the console.
    if len(list_year) == 0:
        print("Game not found...")
    # If games released in that year are found in the file, then those games will be shown on the console.

    else:
      # loop through the list of games and print every single game.
        print("\nHere's the list of games that match the chosen year of release:\n")
        for year in list_year:
          print(year)

  @staticmethod
  def add_game():
    print("\n.: Adding a new video game :.")
    title = input("\n+ Enter title of the game: ")
    genre = input("+ Enter genre:")
    studio = input("+ Enter studio: ")
    year = int(input("+ Enter year: "))
    platform1 = input("+ Enter platform 1:")
    platform2 = input("+ Enter platform 2 or .:")
    platform3 = input("+ Enter platform 3 or .:")
    gameInv_Dict.add_game(title.upper(), genre.upper(), studio.upper(), year, platform1.upper(), platform2.upper(), platform3.upper())
    if gameInv_Dict:
      print("\nGame added successfully")

  @staticmethod
  def show_list():
    print("\n.: Video games in file :.\n")
    #print(gameInv_Dict)
    gameInv_Dict.print()
    
  @staticmethod
  def modif_game():
    print("\n(!!!) You can only modify platforms (!!!)\n")
    title = input("> Enter game title you wish to modify: ")
    
    platform1 = input("> Enter platform 1:")
    platform2 = input("> Enter platform 2 or '.':")
    platform3 = input("> Enter platform 3 or '.':")
    game = gameInv_Dict.mod_game(title.upper(), platform1.upper(), platform2.upper(), platform3.upper())
    if game:
      print("\nGame modified successfully.")

  @staticmethod
  def del_game():
    game_title= input("\n- Enter name of the game: ")
    flag = gameInv_Dict.del_game(game_title.upper())
    if flag:
      print("\nGame deleted successfully.")
    else:
      print("\nGame not found...")
    
  @staticmethod
  def write_back():
    gameInv_Dict.write_back("vgList.csv")
    print("\n*** File updated.***")

class Function_Hash:
  import csv
  @staticmethod
  def load_file():
    #print("\nEnter the name of the inventory file: ")
    #file_name = str(input())
    gameInv_Hash.create_inventory("vgList.csv")
    print("\nFile loaded**\n")

  @staticmethod
  def show_list():
    print("\n.: Video games in file :.\n")
    gameInv_Hash.print()

  @staticmethod
  def search_title():
    print("\nEnter the video game title you're looking for: ")
    title = input()

    game = gameInv_Hash.search_title(title.upper())

    if game is False:
        print("Game not found...")
    else:
        print("\nDetails: ", game)


  # Adds a new video game into the system.
  @staticmethod
  def add_game():
    print("\n.: Adding a new video game :.")
    title = input("\n+ Enter title of the game: ")
    genre = input("+ Enter genre:")
    studio = input("+ Enter studio: ")
    year = int(input("+ Enter year: "))

    platform1 = input("+ Enter platform 1:")
    platform2 = input("+ Enter platform 2 or .:")
    platform3 = input("+ Enter platform 3 or .:")

    gameInv_Hash.add_game(title.upper(), genre.upper(), studio.upper(), year, platform1.upper(), platform2.upper(), platform3.upper())
    if gameInv_Hash:
      print("\nGame added successfully")
        
  # Modifies the platforms of a video game.
  @staticmethod
  def modif_game():
    print("\n(!!!) You can only modify platforms (!!!)\n")
    title = input("> Enter game title you wish to modify: ")

    platform1 = input("> Enter platform 1:")
    platform2 = input("> Enter platform 2 or '.':")
    platform3 = input("> Enter platform 3 or '.':")

    game = gameInv_Hash.mod_game(title.upper(), platform1.upper(), platform2.upper(), platform3.upper())
    if game:
      print("\nGame modified successfully.")

  # Deletes an entry from the list.
  @staticmethod
  def del_game():
    game_title= input("\n- Enter name of the game: ")
    flag = gameInv_Hash.del_game(game_title.upper())
    if flag:
      print("\nGame deleted successfully.")
    else:
      print("\nGame not found...")

# Once you exit the program, all the changes are saved
# in the .csv file.
  @staticmethod
  def write_back():
    game_inv.write_back("vgList.csv")
    print("\n*** File updated.***")

class Function_Sort:
  import csv
  @staticmethod
  def load_file():
    #print("\nEnter the name of the inventory file: ")
    #file_name = str(input())
    gameInv_Sort.create_inventory("vgList.csv")
    print("\nFile loaded**\n")

  @staticmethod
  def show_list():
    print("\n.: Video games in file :.\n")
    gameInv_Sort.print()

  @staticmethod
  def search_title():
    print("\nEnter the video game title you're looking for: ")
    title = input()

    game = gameInv_Hash.search_title(title.upper())

    if game is False:
        print("Game not found...")
    else:
        print("\nDetails: ", game)


  # Adds a new video game into the system.
  @staticmethod
  def add_game():
    print("\n.: Adding a new video game :.")
    title = input("\n+ Enter title of the game: ")
    genre = input("+ Enter genre:")
    studio = input("+ Enter studio: ")
    year = int(input("+ Enter year: "))

    platform1 = input("+ Enter platform 1:")
    platform2 = input("+ Enter platform 2 or .:")
    platform3 = input("+ Enter platform 3 or .:")

    gameInv_Hash.add_game(title.upper(), genre.upper(), studio.upper(), year, platform1.upper(), platform2.upper(), platform3.upper())
    if gameInv_Hash:
      print("\nGame added successfully")
        
  # Modifies the platforms of a video game.
  @staticmethod
  def modif_game():
    print("\n(!!!) You can only modify platforms (!!!)\n")
    title = input("> Enter game title you wish to modify: ")

    platform1 = input("> Enter platform 1:")
    platform2 = input("> Enter platform 2 or '.':")
    platform3 = input("> Enter platform 3 or '.':")

    game = gameInv_Hash.mod_game(title.upper(), platform1.upper(), platform2.upper(), platform3.upper())
    if game:
      print("\nGame modified successfully.")

  # Deletes an entry from the list.
  @staticmethod
  def del_game():
    game_title= input("\n- Enter name of the game: ")
    flag = gameInv_Hash.del_game(game_title.upper())
    if flag:
      print("\nGame deleted successfully.")
    else:
      print("\nGame not found...")

# Once you exit the program, all the changes are saved
# in the .csv file.
  @staticmethod
  def write_back():
    game_inv.write_back("vgList.csv")
    print("\n*** File updated.***")




  

class Analysis:
    
  @staticmethod
  def car_inventory_analysis(rand_file_name, no_queries,no_entries):
    # rand_file_name: the name of the file containing the random data
    # no_queries: the number of queries to run on the system
    # no_entries: the max number of entries in the file
    # this function is responsible for including all the necessary code to analyze the performance of the system
  
    # Car inventory based on list
    ginvent = GameInv()
    ginvent.create_inventory(rand_file_name)
    # car inventory based on the BSTDict
    ginvent_dict = GameInventoryDict()
    ginvent_dict.create_inventory(rand_file_name)
  
    #generating no_queries random queries 
    # using the random vin numbers
    random_title_list = []
    for i in range(0,no_queries):
        n = random.randint(1, no_entries)
        random_title_list.append(n)
    
    #starting time calculation
    start_time = time.time()
    results1 = []
    #running the no_queries query search
    for rand_title in random_title_list:
      result = ginvent.search_title(rand_title)
      results1.append(result)
    #calculating the time after the for loop
    end_time = time.time()
    # calculating how long it took to run the 1000 queries
    print("No of entries: "+ str(no_entries))
    print("searching " + str(no_queries) + " queries using the List based implementation: --- %s seconds ---" % (end_time - start_time))  
  
    # starting the time calculation for the Dict based implementation
    start_time2 = time.time()
    results2 = []
    #running the no_queries query search
    for rand_title in random_title_list:
      result = ginvent_dict.search_title(rand_title)
      results2.append(result)
    #calculating the time after the for loop
    end_time2 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the Dict based implementation: --- %s seconds ---" % (end_time2 - start_time2)) 
    
    
    # comparing to make sure the results are the same and correct
    for i in range(0, len(random_title_list)):
      if results1[i] != results2[i]:
        print("results are not equal: ")
        print(results1[i])
        print(" ")
        print(results2[i])
        print("\n")