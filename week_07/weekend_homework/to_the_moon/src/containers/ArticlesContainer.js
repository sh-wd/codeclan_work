import React,{ useEffect, useState } from 'react';
import ArticlesList from '../components/ArticlesList';

const ArticlesContainer = () => {

const [articles, setArticles] = useState([]);

useEffect(() => {
    getArticles();
}, []);

const getArticles = function(){
    fetch("https://api.spaceflightnewsapi.net/v4/articles/?format=json&limit=20")
    .then (res => res.json())
    .then (articles => setArticles(articles.results))
};


    return ( 
        <>
        <h1>To...to...to the Moon News</h1>
        <ArticlesList articles={articles}/>
        </>
     );
};
 
export default ArticlesContainer;