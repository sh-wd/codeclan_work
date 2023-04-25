var planets = ["Mercury", "Venus", "Earth"];

var numberOfElements = planets.length;
console.log("No of Elements: ", numberOfElements);

var firstPlanet = planets[0];
console.log(firstPlanet);

var secondPlanet = planets[1];
console.log(secondPlanet);

planets.push('Mars');
console.log(planets);

planets.push("Jupiter", "Saturn", "Uranus", "Neptune", "Pluto");
console.log("Planets: ", planets);

var removedPlanet = planets.pop();
console.log("Removed Planet: ", removedPlanet);
console.log("Planets: ", planets);

var removedPlanet = planets.shift();
console.log("Removed Planet: ", removedPlanet);
console.log("Planets: ", planets)

planets.unshift("Mercury");
console.log("Planets: ", planets);

var removedPlanet = planets.splice(2, 1, "Earth 2.0");
console.log(removedPlanet);
console.log(planets);

for (var currentPlanet of planets) {
    var uppercasePlanet = currentPlanet.toUpperCase();
    console.log(uppercasePlanet);
}

for (var i = 0; i < planets.length; i++) { // i += 1, i = 1 + 1
    var currentPlanet = planets[i];
    var lowercasedPlanet = currentPlanet.toLowerCase();
    console.log(lowercasedPlanet);
}

var movie = {
    title: "It's a Wonderful Life",
    year: 1946,
    language: "Spanish"
};
console.log("Movie: ", movie);

var title = movie.title;
console.log("Title: ", title);

movie.cast = ["James Stewart", "Donna Reid"];
console.log("Movie: ", movie);

movie.language = "English";
console.log("Movie: ", movie);

movie["language"] = "French";
console.log("Movie: ", movie)

movie["subtitle-language"] = "German";
console.log("Movie: ", movie);

var propertyToAccess = "subtitle-language";
movie[propertyToAccess] = "German";
console.log("Subtitle Language: ", movie[propertyToAccess]);

delete movie.year;
console.log(movie);

movie.ratings = {
    critic: 94,
    audience: 95
};
console.log(movie);

var audienceRating = movie.ratings.audience;
console.log(audienceRating);

for (var key in movie) {
    var value = movie[key];
    console.log(`the ${key} is ${value}`);
}

var keys = Object.keys(movie);
console.log(keys);