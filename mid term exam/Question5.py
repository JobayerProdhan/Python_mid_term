
class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, show_id, movie_id, movie_name, time):
        show_info = (show_id, movie_id, movie_name, time)
        self.show_list.append(show_info)

    def allocate_seats(self):
        seats = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats['Free'] = seats

    def book_seats(self, show_id, seat_list):
        for show_info in self.show_list:
            if show_info[0] == show_id:
                for row, col in seat_list:
                    if 0 <= row < self.rows and 0 <= col < self.cols:
                        if self.seats['Free'][row][col] == "Free":
                            self.seats['Free'][row][col] = 'Booked'
                            print(f'Seat({row},{col}) booked successfully.')
                        else:
                            print(f'Seat ({row},{col}) is already booked.')
                    else:
                        print(f'Seat ({row},{col}) is out of bounds')
                return
        print("Show ID not found")

    def print_seats(self):
        for row in self.seats['Free']:
            print(' '.join(row))

    def view_show_list(self):
        print("Shows running in Hall", self.hall_no)
        print("Show ID\tMovie ID\tMovie Name\tTime")
        for show_info in self.show_list:
            print(f"{show_info[0]}\t{show_info[1]}\t{show_info[2]}\t{show_info[3]}")


# Get hall details from users
rows = int(input("Enter the Number of rows in the Hall:"))
cols = int(input("Enter the  Number of columns in the Hall: "))
hall_no = input("Enter the hall Number: ")
hall1 = Hall(rows=rows, cols=cols, hall_no=hall_no)
hall1.allocate_seats()

# Get show details from user
show_id = input("Enter show ID: ")
movie_id = input("Enter movie ID: ")
movie_name = input("Enter movie name: ")
time = input("Enter show time: ")
hall1.entry_show(show_id=show_id, movie_id=movie_id, movie_name=movie_name, time=time)

# Book seats for the show
num_seats = int(input("How many seats do you want to book?: "))
seat_list = []
for _ in range(num_seats):
    row = int(input("Enter row number for seat: "))
    col = int(input("Enter col number for seat: "))
    seat_list.append((row, col))

hall1.book_seats(show_id, seat_list)

print("Show List: ", hall1.show_list)
print("Updated seats: ")
hall1.print_seats()

# View all shows running
hall1.view_show_list()

