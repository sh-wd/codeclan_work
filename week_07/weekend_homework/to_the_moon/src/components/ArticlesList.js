import React from 'react';
import ArticleItems from './ArticleItems';

const ArticlesList = ({articles}) => {
    const articleItems = articles.map((article, index) => {
        return <ArticleItems article={article} key={index}/>
    });

    return ( 
        <>
        <ul className="article-container">{articleItems}</ul>
        </>
     );
};
 
export default ArticlesList;