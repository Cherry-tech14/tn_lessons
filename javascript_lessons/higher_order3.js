// .reduce syntax
/*
let prices = [1000, 2000, 3000];
let total = prices.reduce((accumulator, price) => {
    return accumulator + price;
}, 0);
console.log(total);

let deposits = [20000, 15000, 30000, 10000];

let totalDeposits = deposits.reduce((accumulator, deposit) => {
    return accumulator + deposit;
}, 0);
console.log(totalDeposits)


// Tallying complex objects
let cart = [
    { name: "Bread", price: 1000, quantity: 2},
    { name: "Milk", price: 2000, quantity: 3},
    { name: "Rice", price: 5000, quantity: 1}
];

let totalCost = cart.reduce((accumulator, product) => {
    return accumulator + (product.price * product.quantitiy);
}, 0);
console.log(totalCost);

let products = [
    { name: "Sugar", price: 3000, quantity: 2},
    { name: "Oil", price: 5000, quantity: 1},
    { name: "Eggs", price: 2000, quantity: 3}
];
let totalPrice = products.reduce((accumulator, things) => {
    return accumulator + (things.price * things.quantity);
}, 0);
console.log(totalPrice)
*/

// categorical grouping 
let products = [
    { name: "Rice", category: "Food"},
    { name: "Soap", category: "Cleaning"},
    { name: "Bread", category: "Food"},
    { name: "Detergent", category: "Cleaning"}
];
let groupedProducts = products.reduce((accumulator, product) => {
    let category = product.category;

    if (!accumulator[category]) {
        accumulator[category] = [];

    }
    accumulator[category].push(product.name);
    return accumulator;
}, {});
console.log(groupedProducts);
