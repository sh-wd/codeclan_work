import React, { useState } from "react";

const PirateEditForm = ({pirate, ships, handleUpdate}) => {


    if (!pirate){
        return <p>"Loading..."</p>
      }

    const [statePirate, setStatePirate] = useState({
        firstName: "",
        lastName: "",
        age: 0,
        ship: null
    })

    const findShipIndex = () => {
      return ships.findIndex((ship) => {
        return pirate.ship.id === ship.id;
      })
    }

    const handleChange = (event) => {
      let propertyName = event.target.name;
      let copiedPirate = {...statePirate}
      copiedPirate[propertyName] = event.target.value;
      setStatePirate(copiedPirate)
    }

    const handleShip = (event) => {
        const index = parseInt(event.target.value);
        const selectedShip = ships[index];
        let copiedPirate = {...statePirate};
        copiedPirate["ship"] = selectedShip;
        setStatePirate(copiedPirate);
    }

    if(ships.length === 0){
        return <p>Loading...</p>
    }

    const shipOptions = ships.map((ship, index) => {
      return <option key={index} value={index}>{ship.name}</option>
    })

    const handleSubmit = (event) => {
      event.preventDefault();
      let updatedStatePirate = {...statePirate}
      updatedStatePirate["id"] = pirate.id;
      handleUpdate(updatedStatePirate);
    }


    return ( 
        <div>
            <form onSubmit={handleSubmit}>
                <input 
                type="text"
                placeholder={pirate.firstName}
                name="firstName"
                onChange={handleChange}
                value={statePirate.firstName}
                />
                <input
                type="text"
                placeholder={pirate.lastName}
                name="lastName"
                onChange={handleChange}
                value={statePirate.lastName}
                />
                <input
                type="number"
                placeholder={pirate.age}
                name="age"
                onChange={handleChange}
                value={statePirate.age}
                />
                <select name="ship" onChange={handleShip} defaultValue={findShipIndex()}>
                    {shipOptions}
                </select>
                <button type="submit">Save</button> 
            </form>
        </div>
     );
}
 
export default PirateEditForm;