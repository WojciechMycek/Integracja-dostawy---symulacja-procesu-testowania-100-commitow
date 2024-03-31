from typing import TypeVar

T = TypeVar('T')  # Deklaracja generycznego typu T

class Board:
    def __init__(self, height: int, width: int) -> int:
        '''self.higt - > definition of upper part of board
           self.width - > definition of lower part of board'''
        
        if not isinstance(height, int) or not isinstance(width, int):
            raise TypeError("Height and width must be integers")
        
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be positive integers")

        self.height = height
        self.width = width
    
    def draw_heigt(self) -> None:
        '''print height'''
        print("-" * self.height)
    
    def draw_width(self) -> None:
        '''draw width'''
        new = "|"
        for i in range(self.height):
            print(new + " " * self.height + new)
    
    def draw_board(self) -> None:
        '''draw board with previous defined functions'''
        self.draw_heigt()
        self.draw_width()
        self.draw_heigt()
    
    def moving(self) -> None:
        '''Function to define snake's movement'''
        pass

    def generate_matrix_board(self) -> None:
        '''Generate function of matrix to track snake movement
        and to generate board'''
        rows = self.height
        cols = self.width
        matrix = []

        for i in range(3):
            row = []
            for j in range(3):
                row.append(0)
                matrix.append(row)
        return matrix
    
    def starting_position(self) -> None:
        "Starting position of snake"
        board = self.generate_matrix_board()
        print(board)
        for i in range(3):
            board[i][2] = " "
        print(board)
