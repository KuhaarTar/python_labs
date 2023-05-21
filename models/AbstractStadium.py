from abc import ABC, abstractmethod


class AbstractStadium(ABC):
    """
    That class describe Stadium with methods:
    get_instance(),add_attends(),decrease_attendance(),change_home_team(),change_away_team()
    """

    def __init__(self, name=None, capacity=0, current_attendance=0):
        """
        This is constructor to init fileds of class
        :param name:
        :param capacity:
        :param current_attendance:
        """
        self.__name = name
        self.__capacity = capacity
        self.__current_attendance = current_attendance

    def __str__(self):
        """
        The method returns a string view of object
        :return: string view of object
        """
        return f"Stadium(name={self.__name}, capacity={self.__capacity}, " \
               f"current_attendance={self.__current_attendance}"

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

    @abstractmethod
    def get_supported_sports(self):
        """
        :return: Returns a list of sports that can be contested at this sports complex
        """

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
