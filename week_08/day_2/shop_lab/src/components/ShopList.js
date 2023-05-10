import React from 'react';
import ShopItem from './ShopItem';

const ShopList = ({list, onButtonClicked}) => {

    const listItems = list.map((item) => {
        return <ShopItem id={item.id} name={item.name}  brand={item.brand} price={item.price}/>
    })

    return ( 
        <>
        <h1>This is a list:</h1>
            <ul>
               {listItems}
            </ul>
        </>
     );
}
 


export default ShopList;