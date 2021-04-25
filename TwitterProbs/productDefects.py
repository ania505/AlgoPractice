# problem #2 from Twitter code challenge

# A quality agent is responsible for inspecting samples of the 
# finished products in the production line. Each sample contains 
# defective and non-defective products represented by 1 and 0 
# respectively. After placing the product samples sequentially in a 
# two-dimensional square matrix of product samples, determine the 
# size of the largest square area of defective products.

# Example
# nxn = 5x5 matrix of product samples
# samples [[1,1,1,1,1],[1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,1,1]]
# (1) (1) (1)  1   1 
# (1) (1) (1)  0   0 
# (1) (1) (1)  0   0
#  1   1   1   0   0 
#  1   1   1   1   1



import math

def largestArea(samples):
    row = len(samples)
    col = len(samples[0])
    validSqs = 0

    for r in range(row):
        for c in range(col):
            # maybe check lower right diagonal too?
            if samples[r][c+1]:
                rightN = samples[r][c+1]
            if samples[r+1][c]:
                downN = samples[r+1][c]
            if samples[r+1][c+1]:
                diagN = samples[r+1][c+1]
            
            # # need left, down, & downLeft 
            # TO DO WHEN COME BACK
            # adding to row/ col gave indexError: out of range
            # can backtrack by going out of the valid square and subtracting 
            #   from the row/ col. then adjust rest of code to that
            # MAYBE you can just check if the direction exists before?

            if min(rightN, downN, diagN) == 0:
                # check the min of the right direction & down direction & lower right diagonal
                # if one of them is 0, don't continue looking
                # you've reached the edge of the squared area
                print('0 was found', rightN, downN, diagN)
                break
            else:
                # if curr place has valid directions, add to validSqs?
                print('curr square is valid')
                validSqs += 1
    
    
    # might be a hacky way to do it:
    # 4 squares are in area, 2 is returned
    # 9 squares are in area, 3 is returned
    # can I just take the square root of # of valid squares?
    maxArea = math.sqrt(validSqs)
    print(validSqs, maxArea)
    return maxArea



largestArea([[1,1,1,1,1], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,1,1]])