package main.Electrical;

import main.ISell;

public class Fridge extends Electrical implements ISell {

    private int minTemp;
    private boolean freezer;


    public Fridge(double buyPrice, double sellPrice, String manufacturer, long id, String productName, int powerConsumption, int warranty, int minTemp, boolean freezer) {
        super(buyPrice, sellPrice, manufacturer, id, productName, powerConsumption, warranty);

        this.minTemp = minTemp;
        this.freezer = freezer;
    }

    public int getMinTemp() {
        return minTemp;
    }

    public void setMinTemp(int minTemp) {
        this.minTemp = minTemp;
    }

    public boolean isFreezer() {
        return freezer;
    }

    public void setFreezer(boolean freezer) {
        this.freezer = freezer;
    }

    public String turnOn(){
        return "Getting chilly";
    }

    public String sellItem(int bankCard){
        return "Transaction complete";
    }
}
