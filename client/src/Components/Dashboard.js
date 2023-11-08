import React, { useEffect, useState } from 'react';

function ImageUploader() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [description, setDescription] = useState('');
  const [likes, setLikes] = useState(0);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/posts')
    .then(resp => resp.json())
    .then((data) => {
            setPosts(data); // Set the retrieved posts in the state
          })
          .catch((error) => {
            console.error('Error fetching posts:', error);
          });
      }, []);
    
    

    if (selectedFile) {
      // Handle the file upload here and send it to the backend
      const formData = new FormData();
      formData.append('file', selectedFile);
      formData.append('description', description);
      formData.append('likes', likes);
      formData.append('username', 'username'); // Replace with the actual username

      fetch('/upload', {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error('Error uploading the image:', error);
        });
    }
  } [selectedFile, description, likes]);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) setSelectedFile(file);
  };

  return (
    <div>
      <input type="file" accept=".jpg" onChange={handleFileChange} style={{ display: 'none' }} id="fileInput" />
      <label htmlFor="fileInput">
        <button>UPLOAD</button>
      </label>
      <input
        type="text"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <input
        type="number"
        placeholder="Likes"
        value={likes}
        onChange={(e) => setLikes(e.target.value)}
      />
   /</div> 
  );
  

export default ImageUploader;