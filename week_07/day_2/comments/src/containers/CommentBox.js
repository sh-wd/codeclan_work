import React, {useState} from "react"
import CommentList from "../components/CommentList";
import CommmentForm from "../components/CommentForm";

const CommentBox = () => {

    const [comments, setComments] = useState([
        {
          id: 1,
          author: "Rick Henry",
          text: "React is such a great framework!"
        },
        {
          id: 2,
          author: "Valerie Gibson",
          text: "I'm dreaming in React..."
        }
      ]);

    const addComment = (submittedComment) => {
        submittedComment.id = Date.now();
        const updateComments = [...comments, submittedComment];
        setComments(updateComments);
    };

    return (
        <>
            <h1>Comments</h1>
            <CommentList comments={comments}/>
            <h2>Add a comment:</h2>
            <CommmentForm onCommentSubmit={(comment) => addComment(comment)}/>
        </>
    );
};

export default CommentBox;