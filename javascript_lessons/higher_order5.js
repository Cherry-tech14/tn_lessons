// .some() syntax and short curcuiting example
/*
let scores = [45, 60, 75, 90, 55];
let hasHighScore = scores.some((score) => {
    return score > 80;
});
console.log(hasHighScore);

let ages = [12, 15, 16, 17];

let hasAdult = ages.some((age) => {
    return age >= 18;
});
console.log(hasAdult);

//Real world example
let balances = [20000, 50000, 150000, 30000];
let hasLargeBalance = balances.some((balance) => {
    return balance > 100000;
});
console.log(hasLargeBalance);

// exercise
let quantities = [15, 8, 20, 3, 12];
let hasLowStock = quantities.some((quantity) => {
    return quantity < 5;
});
console.log(hasLowStock);

// practical example
let formFields = ["John", "", "password123"];
let hasEmptyField = formFields.some((field) => {
    return field === "";
});
console.log(hasEmptyField);

// Using .some() with if and else
let formFields = ["John", "", "password123"];
let hasEmptyField = formFields.some((field) => {
    return field === "";
});

if (hasEmptyField) {
    console.log("Please fill in all required fields");
} else {
    console.log("Registration successful!");
}

*/
let registrationForm = {
    username: "Alex",
    email: "   ",
    password: "mypassword123"
};

let fields = [
    registrationForm.username,
    registrationForm.email,
    registrationForm.password
];

let hasEmptyField = fields.some((field) => {
    return field.trim() === "";
});

if (hasEmptyField) {
    console.log("Registration failed: All fields are required.");
} else {
    console.log("Registration successful!");
}