import math
#import queue
import heapq

# def dfs(samples):
def bfs(samples):
    stack = []
    stack.append((0,0))
    # myQ = queue.Queue()

    valids = 0
    hashy = {}
    # print(samples)
    # while len(stack) != 0:
    while len(stack) != 0:
        currTup = stack.pop()
        print(currTup)
        if currTup in hashy:
            continue
        hashy[currTup] = 1
        valids += 1
        print('curr', currTup)
        tupX = currTup[0]
        tupY = currTup[1]
        minBoundsY = len(samples)
        minBoundsX = len(samples)
        if samples[tupX][tupY] == 1:
            if tupX+1 < len(samples) and tupY+1 < len(samples[0]):
                right = samples[tupX][tupY+1]
                down = samples[tupX+1][tupY]
                downR = samples[tupX+1][tupY+1]
                if min(right, down, downR) == 1:
                    stack.append((tupX, tupY+1))
                    stack.append((tupX+1, tupY))
                    stack.append((tupX+1, tupY+1))
                else:
                    if right == 0 and tupY+1 < minBoundsY:
                        minBoundsY = tupY+1
                    if down == 0 and tupX+1 < minBoundsX:
                        minBoundsX = tupX+1
                    if downR == 0 and tupX+1 < minBoundsX and tupY+1 < minBoundsY:
                        minBoundsX = tupX+1
                        minBoundsY = tupY+1
                    
                    # stack.insert(0, (tupX, tupY+1))
                    # stack.insert(0, (tupX+1, tupY))
                    # stack.insert(0, (tupX+1, tupY+1))
                # else:
                #     # you are at an edge piece
                #     maxY = tupY + 1
                #     for c in range(len(samples)):
                #         print(maxY, c)
                #         samples[maxY][c] = 0
    
    # print(samples)
    # print(valids, int(math.floor(math.sqrt(valids))))
    # return math.sqrt(valids)
    print(min(minBoundsX, minBoundsY))
    return min(minBoundsX, minBoundsY)

    



bfs([[1,1,1,1,1],[1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,1,1]])