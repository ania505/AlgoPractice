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
    



maxTickets([8, 5, 4, 8, 4])     # should return 3