# Left to right, or top to bottom
# Check available cell
# Apply word 
# Rules:
# 1. Check length 
# 2. Check already existing letter in the same space
# 3. Check existing cipher codes  


crossword_array=[
        [21, 6, 25, 25, 17],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6]
    ]
crossword_array=[
        ['h', 'e', 'l', 'l', 'o'],
        [14, 0, 6, 0, 2],
        [1, 11, 16, 1, 17],
        [11, 0, 16, 0, 5],
        [26, 3, 14, 20, 6]
    ]
crossword_words=['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace']

tmp_crossword_array=crossword_array

def cells_available(start_cell, end_cell):
    xs=start_cell[0]
    xe=end_cell[0]
    ys=start_cell[1]
    ye=end_cell[1]
    if xs == xe:
        # left to right
        x=xs
        for y in range(ys,ye+1):
            if isinstance(crossword_array[x][y],int):
                return True
    elif ys == ye:
        # top to bottom
        y=ys
        for y in range(xs,xe+1):
            if isinstance(crossword_array[x][y],int):
                return True
    else:
        raise Exception

    return False

def last_vertical_cell_index(index, l):
    x=index[0]
    y=index[1]
    for tmp_x in range(len(l)):
        x=tmp_x
        if l[tmp_x][y] == 0:
            break
    return (x,y)
    
def last_horizontal_cell_index(index, l):
    x=index[0]
    y=index[1]
    for tmp_y in range(len(l[x])):
        y=tmp_y
        if l[x][tmp_y] == 0:
            break
    return (x,y)    

def is_top_index(index, l):
    x=index[0]
    y=index[1]
    if x == 0 or l[x-1][y] == 0:
        return True
    return False

def is_left_index(index, l):
    x=index[0]
    y=index[1]
    if y == 0 or l[x][y-1] == 0:
        return True
    return False

def process_word(words):
    for i in range(len(words)):
        word=words.pop(0)
        # check all rules 

def main():
    for x in range(len(crossword_array)):
        for y in range(len(j)):
            c_index=(x,y)
            # check if c_index is not in the middle
            # top->bottom
            if is_top_index(c_index, crossword_array):
                l_index=last_vertical_cell_index(c_index, crossword_array)
                if l_index[0] - c_index[0] > 1:
                    # process
            # left->right
            if is_left_index(c_index, crossword_array):
                l_index=last_horizontal_cell_index(c_index, crossword_array)
                if l_index[1] - c_index[1] > 1:
                    # process

            

print(cells_available((0,0),(0,4)))