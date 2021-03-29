
const indexOf = (s1, s2) => {
    if (s1.length > s2.length) {
        return -1
    }
    let found = -1;
    for (let i=0; i < s2.length; i++) {
        if (s2[i] === s1[0]) {
            found = i;
            for (let j=0; j<s1.length; j++) {
                // console.log(s1[j], s2[i+j])
                // console.log(found)
                if (s1[j] !== s2[i+j]) {
                    found = -1;
                    break;
                }
                if (j === s1.length-1) {
                    return found;
                }
            }
        }
    }
    return found;
}

console.log(indexOf('or', 'hello world'))
console.log(indexOf('hello world', 'or'))
console.log(indexOf('howdy', 'hello world'))
console.log(indexOf('oox', 'ooboxoooxo'))