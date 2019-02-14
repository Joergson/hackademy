#Game of Life

import random

def setup_game(size,max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid,max_alive)


def get_empty_grid(size):
    new_grid = []
    for row in range(size):
        sub_grid = []
        for column in range(size):
            sub_grid.append("-")
        new_grid.append(sub_grid)
    return new_grid	

def rand_alive():
    number = random.randint(1,3)
    if number == 1:
        return True
    else:
        return False

def fill_grid_random(a_grid,max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        if remaining == 0:
            break
        for c_i in range(size):
            if remaining > 0:
                if rand_alive() == True:
                    a_grid[r_i][c_i] = "x"
                    remaining = remaining - 1
                else:
                    a_grid[r_i][c_i] = "-"
                if remaining == 0:
                    break

def print_grid(a_grid):
    for n in a_grid:
        if isinstance(n,list):
            for i in n:
                print(i,end="")
            print()

# Text for programm stars here:

print()
print("Hello to Game of Live!")
size = int(input("How large should the grid be?: "))
alive = int(input("How many cells should max be alive?: "))

a = get_empty_grid(size)

fill_grid_random(a,alive)

print()
print("Game of Life:")
print()
print_grid(a)
print()
            



# Meine Version:
#def fill_grid_random2(a_grid,max_alive):
#    
#    for row in a_grid:
#        count = 0
#        for element in row:
#            if rand_alive() == True:
#                row[count] = "x"
#            else:
#                row[count] = "-"
#            count = count + 1



