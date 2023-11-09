import React, { useRef, useState } from "react";
import { NavLink } from "react-router-dom";

export default function Navbar({ username, onUpload }) {
  const fileInputRef = useRef(null);
  const [file, setFile] = useState(null);
  const [description, setDescription] = useState("");

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const handleUploadSubmit = async (e) => {
    e.preventDefault();

    if (file) {
      try {
        const formData = new FormData();
        formData.append("file", file);
        formData.append("description", description);
        formData.append("likes", 0);
        formData.append("username", username); // Assuming 'username' is available in the scope

        const response = await fetch("http://127.0.0.1:5000/post", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          // Handle successful file upload
          console.log("File uploaded successfully");
          // Optionally, you can trigger a function passed as a prop
          // to update the state in the parent component (onUpload)
          if (onUpload) {
            onUpload();
          }
        } else {
          // Handle file upload failure
          console.error("File upload failed");
        }
      } catch (error) {
        console.error("Error uploading file:", error);
      }
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
          <form onSubmit={handleUploadSubmit}>
            <input
              type="text"
              placeholder="Enter a description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            />
            <button
              type="button"
              className="btn btn-success"
              onClick={handleUploadClick}
            >
              UPLOAD
            </button>
            <input
              type="file"
              accept=".jpg, .png"
              onChange={handleFileChange}
              ref={fileInputRef}
              style={{ display: "none" }}
            />
          </form>
          <NavLink className="nav-item nav-link" to="/logout">
            Logout
          </NavLink>
        </div>
      </div>
    </nav>
  );
}