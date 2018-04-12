

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self,symbol,row,col):
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        self.row = row
        self.col = col

    def get_location(self):
        return (self.row, self.col)

    def eat_sprouts(self,):
        self.num_sprouts_eaten += 1

    def __str__(self):
        result = " {0} at {1} ate {2} sprouts.".format( self.symbol, (self.row,self.col), self.num_sprouts_eaten)
        return result





class Maze:
    """ A 2D maze. """
    def __init__(self, maze, rat_1, rat_2):
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        sprouts = 0
        for line in maze:
            for elem in line:
                if elem ==SPROUT:
                    sprouts += 1
        self.num_sprouts_left = sprouts

    def is_wall(self,row,col):

        elem = self.maze[row][col]
        return (elem == WALL)

    def get_character(self,row,col):
        elem = self.maze[row][col]
        if self.rat_1.get_location() == (row, col):
            elem = self.rat_1.symbol
        if self.rat_2.get_location() == (row, col):
            elem = self.rat_2.symbol
        return elem

    def set_character(self,row,col, new_character):
        self.maze[row][col] = new_character


    def move(self,Rat,ver,hor):
        new_location = (Rat.row + ver, Rat.col + hor )
        elem = self.get_character(new_location[0], new_location[1])
        if elem == WALL:
            return False
        else:
            Rat.set_location(new_location[0], new_location[1])
            if elem == SPROUT:
                Rat.eat_sprouts()
                self.set_character(new_location[0], new_location[1], HALL)
                self.num_sprouts_left -=1
            return True

    def __str__(self):
        result = ""
        rows = len(self.maze)
        cols = len(self.maze[0])
        for i in range(rows):
            for j in range(cols):
                char = self.get_character(i, j)
                result += char
            result += "\n"
        result += str(self.rat_1)
        result += "\n"
        result += str(self.rat_2)
        return result
