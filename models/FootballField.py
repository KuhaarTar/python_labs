from lab8.models.AbstractStadium import AbstractStadium


class FootballField(AbstractStadium):
    """
    Class that describe FootballField
    """

    def __init__(self, name, capacity, current_attendance, length, width, type_field_coverage):
        """
        Initializes a FootballField object.
        :param name: The name of the football field.
        :param capacity: The capacity of the football field.
        :param current_attendance: The current attendance of the football field.
        :param length: The length of the football field.
        :param width: The width of the football field.
        :param type_field_coverage: The type of field coverage for the football field.
        """
        super().__init__(name, capacity, current_attendance)
        self.length = length
        self.width = width
        self.type_field_coverage = type_field_coverage

    def __str__(self):
        """
            The method returns a string view of object
            :return: string view of object
        """
        return f"{super().__str__()} Length: {self.length} " \
               f"Width: {self.width} Type of Field Coverage: {self.type_field_coverage}"

    def get_supported_sports(self):
        """
        overriding abstract method
        :return: Returns a list of sports that can be contested at this sports complex
        """
        return ['Football']
