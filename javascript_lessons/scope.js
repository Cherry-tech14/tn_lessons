// Global Scope
/*
let username = "John";
function showUser() {
    console.log(username)
}
showUser();


// function scope
function greet() {
    let message = "Hello";
    console.log(message)
}
greet();

// function scope with var:
function test() {
    var x = 10;
    if (true) {
        var y = 20;
    }
    console.log(x);
    console.log(y);
}
test();


// function scope with let:
function test() {
    let x = 10;
    if (true) {
        let y = 20;
    }
    console.log(x);
    console.log(y);
}
test();

// Block scope
if (true) {
    let blockVar = "inside block";
    console.log(blockVar);
}

// block scope with let and const:
for (let i = 0; i < 3; i++) {
    console.log(i);
}
*/

// Complete example
// Global scope
let globalVar = "I am global";

function demonstrateScope() {
    // Function scope
    let functionVar = "I am function";

    console.log(globalVar);   
    console.log(functionVar); 

    if (true) {
        // Block scope
        let blockVar = "I am block";
        console.log(globalVar);   
        console.log(functionVar); 
        console.log(blockVar);    
    }

    // console.log(blockVar);   
}

demonstrateScope();
console.log(globalVar);      

