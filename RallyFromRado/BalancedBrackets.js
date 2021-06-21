
const bracketBalance1 = s => {
    // // sol 4: keep count
    // count = 0
    // for (let i=0; i<s.length; i++) {
    //     if (count < 0 && s[i] === '[') {
    //         return false;
    //     } else if (count <= 0 && s[i] === ']') {
    //         return false;
    //     } else if (s[i] === '[') {
    //         count += 1;
    //     } else if (s[i] === ']') {
    //         count -= 1;
    //     }

    //     // if (s[i] === '[') {
    //     //     count += 1
    //     // } else {
    //     //     count -= 1
    //     // }
    //     // if (count < 0 && s[i] === '[') {
    //     //     return false
    //     // } 
    //     // else if (count > 0 && s[i] === ']') {
    //     //     return false
    //     // }
    // }
    // return count===0;
    // runtime: O(n), n being s.length

    // sol 3: recursive
    // is this one just calling recursion instead of using a loop?

    // sol 2: removing bracket pairs
    // let ogLen;
    // // YOOO? i initiated ogLen as s.length. why did that create a problem?
    // while (s.length !== ogLen) {
    //     ogLen = s.length;
    //     // using .replace() makes sense, but i want to know how to solve it without knowing that special func
    //     // i have trouble figuring my  way around needing to delete elems of str or arr as you go thru it
    //     // ^^ we should go over this ^^ 
    //     s = s.replace('[]', '');
    // }
    // return s.length === 0;


    // // sol 1: stack (+count i guess?)
    // // split = s.split("")
    // stack = []
    // // add [ to stack when found. if find ] in s, pop out last item, (bleh)
    // // only adding ['s to stack? if find ] then pop out last item. if last item == ] then u good
    // // but wont the last item always be [ bc you only add [ to stack?
    // // maybe it'll be ok bc eventually the stack will overpopulated in end if false? OHHHHH NEVERMIND IT MAKES SENSE
    // count = 0
    // for (let i=0; i<s.length; i++) {
    //     if (s[i] === '[') {
    //         count += 1
    //         stack.push(s[i])
    //     } else if (s[i] === ']') {
    //         count -= 1
    //         last = stack.pop()
    //         if (last === ']') {
    //             console.log('this part makes sense now')
    //             return false
    //         }
    //     }
    // }
    // // if (stack.length === 0) {
    // //     unpopulated = true;
    // // } else {
    // //     unpopulated = false;
    // // }
    // // return unpopulated && count===0;
    // return stack.length===0 && count===0;

}

console.log(bracketBalance1('['))      // f
console.log(bracketBalance1(']'))      // f
console.log(bracketBalance1('[]'))     // t
console.log(bracketBalance1(']['))     // f
console.log(bracketBalance1('[[]'))    // f
console.log(bracketBalance1('[]]'))    // f
console.log(bracketBalance1('][]['))   // f
console.log(bracketBalance1('[[][[]]'))// f
console.log(bracketBalance1('[[[]]]')) // t
console.log(bracketBalance1('[][][]')) // t
// console.log(bracketBalance1(''))
// console.log(bracketBalance1(''))

