import Crew.CabinCrewMember;
import Crew.Rank;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CabinCrewMemberTest {

    CabinCrewMember cabinCrewMember;

    @Before
    public void before(){
        cabinCrewMember = new CabinCrewMember("Jock", Rank.PURSER);
    }

    @Test
    public void hasRank(){
        assertEquals(Rank.PURSER, cabinCrewMember.getRank());
    }

    @Test
    public void canRelayMessage(){
        assertEquals("In case eh emergency oaxygen masks will drap fae the errheid loackers", cabinCrewMember.relayMessage());
    }
}
