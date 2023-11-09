import React, { useEffect, useState } from 'react';
import './Dashboard.css'; // Import your CSS file
import Navbar from './Navbar';
import { useLocation } from 'react-router-dom';

export default function Dashboard() {
  const [posts, setPosts] = useState([]);
  const location = useLocation();
  const username = location.state && location.state.username;
  const [loggedInUsersId, setLoggedInUsersId] = useState(null); // State to store the logged-in user's ID

  useEffect(() => {
    // Fetch the post data from your seed.py when the component mounts
    fetch('http://127.0.0.1:5000/posts')
      .then((resp) => resp.json())
      .then((data) => {
        setPosts(data);
        console.log(data);
      })
      .catch((error) => {
        console.error('Error fetching posts:', error);
      });

    // Fetch the logged-in user's information and store their ID
    fetch('http://127.0.0.1:5000/users')
      .then((resp) => resp.json())
      .then((data) => {
        // Assuming you can identify the logged-in user based on their username
        const loggedInUser = data.find((user) => user.username === username);
        if (loggedInUser) {
          setLoggedInUsersId(loggedInUser.id);
          console.log(`Logged in user: ${username}, user_id: ${loggedInUser.id}, Is logged in`);
        }
      })
      .catch((error) => {
        console.error('Error fetching users:', error);
      });
  }, [username]);

  return (
    <div>
     <Navbar username={username} loggedInUserId={loggedInUsersId} />
      <h1>Post Section</h1>
      <h1 className="post-section">Post Section</h1>
    <div className="post-container">
      {posts.map((post, index) => (
        <div key={index} className="post-card">
          <p className="post-likes">♡{post.likes}</p>
          <p><img src={post.content} alt="Post Image" /></p>
          <p className="post-username">{post.user.username}</p>
          <p className="post-description">{post.description}</p>
          {/* <p className="post-comments">Comments: {post.comments}</p> */}
        </div>
      ))}
      </div>
    </div>
  );
}
