// .find() example
/*
let scores = [45, 60, 80, 90, 80];
let result = scores.find((score) => {
    return score === 80;
});
console.log(result);

let balances = [5000, 12000, 8000, 25000, 15000];
let firstBalance = balances.find((balance) => {
    return balance > 10000;
});
console.log(firstBalance)


//finding objects by unique id
let customers = [
    { id: 101, name: "John", balance: 5000},
    {id: 102, name: "Mary", balance: 12000},
    { id: 103, name: "Alex", balance: 8000}

];
let customer = customers.find((person) => {
    return person.id === 101;
});
console.log(customer);


let products = [
    { id: 201, name: "Laptop", price: 250000},
    {id: 202, name: "Phone", price: 150000},
    {id: 203, name: "Tablet", price: 100000}
];
let foundProduct = products.find((product) => {
    return product.id === 202;
});
console.log(foundProduct)


//Handling undefined safely example
let numbers = [10, 20, 30];
let result = numbers.find((number) => {
    return number === 50;
});
console.log(result);

// imagine we are trying to access a property
let customers = [
    { id: 1, name: "John" },
    { id: 2, name: "Mary" }
];

let customer = customers.find((person) => {
    return person.id === 5;
});

console.log(customer.name);
*/

// how do we prevent the error
let customers = [
    {id: 1, name: "John"},
    {id: 2, name: "Mary"}
];

let customer = customers.find((person) => {
    return person.id === 5;
});
if (customer !== undefined) {
    console.log(customer.name);
} else {
    console.log("Customer not found")
}

