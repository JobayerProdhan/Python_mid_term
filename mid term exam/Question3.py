class Hall:
     def __init__(self,seats,show_list,rows,cols,hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
    
     def entry_show(self,show_id,movie_id,movie_name,time):
         show_info = (show_id,movie_id,movie_name,time)
         self.show_list.append(show_info)
        
     def allocate_seats(self):
         seats = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]
         self.seats = {'Free':seats}

# hall1 = Hall(seats={},show_list=[],rows=5,cols=10,hall_no = 1)
# hall1.entry_show(show_id="111",movie_id="132",movie_name="pathan",time ="10:00 AM")


# Get hall details from users 
rows = int(input("Enter the Number of rows in the Hall:"))
cols = int(input("Enter the  Number of columns in the Hall: "))
hall_no = input("Enter the hall Number: ")
hall1 = Hall(seats={},show_list=[],rows = rows,cols = cols,hall_no = hall_no)

# Get show details from user 

show_id = input("Enter show ID: ")
movie_id = input("Enter movie ID: ")
movie_name = input("Enter movie name: ")
time = input("Enter show time: ")

hall1.entry_show(show_id=show_id,movie_id=movie_id,movie_name=movie_name,time =time)

print("Show List: ",hall1.show_list)
print("Seats: ",hall1.seats)