package Crew;

public class Pilot extends Crew {

    private String licenceNo;

    public Pilot(String name, Rank rank, String licenceNo) {
        super(name, rank);
        this.licenceNo = licenceNo;
    }

    public String flyPlane() {
        return "Cabin crew git ready fir take aff";
    }
}
