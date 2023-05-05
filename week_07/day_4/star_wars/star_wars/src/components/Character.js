import React from 'react';
import CharactersList from './CharactersList';

const Character = ({character, onCharacterClicked}) => {

    const handleClick= () => {
      console.log("Clicked on " + character.name);
      onCharacterClicked(character);
    };
  
    return <li onClick={handleClick}>{character.name}</li>
  }

  export default Character;