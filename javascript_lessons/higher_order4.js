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


let students = [
    {id: 101, name: "James"},
    {id: 102, name: "Sarah"},
    {id: 103, name: "David"}

];
let foundStudent = students.find((student) => {
    return student.id === 105;
});
if (foundStudent !== undefined) {
    console.log(foundStudent.name);
} else {
    console.log("Student not found")
}


// understanding .tosorted()
let prices = [5000, 1000, 3000, 2000];
let sortedPrices = prices.toSorted((a, b) => a - b);
console.log("Original:", prices);
console.log("Sorted:", sortedPrices)
*/

//practical exercise
let employees = [
    {name: "John", salary: 150000},
    {name: "Mary", salary: 250000},
    {name: "Alex", salary: 100000},
    {name: "Sarah", salary: 200000}
];

let sortedemployees = employees.toSorted((a, b) => {
    return a.salary - b.salary;
});
console.log(sortedemployees);


//Real world application:online shopping
let products = [
    { name: "Laptop", price: 250000},
    { name: "Phone", price: 150000},
    { name: "Tablet", price: 100000}
];
let cheapestFirst = products.toSorted((a, b) => {
    return a.price - b.price;
});
console.log(cheapestFirst);