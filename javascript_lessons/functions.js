// function declaration
/*
function greet(name) {
    console.log("Hello, " + name)
}
greet("Alice");
greet("Bob");

// Multiple parameters

function addNumbers(a, b) {
    return a + b;
    
}
let result = addNumbers(5, 3);
console.log(result);


function doubleNumber(num) {
    return num * 2;
}
let number = doubleNumber(10)
console.log(number)

// function expression
const greet = function(name) {
    console.log("Hello, " + name)
};
greet("Alice");


// Arrow Function
const greet = (name) => {
    console.log("Hello, " + name);
};
greet("Alice");


// parameter and argument

function calculateTotal(price, quantity) {
    console.log(price * quantity);
}
calculateTotal(5000, 3)

// default parameters
function greet(name = "Guest") {
    console.log("Hello, " + name)
}
greet("Alice");
greet();


// rest parameters(...)
function sumAll(...numbers) {
    let total = 0;
    for (let num of numbers) {
        total = total + num;
    }
    return total;
}
console.log(sumAll(1,2,3));
console.log(sumAll(1,2,3,4,5));
*/

// callback functions
function processUser(name, callback) {
    console.log("Processing " + name + "...");
    callback(name);
}

function greetUser(name) {
    console.log("Hello, " + name + "!");
}

processUser("Alice", greetUser);
