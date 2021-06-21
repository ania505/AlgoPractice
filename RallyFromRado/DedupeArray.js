/*
Write a function that takes an array of items and returns an array without any duplicate items in it.
For example, an input of
['Apples', 'Oranges', 'Oranges', 'Apples', 'Pears', 'Apples', 'Pears']
should return
['Apples', 'Oranges', 'Pears']
*/

const deDuper = (input) => {
    // sol 4: helper array
    helper = []
    for (let i=0; i < input.length; i++) {
        firstOccur = input.indexOf(input[i])
        if (firstOccur === i) {
            helper.push(input[firstOccur])
        }
    }
    return helper
    // runtime: O(n), n being array.length


    // // sol 3: map
    // let newItems = new Map()
    // for (let i=0; i < input.length; i++) {
    //     if (newItems.get(input[i]) != null) {
    //         newItems[input[i]] += 1
    //     } else {
    //         newItems[input[i]] = 1
    //     }
    // }
    // // console.log('map', newItems)
    // // MAPS CANT HAVE DUPLICATES YOU DUMMY
    // // return Array.from(newItems.keys())
    // // return [...newItems.keys()]
    // // HOW DO I MAKE THE KEYS RETURN AS AN ARRAY
    // return Object.keys(newItems)
    // runtime: O(n), n being array.length


    // // sol 2: filter() (i thought of)
    // let filtery = input.filter((x, i) => input.indexOf(x) === i )
    // // idk what conditional to use
    // return filtery
    // // runtime: O(n), n being array.length

    // // sol 1: arr >>> set >>> arr (i thought of)
    // setty = new Set(input)
    // console.log(typeof setty, setty)
    // backToArray = [... setty]
    // return backToArray
    // runtime: O(n), n being array.length
}

// test cases
console.log(deDuper(['Apples', 'Oranges', 'Oranges', 'Apples', 'Pears', 'Apples', 'Pears']))
console.log(deDuper([2, 5, 78, 5, 52, 2, 5, 78, 99, 100, 2]))
console.log(deDuper(['%', '$', '#', '#', '{', '%', '*', '*']))
console.log(deDuper([true, true, false, true, false, true, false]))
console.log(deDuper([1, true, false, 5, 55, false, 55, 1]))
console.log(deDuper(['Apples', 'Oranges', 'Pears', 'undefined', null]))
