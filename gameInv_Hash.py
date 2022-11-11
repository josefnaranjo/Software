from dictionaryHash import HashDict
from abstract import *
from game import Game
import csv

class GameInventoryHash(GameInvAbstract):

  # Constructor
  def __init__(self):
    self.h = HashDict()

  # Create invetory. The function reads the CSV file, 'hashes' the
  # title (key), and adds videogames to the list based on their key value.
  def create_inventory(self, videogamelist):
    with open(videogamelist, "r") as csvfile:
      csvreader = csv.reader(csvfile)
      for rows in csvreader:
        game = Game()
        game.set_title(rows[0])
        game.set_genre(rows[1])
        game.set_studio(rows[2])
        game.set_year_released(rows[3])
        game.set_platform1(rows[4])
        game.set_platform2(rows[5])
        game.set_platform3(rows[6])

        self.h.additem(game.get_title(), game)        
    
  # Search for a title
  def search_title(self, title):
    retrieve = self.h.getitem(title)
    return retrieve
    
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

    self.h.additem(game.get_title(), game)
    
  # Deletes an entry
  def del_game(self, game_title):
    delete = self.h.popitem(game_title)
    return delete

  # Print Hash Table
  def print(self):
    
    self.h.print()


  # Search for a genre
  def search_genre(self, genre):
    pass

  # Search for a platform
  def search_platform(self, platform):
    pass

  # Search for a studio
  def search_studio(self, studio):
    pass

  # Search for a year of release
  def search_year_released(self, year_release):
    pass

  # Modify an entry
  # Modifies platform(s) of a video game.
  def mod_game(self, title, platform1, platform2, platform3):
    pass