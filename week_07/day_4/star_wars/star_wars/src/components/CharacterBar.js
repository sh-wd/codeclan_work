import React from 'react';

const CharacterBar = ({handleSelectChange, characters}) =>{
    
    const handleSelected = (event) => {
        handleSelectChange(characters[event.target.value])
    };

    return (
      <div>
        <select onChange={handleSelected}>
          {characters.map((character, index) => {
            return (
            <>
            <option key={character.name} value={index} placeholder="Obi-Wan that you want?">{character.name}</option>
            </>
            )
          })}
        </select>
      </div>
    );
  };
  
  export default CharacterBar;