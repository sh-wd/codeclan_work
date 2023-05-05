import React from 'react';

const CharacterItem = ({character, onCharacterClicked}) => {

  const handleClick= () => {
    console.log("Clicked on " + character.name);
    console.log(character);
    onCharacterClicked(character);
  };

  return <li onClick={handleClick}>{character.name}</li>

}

export default CharacterItem;