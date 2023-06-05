import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CalculatorTest {

    Calculator calculator;

    @Before
    public void before(){
        calculator = new Calculator();
    }

    @Test
    public void canAdd(){
        assertEquals(5, calculator.add(2,3));
    }

    @Test
    public void canSubtract(){
        assertEquals(4, calculator.subtract(5,1));
    }

    @Test
    public void canMultiply(){
        assertEquals(10, calculator.multiply(2,5));
    }

    @Test
    public void canDivide(){
        assertEquals(4, calculator.divide(8,2), 0.0);
    }
}
