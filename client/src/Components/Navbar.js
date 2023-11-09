import React from "react";
import { NavLink } from "react-router-dom";

export default function Navbar({ username, onUpload, loggedInUserId }) {
  let postImageURL;
  let userDescription;

  const handlePostClick = () => {
    const imageURL = prompt("PLEASE INPUT IMAGE URL");
    if (imageURL) {
      postImageURL = imageURL;

      const description = prompt("PLEASE INPUT IMAGE DESCRIPTION");
      if (description) {
        userDescription = description;
        console.log("Image Description entered:", userDescription);
      }
    }
  };

  const handleUploadSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:5000/posts", {
        method: "POST",
        body: JSON.stringify({
          content: postImageURL,
          description: userDescription,
          likes: 0,
          comments: "",
          user_id: loggedInUserId,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        console.log("Data submitted successfully");

        // Continue with any desired behavior here with the response data
        const responseData = await response.json();
        console.log("Response Data:", responseData);

        if (onUpload) {
          onUpload();
        }
      } else {
        console.error("Data submission failed");
      }
    } catch (error) {
      console.error("Error submitting data:", error);
    }
  };

  return (
    <div className="navbar navbar-expand-lg navbar-dark bg-dark">
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbar"
      >
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="justify-content-end collapse navbar-collapse" id="navbar">
        <div className="navbar-nav">
          <button
            type="button"
            className="btn btn-success"
            onClick={handlePostClick}
          >
            POST
          </button>
          <button
            type="submit"
            className="btn btn-primary"
            onClick={handleUploadSubmit}
          >
            SUBMIT
          </button>
          <NavLink className="nav-item nav-link" to="/logout">
            Logout
          </NavLink>
        </div>
        <div className="ml-auto">
          <p className="text-white">{username}</p>
        </div>
      </div>
    </div>
  );
}
