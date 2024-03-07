import tkinter as tk

class SquareMovementApp:
    """Class representing an application allowing movement of a square on a canvas with an obstacle."""

    def __init__(self, master, width=600, height=400):
        """Initialize the application.

        Args:
            master (tk.Tk): The main Tkinter widget.
            width (int): The width of the canvas.
            height (int): The height of the canvas.
        """
        self.master = master
        self.width = width
        self.height = height
        self.score = 0  # Initial score
        
        # Create canvas for drawing objects
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        
        # Height of the ground line
        self.ground_y = 250
        
        # Create ground line
        self.canvas.create_line(0, self.ground_y, self.width, self.ground_y, fill="black")
        
        # Size of the player square
        self.square_size = 30
        self.square_size = 50
        
        # Create player square
        self.square = self.canvas.create_rectangle(50, 200, 50 + self.square_size, 200 + self.square_size, fill="blue")
        
        # Size of the obstacle
        self.obstacle_size = 30
        
        # Create obstacle
        self.obstacle = self.canvas.create_rectangle(300, 220, 300 + self.obstacle_size, 220 + self.obstacle_size, fill="red")
        
        # Set initial velocity
        self.velocity = 0
        
        # Set gravity
        self.gravity = 1
        
        # Bind arrow keys to movement functions
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.jump)
        
        # Create label to display score
        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack()
        
        # Start the game loop
        self.game_loop()
        
    def move_left(self, event):
        """Move the square to the left."""
        if not self.check_collision(-10, 0):
            self.canvas.move(self.square, -10, 0)
        
    def move_right(self, event):
        """Move the square to the right."""
        if not self.check_collision(10, 0):
            self.canvas.move(self.square, 10, 0)
        
    def jump(self, event):
        """Jump the square upwards."""
        self.velocity = -15
    
    def game_loop(self):
        """Game loop for controlling gravity and updating square position."""
        # Update square position / pipeline test
        self.canvas.move(self.square, 0, self.velocity)
        
        # Update velocity with gravity
        self.velocity += self.gravity
        
        # Check if square hits the ground
        square_coords = self.canvas.coords(self.square)
        if square_coords[3] >= self.ground_y:
            self.velocity = 0
            self.canvas.coords(self.square, square_coords[0], self.ground_y - self.square_size,
                               square_coords[0] + self.square_size, self.ground_y)
        
        # Check for collision with obstacle
        if self.check_collision(0, self.velocity):
            self.velocity = 0
            square_coords = self.canvas.coords(self.square)
            self.canvas.coords(self.square, square_coords[0], square_coords[1] - self.velocity,
                               square_coords[2], square_coords[3] - self.velocity)
            self.score += 1
            self.score_label.config(text="Score: " + str(self.score))
            self.canvas.delete(self.obstacle)
            self.spawn_obstacle()
            print("Score:", self.score)
        
        # Repeat the loop after a delay
        self.master.after(50, self.game_loop)
    
    def check_collision(self, x_offset, y_offset):
        """Check collision between the square and the obstacle."""
        square_coords = self.canvas.coords(self.square)
        obstacle_coords = self.canvas.coords(self.obstacle)
        
        square_coords_moved = [square_coords[0] + x_offset, square_coords[1] + y_offset,
                               square_coords[2] + x_offset, square_coords[3] + y_offset]
        
        if (square_coords_moved[0] < obstacle_coords[2] and square_coords_moved[2] > obstacle_coords[0] and
            square_coords_moved[1] < obstacle_coords[3] and square_coords_moved[3] > obstacle_coords[1]):
            return True
        else:
            return False
    
    def spawn_obstacle(self):
        """Spawn a new obstacle."""
        self.obstacle = self.canvas.create_rectangle(600, 220, 600 + self.obstacle_size, 220 + self.obstacle_size, fill="red")

root = tk.Tk()
root.title("Square Movement")

app = SquareMovementApp(root)

root.mainloop()
