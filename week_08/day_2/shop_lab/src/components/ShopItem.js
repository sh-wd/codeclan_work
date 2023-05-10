import React from 'react';
import { Link } from 'react-router-dom';

const ShopItem = ({id, name, brand, price}) => {
    return ( 
        <li> 
            Name: {name} - Brand: {brand} - Price: £{price}
            <Link to={`/basket/${id}`}>
                <button type="button">Add to basket!</button>
            </Link>
        </li>

     );
}
 
export default ShopItem;