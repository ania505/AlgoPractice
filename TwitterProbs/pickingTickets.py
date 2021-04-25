# problem #1 from Twitter code challenge

# Consider an array of n ticket prices, tickets. A number, m, is defined as the size 
# of some subsequence, s, of tickets where each element covers an unbroken range of Integers. 
# That is to say, if you were to sort the elements in s, the absolute difference between any 
# elements j and j+1 would be either 0 or 1. Determine the maximum length of a subsequence 
# chosen from the tickets array.

# Example
# tickets = [8, 5, 4, 8, 4]
# Valid subsequences, sorted, are (4, 4, 5) and (8, 8). 
# These subsequences have m values of 3 and 2, respectively. 
# Return 3.

def maxTix(tickets):
    sorty = sorted(tickets)
    print(sorty)
    i = 0
    j = 1
    bigSub = 0


    while i < len(sorty) and j < len(sorty):
        # 
        if j+1 < len(sorty):
            print(sorty[i], sorty[j], sorty[j+1])
            if abs(sorty[j] - sorty[j+1]) == 0 or abs(sorty[j] - sorty[j+1]) == 1:
                # i += 1
                j += 1
            else:
                recentSub = abs(j-i) + 1
                print('recent: ', recentSub, 'big: ', bigSub)
                if recentSub > bigSub:
                    bigSub = recentSub
                i = j+1
                if j < len(sorty):
                    j += 1
        else:
            recentSub = abs(j-i) + 1
            print('recent: ', recentSub, 'big: ', bigSub)
            if recentSub > bigSub:
                bigSub = recentSub
            i = j+1
            if j < len(sorty):
                j += 1
        
    return bigSub
    

print('outputONE', maxTix([8, 5, 4, 8, 4]))     # should return 3
print('outputTWO', maxTix([4, 13, 2, 3]))    # should return 3
print('outputTHREE', maxTix([0, 1, 3, 4, 5, 6, 7, 12, 13, 14]))    # should return 5


def maxTickets(tickets):
    sorty = sorted(tickets)
    # print(sorty)
    groups = []
    for i in range(len(sorty)):
        if i != 0:
            prev = sorty[i-1]
            curr = sorty[i]
            if abs(prev-curr)==1 or abs(prev-curr)==0:
                # you want to keep adding to the group until the above is false
                print('in if', prev, curr)
                # groups.append([prev, curr])
                # for j in range(len(sorty[i:])):

                #   might need to make a helper function. recursion maybe?
                # recursion >>> keep going until line 23 is false
                # unsure how to add multiple numbers to one subsequence

                currSub = [prev, curr]
            else:
                groups.append(currSub)
        else:
            continue
    print(groups)
    # bigSub = []
    # for sub in range(len(groups)):
    #     if len(bigSub) < len(sub):
    #         bigSub = sub
    # return bigSub
    



# maxTickets([8, 5, 4, 8, 4])     # should return 3