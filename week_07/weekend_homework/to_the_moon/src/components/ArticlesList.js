import React from 'react';
import ArticleItems from './ArticleItems';

const ArticlesList = ({articles}) => {
    const articleItems = articles.map((article, index) => {
        return <ArticleItems article={article} key={index}/>
    });

    return ( 
        <>
        <ul>
            <li>{articleItems}</li>
        </ul>
        </>
     );
};
 
export default ArticlesList;