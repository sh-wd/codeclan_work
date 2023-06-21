import React, {Component, Fragment, useEffect, useState} from 'react';
import {BrowserRouter as Router, Route, Switch, Routes, useParams} from 'react-router-dom';
import PirateList from '../components/pirates/PirateList';
import Request from '../helpers/request.js';
import PirateDetail from '../components/pirates/PirateDetail';
import PirateForm from '../components/pirates/PirateForm';
import PirateEditForm from '../components/pirates/PirateEditForm';

const PirateContainer = () => {

  const [pirates, setPirates] = useState([]);
  const [ships, setShips] = useState([]);
  const [raids, setRaids] = useState([]);

  useEffect(() => {
    getPirates()
    getShips()
    getRaids()
  }, [])

  const getPirates = () => {
    const request = new Request()
    request.get("/api/pirates")
    .then((data) => {
      console.log(data)
      setPirates(data)
    })
  }

  const getShips = () => {
    const request = new Request()
    request.get("/api/ships")
    .then((data) => setShips(data));
  }

  const getRaids = () => {
    const request = new Request()
    request.get("/api/raids")
    .then((data) => setRaids(data));
  }

  const PirateDetailWrapper = () => {
    console.log("wrapper triggered")
    //extract id from url
    const {id} = useParams()
    let foundPirate = findPirateById(id)
    return <PirateDetail pirate={foundPirate} handleDelete={handleDelete}/>
  }

  const handleUpdate = (pirate) => {
    console.log("pirate ", pirate)
    const request = new Request()
    request.patch("/api/pirates/" + pirate.id, pirate)
    .then(() => {
      window.location = "/pirates/" + pirate.id
    })
  }

  const PirateEditWrapper = () => {
    const {id} = useParams()
    let foundPirate =findPirateById(id)
    return <PirateEditForm pirate={foundPirate} ships={ships} handleUpdate={handleUpdate}/>
  }

  const findPirateById = (id) => {
    let foundPirate = null;
    for (let pirate of pirates){
      if(pirate.id === parseInt(id)){
        foundPirate = pirate
      }
    }
    return foundPirate;
  }

  const handleDelete = (id) => {
    const request = new Request()
    const url = "/api/pirates/" + id;
    request.delete(url)
    .then(() => {
      window.location= "/pirates"
    })
  }
    const handlePost = (pirate) => {
      const request = new Request()
      request.post("/api/pirates", pirate)
      .then(() => {
        window.location = "/pirates"
      })
  

  }

    return(
      <div>
        <Routes>
          <Route path="/:id" element={<PirateDetailWrapper/>}/>
          {pirates.length> 0 ? <Route path="/" element={<PirateList pirates={pirates}/>}/> :null}
          <Route path="/new" element={<PirateForm ships={ships} onCreate={handlePost}/>}/>
          <Route path="/edit/:id" element={<PirateEditWrapper/>}/>
        </Routes>
      </div>
      )


}




export default PirateContainer;
