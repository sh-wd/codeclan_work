const Taxi = function(manufacturer, model, driver){
    this.manufacturer = manufacturer;
    this.model = model;
    this.driver = driver;
    this.passengers = [];
}

Taxi.prototype.addPassenger = function(passenger){
    this.passengers.push(passenger);
};

Taxi.prototype.numberOfPassengers = function(){
    return this.passengers.length;
};

Taxi.prototype.removePassengerByName = function(name){
    const indexOfPassenger = this.passengers.indexOf(name);
    this.passengers.splice(indexOfPassenger, 1);
};

Taxi.prototype.removeAllPassengers = function(){
    this.passengers = [];
};

module.exports = Taxi;