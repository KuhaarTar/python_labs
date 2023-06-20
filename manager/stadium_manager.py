from lab8.decorators.decorators import registerer, result_to_file
from lab8.manager.set_manager import SetManager
from lab8.models.football_field import FootballField
from lab8.models.stadium import Stadium
from lab8.models.gym import Gym
from lab8.models.swimming_pool import SwimmingPool


class StadiumManager:
    """
    This is class to manage stadiums
    """

    def __init__(self, stadiums_list=None):
        """
        Initializes a StadiumManager object.
        """
        if stadiums_list is None:
            self.stadiums = []
        else:
            self.stadiums = stadiums_list

    def __len__(self):
        """
        :return: length of list
        """
        return len(self.stadiums)

    def __getitem__(self, key):
        """
        :param key:
        :return: element from list by key
        """
        return self.stadiums[key]

    def __iter__(self):
        """
        :return: iterator on stadiums list
        """
        return iter(self.stadiums)

    def check_conditions(self):
        res_dictionary = {"all": all((item.capacity >= 1000 for item in self.stadiums)),
                          "any": any((item.capacity >= 1000 for item in self.stadiums))}
        return res_dictionary

    def execute_abstract_method(self):
        """
        Executes the abstract method 'get_supported_sports()'
        for each stadium object in the manager's list.
        :return:
            A list containing the results of calling the 'get_supported_sports()'
            method on each stadium object.
        """
        new_list = [s.get_supported_sports() for s in self.stadiums]
        return new_list

    def get_object_with_index_concatenation(self):
        """
        :return: a concatenation of the object and its serial number in the list;
        """
        return list(enumerate(self.stadiums))

    def get_object_and_method_result_concatenation(self):
        execute_abstract_method = self.execute_abstract_method()
        return list(zip(execute_abstract_method, self.stadiums))

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

    @result_to_file
    def find_all_with_capacity_greater_than(self, capacity):
        """
        Знаходить усі спортивні комплекси з місткістю більше заданого значення.
        :param capacity: Значення місткості для порівняння.
        :return: Список спортивних комплексів.
        """
        return filter(lambda s: s.capacity >= capacity, self.stadiums)

    def find_all_by_name(self, name):
        """
        Знаходить усі спортивні комплекси з заданою назвою.
        :param name: Назва спортивних комплексів для пошуку.
        :return: Список спортивних комплексів.
        """
        return filter(lambda s: s.name == name, self.stadiums)


if __name__ == "__main__":
    stadium_manager = StadiumManager()
    swimming_pool_1 = SwimmingPool("Swimming Pool 1", 200, 100, 5, 1000, 50)
    swimming_pool_2 = SwimmingPool("Swimming Pool 2", 150, 80, 3, 800, 40)

    stadium_1 = Stadium("Stadium 1", 50000, 20000, "Home Team 1", "Away Team 1")
    stadium_2 = Stadium("Stadium 2", 60000, 25000, "Home Team 2", "Away Team 2")

    football_field_1 = FootballField("Football Field 1", 10000, 5000, 120, 80, "Grass")
    football_field_2 = FootballField("Football Field 2", 15000, 8000, 110, 75, "Artificial Turf")
    # print(football_field_2.get_attributes_by_type(int))
    gym_1 = Gym("Gym 1", 200, 150, 20, "$50", 3)
    gym_2 = Gym("Gym 2", 300, 200, 30, "$60", 4)
    stadium_manager.add_stadium(football_field_1)
    stadium_manager.add_stadium(football_field_2)
    stadium_manager.add_stadium(gym_1)
    stadium_manager.add_stadium(gym_2)
    stadium_manager.add_stadium(stadium_1)
    stadium_manager.add_stadium(stadium_2)
    stadium_manager.add_stadium(swimming_pool_2)
    stadium_manager.add_stadium(swimming_pool_1)

    swimming_pool_1.add_attends(750)
