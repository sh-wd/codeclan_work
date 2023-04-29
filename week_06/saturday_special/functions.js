function square(number) {
    return number * number;
};

console.log(square(5));
console.log(square(3));

function getUserDetails(firstName, lastName, email) {
    const userDetails = `Name: ${firstName} ${lastName}, Email: ${email}`
    return userDetails;
};

console.log(getUserDetails("Peter", "Pan", "peterp@howsmyflying.com"));

function multiply(num1, num2) {
    return num1 * num2;
};

console.log(multiply(2, 2));

function sumArray(arr) {
    let total = 0;
    for (let number of arr) {
        total += number;
    };
    return total;
};

console.log(sumArray([10, 20, 30, 40, 50]));

function containsValue (num, arr) {
    for(let number of arr) {
        if ( number === num ) {
            return true;
        };
    };
    return false;
};

console.log(containsValue(3, [1, 2, 3]));
console.log(containsValue(5, [1, 2, 3]));