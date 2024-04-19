class Hall:
    def __init__(self, hall_name):
        self.hall_name = hall_name

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

# Example usage:
hall1 = Hall("Hall 1")
hall2 = Hall("Hall 2")

Star_Cinema.entry_hall(hall1)
Star_Cinema.entry_hall(hall2)

print(Star_Cinema.hall_list)
