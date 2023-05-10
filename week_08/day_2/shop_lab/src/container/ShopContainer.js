import React, {useState} from 'react';
import storedItems from '../App';
import ShopList from '../components/ShopList';


const ShopContainer = () => {

    const [shoes, setShoes] = useState(storedItems);
    const [selectedShoes, setSelectedShoes] = useState(null);
    const [basket, setBasket] = useState([]);

    const addtoBasket = (basketItem) => {
        const updateBasket = [...basket, basketItem];
        setBasket(updateBasket);
    };

    return ( 
        <>
        <h1>Shop init - THIS IS THE HOMEPAGE</h1>
        <ShopList addtoBasket={addtoBasket}/>
        </>
     );
}
 
export default ShopContainer;