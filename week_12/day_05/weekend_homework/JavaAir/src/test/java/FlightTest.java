import Crew.CabinCrewMember;
import Crew.Pilot;
import Crew.Rank;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class FlightTest {

    Flight flight;
    Passenger passenger1;
    Passenger passenger2;
    Passenger passenger3;
    Passenger passenger4;
    Pilot pilot1;
    Pilot pilot2;
    CabinCrewMember cabinCrewMember1;
    CabinCrewMember cabinCrewMember2;
    CabinCrewMember cabinCrewMember3;
    CabinCrewMember cabinCrewMember4;


    @Before
    public void before(){
        flight = new Flight(
                Plane.BAGPIPE_500,
                "JA842",
                Airport.OBN,
                Airport.DND,
                "12:50");

        passenger1 = new Passenger("Jimmy", 2);
        passenger2 = new Passenger("Morag", 1);
        passenger3 = new Passenger("Iona", 5);
        passenger4 = new Passenger("Maisy", 2);

        pilot1 = new Pilot("Agnus", Rank.CAPTAIN, "Br00n");
        pilot2 = new Pilot("Duncan", Rank.FIRST_OFFICER, "Wu11i3");

        cabinCrewMember1 = new CabinCrewMember("Jock", Rank.PURSER);
        cabinCrewMember2 = new CabinCrewMember("Oona", Rank.PURSER);
        cabinCrewMember3 = new CabinCrewMember("Cormac", Rank.PURSER);
        cabinCrewMember4 = new CabinCrewMember("Mairaed", Rank.PURSER);
    }

    @Test
    public void canAddPassengerToFlight() {
        flight.addPassengerToFlight(passenger1);
        assertEquals(1, flight.getPassengers().size());
    }

    @Test
    public void flightCannotBeOverBooked(){
        flight.addPassengerToFlight(passenger1);
        flight.addPassengerToFlight(passenger1);
        flight.addPassengerToFlight(passenger1);
        flight.addPassengerToFlight(passenger1);
        flight.addPassengerToFlight(passenger2);
        flight.addPassengerToFlight(passenger3);
        flight.addPassengerToFlight(passenger4);
        assertEquals(6, flight.getPassengers().size());
    }

    @Test
    public void checkForEmptySeats(){
        flight.addPassengerToFlight(passenger1);
        flight.addPassengerToFlight(passenger2);
        assertEquals(4, flight.getEmptySeats());
    }

    @Test
    public void canAddPilotToFlight(){
        flight.addPilotToFlight(pilot1);
        assertEquals(1, flight.getPilots().size());
    }

    @Test
    public void canAddCabinCrewToFlight(){
        flight.addCabinCrewToFlight(cabinCrewMember1);
        flight.addCabinCrewToFlight(cabinCrewMember2);
        flight.addCabinCrewToFlight(cabinCrewMember3);
        flight.addCabinCrewToFlight(cabinCrewMember4);
        assertEquals(4, flight.getCrewMembers().size());
    }
}
