import { Link } from "react-router-dom";
import Pirate from "./Pirate";
import React from "react";

const PirateDetail = ({pirate, handleDelete}) => {

    if(!pirate){
    return "Loading...";
    }

    const onDelete = () => {
      handleDelete(pirate.id);
    }

    const piratesRaids = pirate.raids.map((raid, index) => {
      return <li key={index}>{raid.location}</li>
    })

    return(
        <div className="component">
            <Pirate pirate={pirate}/>
            <ul>
                {piratesRaids}
            </ul>
            <button onClick={onDelete}>Delete {pirate.firstName}</button>
            <Link to={"/pirates/edit/" + pirate.id}>Edit Pirate</Link>
        </div>
    )
}
export default PirateDetail;