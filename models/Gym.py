from lab8.models.AbstractStadium import AbstractStadium


class Gym(AbstractStadium):
    def __init__(self, name, capacity, current_attendance, count_of_simulator, monthly_subscription_fee, count_of_coach):
        """
        Initializes a Gym object.

        :param name: The name of the gym.
        :param capacity: The capacity of the gym.
        :param current_attendance: The current attendance of the gym.
        :param count_of_simulator: The count of simulators in the gym.
        :param monthly_subscription_fee: The monthly subscription fee for the gym.
        :param count_of_coach: The count of coaches in the gym.
        """
        super().__init__(name, capacity, current_attendance)
        self.count_of_simulator = count_of_simulator
        self.monthly_subscription_fee = monthly_subscription_fee
        self.count_of_coach = count_of_coach

    def get_supported_sports(self):
        """
        Returns the list of supported sports for the gym.

        :return: The list of supported sports for the gym.
        """
        return ['BOX']

    def __str__(self):
        """
        Returns a string representation of the Gym object.

        :return: String representation of the Gym object.
        """
        return f"{super().__str__()} Count of Simulator: {self.count_of_simulator} " \
               f"Monthly Subscription Fee: {self.monthly_subscription_fee} " \
               f"Count of Coach: {self.count_of_coach}"
