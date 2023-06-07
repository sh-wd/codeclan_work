import main.Clothing.RunningShoe;
import main.Electrical.Fridge;
import main.Product;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ProductTest {

    Product product;
    Fridge fridge;

    RunningShoe shoe;

    @Before
    public void before(){
        fridge = new Fridge(1000.00, 2500.00, "Samsung", 7654, "Gigafridge", 900,5, 1,true);
        shoe = new RunningShoe(10.00, 200.00, "Sketchers", 1234, "Zoom Zoom 2000", 7, "Denim", true, true);
    }

    @Test
    public void hasManufacturer(){
        assertEquals("Samsung", fridge.getManufacturer());
    }

    @Test
    public void canCalculateMarkup(){
        assertEquals(1500.00, fridge.calculateMarkup(), 0.0);
    }

    @Test
    public void canTurnFridgeOn(){
        assertEquals("Getting chilly", fridge.turnOn());
    }

    @Test
    public void canLightUp(){
        assertEquals(true, shoe.isLightUp());
    }

    @Test
    public void canSell(){
        assertEquals("Transaction complete", fridge.sellItem(12356));
    }
}
