class Hall:
    def __init__(self,seats,show_list,rows,cols,hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

class Star_cinema(Hall):
    hall_list = []

    def __init__(self, seats, show_list, rows, cols, hall_no) -> None:
        super().__init__(seats, show_list, rows, cols, hall_no)
        Star_cinema.hall_list.append(self)

hall1 = Star_cinema(rows=5,cols=10,hall_no = 1)
hall1 = Star_cinema(rows=6,cols=12,hall_no = 2)

for hall in Star_cinema.hall_list:
    print(f"Hall number:{hall.hall_no},Rows:{hall.rows},Columns: {hall.cols}")
    
        