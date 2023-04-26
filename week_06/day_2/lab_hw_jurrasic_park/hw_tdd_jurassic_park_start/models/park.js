const Park = function(name, price) {
    this.name = name;
    this.price = price;
    this.dinosaurs = [];
};

Park.prototype.addDinosaurToPark = function(dinosaur){
    this.dinosaurs.push(dinosaur);
};

Park.prototype.removeDinosaurFromPark = function(dinosaur){
    const indexOfDinosaur = this.dinosaurs.indexOf(dinosaur);
    this.dinosaurs.splice(indexOfDinosaur, 1);
};

// Park.prototype.findMostPopularDinosaur = function(){
//     for(let dinosaur of this.dinosaurs){
    
//     };
// };

Park.prototype.findDinosaursBySpecies = function(species){
    let speciesList = []
    for(let dinosaur of this.dinosaurs){
        if(species = dinosaur.species){
            speciesList.push(dinosaur);
        }
    }
    return speciesList.length;
};

Park.prototype.calculateTotalVisitorsPerDay = function(){
    let totalVisitors = 0
    for(let dinosaur of this.dinosaurs){
        totalVisitors += dinosaur.guestsAttractedPerDay;
    };
    return totalVisitors;
};

Park.prototype.calculateVisitorsPerYear = function(){
    let dailyVisitors = 0;
    for(let dinosaur of this.dinosaurs){
        dailyVisitors += dinosaur.guestsAttractedPerDay;
    };
    yearlyVisitors = dailyVisitors * 365;
    return yearlyVisitors;
};

Park.prototype.calculateYearlyRevenue = function(price){
    let dailyVisitors = 0;
    for(let dinosaur of this.dinosaurs){
        dailyVisitors += dinosaur.guestsAttractedPerDay;
    };
    yearlyRevenue = dailyVisitors * 365 * price;
}

module.exports = Park;
