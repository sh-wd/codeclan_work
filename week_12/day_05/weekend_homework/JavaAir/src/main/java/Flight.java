
import Crew.CabinCrewMember;
import Crew.Pilot;

import java.util.ArrayList;

public class Flight {

    private Plane plane;
    private ArrayList<Pilot> pilots;
    private ArrayList<CabinCrewMember> crewMembers;
    private ArrayList<Passenger> passengers;
    private String flightNo;
    private Airport destinationAirport;
    private Airport departureAirport;
    private String depTime;

    public Flight(Plane plane,
                  String flightNo,
                  Airport destinationAirport,
                  Airport departureAirport,
                  String depTime) {
        this.plane = plane;
        this.pilots = new ArrayList<Pilot>();
        this.crewMembers = new ArrayList<CabinCrewMember>();
        this.passengers = new ArrayList<Passenger>();
        this.flightNo = flightNo;
        this.destinationAirport = destinationAirport;
        this.departureAirport = departureAirport;
        this.depTime = depTime;
    }

    public Plane getPlane() {
        return plane;
    }

    public void setPlane(Plane plane) {
        this.plane = plane;
    }

    public ArrayList<Pilot> getPilots() {
        return pilots;
    }

    public void setPilots(ArrayList<Pilot> pilots) {
        this.pilots = pilots;
    }

    public ArrayList<CabinCrewMember> getCrewMembers() {
        return crewMembers;
    }

    public void setCrewMembers(ArrayList<CabinCrewMember> crewMembers) {
        this.crewMembers = crewMembers;
    }

    public ArrayList<Passenger> getPassengers() {
        return passengers;
    }

    public void setPassengers(ArrayList<Passenger> passengers) {
        this.passengers = passengers;
    }

    public String getFlightNo() {
        return flightNo;
    }

    public void setFlightNo(String flightNo) {
        this.flightNo = flightNo;
    }

    public Airport getDestinationAirport() {
        return destinationAirport;
    }

    public void setDestinationAirport(Airport destinationAirport) {
        this.destinationAirport = destinationAirport;
    }

    public Airport getDepartureAirport() {
        return departureAirport;
    }

    public void setDepartureAirport(Airport departureAirport) {
        this.departureAirport = departureAirport;
    }

    public String getDepTime() {
        return depTime;
    }

    public void setDepTime(String depTime) {
        this.depTime = depTime;
    }


    public int getEmptySeats() {
        return plane.getCapacity() - passengers.size();
    }

    public void addPassengerToFlight(Passenger passenger) {
        if(getEmptySeats() > 0) {
            this.passengers.add(passenger);
        }
    }

    public void addPilotToFlight(Pilot pilot) {
        this.pilots.add(pilot);
    }

    public void addCabinCrewToFlight(CabinCrewMember cabinCrewMember) {
        this.crewMembers.add(cabinCrewMember);
    }
}
