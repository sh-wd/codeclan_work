public class FlightManager {
    public static double calculateBaggageAllowance(Flight flight) {
        return (calculateTotalBaggageAllowance(flight)/flight.getPlane().getCapacity());
    }

    public static double calculateTotalBaggageAllowance(Flight flight) {
        return flight.getPlane().getTotalWeight()/2;
    }

}
