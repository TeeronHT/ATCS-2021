"""
An AI that uses Finite State Machines to solve a maze

@author: Teeron Hajebi Tabrizi
@version: 2022
"""
from fsm import FSM


class MazeBot:
    def __init__(self, maze_file):
        # The location of the bot
        self.x = None
        self.y = None

        # The map of the maze
        self.maze = None

        # The route the bot will take to get to the $
        self.path = None

        # Create an initialize the maze
        self.reset(maze_file)

        # TODO: Create the Bot's finite state machine (self.fsm) with initial state
        self.fsm = FSM('Neutral South')
        self.add_state_transitions()

    def add_state_transitions(self):
        """
        TODO: Implement add state transitions
        Adds all the state transitions to the fsm
        """
        self.fsm.add_transition(' ', 'Neutral South', self.move_south, 'Neutral South')
        self.fsm.add_transition(' ', 'Neutral East', self.move_east, 'Neutral East')
        self.fsm.add_transition(' ', 'Neutral North', self.move_north, 'Neutral North')
        self.fsm.add_transition(' ', 'Neutral West', self.move_west, 'Neutral West')

        self.fsm.add_transition('#', 'Neutral South', None, 'Neutral East')
        self.fsm.add_transition('#', 'Neutral East', None, 'Neutral North')
        self.fsm.add_transition('#', 'Neutral North', None, 'Neutral West')
        self.fsm.add_transition('#', 'Neutral West', None, 'Neutral South')

        self.fsm.add_transition('X', 'Neutral South', None, 'Neutral East')
        self.fsm.add_transition('X', 'Neutral East', None, 'Neutral North')
        self.fsm.add_transition('X', 'Neutral North', None, 'Neutral West')
        self.fsm.add_transition('X', 'Neutral West', None, 'Neutral South')

        self.fsm.add_transition('B', 'Neutral South', self.move_south, 'Boosted South')
        self.fsm.add_transition('B', 'Neutral East', self.move_east, 'Boosted East')
        self.fsm.add_transition('B', 'Neutral North', self.move_north, 'Boosted North')
        self.fsm.add_transition('B', 'Neutral West', self.move_west, 'Boosted West')

        self.fsm.add_transition(' ', 'Boosted South', self.move_south, 'Boosted South')
        self.fsm.add_transition(' ', 'Boosted East', self.move_east, 'Boosted East')
        self.fsm.add_transition(' ', 'Boosted North', self.move_north, 'Boosted North')
        self.fsm.add_transition(' ', 'Boosted West', self.move_west, 'Boosted West')

        self.fsm.add_transition('X', 'Boosted South', self.move_south, 'Boosted South')
        self.fsm.add_transition('X', 'Boosted East', self.move_east, 'Boosted East')
        self.fsm.add_transition('X', 'Boosted North', self.move_north, 'Boosted North')
        self.fsm.add_transition('X', 'Boosted West', self.move_west, 'Boosted West')

        self.fsm.add_transition('B', 'Boosted South', self.move_south, 'Neutral South')
        self.fsm.add_transition('B', 'Boosted East', self.move_east, 'Neutral East')
        self.fsm.add_transition('B', 'Boosted North', self.move_north, 'Neutral North')
        self.fsm.add_transition('B', 'Boosted West', self.move_west, 'Neutral West')

        self.fsm.add_transition('#', 'Boosted South', None, 'Boosted East')
        self.fsm.add_transition('#', 'Boosted East', None, 'Boosted North')
        self.fsm.add_transition('#', 'Boosted North', None, 'Boosted West')
        self.fsm.add_transition('#', 'Boosted West', None, 'Boosted South')

        self.fsm.add_transition('$', 'Boosted South', self.move_south, 'Finished')
        self.fsm.add_transition('$', 'Boosted East', self.move_east, 'Finished')
        self.fsm.add_transition('$', 'Boosted North', self.move_north, 'Finished')
        self.fsm.add_transition('$', 'Boosted West', self.move_west, 'Finished')

        self.fsm.add_transition('$', 'Neutral South', self.move_south, 'Finished')
        self.fsm.add_transition('$', 'Neutral East', self.move_east, 'Finished')
        self.fsm.add_transition('$', 'Neutral North', self.move_north, 'Finished')
        self.fsm.add_transition('$', 'Neutral West', self.move_west, 'Finished')

    def reset(self, filename):
        """
        Resets the maze bot to have an empty path and sets the maze
        from the given filename. The bot starts at position 1, 1
        :param filename: The name of the file to read the maze in from
        """
        # The bot always starts at the Northwest corner of the maze
        self.x = 1
        self.y = 1

        # The path resets to empty
        self.path = []

        # Read in the maze from the file
        self.maze = []
        with open(filename) as f:
            line = f.readline().strip()
            self.maze.append(line)
            while line:
                line = f.readline().strip()
                self.maze.append(line)

    def move_south(self):
        """
        TODO: Implement move south
        Changes the bot's location 1 spot South
        and records the movement in self.path
        """
        self.y = self.y + 1
        self.path.append("South")

    def move_east(self):
        """
        TODO: Implement move east
        Changes the bot's location 1 spot East
        and records the movement in self.path
        """
        self.x = self.x + 1
        self.path.append("East")

    def move_north(self):
        """
        TODO: Implement move north
        Changes the bot's location 1 spot North
        and records the movement in self.path
        """
        self.y = self.y - 1
        self.path.append("North")

    def move_west(self):
        """
        TODO: Implement move west
        Changes the bot's location 1 spot West
        and records the movement in self.path
        """
        self.x = self.x - 1
        self.path.append("West")

    def get_next_space(self):
        """
        TODO: Implement get next space
        Using the current state of the bot, returns the next space in the maze
            Ex. If the current state has the bot moving south, the next space in the
            maze would be self.maze[self.y+1][self.x]
        :return: The next spot in the maze Ex. "B", "#", " ", "X"
        """

        if "South" in self.fsm.current_state:
            return self.maze[self.y + 1][self.x]
        elif "East" in self.fsm.current_state:
            return self.maze[self.y][self.x + 1]
        elif "North" in self.fsm.current_state:
            return self.maze[self.y - 1][self.x]
        elif "West" in self.fsm.current_state:
            return self.maze[self.y][self.x - 1]

    def print_maze(self):
        """
        Prints the 2D array representing the maze
        Prints an 'M' for the current location of the bot in the maze
        """
        for row in range(len(self.maze)):
            curr = ''
            for col in range(len(self.maze[row])):
                if row == self.y and col == self.x:
                    curr += 'M'
                else:
                    curr += self.maze[row][col]
            print(curr)

    def solve_maze(self):
        """
        Calls on the FSM to process the next input symbol from the maze
        in order to transition the bot between states until it reaches the "FIN" state
        """
        # TODO: Implement solve maze
        while self.fsm.current_state != 'Finished':
            next_space = self.get_next_space()
            self.fsm.process(next_space)
            self.print_maze()

        print("Determined the path:")
        print(self.path)