const assert = require("assert");
const Decorator = require("../decorator.js");
const Room = require("../room.js");
const PaintCan = require("../paint_can.js");

describe("Decorator", function(){
    this.beforeEach(function(){
        decorator = new Decorator();
    });
    it("should start with empty paint stock", function(){
        const actual = decorator.paintStock;
        assert.deepStrictEqual(actual, []);
    });
    it("should be able to add a can of paint", function(){
        decorator.addPaintCan(5);
        const actual = decorator.paintStock.length;
        assert.strictEqual(actual, 1);
    });
    it("should be able to check total volume of paint", function(){
        paintCan1 = new PaintCan(5);
        paintCan2 = new PaintCan(3);
        paintCan3 = new PaintCan(2);
        decorator.addPaintCan(paintCan1);
        decorator.addPaintCan(paintCan2);
        decorator.addPaintCan(paintCan3);
        const actual = decorator.sumOfPaintVolume();
        assert.strictEqual(actual, 10);
    });
    it("should be able to check if there's enough paint for a room", function(){
        paintCan1 = new PaintCan(5);
        paintCan2 = new PaintCan(3);
        paintCan3 = new PaintCan(2);
        room1= new Room(15);
        const actual = decorator.hasEnoughPaint(room1);
        assert.strictEqual(actual, false);
    });
});