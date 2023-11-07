import { useState } from 'react';

function SignUp() {
  const [email, setEmail] = useState('');
  const [firstName, setFirstName] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');

  const handleSignUp = (e) => {
    e.preventDefault();

    // Check if the passwords match
    if (password1 !== password2) {
      alert('Passwords do not match');
      return;
    }

    const userData = {
      username: email,
      password: password1,
      firstName,
    };

    fetch('http://localhost:5000/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    })
      .then((response) => {
        if (response.ok) {
          // Handle successful sign-up here, e.g., redirect to login page
          console.log('User registered successfully');
          // You can add code to redirect to the login page
        } else {
          // Handle sign-up failure here
          console.error('User registration failed');
        }
      })
      .catch((error) => {
        // Handle network errors here
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <form onSubmit={handleSignUp}>
        <div className="card mx-auto my-5" style={{ width: '25rem' }}>
          <img
            src="https://blog.trello.com/hubfs/marker_trello_bug_tracking.png"
            className="card-img-top"
            alt="..."
          />
          <h4 className="text-center">Sign Up</h4>
          <div className="form-group">
            <label htmlFor="email">Email Address:</label>
            <input
              type="email"
              className="form-control"
              id="email"
              name="email"
              placeholder="Enter Email"
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label htmlFor="firstName">First Name:</label>
            <input
              type="text"
              className="form-control"
              id="firstName"
              name="firstName"
              placeholder="Enter First Name"
              onChange={(e) => setFirstName(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password1">Password:</label>
            <input
              type="password"
              className="form-control"
              id="password1"
              name="password1"
              placeholder="Enter Password"
              onChange={(e) => setPassword1(e.target.value)}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password2">Password (Confirm):</label>
            <input
              type="password"
              className="form-control"
              id="password2"
              name="password2"
              placeholder="Confirm Password"
              onChange={(e) => setPassword2(e.target.value)}
            />
          </div>

          <br />
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}

export default SignUp;
