import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PrinterTest {

    Printer printer;

    @Before
    public void before() {
        printer = new Printer(100, 60);
    }

    @Test
    public void canPrint(){
        printer.print(10,5);
        assertEquals(50, printer.getPaper());
    }

    @Test
    public void cannotOverPrint(){
        printer.print(10,50);
        assertEquals(100, printer.getPaper());
    }

    @Test
    public void canReduceToner(){
        printer.print(5,10);
        assertEquals(10, printer.getToner());
    }
}