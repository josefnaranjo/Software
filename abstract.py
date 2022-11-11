from abc import abstractmethod
from abc import ABC

# Creates abstract class
class GameInvAbstract(ABC): 

  @abstractmethod
  # Searches inventory for game matching the title given and returns info
  def search_title(self, title):  
    pass

  @abstractmethod  
  # Searches inventory for games matching genre given and returns info
  def search_genre(self, genre):
    pass 

  @abstractmethod 
  # Searches inventory for games matching platform given and returns info
  def search_platform(self, platform): 
    pass 

  @abstractmethod  
  # Searches inventory for games matching studio given and returns info
  def search_studio(self, studio):  
    pass 

  @abstractmethod 
  # Searches inventory for games matching year of release given and returns info
  def search_year_released(self, year_release):
    pass  

  #@abstractmethod 
  # Completely clears information stored in the .csv file
  #def delList():  
    #pass 
  @abstractmethod
  def add_game():
    pass
    
  @abstractmethod
  def mod_game():
    pass
    
  @abstractmethod
  def del_game():
    pass
    
  @abstractmethod 
  # Creates inventory and loads entries
  def create_inventory(self, videogameList):
    pass

class DictGameAbstract(ABC):
  
  @abstractmethod
  def getitem(self, key):
    pass

  @abstractmethod
  def additem(self, key, data):
    pass

  @abstractmethod
  def popitem(self, key):
    pass

  @abstractmethod
  def length(self, key):
    pass