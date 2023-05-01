import './App.css';
import React, { useState } from 'react';

function App() {
  const [items, setItems] = useState([
    {name: "Duct tape", isPurchased: false},
    {name: "Rope", isPurchased: true},
    {name: "Industrial Acid", isPurchased: false},
  ]);

  const [newItem, setNewItem] = useState("");

  const itemNodes = items.map((item, index) => {
    return(
      <li key={index} className={item.isPurchased ? "purchased" : "not-purchased"}>
        <span>{item.name}</span>
      {item.isPurchased ? <span className="purchased">Purchased</span> : <button onClick={() => {purchaseItem(index)}}>Purchase</button>}
      </li>
    );
  });

  const handleItemInput = (event) => {
    setNewItem(event.target.value)
  };

  const saveNewItem = (event) => {
    event.preventDefault();
    const copyItems = [...items];
    copyItems.push({name: newItem, isPurchased: false});
    setItems(copyItems);
    setNewItem("");
  };

  const purchaseItem = (index) => {
    const copyItems = [...items];
    copyItems[index].isPurchased = true;
    setItems(copyItems);
  };

  return (
    <div className="App">

      <h1>Shopping List</h1>
      <hr></hr>

      <ul>
        {itemNodes}
      </ul>

      <form onSubmit={saveNewItem}>
        <label htmlFor="new-item">Add a new item:</label>
        <input id="new-item" type="text" value={newItem} onChange={handleItemInput}></input>
        <input type="submit" value="Save New Item"></input>
      </form>

    </div>
  );
}

export default App;
