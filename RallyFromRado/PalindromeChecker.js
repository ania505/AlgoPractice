// A palindrome is a word that is spelled the same forwards as backwards. Please write a function that takes an input
// string and returns a boolean indicating whether the input is a palindrome.

const isPali = (s) => {
    
    
    // solution 2: reverse str comparision (suggested)
    low = s.toLowerCase()
    rev = low.split("").reverse().join("")
    res = true

    i = 0
    while (i < low.length) {
        if (low[i].toUpperCase()!=low[i].toLowerCase() && rev[i].toUpperCase()!=rev[i].toLowerCase()) {
            if (low[i] != rev[i]) {
                res = false
            }
        }
        i++
    }
    // while loop not needed, sol was to just to return low === rev
    return res


    // // solution 1: 2 pointer
    // l = 0
    // r = s.length-1
    // lowS = s.toLowerCase();
    // console.log(lowS)
    // res = true

    // while (l < r) {
    //     console.log(lowS[l], lowS[r])
    //     if (lowS[l].toUpperCase()!=lowS[l].toLowerCase() && lowS[r].toUpperCase()!=lowS[r].toLowerCase()) {
    //         console.log('both letters')
    //         if (lowS[l] != lowS[r]) {
    //             res = false
    //             break
    //         }
    //     }
    //     l++
    //     r--
    // }
    // return res
}



console.log(isPali('racecar'))  //true
console.log(isPali('rAcEcAr'))  //true
console.log(isPali('2r4ac5e9c3ar')) //false
console.log(isPali('racecaR !'))    //false
// isPali()
// isPali()
