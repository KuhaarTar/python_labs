from lab8.models.AbstractStadium import AbstractStadium


class Stadium(AbstractStadium):
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
        super().__init__(name, capacity, current_attendance)
        self.home_team = home_team
        self.away_team = away_team

    def __str__(self):
        """
        The method returns a string view of object
        :return: string view of object
        """
        return f"Stadium(name={self.name}, capacity={self.capacity}, " \
               f"current_attendance={self.current_attendance}, home_team={self.home_team}, " \
               f"away_team={self.away_team})"

    def __repr__(self):
        """
        The method returns a string view of object
        :return: string view of object
        """

        return "test repr"

    @staticmethod
    def get_instance():
        """
        Method return instance of Stadium class
        :return: __instance
        """
        if Stadium.__instance is None:
            Stadium.__instance = Stadium()
        return Stadium.__instance

    def get_supported_sports(self):
        """
        overriding abstract method
        :return:Returns a list of sports that can be contested at this sports complex
        """
        return ['Football', 'Basketball', 'Volleyball']

    def add_attends(self, count):
        """
        method increase current_attendance if there are free places
        :param count:
        :return:
        """
        if self.current_attendance + count > self.__capacity:
            print('There are no vacant seats')
        else:
            self.current_attendance += count

    def decrease_attendance(self):
        """
        method decrease attendance by 100
        :return:
        """
        if self.current_attendance - 100 < 0:
            print('There are not so many visitors')
        else:
            self.current_attendance -= 100

    def change_home_team(self, new_home_team):
        """
        change home_team in stadium
        :param new_home_team:
        :return:
        """
        self.home_team = new_home_team

    def change_away_team(self, new_away_team):
        """
        change away_team in stadium
        :param new_away_team:
        :return:
        """
        self.away_team = new_away_team
