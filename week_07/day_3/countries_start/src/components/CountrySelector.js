import React from 'react';
import OptionItem from './OptionItem';

const CountrySelector = ({countries, onCountrySelected}) => {

    const handleChange = (event) => {
        const chosenCountry = countries[event.target.value];
        onCountrySelected(chosenCountry);
    };

    const sortedCountries = countries.sort((country1, country2) => (country1.name.common > country2.name.common ? 1 : - 1));

    const countryOptions = sortedCountries.map((country, index) => {
        return <OptionItem key={index} country={country} index={index}/>
    });

    return ( 
        <select defaultValue="" onChange={handleChange}>
            <option value="" selected>What's the capital of?</option>
            {countryOptions}
        </select>
     );
};
 
export default CountrySelector;