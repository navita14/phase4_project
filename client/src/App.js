import { createBrowserRouter, createRoutesFromElements, RouterProvider } from 'react-router-dom';
import { Route } from 'react-router-dom';
import PostPage from "./Components/PostPage"; 
import Login from "./Components/Login"; 
import SignUp from "./Components/Signup"; 
import Logout from "./Components/Logout"; 
import Dashboard from './Components/Dashboard';

const router = createBrowserRouter(
  createRoutesFromElements(
      <Route>
          <Route exact path="/" element={<Dashboard />} />
          <Route path="/posts" element={<PostPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/signup" element={<SignUp />} />
      </Route>
  )
);

export default function App() {
return (
    <>
      <RouterProvider router={router} />
    </>
);
}