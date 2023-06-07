import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class BearTest {

    private Bear bear;
    private Salmon salmon;

    private River river;

    @Before
    public void before(){
        bear = new Bear("Baloo");
        salmon = new Salmon();
        river = new River();
        river.addFish(salmon);
    }

    @Test
    public void bellyStartsEmpty(){
        assertEquals(0, bear.foodCount());
    }

    @Test
    public void canEatSalmon(){
        bear.eatFishFromRiver(river);
        assertEquals(0, river.fishCount());
    }

    @Test
    public void eatSleepPoopRepeat(){
        bear.eatFishFromRiver(river);
        bear.sleep();
        assertEquals(0, bear.foodCount());
    }
}
