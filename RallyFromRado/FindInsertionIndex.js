// i think im missing the 1st part of the problem pic

// 1st arg is array that 2nd arg needs to be put Into. need to get index of where 2nd arg would fit

const binSearch = (input, l, r, x) => {
    while (l <= r) {
        mid = Math.floor((l+r) / 2)
        if (input[mid] < x) {
            // if x == greater, mid needs to move towards the right
            binSearch(input, mid+1, r, x)
        }
        else if (input[mid] < x) {
            // if x == lesser, mid needs to move towards the left

            binSearch(input, l, mid-1, x)
        }
        else{
            // if arr[mid] === x
            return mid
        }
    }

}

const findInsertionIndex = (input, x) => {
    // binary search
    if (input.length === 0) {
        return 0
    }

    l = 0
    r = input.length - 1
    return binSearch(input, l, r, x)

}

console.log(findInsertionIndex([], 10))    //---> 0
console.log(findInsertionIndex([1, 2, 3], 4))  //---> 3
console.log(findInsertionIndex([1, 2, 3, 5], 4))   //---> 3
console.log(findInsertionIndex([1, 2, 3, 5], 6))   //---> 4
