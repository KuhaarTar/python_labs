class Stadium:
    __instance = None

    def __str__(self):
        print(f"Stadium( name={self.__name}, capacity={self.__capacity}, "
              f"{self.__current_attendance}, home_team={self.__home_team}, away_team={self.__away_team})")

    def __init__(self, name=None, capacity=0, current_attendance=0, home_team=None, away_team=None):
        self.__name = name
        self.__capacity = capacity
        self.__current_attendance = current_attendance
        self.__home_team = home_team
        self.__away_team = away_team

    @property
    def away_team(self):
        return self.__away_team

    @away_team.setter
    def away_team(self, away_team):
        self.__away_team = away_team

    @property
    def home_team(self):
        return self.__home_team

    @home_team.setter
    def capacity(self, home_team):
        self.__home_team = home_team

    @property
    def current_attendance(self):
        return self.__current_attendance

    @current_attendance.setter
    def current_attendance(self, current_attendance):
        self.__current_attendance = current_attendance

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @staticmethod
    def get_instance():
        if Stadium.__instance is None:
            Stadium.__instance = Stadium()
        return Stadium.__instance

    def add_attends(self, count):
        if self.__current_attendance + count > self.__capacity:
            print('There are no vacant seats')
        else:
            self.__current_attendance += count

    def decrease_attendance(self):
        if self.__current_attendance - 100 < 0:
            return print('There are not so many visitors')
        else:
            self.__current_attendance - 100

    def change_home_team(self, new_home_team):
        self.__home_team = new_home_team

    def change_away_team(self, new_away_team):
        self.__away_team = new_away_team


stadiums = [Stadium(),
            ('Silmash', 10000, 45, "Lviv red team", "Blue team"),
            Stadium.get_instance(),
            Stadium.get_instance()]
print(stadiums)
