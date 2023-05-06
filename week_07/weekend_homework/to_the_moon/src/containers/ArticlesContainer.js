import React,{ useEffect, useState } from 'react';
import ArticlesList from '../components/ArticlesList';
import FilterArticles from '../components/FilterArticles';
// import IncreaseList from '../components/IncreaseList';
import './ArticlesContainer.css'

const ArticlesContainer = ({sources}) => {

    const [articles, setArticles] = useState([]);

    useEffect(() => {
        getArticles(sources[0].url);
    }, [sources]);

    const getArticles = function(url){
        fetch(url)
        .then (res => res.json())
        .then (articles => setArticles(articles.results))
    };

    // const handleButtonClick = (event) => {
    //     getArticles(event.target.value)
    // };

    const handleSelectChange = event => {
        getArticles(event.target.value);
    };

    return ( 
        <>
        <h1>To...to...to the Moon News</h1>
        <FilterArticles handleSelectChange={handleSelectChange} sources={sources}/>
        <ArticlesList articles={articles}/>
        {/* <IncreaseList/> */}
        </>
     );
};
 
export default ArticlesContainer;