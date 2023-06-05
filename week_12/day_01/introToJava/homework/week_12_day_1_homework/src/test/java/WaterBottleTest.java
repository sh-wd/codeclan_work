import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class WaterBottleTest {

    WaterBottle waterBottle;

    @Before
    public void before(){
        waterBottle = new WaterBottle();
    }

    @Test
    public void hasVolumeOf100(){
        assertEquals(100, waterBottle.getVolume());
    }

    @Test
    public void canRemove10FromVolume(){
        waterBottle.remove10();
        assertEquals(90, waterBottle.getVolume());
    }

    @Test
    public void canEmptyVolume(){
        waterBottle.emptyVolume();
        assertEquals(0, waterBottle.getVolume());
    }

    @Test
    public void canFillVolume(){
        waterBottle.fillVolume();
        assertEquals(100, waterBottle.getVolume());
    }
}
