var minCost = function(costs) {
    let currentHouse, currentMin;
    
    let dpArrayOne = [Math.min(...costs[0])];
    let dpArrayTwo = [Math.min(...costs[0])];

    let idxMin = costs[0].indexOf(dpArray[0]); 
    
    for (let i = 1; i < costs.length; i++) {
        currentHouse = costs[i];
        currentMin = Number.MAX_VALUE;

        if (idxMin !== 0) dpArrayOne.length === dpArrayTwo.length ? dpArrayOne.push(dpArrayOne[i -1] + currentHouse[0]) : dpArrayTwo.push(dpArrayTwo[i -1] + currentHouse[0]);
        if (idxMin !== 1) dpArrayOne.length === dpArrayTwo.length ? dpArrayOne.push(dpArrayOne[i -1] + currentHouse[1]) : dpArrayTwo.push(dpArrayTwo[i -1] + currentHouse[1]);
        if (idxMin !== 2) dpArrayOne.length === dpArrayTwo.length ? dpArrayOne.push(dpArrayOne[i -1] + currentHouse[2]) : dpArrayTwo.push(dpArrayTwo[i -1] + currentHouse[2]);

        
    }
    
    return minimumCost;
};

console.log(minCost([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]))

5
13
5
17
3


