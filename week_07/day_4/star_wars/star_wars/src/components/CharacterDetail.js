import React from 'react';


const CharacterDetail = ({character}) => {
    return ( 
        <div className= "character-detail">
            <p><b>Name:</b> {character.name}</p>
            <p><b>Height:</b> {character.height}</p>
            <p><b>Mass:</b> {character.mass}</p>
            <p><b>Hair colour:</b> {character.hair_color}</p>
            <p><b>Eye colour:</b> {character.eye_color}</p>
            <p><b>Gender:</b> {character.gender}</p>
        </div>
     );
};
 
export default CharacterDetail;

