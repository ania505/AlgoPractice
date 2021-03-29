const isPal = (str) => {
    let low = str.toLowerCase();
    let res = true;
    let l = 0;
    let r = low.length-1;

    while(l < low.length / 2) {
        if (low[l] === low[r]) {
            l++;
            r--;
        } else {
            res = false;
            break;
        }
    }
    return res;

    // for (let i=0; i < str.length; i++) {
    //     // for (let j=str.length; j >= 0; j--)
    //     if (str[i] === str[j]) {

    //     }
    // }

}

console.log(isPal('car'))
console.log(isPal('racecar'))
console.log(isPal('RaCecAr'))
console.log(isPal('!? 100 ABCcba 001 ?!'))