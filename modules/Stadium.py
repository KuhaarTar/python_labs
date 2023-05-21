class Stadium:
    """
    That class describe Stadium with methods:
    get_instance(),add_attends(),decrease_attendance(),change_home_team(),change_away_team()
    """
    __instance = None

    def __init__(self, name=None, capacity=0, current_attendance=0, home_team=None, away_team=None):
        """
        This is constructor to init fileds of class
        :param name:
        :param capacity:
        :param current_attendance:
        :param home_team:
        :param away_team:
        """
        self.__name = name
        self.__capacity = capacity
        self.__current_attendance = current_attendance
        self.__home_team = home_team
        self.__away_team = away_team

    def __str__(self):
        """
        The method returns a string view of object
        :return: string view of object
        """
        return f"Stadium(name={self.__name}, capacity={self.__capacity}, " \
               f"current_attendance={self.__current_attendance}, home_team={self.__home_team}, " \
               f"away_team={self.__away_team})"

    def __repr__(self):
        """
        The method returns a string view of object
        :return: string view of object
        """

        return "test repr"

    @property
    def away_team(self):
        """
        Method return __away_team field value
        :return: __away_team
        """
        return self.__away_team

    @away_team.setter
    def away_team(self, away_team):
        """
        Sets the away_team field value
        :param away_team:
        :return:
        """
        self.__away_team = away_team

    @property
    def home_team(self):
        """
        Method return __home_team field value
        :return: __home_team
        """
        return self.__home_team

    @home_team.setter
    def home_team(self, home_team):
        """
        Sets the home_team field value
        :param home_team:
        :return:
        """
        self.__home_team = home_team

    @property
    def current_attendance(self):
        """
        Return __current_attendance filed value
        :return:
        """
        return self.__current_attendance

    @current_attendance.setter
    def current_attendance(self, current_attendance):
        self.__current_attendance = current_attendance

    @property
    def capacity(self):
        """
        Method return field __capacity value
        :return: __capacity
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Method set filed value
        :param capacity:
        :return:
        """
        self.__capacity = capacity

    @property
    def name(self):
        """
        method return field value
        :return: __name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        method set field value
        :param name:
        :return:
        """
        self.__name = name

    @staticmethod
    def get_instance():
        """
        Method return instance of Stadium class
        :return: __instance
        """
        if Stadium.__instance is None:
            Stadium.__instance = Stadium()
        return Stadium.__instance

    def add_attends(self, count):
        """
        method increase current_attendance if there are free places
        :param count:
        :return:
        """
        if self.__current_attendance + count > self.__capacity:
            print('There are no vacant seats')
        else:
            self.__current_attendance += count

    def decrease_attendance(self):
        """
        method decrease attendance by 100
        :return:
        """
        if self.__current_attendance - 100 < 0:
            print('There are not so many visitors')
        else:
            self.__current_attendance -= 100

    def change_home_team(self, new_home_team):
        """
        change home_team in stadium
        :param new_home_team:
        :return:
        """
        self.__home_team = new_home_team

    def change_away_team(self, new_away_team):
        """
        change away_team in stadium
        :param new_away_team:
        :return:
        """
        self.__away_team = new_away_team


stadiums = [Stadium(),
            Stadium('Silmash', 10000, 45, "Lviv red team", "Blue team"),
            Stadium.get_instance(),
            Stadium.get_instance()]

for item in stadiums:
    print(item)
