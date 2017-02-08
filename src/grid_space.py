class Grid(object):
    def __init__(self,row, col):
        self.row = row
        self.col = col

        local_grid = [[]]
        i = 1
        while(i < self.col-1):
            local_grid.append([])
            j = 1
            while(j < self.row-1):
                local_grid[i].append("O")
                j+=1
            i+=1
        self.grid = local_grid

    def print_grid(self):
        # print(self.grid)
        for row in self.grid:
            print(' '.join(row))
        # i = 0
        # while(i < self.col-1):
        #     j = 0
        #     while(j < self.row-1):
        #         print(self.grid[i][j])
        #         j+=1
        #     i+=1

grid = Grid(25,25)

grid.print_grid()
