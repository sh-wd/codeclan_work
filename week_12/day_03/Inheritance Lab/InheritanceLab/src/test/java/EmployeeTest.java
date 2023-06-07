import Staff.Employee;
import Staff.Management.Director;
import Staff.Management.Manager;
import Staff.techStaff.DatabaseAdmin;
import Staff.techStaff.Developer;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class EmployeeTest {

    Employee employee;

    Manager manager;

    DatabaseAdmin databaseadmin;

    Director director;

    Developer developer;

    @Before
    public void before() {
        manager = new Manager("Richard", "DE113456 A", 50000.00, "Cyber Someshite");
        developer = new Developer("Zoe", "AS123452 R", 35000.00);
        databaseadmin = new DatabaseAdmin("Scott", "WE124365 G", 40000.00);
        director = new Director("Lovely Steve", "AW236543 S", 80000.00, "Top Doge", 5000000.00);
    }

    @Test
    public void canSetSalary() {
        manager.setSalary(45000.00);
        assertEquals(45000.00, manager.getSalary(), 0.0);
    }

    @Test
    public void canRaiseSalary() {
        manager.raiseSalary(5000.00);
        assertEquals(55000.00, manager.getSalary(), 0.0);
    }

    @Test
    public void canPayBonus() {
        assertEquals(500.00, manager.payBonus(), 0.0);
    }

    @Test
    public void canRaiseDeveloperSalary() {
        developer.raiseSalary(4000.00);
        assertEquals(39000.00, developer.getSalary(), 0.0);
    }

    @Test
    public void canPayDeveloperBonus() {
        assertEquals(350.00, developer.payBonus(), 0.0);
    }

    @Test
    public void canRaiseDatabaseAdminSalary() {
        databaseadmin.raiseSalary(5000.00);
        assertEquals(45000.00, databaseadmin.getSalary(), 0.0);
    }

    @Test
    public void canPayDatabaseAdminBonus() {
        assertEquals(400.00, databaseadmin.payBonus(), 0.0);
    }

    @Test
    public void canSetBudget() {
        director.setBudget(6000000.00);
        assertEquals(6000000.00, director.getBudget(), 0.0);
    }

    @Test
    public void canRaiseDirectorSalary() {
        director.raiseSalary(5000.00);
        assertEquals(85000.00, director.getSalary(), 0.0);
    }

    @Test
    public void canPayDirectorBonus() {
        assertEquals(800.00, director.payBonus(), 0.0);
    }

    @Test
    public void cannotRaiseByNegative() {
        director.raiseSalary(-70000.00);
        assertEquals(80000.00, director.getSalary(), 0.0);
    }

    @Test
    public void cannotNameNameNull() {
        director.setName(null);
        assertEquals("Lovely Steve", director.getName());

    }

    @Test
    public void canSetDirectorBonus() {
        assertEquals(1600.00, director.payBonus(), 0.0);
    }

}



