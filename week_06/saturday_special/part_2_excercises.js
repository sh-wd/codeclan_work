// Create a file called part_2_exercises.js and paste in this code:

/* -------------------------------------------------------------
EXERCISE 1
Let's start off with some basic array practice. In this exercise we'd like you to create an array of three items, 
stored inside a variable called myArray. The items can be anything you want — how about your favourite bands or movies?
Next, modify the first two items in the array using simple bracket notation and assignment. 
Then add a new item to the beginning of the array. 
Finally, 'pop off' the last item in the array and log it out.
-------------------------------------------------------------- */

// Write your code here...
const myArray = ["The Lord of the Rings: The Fellowship of the Ring", "The Lord of the Rings: The Two Towers", "The Lord of the Rings: The Return of the King"]

myArray[0] = "The Hobbit: The Desolation of Smauag";
myArray[1] = "The Hobbit: The Battle of the Five Armies";
console.log(myArray)
myArray.shift()
console.log(myArray);
/* -------------------------------------------------------------
EXERCISE 2
Now let's practice removing items from an array. 
Using the indexOf() and splice() methods, remove 'Visual Basic' from the programmingLanguages array. 
-------------------------------------------------------------- */
const programmingLanguages = ['JavaScript', 'Python', 'Java', 'C', 'Visual Basic', 'Go'];
// Write your code here...


/* -------------------------------------------------------------
EXERCISE 3
Given an array of numbers and an empty array called doubles, use a for loop to iterate through the array, 
multiply each number by 2 and push the result onto the doubles array.
Finally, log out the doubles array.
-------------------------------------------------------------- */
const numbers = [2, 4, 5, 7];
const doubles = [];
​
// Write your code here...