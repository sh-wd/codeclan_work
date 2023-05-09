import React from 'react';

const ArticleItems = ({article}) => {

    return ( 
        <div className="article">
        <a href={article["url"]}>
            <li>
                <h2>{article["title"]}</h2>
                <img src={article["image_url"]} className="article-img" alt=""/>
                <p>{article["summary"]}</p>
                <p>Source: {article["news_site"]} Published: {article["published_at"].slice(0,10)}</p>
            </li>
        </a>
        </div>
     );
};
 
export default ArticleItems;