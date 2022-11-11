# General idea of the project.
# CS 3100
# Jose Naranjo

from dictionaryLinkedList import LinkedListDict
from commandline import Function
from commandline import Function_Dict
from commandline import Function_Hash
from commandline import Analysis
from commandline import Function_Sort
from random_file import * 

class Interface:
  # Jose Naranjo
  @staticmethod
  def menu():
    
    print("***********************************************************")
    print("*                 Game Inventory System                   *")
    print("***********************************************************")
    print("[1] - Input file")
    print("[2] - Search by title")
    print("[3] - Search by genre")
    print("[4] - Search by platform")
    print("[5] - Search by studio")
    print("[6] - Search by year of release")
    print("[7] - Add video game")
    print("[8] - Show video games")
    print("[9] - Edit video game")
    print("[10] - Delete video game")
    print("[0] - Exit program")
    print("")
    
  @staticmethod
  def game_inventory():
    Interface.menu()
    function = Function()
  
    option = 1
    while option != 0:
        option = int(input("Option: "))
        if option == 1:
            function.load_file()

        elif option == 2:
            function.search_title()

        elif option == 3:
            function.search_genre()

        elif option == 4:
            function.search_platform()

        elif option == 5:
            function.search_studio()

        elif option == 6:
            function.search_year()

        elif option == 7:
            function.add_game()

        elif option == 8:
            function.show_list()

        elif option == 9:
            function.modif_game()
        elif option == 10:
            function.del_game()
        elif option == 0:
            function.write_back()
        elif option != 0:
            print("\n (!!) Invalid option (!!)")
          
  
  @staticmethod
  def gameInventory_Dict():
    Interface.menu()
    funct = Function_Dict
    
    option = 1
    while option != 0:
      option = int(input("Option: "))
      if option == 1:
        funct.load_file()

      elif option == 2:
        funct.search_title()

      elif option == 3:
        funct.search_genre()

      elif option == 4:
        funct.search_platform()

      elif option == 5:
        funct.search_studio()

      elif option == 6:
        funct.search_year()

      elif option == 7:
        funct.add_game()

      elif option == 8:
        funct.show_list()

      elif option == 9:
        funct.modif_game()
      elif option == 10:
        funct.del_game()
      #elif option == 0:
        #funct.write_back()
      elif option != 0:
        print("\nInvalid option")
          
  @staticmethod
  def gameInventory_Hash():
    Interface.menu()
    function = Function_Hash()
  
    option = 1
    while option != 0:
      option = int(input("Option: "))
      if option == 1:
        function.load_file()

      elif option == 2:
        function.search_title()

      elif option == 3:
        function.search_genre()

      elif option == 4:
        function.search_platform()

      elif option == 5:
        function.search_studio()

      elif option == 6:
        function.search_year()

      elif option == 7:
        function.add_game()

      elif option == 8:
        function.show_list()

      elif option == 9:
        function.modif_game()
        
      elif option == 10:
        function.del_game()
        
      elif option == 0:
        pass
        #function.write_back()
        
      elif option != 0:
        print("\n (!!) Invalid option (!!)")

  @staticmethod
  def gameInventory_Sort():
    Interface.menu()
    function = Function_Sort()
  
    option = 1
    while option != 0:
      option = int(input("Option: "))
      if option == 1:
        function.load_file()

      elif option == 2:
        function.search_title()

      elif option == 3:
        function.search_genre()

      elif option == 4:
        function.search_platform()

      elif option == 5:
        function.search_studio()

      elif option == 6:
        function.search_year()

      elif option == 7:
        function.add_game()

      elif option == 8:
        function.show_list()

      elif option == 9:
        function.modif_game()
        
      elif option == 10:
        function.del_game()
        
      elif option == 0:
        pass
        #function.write_back()
        
      elif option != 0:
        print("\n (!!) Invalid option (!!)")
          
def simple_main():
  dict = LinkedListDict()
  # Testing Linked list.
  # Add three items into the Linked list.
  dict.additem(1, 'John')
  dict.additem(2, "Luis")
  dict.additem(3, "Diego")

  print("Elements in the list: ")
  dict.print()
  print("\nLength of the list:")
  print(dict.length()) 

  print("\n--- Deleting item '2'...")
  dict.popitem(2) # Eliminates item at index 2.
  
  print("\nElements in the list without item '2':")
  dict.print()
  print("Length of the list")
  print(dict.length())

  print("\n+++ Adding '4' into the list...")
  dict.additem(4, "Alex") # Adds a new item into the list.
  
  print("\nElements in the list after having added '4' into the list:")
  dict.print()
  print("Length of the list:")
  print(dict.length())

  print("\n+++ Adding '5', '6', and '7' into the list...")
  dict.additem(5, "Pedro") # Adds three more items into the list.
  dict.additem(6, "Angel")
  dict.additem(7, "Jesus")
  print("\nElements in the list after having added '5', '6', and '7' into the list:")
  dict.print()
  print("Length:")
  print(dict.length())
  print("\nGet item '6':")
  print(dict.getitem(6))

  print("\n--- Deleting item '3'...")
  dict.popitem(3) # Eliminates item at index 3.
  
  print("\nElements in the list without item '3'.")
  dict.print()
  print("Length of the list:")
  print(dict.length())

def main_analysis():
  no_entries = 500
  file_name = "rand_file_"+str(no_entries)+".csv"
  random_data(file_name, no_entries)
  Analysis.car_inventory_analysis(file_name, 10000, no_entries)
  
if __name__ == "__main__":
  Interface.game_inventory()
  #Interface.gameInventory_Dict()
  #Interface.gameInventory_Sort()
  #Interface.gameInventory_Hash()
  #simple_main()
  #main_analysis()
