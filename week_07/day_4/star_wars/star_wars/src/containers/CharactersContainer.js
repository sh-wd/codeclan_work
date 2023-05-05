import React, {useState, useEffect} from 'react';
import CharacterDetail from '../components/CharacterDetail';
import CharactersList from '../components/CharactersList';
import CharacterBar from '../components/CharacterBar';


const CharactersContainer = () => {

    const [characters, setCharacters] = useState([]);
    const [selectedCharacter, setSelectedCharacter] = useState(null)

    useEffect(() => {
        getAllCharacters();
    }, []);

    const handleCharacterSelect = (character) => {
        setSelectedCharacter(character)
    }

    const handleSelectChange = character => {
        setSelectedCharacter(character)
    }

    const getAllCharacters = () => {
        const allRequests = [];

        for( let i = 1; i <= 9; i++ ) {
            const newFetch = fetch("https://swapi.dev/api/people/?page=" + i + "&format=json")
            .then((response) => response.json());
            allRequests.push(newFetch);
        };


        Promise.all(allRequests)
        .then((data) => setCharacters(data))
    };

    const allCharacters = [];
    for(let charArray of characters) {
        for(let charObj of charArray.results){
            allCharacters.push(charObj);
        };
    };
    console.log(characters)
    return ( 
        <>
        <h1>A long time ago in a galaxy far far away...</h1>
        <h2>Yo-da wanna meet somebody?</h2>
        <CharacterBar
            handleSelectChange={handleSelectChange}
            characters={allCharacters}
        />
            { selectedCharacter ? <CharacterDetail character={selectedCharacter}/> : null}
        </>
     );
};
 
export default CharactersContainer;