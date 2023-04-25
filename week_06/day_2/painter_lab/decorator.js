const Decorator = function(){
    this.paintStock = [];
};

Decorator.prototype.addPaintCan = function(paintCan){
    this.paintStock.push(paintCan);
};

Decorator.prototype.sumOfPaintVolume = function(){
    let sum = 0
    for(let paintCan of this.paintStock) {
        sum += paintCan.volume;
    };
    return sum;
};

Decorator.prototype.hasEnoughPaint = function(room){
    if ( this.sumOfPaintVolume() >= room.area){
        return true;
    }else { 
        return false;
    };
};

module.exports = Decorator;