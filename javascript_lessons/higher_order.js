// Example of map
/*
let prices = [1000, 2000, 3000];
let newPrices = prices.map(function(price) {
    return price * 2;
});
console.log(newPrices);
*/
// example using arrow functions
let prices = [1000, 2000, 3000];

let newPrices = prices.map((price) => {
    return price * 2;
});

console.log(newPrices);