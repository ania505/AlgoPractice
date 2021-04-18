// pancake sort problem from pramp

const flip = (arr, k) => {
    // reverses the order of the first k elements in the array arr
    // approach: 
        // use pointers to switch nums starting from opp ends going inward
        // L pointer on index 0, R pointer on k-1

    let pointL = 0;
    let pointR = k-1;
    while (pointL < pointR) {
        // console.log('HELLLOOOOOOO')
        // console.log(arr[pointL], arr[pointR])
        temp = arr[pointL]
        arr[pointL] = arr[pointR]
        arr[pointR] = temp
        // console.log(temp, arr[pointL], arr[pointR])
        pointL++;
        pointR--;
    }
    console.log(arr)
    return arr
}

const pancakeSort = (arr) => {
    // sorts and returns the input array
    // "you are allowed" to use flip() to make the changes in the array

    let max = 0;
    let maxIdx = 0;
    for (let i=0; i<arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i]
            maxIdx = i
        }

    }
    console.log(max, maxIdx)
    return flip(arr, maxIdx+1)
}


pancakeSort([1, 5, 4, 3, 2])        // output: [1, 2, 3, 4, 5]
// console.log(flip([5, 4, 3, 2, 1], 4) )       // output: [2, 3, 4, 5, 1]