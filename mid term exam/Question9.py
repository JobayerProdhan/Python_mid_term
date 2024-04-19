class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    def entry_show(self, show_id, movie_id, movie_name, time):
        show_info = (show_id, movie_id, movie_name, time)
        self._show_list.append(show_info)

    def allocate_seats(self):
        seats = [['Free' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats['Free'] = seats

    def book_seats(self, show_id, seat_list):
        show_found = False
        for show_info in self._show_list:
            if show_info[0] == show_id:
                show_found = True
                for row, col in seat_list:
                    if 0 <= row < self._rows and 0 <= col < self._cols:
                        if self._seats['Free'][row][col] == "Free":
                            self._seats['Free'][row][col] = 'Booked'
                            print(f'Seat({row},{col}) booked successfully.')
                        else:
                            print(f'Seat ({row},{col}) is already booked.')
                    else:
                        print(f'Seat ({row},{col}) is out of bounds')
                break
        if not show_found:
            print("Show ID not found")

    def print_seats(self, status='Free'):
        for row in self._seats[status]:
            print(' '.join(row))

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        print("Show ID\tMovie ID\tMovie Name\tTime")
        for show_info in self._show_list:
            print(f"{show_info[0]}\t{show_info[1]}\t{show_info[2]}\t{show_info[3]}")

    def view_available_seats(self, show_id):
        show_found = False
        for show_info in self._show_list:
            if show_info[0] == show_id:
                show_found = True
                print(f"Available seats for Show ID {show_id}:")
                for i, row in enumerate(self._seats['Free']):
                    for j, seat in enumerate(row):
                        if seat == "Free":
                            print(f"Row: {i}, Col: {j}")
                break
        if not show_found:
            print("Show ID not found")

    def print_all_seats(self):
        print("All Seats:")
        for row in self._seats['Free']:
            print(' '.join(row))


class CounterSystem:
    def __init__(self, hall):
        self._hall = hall

    def run(self):
        while True:
            print("\nCounter Menu:")
            print("1. View all shows running")
            print("2. View available seats for a show")
            print("3. Book tickets for a show")
            print("4. View all seats")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self._hall.view_show_list()
            elif choice == "2":
                show_id = input("Enter the show ID to view available seats: ")
                self._hall.view_available_seats(show_id)
            elif choice == "3":
                show_id = input("Enter the show ID to book tickets: ")
                if not self.validate_show_id(show_id):
                    continue
                num_seats = int(input("How many seats do you want to book?: "))
                seat_list = []
                for _ in range(num_seats):
                    row = int(input("Enter row number for seat: "))
                    col = int(input("Enter col number for seat: "))
                    if not self.validate_seat(row, col):
                        continue
                    seat_list.append((row, col))
                self._hall.book_seats(show_id, seat_list)
            elif choice == "4":
                self._hall.print_all_seats()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def validate_show_id(self, show_id):
        for show_info in self._hall.show_list:
            if show_info[0] == show_id:
                return True
        print("Show ID not found")
        return False

    def validate_seat(self, row, col):
        if 0 <= row < self._hall.rows and 0 <= col < self._hall.cols:
            if self._hall.seats['Free'][row][col] == "Free":
                return True
            else:
                print("Seat is already booked.")
        else:
            print("Seat is out of bounds.")
        return False


# Get hall details from users
rows = int(input("Enter the Number of rows in the Hall:"))
cols = int(input("Enter the  Number of columns in the Hall: "))
hall_no = input("Enter the hall Number: ")
hall = Hall(rows=rows, cols=cols, hall_no=hall_no)
hall.allocate_seats()

# Get show details from user
show_id = input("Enter show ID: ")
movie_id = input("Enter movie ID: ")
movie_name = input("Enter movie name: ")
time = input("Enter show time: ")
hall.entry_show(show_id=show_id, movie_id=movie_id, movie_name=movie_name, time=time)

# Book seats for the show
num_seats = int(input("How many seats do you want to book?: "))
seat_list = []
for _ in range(num_seats):
    row = int(input("Enter row number for seat: "))
    col = int(input("Enter col number for seat: "))
    seat_list.append((row, col))

hall.book_seats(show_id, seat_list)

# Create counter system and run it
counter_system = CounterSystem(hall)
counter_system.run()
