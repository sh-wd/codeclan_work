const PaintCan = function(volume){
    this.volume = volume;
};

PaintCan.prototype.emptyPaintCan = function(){
    this.volume = 0;
};

module.exports = PaintCan;