public class Passenger {

    private String name;
    private int NoOfBags;

    public Passenger(String name, int noOfBags) {
        this.name = name;
        NoOfBags = noOfBags;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getNoOfBags() {
        return NoOfBags;
    }

    public void setNoOfBags(int noOfBags) {
        NoOfBags = noOfBags;
    }
}
