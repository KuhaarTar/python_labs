from lab8.models.abstract_stadium import AbstractStadium


class SwimmingPool(AbstractStadium):
    """
    That class describe Stadium with methods:
    get_instance(),add_attends(),decrease_attendance(),change_home_team(),change_away_team()
    """

    def __init__(self, name=None, capacity=0, current_attendance=0, number_of_shower_rooms=0,
                 volume_of_the_pool=0, maximum_number_of_participants_in_competition=0):
        """
        This is constructor to init fileds of class
        :param name:
        :param capacity:
        :param current_attendance:
        """
        super().__init__(name, capacity, current_attendance)
        self.maximum_number_of_participants_in_competition = maximum_number_of_participants_in_competition
        self.volume_of_the_pool = volume_of_the_pool
        self.number_of_shower_rooms = number_of_shower_rooms
        self.equipment_set = {"swimming cap","goggles","flippers"}

    def __str__(self):
        """
            The method returns a string view of object
            :return: string view of object
        """
        return f"{super().__str__()}\nNumber of Shower Rooms: {self.number_of_shower_rooms}\n" \
               f"Volume of the Pool: {self.volume_of_the_pool}\n" \
               f"Maximum Number of Participants in Competition: {self.maximum_number_of_participants_in_competition}"

    def get_supported_sports(self):
        """
        overriding abstract method
        :return: Returns a list of sports that can be contested at this sports complex
        """
        return ['SWIMMING']
