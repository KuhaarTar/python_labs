from lab8.models.FootballField import FootballField
from lab8.models.Stadium import Stadium
from lab8.models.Gym import Gym
from lab8.models.SwimmingPool import SwimmingPool


class StadiumManager:

    def __init__(self):
        """
        Initializes a StadiumManager object.
        """
        self.stadiums = []

    def add_stadium(self, stadium):
        """
        Adds a stadium to the list of stadiums.

        :param stadium: The stadium object to be added.
        """
        self.stadiums.append(stadium)

    def print_stadiums(self):
        """
        print all stadiums in list
        :return:
        """
        print(self.stadiums)

    def find_all_with_capacity_greater_than(self, capacity):
            """
            Знаходить усі спортивні комплекси з місткістю більше заданого значення.

            :param capacity: Значення місткості для порівняння.
            :return: Список спортивних комплексів.
            """
            return list(filter(lambda s: s.capacity >= capacity, self.stadiums))

    def find_all_by_name(self, name):
            """
            Знаходить усі спортивні комплекси з заданою назвою.

            :param name: Назва спортивних комплексів для пошуку.
            :return: Список спортивних комплексів.
            """
            return list(filter(lambda s: s.name == name, self.stadiums))

if __name__ == "__main__":
    stadium_manager = StadiumManager()

    swimming_pool_1 = SwimmingPool("Swimming Pool 1", 200, 100, 5, 1000, 50)
    swimming_pool_2 = SwimmingPool("Swimming Pool 2", 150, 80, 3, 800, 40)

    stadium_1 = Stadium("Stadium 1", 50000, 20000, "Home Team 1", "Away Team 1")
    stadium_2 = Stadium("Stadium 2", 60000, 25000, "Home Team 2", "Away Team 2")

    football_field_1 = FootballField("Football Field 1", 10000, 5000, 120, 80, "Grass")
    football_field_2 = FootballField("Football Field 2", 15000, 8000, 110, 75, "Artificial Turf")

    gym_1 = Gym("Gym 1", 200, 150, 20, "$50", 3)
    gym_2 = Gym("Gym 2", 300, 200, 30, "$60", 4)

    stadium_manager.add_stadium(football_field_1)
    stadium_manager.add_stadium(football_field_2)
    stadium_manager.add_stadium(gym_1)
    stadium_manager.add_stadium(gym_2)

    result_capacity = stadium_manager.find_all_with_capacity_greater_than(5000)
    for sport_complex in result_capacity:
        print(sport_complex)

    result_name = stadium_manager.find_all_by_name("Gym 1")
    for sport_complex in result_name:
        print(sport_complex)
