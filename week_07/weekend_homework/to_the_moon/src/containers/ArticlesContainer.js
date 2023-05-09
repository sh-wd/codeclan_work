import React,{ useEffect, useState } from 'react';
import logo from '../moon.png';
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
            <div className="logo-banner">
                <img src={logo} className="App-logo" alt="logo of the moon" />
                <div className="logo-banner-text">
                    <h1>To...to...to the Moon News</h1>
                    <h1 className="logo-banner-reflection">To...to...to the Moon News</h1>
                </div>
            </div>
        <FilterArticles handleSelectChange={handleSelectChange} sources={sources}/>
        <ArticlesList articles={articles}/>
        {/* <IncreaseList/> */}
        </>
     );
};
 
export default ArticlesContainer;