// Named Funtion
function sayHello(greeting, name = "Aqib"){
    return `${greeting} ${name}`
}

console.log("sayHello Message: ", sayHello("Hi", "Steve"));

//Anonymous Function
var add = function (firstNumber, secondNumber) {
    return firstNumber + secondNumber;
}
console.log("1 + 3 with add:", add(1,3));

// 1. Declare a **named** function that takes an array of numbers, and returns the sum, or total, of all of the numbers in the array.

function sumOfNumbers(numbers) {
    var sum = 0
    for ( i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }
    return sum
}
var numbers = [2, 5, 6]
console.log(`The sum of the numbers is`, sumOfNumbers(numbers));

// 2. Define an **anonymous** function expression that takes two arguments:
//   - an object, for example, `{ name: ‘Wojtek’, age: 30 }`
//   - a string, for exmaple, `‘name’`
//   Your function should return `true` if the given string is a `key` on the given object and `false` if the
//   object does not have a key that matches the string. Store this function in an appropriately named variable to invoke it.

var keyCheck = function (object, key) {
    if (object[key]) {
        return true
    } else {
        return false
    }
}

console.log(keyCheck({name: "Wojtek", age: 30}, "name"));

var keyCheck = function (object, searchString) {
    for (var key in object) {
        if (searchString === key) {
            return true
        }
    }
    return false
}
console.log(keyCheck({name: "Wojtek", age: 30}, "name"));


//Arrow Functions
var multiply = (noOne, noTwo) => {
    return noOne * noTwo
}
console.log(multiply(2,5));

var multiply = (noOne, noTwo) => noOne * noTwo
console.log(multiply(2,5));