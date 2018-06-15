import scrollphathd


# Avoid retina-searage!
scrollphathd.set_brightness(0.5)

# The height and width of the forest. Same as Scroll pHAT HD
# dimensions


# Brightness values for a tree, fire, and blank space
full, half, off = (1.0, 0.5, 0.0)

class MyScrollPhat:
    def __init__(self):
        self.height = scrollphathd.height
        self.width = scrollphathd.width
	self.grid = [[off for j in range(self.height)] for i in range(self.width)]

    def get_grid(self):
        return self.grid

    def get_height(self):
        return self.height
   
    def get_width(self):
        return self.width

    def reset_grid(self):
	self.grid = [[off for j in range(self.height)] for i in range(self.width)]
	self.show_grid()

    def show_grid(self):
        scrollphathd.clear()
        for x in range(self.width):
            for y in range(self.height):
                scrollphathd.set_pixel(x, y, self.grid[x][y])
        scrollphathd.show()

    def update_grid(self,grid):
        self.grid = grid

    def update_pos(self,state,x,y):
        self.grid[x][y] = state

    def update_and_show(self,grid):
        self.update_grid(grid)
        self.show_grid()
