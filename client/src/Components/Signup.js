import { useState } from 'react';
import { Link } from 'react-router-dom';

function SignUp() {
  const [user, setUser] = useState([])
  const [formData, setFormData] = useState({
    username: '',
    email_address: '',
    full_name: '',
    _password_hash: '',
    confirm_password: ''
  });

  function handleSubmit(event) {
    event.preventDefault();

    // Check if the passwords match
    if (formData.password1 !== formData.password2) {
      alert('Passwords do not match');
      return;
    }

    fetch("http://127.0.0.1:5000/signup", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
      .then(resp => resp.json())
      .then(data => {
        setUser(prevUsers => [...prevUsers,data]);
        // Reset the form data after a successful response
        setFormData({
          username: '',
          email_address: '',
          full_name: '',
          _password_hash: '',
          confirm_password: ''
        });
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  }

    if (!user){
      return <p>Loading ...</p>
    }


  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div className="card mx-auto my-5" style={{ width: '25rem' }}>
          <img
            src="https://www.myfitnesschat.com/wp-content/uploads/2019/03/pexels-photo-1509428.jpeg"
            className="card-img-top"
            alt="..."
          />
          <h4 className="text-center">Sign Up</h4>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="username"
              className="form-control"
              id="username"
              name="username"
              placeholder="Create Username"
              value={formData.username}
              onChange={handleInputChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email Address:</label>
            <input
              type="email"
              className="form-control"
              id="email"
              name="email_address"
              placeholder="Enter Email"
              value={formData.email_address}
              onChange={handleInputChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="fullName">First Name:</label>
            <input
              type="text"
              className="form-control"
              id="full_name"
              name="full_name"
              placeholder="Enter Full Name"
              value={formData.full_name}
              onChange={handleInputChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password1">Password:</label>
            <input
              type="password"
              className="form-control"
              id="password1"
              name="_password_hash"
              placeholder="Enter Password"
              value={formData._password_hash}
              onChange={handleInputChange}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password2">Password (Confirm):</label>
            <input
              type="password"
              className="form-control"
              id="password2"
              name="confirm_password"
              placeholder="Confirm Password"
              value={formData.confirm_password}
              onChange={handleInputChange}
            />
          </div>

          <br />
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
          <p>
            Have an account? <Link to="/login">Login</Link>
          </p>
        </div>
      </form>
    </div>
  );
}

export default SignUp;