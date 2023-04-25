const assert = require("assert");
const PaintCan = require("../paint_can.js");

describe("PaintCan", function(){
    beforeEach(function(){
        paintCan = new PaintCan(5)
    });
    it("should have a volume", function(){
        const actual = paintCan.volume;
        assert.strictEqual(actual, 5);
    });
    it("check if can is empty", function(){
        paintCan.emptyPaintCan();
        const actual = paintCan.volume;
        assert.strictEqual(actual, 0);
    });
});