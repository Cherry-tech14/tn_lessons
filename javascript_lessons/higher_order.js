// Example of map
/*
let prices = [1000, 2000, 3000];
let newPrices = prices.map(function(price) {
    return price * 2;
});
console.log(newPrices);

// example using arrow functions
let prices = [1000, 2000, 3000];

let newPrices = prices.map((price) => {
    return price * 2;
});

console.log(newPrices);

// .forEach() example

let fruits = ["Apple", "Banana", "Orange"];

fruits.forEach((fruit) => {
    console.log(fruit);
})
*/
// .map() example
let fruits = ["Apple", "Banana", "Orange"];

let newFruits = fruits.map((fruit) => {
    return fruit + " Juice";
});

console.log(newFruits);