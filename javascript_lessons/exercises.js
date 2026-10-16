// exercise
/*
const colors = ["Red", "Blue", "Green", "Yellow", "Black"]
console.log(colors[0])

// Exercise on Arrays methods
const queue = [];

queue.push("Customer A");
queue.push("Customer B");
queue.push("Customer C");

queue.shift();

queue.push("Customer D");

console.log(queue);

// exercise on Array
let foods = ["Rice", "Beans", "Yam", "Plantain"];
console.log(foods[0]);
console.log(foods[3]);

foods[1] = "Spaghetti";
console.log(foods)


let patients = ["Alex", "John", "Mary"];
patients.push("David");
patients.shift("Alex");
patients.unshift("Sarah")
console.log(patients)

 
// Exercise on Higher_order methods: Map
let salaries = [50000, 80000, 100000];

let newSalaries = salaries.map((salary) => {
    return salary + (salary * 10 / 100);
});
console.log(newSalaries)


//questions: Suppose a company wants to increase every employee's salary by 20%.

let salaries = [20000, 40000, 60000];
let newSalaries = salaries.map((salary) => {
    return salary + (salary * 20/100);
});
console.log(newSalaries)

// exercise map to update object properties
let products = [
    {name: "Laptop", price: 200000},
    {name: "Phone", price:  100000}
];
let updatedProducts = products.map((product) => {
    return {
        name: product.name,
        price: product.price + (product.price * 10/100)
    };
});
console.log(updatedProducts);
*/

//Using the .each()
let students = ["John", "Mary", "Alex"];

students.forEach((student) => {
    console.log("Welcome " + student);
})

let products = ["Laptop", "Phone", "Tablet"];
products.forEach((product) => {
    console.log("Available: " + product)
})