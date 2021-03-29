const pairSum2 = (arr, sum) => {
    for (let i=0; i<arr.length; i++) {
        for (let j=i+1; j<arr.length; j++) {
            let currSum = arr[i] + arr[j];
            if (currSum === sum) {
                return true
            }

        }
    }
    return false
}

//using binary search 
const pairSum = (arr, sum) => {
    // look at 1st # 
    // sum - current # = number to find in arr
    // if that # in the arr return true
    // if not keep searching or return false

    if (arr.length < 2) {
        return false;
    }
    if (arr[0] >= sum) {
        return false;
    }

    for (let i=0; i<arr.length; i++) {
        let find = sum - arr[i]
        
        if (binSearch(find, arr.slice(i))) {
            console.log('here1')
            return true;
        }
    }
    return false;

}

function binSearch(find, arr){
    let l = 0;
    let mid = arr.length-1 / 2

    while (arr.length>1) {
        console.log('here2')
        if (find === arr[mid]) {
            console.log('here3')
            return true
        }
        if (find < arr[mid]) {
            // binSearch(find, arr.slice(l, mid))
            console.log('here4')
            arr = arr.slice(l, mid)
        }
        if (find > arr[mid]) {
            // binSearch(find, arr.slice(mid))
            console.log('here5')
           arr = arr.slice(mid)
        }
        else{
            console.log('fuck')
            break;
    }
    }
    if (arr[0] === find) {
        console.log('here6')
        return true
    } else {
        console.log('here7')
        return false
    }
}

console.log(pairSum([1, 1, 2, 3, 4, 5], 7))
console.log(pairSum([1, 2, 3, 4, 5], 10))
console.log(pairSum([0, 2, 3, 6, 9, 10], 10))
console.log(pairSum([1, 2, 3, 7, 8], 7))
console.log(pairSum([-2, 0, 4, 6, 10], 8))
console.log(pairSum([1, 2, 3, 4, 5], 2))

console.log(pairSum([1], 2))
console.log(pairSum([2], 2))
console.log(pairSum([], 1))