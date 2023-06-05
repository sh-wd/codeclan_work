public class WaterBottle {
    private int volume;

    public WaterBottle(){
        this.volume = 100;
    }

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }

    public void remove10(){
        volume -= 10;
    }

    public void emptyVolume(){
        volume = 0;
    }

    public void fillVolume(){
        volume = 100;
    }
}
