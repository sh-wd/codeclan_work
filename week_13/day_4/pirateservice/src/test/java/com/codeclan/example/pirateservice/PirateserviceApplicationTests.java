package com.codeclan.example.pirateservice;

import com.codeclan.example.pirateservice.repositories.PirateRepository;
import com.codeclan.example.pirateservice.repositories.RaidRepository;
import com.codeclan.example.pirateservice.repositories.ShipRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@SpringBootTest
class PirateserviceApplicationTests {

	@Autowired
	PirateRepository pirateRepository;

	@Autowired
	ShipRepository shipRepository;

	@Autowired
	RaidRepository raidRepository;

	@Test
	void contextLoads() {
	}

	@Test
	public void createPirate(){
		Ship ship = new Ship("The Bloody Awful");
		shipRepository.save(ship);
		Pirate pirate = new Pirate("Jack", "Sparrow", 32, ship);
		pirateRepository.save(pirate);

		Raid raid1 = new Raid("The ram raiding of Greggs",500 );
		raidRepository.save(raid1);

		pirate.addRaid(raid1);
		pirateRepository.save(pirate);
	}

	@Test
	public void canFindPiratesOver30(){
		List<Pirate> found = pirateRepository.findByAgeGreaterThan(30);
		assertTrue(found.size() > 0);
	}

	@Test
	public void canFindByLocation(){
		List<Raid> found = raidRepository.findRaidByLocation("Tortuga");
		assertEquals("Tortuga", found.get(0).getLocation());
	}

	@Test
	public void canFindPiratesByRaidId(){
		List<Pirate> foundPirates = pirateRepository.findByRaidsId(1L);
		assertEquals(1, foundPirates.size());
		assertEquals("Jack", foundPirates.get(0).getFirstName());
	}

	@Test
	public void canFindShipsWithPratesFirstName(){
		List<Ship> foundShips = shipRepository.findByPiratesFirstName("Maggie");
		assertTrue(foundShips.size() > 0);
	}

	@Test
	public void canFindAllRaidsForAGivenShipName(){
		List<Raid> foundRaids = raidRepository.findByPiratesShipName("The Black Pearl");
		assertTrue(foundRaids.size() > 0);
	}
}
