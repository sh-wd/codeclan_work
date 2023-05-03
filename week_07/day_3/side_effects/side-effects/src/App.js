import React, {useEffect, useState} from 'react';
import './App.css';

function App() {
  const [number, setNumber] = useState(0);
  const [doubleNum, setDoubleNum] = useState(0);

  useEffect(() => {
    console.log("useEffect called");
    setDoubleNum(number * 2);
  }, [number]);

  const handleInc = () => {
    setNumber(number + 1);
    // setDoubleNum(number * 2);
  };

  const handleDec = () => {
    setNumber(number - 1);
    // setDoubleNum(number *2);
  };

  return (
    <div className="App">
      <button value={number} onClick={handleInc}> + </button>
      <button value={number} onClick={handleDec}> - </button>
      <h2>Number is {number}</h2>
      <h2>Double number is {doubleNum}</h2>
    </div>
  );
}

export default App;
