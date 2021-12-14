from game_parameters import HEIGHT, WIDTH
# from snake import *


class Board:
    def __init__(self):
        self.__height = HEIGHT
        self.__width = WIDTH
        self.current_board = self.new_board()

    def add_snake(self, snake) -> bool:
        """
        Adds a car to the game.
        :param snake: snake object of car to add
        :return: None
        """
        coordination = snake.snake_coordinates()
        add = True

        for coordinate in coordination:
            if (snake.length < 1 or snake.length > 3
                    or coordinate not in self.cell_list()
                    or self.cell_content(
                        (coordinate[0], coordinate[1])) is not None):
                return False
        if add:
            for coordinate in coordination:
                self.current_board[coordinate[0]][coordinate[1]] = snake

    def new_board(self) -> list:
        """
        function that create new empty board
        :return: new empty board
        """
        board = []

        for row in range(self.__height):
            new_row = []
            for col in range(self.__width):
                new_row.append('*')
            board.append(new_row)

        return board

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_print = ""

        for row in range(len(self.current_board)):
            board_print += '\n'
            for col in range(len(self.current_board) + 1):
                board_print += self.current_board[row][col] + '  '

        return board_print

    def cell_list(self) -> list:
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        board = []

        for row in range(HEIGHT):
            board.append((row, 0))
            for col in range(1, WIDTH):
                board.append((row, c))

        return board

    def cell_content(self, coordinate: tuple) -> any:
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        coordinate = list(coordinate)
        row = coordinate[0]
        col = coordinate[1]

        if 0 <= row < HEIGHT and 0 <= col < WIDTH:
            if self.current_board[row][col] != '*':
                return self.current_board[row][col]
            return None

    def add_bomb(self, x: int, y: int, bomb) -> None:
        if self.cell_content((x, y)) is None:
            self.current_board[x][y] = bomb

    def add_apple(self, x:int, y:int, apple):
        if self.cell_content((x, y)) is None:
            self.current_board[x][y] = apple


b = Board()

c = b.cell_list()

print(c)
