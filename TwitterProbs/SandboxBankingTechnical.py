# """
# Implement the "wrap" function below.  It should accept a function as input and return a different function.  The newly created function should invoke the original input function on its parameters, and then either:

# (a) Return the original function's return value if no exception is thrown.  
# - OR - 
# (b) Return the int 1000 if an exception was thrown during the invocation of the original function

# Please see the `assert` tests below for clarification.
# """

# def wrap(function):
#     # Function to be implemented...
#     try:
            # function()
            # return function
        result = function
        
        return result
#     except:
#         return 1000
#     pass

# def function0(a):
#     return 10

# def function1(a, b, c):
#     raise Exception("function1 exception")
    
# def function2(a, b, c=10):
#     return c
    
# def function3(a=100, b=10, c="asdf"):
#     if b < 10:
#         raise Exception("function exception")
#     return c
    
# def function4():
#     return "dog"

# def function5(*args, **kwargs):
#     if args[2] == 3 and kwargs["g"] == "house":
#         return 0
#     raise Exception("function5 exception")

# function0 = wrap(function0)
# function1 = wrap(function1)
# function2 = wrap(function2)
# function3 = wrap(function3)
# function4 = wrap(function4)
# function5 = wrap(function5)

# assert(10 == function0(100))
# assert(1000 == function0("a", "bc", 5))
# assert(1000 == function1(0, 1, 2))
# assert(30 == function2(0, 0, c=30))
# assert(1000 == function2(0, 0, 0, c=30))
# assert(1000 == function3(b=9))
# assert("asdf" == function3(b=10))
# assert("dog" == function4())
# assert(1000 == function4(0))
# assert(0 == function5(0, 0, 3, a=10, g="house"))
# assert(1000 == function5())

# print("Success — end of script reached!")



# each person has 5 cards, 2 input hand cards, return which hand wins
# win: 2 pair, 1 pair, high card
#  suits dont matter
# ace is high
"""
def pokerWinner(hand1, hand2):
    player1 = {}
    player2 = {}
    
    sorty1  = sorted(hand1)
    i=0
    while i < len(hand1):
        card = sorty1[i]
        if card in player1:
            player1[card] += 1
        else:
            player1[card] = 1
        i+=1
        
    sorty2  = sorted(hand2)
    j=0
    while j < len(hand2):
        card = sorty2[i]
        if card in player2:
            player2[card] += 1
        else:
            player2[card] = 1
        j+=1
    
    bestHand1 = ''
    
    maxVal1 = 0
    for k in player1.keys():
        if player1[k] > maxVal1:
            maxVal1 = player1[k]
    
    if maxVal1 == 2:
        bestHand1 = '2pair'
    
    bestHand2 = ''
    maxVal2 = 0
    for k in player2.keys():
        if player2[k] > maxVal2:
            maxVal2 = player2[k]
    
    if maxVal2 == 2:
        bestHand2 = '2pair'
    
    
    
#     i=0
#     while i < len(hands):
#         eachHand = hands[i]
#         hands[i] = sorted(eachHand)
        
#         j=0
#         while j < len(hands[i]):
            
#             card = hands[i][j]
#             if card in hashy:
#                 hashy[card] += 1
#             else:
#                 hashy[card] = 1
#             j+=1
        
#         i+=1
        # print(hashy)
    


print(pokerWinner([6, 6, 10, 11, 4], [8, 8, 11, 11, 12]))

"""
"""
Implement the "get_account_balances" function below.  It should accept a list of int values that represent account numbers and return a list of "balance result" dicts that represent deposit account balances. There should be a result dict in the returned list for each account number in the input list.

The "get_account_balances" function should call the "_get_balance_for_account" function to retrieve the
correct balances for a given account number.  Returned values will be the "current_balance" and "available_balance" respectively.

If "_get_balance_for_account" completes successfully for a given account number, the corresponding dict in the list returned by "get_account_balances" should be:

{
    "success": True,
    "current_balance": 1000.0,
    "available_balance": 995.0
}

However, "_get_balance_for_account" will throw an exception if the account is not found.  In such cases,
the corresponding dict within the list returned by "get_account_balances" should be:

{
    "success": False,
    "message": "No account exists for provided account number"
}

Furthermore, any dict returned by "get_account_balances" corresponding to an input account number that was
not a Python int should be:

{
    "success": False,
    "message": "Provided account number is not an integer"
}

IMPORTANT HINT: Look at the assert statement at the end of this file -- it clarifies the requirements.

"""

def _get_balance_for_account(account_number):
    if account_number % 2 != 0:
        raise Exception("No account exists for provided account number")
    return 1000.0, 995.0

def get_account_balances(*account_numbers):
    # Please implement this function
    accnts = []
    for num in account_numbers:
         accnts.append(num)
    
    result = []
    i = 0
    while i < len(accnts):
        currAccnt = {}
        current_balance, available_balance = _get_balance_for_account(accnts[i])
        currAccnt["success"] = True
        currAccnt["current_balance"]  = current_balance
        currAccnt["available_balance"] = available_balance
        result.append(currAccnt)
        print(result)
        i+=1
    
    
    
    return result


# The assert statements below this line exist for testing purposes
expected = [
    {
        "success": True,
        "current_balance": 1000.0,
        "available_balance": 995.0
    },
    {
        "success": False,
        "message": "No account exists for provided account number"
    },
    {
        "success": False,
        "message": "Provided account number is not an integer"
    },
    {
        "success": True,
        "current_balance": 1000.0,
        "available_balance": 995.0
    }
]
     
assert(expected == get_account_balances(1001000, 1001005, "invalid number", 1001010))

print("Reached the end of the script!")







