from dictionaryLinkedList import *
from abstract import *
from game import Game
import csv

class GameInventoryDict(GameInvAbstract):
  def __init__(self):
    self.__game_dict = LinkedListDict()
    
  # Search for a title
  def search_title(self, title):
    return self.__game_dict.getitem(title)
    
  # Search for a genre
  def search_genre(self, genre):
    genre_list = []
    
    for game in self.__game_dict:
      #self.__game_dict.getitem(genre)
      if self.__game_dict.getitem(genre) == genre:
        genre_list.append(game)
    return genre_list

  # Search for a platform
  def search_platform(self, platform):
    plat_list = []
    
    for game in self.__game_dict:
      #list_platform = game.get_platform1() and game.get_platform2() and game.get_platform3()
      #for current_platform in list_platform:
        if game.get_platform1() == platform or game.get_platform2() == platform or game.get_platform3() == platform:
          plat_list.append(game)
    return plat_list

  # Search for a studio
  def search_studio(self, studio):
    studio_list = []
    
    for game in self.__game_dict:
      if game.get_studio() == studio:
        studio_list.append(game)
    return studio_list

  # Search for a year of release
  def search_year_released(self, year_release):
    year_list = []

    for game in self.__game_dict:
      if game.get_year_released() == year_release:
        year_list.append(game)
    return year_list

  # Adds a new game into the list.
  def add_game(self, title, genre, studio, year, platform1, platform2, platform3):
    game = Game()
    game.set_title(title)
    game.set_genre(genre)
    game.set_studio(studio)
    game.set_year_released(year)
    game.set_platform1(platform1)
    game.set_platform2(platform2)
    game.set_platform3(platform3)

    self.self.__game_dict.append(game)

  # Modify an entry
  # Modifies platform(s) of a video game.
  def mod_game(self, title, platform1, platform2, platform3):
    game = self.search_title(title)
    if game == None:
      return None

    #game.set_platform_clear()
    game.set_platform1(platform1)
    game.set_platform2(platform2)
    game.set_platform3(platform3)

    return game
    
  # Deletes an entry
  def del_game(self, game_title):

    delete = self.__game_dict.popitem(game_title)
    if delete:
      return True
      
    return False  

  # Create inventory (reads csv file)
  def create_inventory(self, videogamelist):
    with open(videogamelist, "r") as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      for rows in csvreader:
        game = Game()
        game.set_title(rows[0])
        game.set_genre(rows[1])
        game.set_studio(rows[2])
        game.set_year_released(rows[3])
        game.set_platform1(rows[4])
        game.set_platform2(rows[5])
        game.set_platform3(rows[6])

        self.__game_dict.additem(game.get_title(), game)
        #self.__game_dict[game.get_title()] = game
    
  # Print Dictionary
  def print(self):
    self.__game_dict.print()
  
  def __str__(self):
    gameInv_Dict = ""
    count = 1

    for game in self.__game_dict:
      gameInv_Dict += "#" + str(count) + " -> " + str(game) + "\n"
      count += 1
    
    return gameInv_Dict