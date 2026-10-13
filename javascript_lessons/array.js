// Creating an array
/*
const fruits = ["Apple", "Banana", "Orange"];
console.log(fruits[0]);

let fruits = ["Apple", "Banana", "Cashew"];
console.log(fruits[1]);



// push method
const fruits = ["Apple", "Banana"];
fruits.push("Orange");
console.log(fruits);

// pop() method
const fruit = ["Apple", "Banana", "Orange"];
fruit.pop("Orange");
console.log(fruit);

// element that was removed 
const removedFruit = fruits.pop();

console.log(removedFruit);


// unshift() method: Adds an item to the beginning
const fruits = ["Banana", "Orange"];
fruits.unshift("Apple");
console.log(fruits);

// shift(): Remove the first item
const fruit = ["Apple", "Banana", "Orange"];
fruit.shift();
console.log(fruit);

// Accessing an array values
let products = ["Laptop", "Phone", "Headphones"];

console.log(products[0]);
console.log(products[1]);
console.log(products[2]);


// Changing an array value
let product = ["Laptop", "Phone", "Headphones"];
product[1] = "Tablet";
console.log(product);

//Real World application: Customer service queue

let customers = ["John", "Sarah", "David"];
customers.push("Emma");

customers.shift();
console.log(customers);


// Reference Trap
let shoppingList = ["Rice", "Beans", "Yam"];
let newList = shoppingList;
newList.push("Bread");

console.log(shoppingList);
console.log(newList);


// shallow clone
let shoppingList = ["Rice", "Beans", "Yam"];
let newList = [...shoppingList];

newList.push("Bread");

console.log(shoppingList);
console.log(newList);


// Deep cloning
let students = [
    { name: "John", score: 80},
    { name: "Mary", score: 90}
];
let newStudents = structuredClone(students);

newStudents[0].score = 100;

console.log(students[0].score);
console.log(newStudents[0].score);
*/
// Real world Application
let transactions = [
    {type: "Deposit", amount: 5000},
    {type: "Withdrawal", amount: 2000}
];

let backup = structuredClone(transactions);

transactions[0].amount = 10000;

console.log(transactions[0].amount);
console.log(backup[0].amount);