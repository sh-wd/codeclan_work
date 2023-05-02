import React from 'react';
import Comment from './Comment';

const CommentList = ({comments}) => {

    const commentNodes = comments.map((comment) => {
      return <Comment key={comment.id} comment={comment} />
    });

    return ( 
        <>
            <p>I'm a CommentList!</p>
            {commentNodes}
        </>
     );
};
 
export default CommentList;