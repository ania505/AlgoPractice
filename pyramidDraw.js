const pyramidDraw = (size) => {
    // [x, 0, 0, 0]
    // [x, x, 0, 0]
    // [x, x, x, 0]
    // [x, x, x, x]
    res = []
    
    i = 0
    while (i < size) {
        tempArr = []
        j=0
        while (j < size-i) {
            tempArr.push('x') 
            j += 1
            
        }
        res.push(tempArr)
        i += 1
    }
    console.log(res)

}

pyramidDraw(4)