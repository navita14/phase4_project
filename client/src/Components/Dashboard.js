import React, { useEffect, useState } from 'react';
import './Dashboard.css'; // Import your CSS file
import Navbar from './Navbar'
import { useLocation } from 'react-router-dom';


export default function Dashboard() {
  const [posts, setPosts] = useState([]);
  const location = useLocation();
  const username = location.state && location.state.username;

  useEffect(() => {
    // Fetch the post data from your seed.py when the component mounts
    fetch('http://127.0.0.1:5000/post')
      .then((resp) => resp.json())
      .then((data) => {
        setPosts(data);
        console.log(data);
      })
      .catch((error) => {
        console.error('Error fetching posts:', error);
      });
  }, []);

  return (
    <div> 
        <Navbar username={username} />
        <h1>Post Section</h1>
        <div className="post-container">
            {posts.map((post, index) => (
            <div key={index} className="post-card">
                <p><img src={post.content} alt="Post Image" /></p>
                <p>User: {post.user.username}</p>
                <p>Description: {post.description}</p>
                <p>Likes: {post.likes}</p>
                <p>Comments: {post.comments}</p>
        </div>
        ))}
      </div>
    </div>
  );
}