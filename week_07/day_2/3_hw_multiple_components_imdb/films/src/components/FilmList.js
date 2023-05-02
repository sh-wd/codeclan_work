import React from 'react';
import Film from './Film';

const FilmList = ({films}) => {

    const filmNodes = films.map((film) => {
      return <Film key={film.id} film={film} />
    });

    return ( 
        <>
            {filmNodes}
            <h2 className="upcoming-box"><a href="https://www.imdb.com/calendar/?region=gb">View more upcoming releases...</a></h2>
        </>
     );
};
 
export default FilmList;