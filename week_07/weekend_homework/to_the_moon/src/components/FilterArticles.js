import React from 'react';

const FilterArticles = ({sources, handleSelectChange}) => {
    return ( 
        <>
        <select onChange={handleSelectChange}>
        {sources.map(source => {
          return <option key={source.name} value={source.url}>{source.name}</option>
        })};
        </select>
        </>
     );
}
 
export default FilterArticles;