public enum Plane {

    BAGPIPE_500(6, 1200),
    HAGGIS_EXPRESS(10, 1900),
    TARTAN_JET(12, 2500);

    private final int capacity;
    private final int totalWeight;

    Plane(int capacity, int totalWeight) {
        this.capacity = capacity;
        this.totalWeight = totalWeight;
    }

    public int getCapacity() {
        return capacity;
    }

    public int getTotalWeight() {
        return totalWeight;
    }
}
