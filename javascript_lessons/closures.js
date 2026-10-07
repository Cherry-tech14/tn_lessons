// Closure example
/*
function outer() {
    let message = "Hello";

    function inner() {
        console.log(message);
    }
    return inner;
}

const myFunction = outer();
myFunction();

// encapsulating private state
function createCounter() {
    let count = 0;
    return function() {
        count++;
        console.log(count);
    };
}
const counter = createCounter();

counter();
counter();
counter();
counter();

*/
// one-time use execution wrappers__ once()
function once(fn) {
    let hasRun = false;

    return function() {
        if (!hasRun) {
            fn();
            hasRun = true;
        }
    };
}
function sayHello() {
    console.log("Hello!");
}

const sayHelloOnce = once(sayHello);

sayHelloOnce();
sayHelloOnce();
sayHelloOnce();