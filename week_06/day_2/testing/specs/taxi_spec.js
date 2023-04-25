const assert = require("assert");
const Taxi = require("../taxi.js");

describe("Taxi", function(){

    beforeEach(function(){
        //Arrange
        taxi = new Taxi("Opel", "Manta", "Jane")
    })
    it("should have a manufacturer", function(){
        //Act
        const actual = taxi.manufacturer;
        //Assert
        assert.strictEqual(actual, "Opel");
    });
    it("should have a model", function(){
        const actual = taxi.model;
        assert.strictEqual(actual, "Manta");
    });
    it("should have a driver", function(){
        assert.strictEqual(taxi.driver, "Jane")
    });
    it("should start with no passengers", function(){
        const actual = taxi.passengers;
        assert.deepStrictEqual(actual, []);
    });
    it("should know how many passengers are aboard", function(){
        taxi.addPassenger("Fred");
        actual = taxi.numberOfPassengers();
        assert.strictEqual(actual, 1);
    });
    it("should remove a passenger by name", function(){
        taxi.addPassenger("Fred");
        taxi.addPassenger("Velma");
        taxi.removePassengerByName("Fred");
        assert.strictEqual(taxi.numberOfPassengers(), 1);
    });
    it("should remove all passengers", function(){
        taxi.addPassenger("Fred");
        taxi.addPassenger("Velma");
        taxi.removeAllPassengers();
        assert.strictEqual(taxi.numberOfPassengers(), 0);
    });
});
