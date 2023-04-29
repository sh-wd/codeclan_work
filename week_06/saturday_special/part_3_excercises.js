// Create a file called part_3_exercises.js and paste in this code:

/* ------------------------------------------------------------- 
EXERCISE 1
You've been provided with an object called myGuitar. Use a for loop to log out all the previous owners.
-------------------------------------------------------------- */
const myGuitar = {
    make: 'Gretsch',
    model: '6120W',
    year: 1962,
    previousOwners: ['Chuck Berry', 'Keith Richards', 'Angus Young']
}

// Write your code here...

    for(let owner of myGuitar.previousOwners) {
        console.log(owner);
    };
    

/* -------------------------------------------------------------
EXERCISE 2
Create an object that represents your favourite band. Include any key/value pairs that you think are appropriate but the band members should be an array of objects.
-------------------------------------------------------------- */

// Write your code here...

const favouriteBand = {
    name: "Spice Girls",
    noOfMembers : 5,
    members : ["Scary", "Sporty", "Baby", "Ginger", "Posh"],
    getDetails : function(){
        console.log(favouriteBand.members);
    }
};
favouriteBand.getDetails()


/* -------------------------------------------------------------
EXERCISE 3
Add a function to your favourite band object called getDetails that returns some details of the band
-------------------------------------------------------------- */

// Write your code here...

