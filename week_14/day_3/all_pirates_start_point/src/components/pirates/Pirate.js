import React, {Fragment} from 'react';
import { Link } from 'react-router-dom';


const Pirate = ({pirate}) => {

  if (!pirate){
    return <p>"Loading..."</p>
  }
  const url = "/pirates/" + pirate.id;
  return (
    <Fragment>
    <p>
      <Link to={url} className="name">
        {pirate.firstName} {pirate.lastName}
      </Link>
    </p>
    <p>Age: {pirate.age}</p>
    <p>Ship: {pirate.ship.name}</p>
    </Fragment>
  )
}

export default Pirate;
