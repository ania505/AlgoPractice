//  time planner problem from pramp mock tech interview

const meetingPlanner = (slotsA, slotsB, dur) => {
    // output = [start, start+dur]
    let ia = 0;
    let ib = 0;
    let start;
    let end;

    while (ia<slotsA.length && ib<slotsB.length) {
        start = Math.max(slotsA[ia][0], slotsB[ib][0])
        // compares 1st value of the pair in both, choosing larger one
        end = Math.min(slotsA[ia][1], slotsB[ib][1])
        // compares 2nd value of the pair in both, choosing smaller one
        
        if (start + dur <= end) {
            return [start, start+dur]
        }
        ia++;
        ib++;
    }
    return []
}




console.log(meetingPlanner(
    [[10, 50], [60, 120], [140, 210]], 
    [[0, 15], [60, 70]],
    8
))  // expected output: [60, 68]
console.log(meetingPlanner(
    [[10, 50], [60, 120], [140, 210]],
    [[0, 15], [60, 70]],
    12
))  // expected output: []