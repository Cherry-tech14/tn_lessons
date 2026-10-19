// The filter predicate
/*
let prices = [2000, 5000, 8000, 12000];
let expensivePrices = prices.filter((price) => {
    return price > 5000;
});
console.log(expensivePrices)

// example 2
let jobs = [
    { title: "Frontend Developer", salary: 150000},
    { title: "Backend Developer", salary: 250000},
    { title: "UI Designer", salary: 120000}
];
let highPayingJobs = jobs.filter((job) => {
    return jobs.salary >= 150000;

});
console.log(highPayingJobs);

let students = [
    { name: "John", score: 45},
    { name: "Mary", score: 75},
    { name: "Alex", score: 60},
    { name: "Sarah", score: 30}
];
let passedStudents = students.filter((student) => {
    return student.score >= 50;
});
console.log(passesStudents);

// sorting

let students = ["Mary", "Alex", "John", "Sarah"];
students.sort();
console.log(students);

// The alphabetical Quirk: Sorting numbers
let numbers = [5, 100, 20, 3, 50];
numbers.sort();
console.log(numbers);


// sorting numbers correctly: ascending order
let numbers = [5, 100, 20, 3, 50];
numbers.sort((a, b) => {
    return a - b;
});
console.log(numbers);

//sorting numbers correctly: descending order
let numbers = [5, 100, 20, 3, 50]

numbers.sort((a, b) => {
    return b - a;
});
console.log(numbers);

// .sort() mutates the original array
let numbers = [30, 10, 20];
let sortedNumbers = [...numbers].sort((a, b) => {
    return a - b;
});
console.log("Original:", numbers);
console.log("Sorted:", sortedNumbers);

// real world application
let balances = [50000, 20000, 80000, 10000];
let sortedBalances = [...balances].sort((a, b) => {
    return b - a;
});
console.log("Original Balances:", balances);
console.log("Sorted Balances:", sortedBalances);
*/

// Building a chained pipeline

let salaries = [30000, 70000, 50000, 90000, 40000];
let updatedSalaries = salaries
    .filter((salary) => {
        return salary >= 50000;
    })
    .map((salary) => {
        return salary + 10000;
    })
    .sort((a, b) => {
        return a - b;
    });
console.log(updatedSalaries);
