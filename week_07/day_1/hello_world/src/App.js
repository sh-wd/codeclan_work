import React, {useState} from 'react'
import './App.css';

function App() {
  
  const [greeting, setGreeting] = useState("Hello World");
  const [total, setTotal] = useState(0);
  const [doubleTotal, setDoubleTotal] = useState(0);

  const handleClick = (name) => {
    setGreeting("Good day to you " + name);
  };
  const deposit = () => {
    setTotal(total + 10);
    setDoubleTotal(total * 2);
  };
  const withdraw = () => {
    if( total >= 10 ) {
    setTotal(total - 10)
    setDoubleTotal(total * 2);
    };
  };

  return (
    <>
    <h1>{greeting}</h1>
      <button onClick={() => handleClick("Steve")}>Change Greeting</button>
      <p>Total : £{total}</p>
      <p>Double Total : £{doubleTotal}</p>
      <button onClick={deposit}>Deposit</button>
      <button onClick={withdraw}>Withdraw</button>
    </>
  );
};

export default App;
