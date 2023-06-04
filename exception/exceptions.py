class NotEnoughSeatsException(Exception):
    def __init__(self):
        super().__init__("There are not enough seats")


class NotMatchingModeException(Exception):
    def __int__(self):
        super().__init__("Exception: does not matching mode.")

    def __str__(self):
        return "Exception: does not matching mode."