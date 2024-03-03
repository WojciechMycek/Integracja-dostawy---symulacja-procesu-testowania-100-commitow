import tkinter as tk

class SquareMovementApp:
    def __init__(self, master, width=600, height=400):
        self.master = master
        self.width = width
        self.height = height
        
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        
        self.ground_y = 250
        
        self.canvas.create_line(0, self.ground_y, self.width, self.ground_y, fill="black")
        
        self.square_size = 50
        self.square = self.canvas.create_rectangle(50, 200, 50 + self.square_size, 200 + self.square_size, fill="blue")
        
        self.obstacle_size = 30
        self.obstacle = self.canvas.create_rectangle(300, 220, 300 + self.obstacle_size, 220 + self.obstacle_size, fill="red")
        
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)
        
    def move_left(self, event):
        if not self.check_collision(-10, 0):
            self.canvas.move(self.square, -10, 0)
        
    def move_right(self, event):
        if not self.check_collision(10, 0):
            self.canvas.move(self.square, 10, 0)
        
    def move_up(self, event):
        self.canvas.move(self.square, 0, -60)
        
    def move_down(self, event):
        square_coords = self.canvas.coords(self.square)
        if square_coords[3] < self.ground_y:
            self.canvas.move(self.square, 0, 10)
    
    def check_collision(self, x_offset, y_offset):
        square_coords = self.canvas.coords(self.square)
        obstacle_coords = self.canvas.coords(self.obstacle)
        
        square_coords_moved = [square_coords[0] + x_offset, square_coords[1] + y_offset,
                               square_coords[2] + x_offset, square_coords[3] + y_offset]
        
        if (square_coords_moved[0] < obstacle_coords[2] and square_coords_moved[2] > obstacle_coords[0] and
            square_coords_moved[1] < obstacle_coords[3] and square_coords_moved[3] > obstacle_coords[1]):
            return True
        else:
            return False 

root = tk.Tk()
root.title("Square Movement")

app = SquareMovementApp(root)

root.mainloop()
