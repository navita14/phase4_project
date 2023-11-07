import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';

function Login() {
  const history = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  function handleLogin(e) {
    e.preventDefault(); // Prevent the default form submission

    // Create an object with the user's email and password
    const userCredentials = {
      username: email, // Use 'username' based on your backend's expectation
      password: password,
    };

    // Send a POST request to your server
    fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userCredentials),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Login failed');
        }
      })
      .then((data) => {
        // Check the 'message' property in the server response
        if (data.message === 'login success') {
          // Assuming 'permission_level' is obtained from the server response
          const permission_level = data.permission_level;
          if (permission_level === 1) {
            history.push('/admin_dashboard');
          } else if (permission_level === 2) {
            history.push('/manager_dashboard');
          } else if (permission_level === 3) {
            history.push('/worker_dashboard');
          } else {
            // Handle invalid login or unauthorized access
            console.log('Unauthorized access');
          }
        } else {
          // Handle login failure
          console.log('Login failed');
        }
      })
      .catch((error) => {
        // Handle login failure or errors
        console.error(error);
      });
  }

  return (
    <div>
      <form onSubmit={handleLogin}>
        <div className="card mx-auto my-5" style={{ width: '25rem' }}>
          <img
            src="https://www.myfitnesschat.com/wp-content/uploads/2019/03/pexels-photo-1509428.jpeg"
            className="card-img-top"
            alt="..."
          />
          <h4 className="text-center">Login</h4>
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
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              className="form-control"
              id="password"
              name="password"
              placeholder="Enter Password"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <br />
          <button type="submit" className="btn btn-primary">
            Login
          </button>

          <p>
            Do not have an account? <Link to="/signup">Sign Up</Link>
          </p>

        </div>
      </form>
    </div>
  );
}

export default Login;
