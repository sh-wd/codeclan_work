// let isRaining = true;
// let message = "";

// if ( isRaining === true) {
//     message = "Take an umbrella";
// } else {
//     message = "No need for an umbrella"
// };

// console.log(message);

// const fruitType = "Apple";

// if (fruitType === "Apple") {
//     console.log("Apples are £2.50 per bushle");
// } else if (fruitType === "Orange") {
//     console.log("Oranges are £1.50 per kilo");
// } else {
//     console.log("Sorry we don't have any " + fruitType);
// };

// Falsy values
// - false
// - undefined
// - null
// - NaN
// - 0
// - ""

// let isLoggedIn = 0
// console.log("isLoggedIn", isLoggedIn);

// if(isLoggedIn){
//     console.log("Welcome Back");
// } else {
//     console.log("Please Log In");
// };

// let number = 15;

// if (number % 3 === 0 && number % 5 === 0) {
//     console.log("The number is divisable by 3 and 5");
// };

// if (number % 3 === 0 || number % 5 === 0) {
//     console.log("The number is divisable by 3 or 5");
// };

// const number = 10;

// if (number > 5) {
//     console.log("Number is greater than 5");
// };

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for( let number of numbers){
    if (number % 2 === 0) {
        console.log(number);
    };
};

const mark = 6;

if ( mark < 5) {
    console.log("Failed");
} else if ( mark >= 5 && mark <= 8) {
    console.log("You passed");
} else {
    console.log("Distinction!");
};
