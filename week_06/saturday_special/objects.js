const person = {
    name : {
        first : "Brendan",
        last : "Eich"
    },
    age : 62
};

console.log(person.name.first);

person.age = 63;

// Add a new key/value
person.address = "7 Silicon Way";

console.log(person);

const movie = {
    title : "Robocop",
    yearOfRelease : 1987,
    director : "Paul Verhoeven",
    cast : ["Paul Weller", "Nancy Allen", "Dan Herlihy"]
};

console.log(movie.yearOfRelease);

for( castMember of movie.cast) {
    console.log(castMember);
};

movie.ratings = {
    critics : 98,
    audience : 99
};

console.log(movie.ratings.critics);