const assert = require("assert");
const Room = require("../room.js");

describe("Room", function(){
    beforeEach(function(){
        room = new Room(20);
    });

    it("should have an area", function(){
        const actual = room.area;
        assert.strictEqual(actual, 20);
    });
    it("should start unpainted", function(){
        const actual = room.painted;
        assert.strictEqual(actual, false);
    });
    it("should start unpainted", function(){
        room.paintRoom();
        const actual = room.painted;
        assert.strictEqual(actual, true); 
    })
});