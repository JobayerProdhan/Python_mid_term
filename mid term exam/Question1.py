class Hall:
    def __init__(self,hall_name) -> None:
        self.name = hall_name

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(clss,hall):
        clss.hall_list.append(hall)


hall1 = Hall("Star cinema")
hall2 = Hall("Modumoti")

Star_Cinema.entry_hall(hall1)
Star_Cinema.entry_hall(hall2)

print(Star_Cinema.hall_list)


