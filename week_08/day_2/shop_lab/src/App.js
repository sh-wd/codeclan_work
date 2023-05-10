import React, {useState} from "react"
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import './App.css';
import ShopContainer from './container/ShopContainer';
import ShopList from './components/ShopList';
import Basket from './components/Basket';
import ShopItem from './components/ShopItem';
import NavBar from './components/NavBar';

function App() {

  const storedItems = [
    { id: 1, name: "Air Max Dawn", brand: "Nike", image: 'nike_air_max_dawn.jpeg', price: 105 },
    { id: 2, name: "React Vision", brand: "Nike", image: 'react_vision.jpeg', price: 115 },
    { id: 3, name: "Originals ZX Flux", brand: "Adidas", image: 'adidas_originals_zs_flux.jpeg', price: 75 },
    { id: 4, name: "Chuck Taylor All Star", brand: "Converse", image: 'converse_chuck_taylor.jpeg', price: 50 },
    { id: 5, name: "Old Skool", brand: "Vans", image: 'vans_oldskool.jpeg', price: 65 },
    { id: 6, name: "Originals Atlantic MKII", brand: "Adidas", image: 'adidas_originals_atlantic_MKII.jpeg', price: 110 },
    { id: 7, name: "Future", brand: "Puma", image: 'puma_future.jpeg', price: 90 },
    { id: 8, name: "Classic", brand: "Reebok", image: 'reebok_classic.jpeg', price: 80 },
    { id: 9, name: "Classic Slip On", brand: "Vans", image: 'vans_classic_slipon.jpeg', price: 100 },
    { id: 10, name: "Metacon", brand: "Nike", image: 'nike_metacon.jpeg', price: 75 }
];

  return (
    <div className="App">
      <Router>
        <NavBar/>
        <Routes>
          <Route path="/" element={<ShopContainer/>}/>
          <Route path="/list" element={<ShopList list={storedItems}/>}/>
          <Route path="/basket" element={<Basket/>}/>
          <Route path="/list/:id" render={props => <ShopItem {...props}/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
