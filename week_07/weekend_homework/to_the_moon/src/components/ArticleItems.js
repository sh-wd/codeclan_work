import React from 'react';

const ArticleItems = ({article}) => {

    return ( 
        <>
        <a href={article["url"]}>
            <li>
                <h2>{article["title"]}</h2>
                <img src={article["image_url"]} alt=""/>
                <h3>{article["summary"]}</h3>
                <p>Source: {article["news_site"]} Published: {article["published_at"].slice(0,10)}</p>
            </li>
        </a>
        </>
     );
};
 
export default ArticleItems;