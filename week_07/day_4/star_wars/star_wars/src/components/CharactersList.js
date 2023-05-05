import React from 'react';
import CharacterItem from './CharacterItem';

const CharactersList = ({characters, handleCharacterSelect}) => {

    const allCharacters = [];
    for(let charArray of characters) {
        for(let charObj of charArray.results){
            allCharacters.push(charObj);
        };
    };
    console.log(allCharacters);



    const characterItems = allCharacters.map((character, index) => {
        return <CharacterItem character={character} key={index} onCharacterClicked={handleCharacterSelect}/>
    });

    return ( 
        <>
        <ul>
            <p>{characterItems}</p>
        </ul>
        </>
     );
};
 
export default CharactersList;