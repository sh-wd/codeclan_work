import React from 'react';

const Comment = ({comment}) => {
    return (
        <>
            <h4>{comment.text}</h4>
            <p>{comment.author}</p>
        </>
      );
};
 
export default Comment;