# Jose Naranjo.
class Game:
    # Info of video game(s).
    def __init__(self):
        self.__title = ""
        self.__genre = ""
        self.__studio = ""
        self.__year_released = 0
        self.__platform1 = ""
        self.__platform2 = ""
        self.__platform3 = ""

    # Get and Set the title of a video game.
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    # Get and Set the genre of a video game.
    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    # Get and Set the studio of a video game.
    def get_studio(self):
        return self.__studio

    def set_studio(self, studio):
        self.__studio = studio

    # Get and Set the year of release of a video game.
    def get_year_released(self):
        return self.__year_released

    def set_year_released(self, released):
        self.__year_released = released

    # Get and Set platforms of a video game.
    def get_platform1(self):
        return self.__platform1

    #def set_platform_clear(self):
        #self.__list_platforms = []
      
    def set_platform1(self, platform1):
        self.__platform1 = platform1
    # Get and Set the platform of a video game.
    def get_platform2(self):
        return self.__platform2
      
    def set_platform2(self, platform2):
        self.__platform2 = platform2
    # Get and Set the platform of a video game.
    def get_platform3(self):
        return self.__platform3
      
    def set_platform3(self, platform3):
        self.__platform3 = platform3

    def __str__(self):
        #line =  "Title: " + self.__title + " Genre:" + self.__genre + " Studio: " + self.__studio + " Year: " + str(self.__year_released) + " Plat1: " + self.__platform1 + " Plat2: " + self.__platform2 + " Plat3: " + self.__platform3
        return str(self.__title) + ", " + str(self.__genre) + ", " + str(self.__studio) + ", " + str(self.__year_released) + ", " + str(self.__platform1) + ", " + str(self.__platform2) + ", " + str(self.__platform3)