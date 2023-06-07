package main.Clothing;

import main.Product;

public abstract class Clothing extends Product {

    private int size;
    private String material;
    private boolean tryable;

    public Clothing(double buyPrice, double sellPrice, String manufacturer, long id, String productName, int size, String material, boolean tryable) {
        super(buyPrice, sellPrice, manufacturer, id, productName);

        this.size = size;
        this.material = material;
        this.tryable = tryable;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public boolean isTryable() {
        return tryable;
    }

    public void setTryable(boolean tryable) {
        this.tryable = tryable;
    }
}
