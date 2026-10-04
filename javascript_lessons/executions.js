// Global context
/*
let product = "Laptop";

console.log(product);

let name = "John";
function greet() {
    console.log(name);
}
greet();

//Real world example
let storeName = "Tech Store";
let currency = "NGN";

function showStore() {
    console.log(storeName);
    console.log(currency);
}

showStore();

// local context
function login() {
    let username = "John";
    console.log(username);
}
login();


// global vs local: The interaction
let product = "Laptop";

function buyProduct() {
    let quantity = 2;

    console.log(product);
    console.log(quantity);
}

buyProduct();

// The call stack
function first() {
    console.log("First");
}

function second() {
    first();
    console.log("Second");
}
second();
*/

// Tracing variable values 
let score = 50;
function updateScore() {
    let score = 80;
    console.log(score);
}
console.log(score);
updateScore();