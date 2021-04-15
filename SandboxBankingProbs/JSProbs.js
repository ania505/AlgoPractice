// Problems #1 & #2 from Sandbox Banking JS Code Challenge

// func takes in str, returns str
// each odd positioned char is capitalized
// each even positioned char is lowered

const longSol = (str) => {
    sol = "";
    for (let i=0; i<str.length; i++) {
        // if (typeof str[i] === "string") {
        //     console.log(str[i])
        // }
        if (i%2 === 0) {
            // even index >>> odd position >>> to upper
            sol += str[i].toUpperCase();
        } else {
            sol += str[i].toLowerCase();
        }
    }
    return sol
}

// console.log(longSol("spongebob"));
// console.log(longSol("12tHrEeEeEeEe"));
// console.log(longSol("678 oRangE 123"));


const shortSol = (str) => {
    // remember: split/join, ternary
    return str.split().map((x,i) => i%2===0 ? x.toUpperCase() : x.toLowerCase()).join()
}

console.log(shortSol("spongebob"));
console.log(shortSol("12tHrEeEeEeEe"));
console.log(shortSol("678 oRangE 123"));

// MESSING UP ON THE SHORT SOLUTION >>>> RESULTS ARE IN ALL CAPS