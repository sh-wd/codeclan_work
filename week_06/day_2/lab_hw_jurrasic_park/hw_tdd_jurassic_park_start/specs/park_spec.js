const assert = require('assert');
const Park = require('../models/park.js');
const Dinosaur = require('../models/dinosaur.js');

describe('Park', function() {

  let park;

  let dinosaur1 = new Dinosaur("T-Rex", "Carnivore", 50);
  let dinosaur2 = new Dinosaur("Pterodactyl", "Carnivore", 20);
  let dinosaur3 = new Dinosaur("Diplodocus", "Herbivore", 35);
  let dinosaur4 = new Dinosaur("T-Rex", "Carnivore", 30);


  beforeEach(function () {
    park = new Park("Jurassic", 150);
  }); 

  it('should have a name', function(){
    const actual = park.name;
    assert.strictEqual(actual, "Jurassic");
  });

  it('should have a ticket price', function(){
    const actual = park.price;
    assert.strictEqual(actual, 150);
  });

  it('should have a collection of dinosaurs', function(){
    const actual = park.dinosaurs;
    assert.deepStrictEqual(actual, []);
  });

  it('should be able to add a dinosaur to its collection', function(){
    park.addDinosaurToPark(dinosaur1);
    const actual = park.dinosaurs.length;
    assert.strictEqual(actual, 1);
  });

  it('should be able to remove a dinosaur from its collection', function(){
    park.removeDinosaurFromPark(dinosaur1);
    const actual = park.dinosaurs.length;
    assert.strictEqual(actual, 0);
  });

  // it('should be able to find the dinosaur that attracts the most visitors', function(){
  //   park.addDinosaurToPark(dinosaur1);
  //   park.addDinosaurToPark(dinosaur2);
  //   park.addDinosaurToPark(dinosaur3);
  //   const actual = park.findMostPopularDinosaur();
  //   assert.strictEqual(actual, "T-rex");
  // });

  it('should be able to find all dinosaurs of a particular species', function(){
    park.addDinosaurToPark(dinosaur1);
    park.addDinosaurToPark(dinosaur2);
    park.addDinosaurToPark(dinosaur3);
    park.addDinosaurToPark(dinosaur4);
    const actual = park.findDinosaursBySpecies("T-Rex");
    assert.strictEqual(actual, 2);
  });

  it('should be able to calculate the total number of visitors per day', function(){
    park.addDinosaurToPark(dinosaur1);
    park.addDinosaurToPark(dinosaur2);
    park.addDinosaurToPark(dinosaur3);
    park.addDinosaurToPark(dinosaur4);
    const actual = park.calculateTotalVisitorsPerDay();
    assert.strictEqual(actual, 135);
  });

  it('should be able to calculate the total number of visitors per year', function(){
    park.addDinosaurToPark(dinosaur1);
    park.addDinosaurToPark(dinosaur2);
    park.addDinosaurToPark(dinosaur3);
    park.addDinosaurToPark(dinosaur4);
    const actual = park.calculateVisitorsPerYear();
    assert.strictEqual(actual, 49275);
  });

  it('should be able to calculate total revenue for one year', function(){
    park.addDinosaurToPark(dinosaur1);
    park.addDinosaurToPark(dinosaur2);
    park.addDinosaurToPark(dinosaur3);
    park.addDinosaurToPark(dinosaur4);
    const actual = park.calculateYearlyRevenue(150);
    assert.strictEqual(actual, 7391250);
  });

});
