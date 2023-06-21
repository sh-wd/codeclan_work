package com.codeclan.example.pirateservice.repositories;

import com.codeclan.example.pirateservice.Raid;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RaidRepository extends JpaRepository<Raid, Long> {

    List<Raid> findRaidByLocation(String location);
    List<Raid> findByPiratesShipName(String name);
}
