package main.Electrical;

import main.Product;

public abstract class Electrical extends Product {

    private int powerConsumption;
    private int warranty;

    public Electrical(double buyPrice, double sellPrice, String manufacturer, long id, String productName, int powerConsumption, int warranty) {
        super(buyPrice, sellPrice, manufacturer, id, productName);
        this.powerConsumption = powerConsumption;
        this.warranty = warranty;
    }

    public int getPowerConsumption() {
        return powerConsumption;
    }

    public void setPowerConsumption(int powerConsumption) {
        this.powerConsumption = powerConsumption;
    }

    public int getWarranty() {
        return warranty;
    }

    public void setWarranty(int warranty) {
        this.warranty = warranty;
    }

    public String turnOn(){
        return "Turning on";
    }
}
