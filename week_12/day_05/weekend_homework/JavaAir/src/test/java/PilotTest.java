import Crew.Pilot;
import Crew.Rank;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PilotTest {

    Pilot pilot;

    @Before
    public void before() {
        pilot = new Pilot("Agnus", Rank.CAPTAIN, "br00n");
    }

    @Test
    public void hasRank(){
        assertEquals(Rank.CAPTAIN, pilot.getRank());
    }

    @Test
    public void canFlyPlane(){
        assertEquals("Cabin crew git ready fir take aff", pilot.flyPlane());
    }

}