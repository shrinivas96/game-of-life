import numpy as np

class GoL:
    def __init__(self, grid_dim=(5, 5)):
        self.grid_dim = grid_dim        
        self.grid = np.zeros(grid_dim, dtype=int)
        self.set_seed()
        

    def set_seed(self):
        print("The grid is initialized with 0's. Now, you can set the seed.")
        # seed_input = input("Please enter all the 1's and 0's in a space separated format").split(" ")
        seed_input = "0 1 0 0 1 0 0 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1 1".split(" ")
        seed_arr = np.array(seed_input).astype(int)
        seed = seed_arr.reshape(self.grid_dim)
        self.grid = seed

    """
    def set_seed(self):
        print("The grid is initialized with 0's. Now, you can set the seed.")
        print("You will first enter the number of live cells, and then enter the (row, column) tuple for the live cells")

        num_of_live_cells = int(input("\nPlease enter the number of live cells to create the initial pattern: "))

        # These are the (row, column) indices that will be set to 1 when the user enters them
        row, col = 0, 0
        for _ in range(num_of_live_cells):
            # The user should have the initial pattern in mind in termns of the row, column.
            row, col = input("Enter the index that you want to set as live in tuple (comma separated): ").split(",")

            self.grid[int(row), int(col)] = 1.0
    """


    def print_grid(self):
        print(self.grid)
    

    def black_box(self, curr_cell_st, sum_of_adj):
        """
        The rules for determining the next state is given by:
         - Any live cell with two or three live neighbours survives.
         - Any dead cell with three live neighbours becomes a live cell.
         - All other live cells die in the next generation. Similarly, all other dead cells stay dead.
        """
        
        if (curr_cell_st == 0 and sum_of_adj == 3):
            nxt_cell_st = 1

        elif (curr_cell_st == 1 and 2 <= sum_of_adj <= 3):
            nxt_cell_st = 1

        else:
            nxt_cell_st = 0
        
        return nxt_cell_st


if __name__ == "__main__":

    # Grid will be of size nxn
    n = 5
    m = 5
    obj1 = GoL((n, m))
    obj1.print_grid()