import { useState } from 'react';
import { useHistory, Link,} from 'react-router-dom';

function Login() {
  // const history = useNavigate();
  const [username, setUserName] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  function handleLogin(e) {
    e.preventDefault(); // Prevent the default form submission
    console.log(username, password)

    // Create an object with the user's email and password
    const userCredentials = {
      username: username, // Use 'username' based on your backend's expectation
      _password_hash: password,
    };

    console.log(userCredentials)

    // Send a POST request to your server
    fetch('http://127.0.0.1:5000/login', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userCredentials),
    })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Login failed 1');
      }
    })
    .then((data) => {
      // Check the 'message' property in the server response
      if (data.message === 'login success') {
        // <Redirect to='/dashboard'/>
        history.push('/dashboard')
        console.log('yay')
      } else {
        // Handle login failure
        console.log('Login failed 2');
      }
    })
    .catch((error) => {
      // Handle login failure or errors
      console.error(error);
    });
  }
    // if (!username){
    //   return <p>Loading ...</p>
    // }

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
            <label htmlFor="username">Username:</label>
            <input
              type="username"
              className="form-control"
              id="username"
              name="username"
              placeholder="Enter Username"
              onChange={(e) => setUserName(e.target.value)}
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
