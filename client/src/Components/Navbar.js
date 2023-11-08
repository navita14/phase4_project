import { NavLink } from "react-router-dom";

export default function Navbar() {
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
        <div
          className="justify-content-end collapse navbar-collapse"
          id="navbar"
        >
          <div className="navbar-nav">  
            <NavLink className="nav-item nav-link" to="/logout">
              Logout
            </NavLink>
          </div>
        </div>
      </nav>

    );
}