import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class FlightManagerTest {
    Flight flight;

    Passenger passenger1;
    Passenger passenger2;
    Passenger passenger3;

    @Before
    public void before(){
        flight = new Flight(Plane.HAGGIS_EXPRESS,
                "JA842",
                Airport.GLA,
                Airport.ABZ,
                "09:00");
        passenger1 = new Passenger("Jimmy", 2);
        passenger2 = new Passenger("Morag", 1);
        passenger3 = new Passenger("Iona", 5);
    }

    @Test
    public void canCalculateTotalBaggageAllowanceForFlight(){
        assertEquals(950.00, FlightManager.calculateTotalBaggageAllowance(flight), 0.0);
    }

    @Test
    public void canCalculatePassengerBaggageAllowance(){
        assertEquals(95.00, FlightManager.calculateBaggageAllowance(flight), 0.0);
    }

//    @Test
//    public void canCalculatePassengerBaggageWeight(){
//        flight.addPassengerToFlight(passenger1);
//        flight.addPassengerToFlight(passenger2);
//        flight.addPassengerToFlight(passenger3);
//        assertEquals(760.00, FlightManager.calculatePassengerBaggageWeight(), 0.0);
//    }

}
