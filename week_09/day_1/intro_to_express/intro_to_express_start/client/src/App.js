import './App.css';
import React, {useEffect, useState} from 'react';


function App() {

  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:9000")
    .then(response => response.json())
    .then(data => setMessage(data.message));
  });


  return (
    <>
      <h1>My App</h1>
      <p>The server said: {message}</p>
    </>
  );
}

export default App;