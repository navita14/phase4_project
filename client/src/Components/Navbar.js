import React, { useRef, useState } from "react";
import { NavLink } from "react-router-dom";

export default function Navbar({ username, onUpload, loggedInUserId }) {
  const fileInputRef = useRef(null);
  const [descriptionInput, setDescriptionInput] = useState("");

  const handleFileSelection = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    if (e.target.files.length > 0) {
      console.log("Selected File:", e.target.files[0].name);
    }
  };

  const handleUploadSubmit = async (e) => {
    e.preventDefault();

    const selectedFile = fileInputRef.current.files[0];

    if (!selectedFile || !descriptionInput) {
      console.error("Image and description are required.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile); // Use "file" as the key
    formData.append("description", descriptionInput);
    formData.append("likes", 0);
    formData.append("comments", "");
    formData.append("user_id", loggedInUserId);

    try {
      const response = await fetch("http://127.0.0.1:5000/posts", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log("Data submitted successfully");
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
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbar"
      >
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="justify-content-end collapse navbar-collapse" id="navbar">
        <div>
          <p className="text-white">{username}</p>
        </div>
        <div className="navbar-nav">
          <button
            type="button"
            className="btn btn-success"
            onClick={handleFileSelection}
          >
            POST
          </button>
          <form onSubmit={handleUploadSubmit}>
            <input
              type="file"
              accept=".jpg, .png"
              onChange={handleFileChange}
              ref={fileInputRef}
              style={{ display: "none" }}
            />
            <input
              type="text"
              placeholder="Enter a description"
              value={descriptionInput}
              onChange={(e) => setDescriptionInput(e.target.value)}
            />
            <button type="submit" className="btn btn-primary">
              SUBMIT
            </button>
          </form>
          <NavLink className="nav-item nav-link" to="/logout">
            Logout
          </NavLink>
        </div>
      </div>
    </nav>
  );
}
