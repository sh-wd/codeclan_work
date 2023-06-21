import React from 'react';
import Pirate from './Pirate.js';


const PirateList = ({pirates}) => {

	const pirateElements = pirates.map((pirate, index) => {
	  return (
		<li key={index} className="component-item">
			<div className='component'>
	 	 		<Pirate pirate={pirate}/>
		 	</div>
	  	</li>
	  )
	})


	return (
		<div>
			{pirateElements}
		</div>
	)
}
 export default PirateList;
