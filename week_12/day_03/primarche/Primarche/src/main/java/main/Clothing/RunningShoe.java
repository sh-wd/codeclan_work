package main.Clothing;

import main.ISell;

public class RunningShoe extends Clothing implements ISell {

    private boolean lightUp;

    public RunningShoe(double buyPrice,
                       double sellPrice,
                       String manufacturer,
                       long id,
                       String productName,
                       int size,
                       String material,
                       boolean tryable,
                       boolean lightUp) {
        super(buyPrice, sellPrice, manufacturer, id, productName, size, material, tryable);

        this.lightUp = lightUp;
    }

    public boolean isLightUp() {
        return lightUp;
    }

    public void setLightUp(boolean lightUp) {
        this.lightUp = lightUp;
    }

    public String sellItem(int bankCard){
        return "Shoe purchase successful";
    }
}
