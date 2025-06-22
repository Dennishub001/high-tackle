import React from "react";
import { NavLink } from "react-router-dom";
import "../styles/NavBar.css";

function NavBar() {
  return (
    <nav className="navbar">
      <h1 className="logo">High Tackle</h1>
      <div className="nav-links">
        <NavLink to="/" exact="true" className="nav-link">
          Home
        </NavLink>
        <NavLink to="/members" className="nav-link">
          Members
        </NavLink>
        <NavLink to="/players" className="nav-link">
          Players
        </NavLink>
        <NavLink to="/coaches" className="nav-link">
          Coaches
        </NavLink>
        <NavLink to="/matches" className="nav-link">
          Matches
        </NavLink>
      </div>
    </nav>
  );
}

export default NavBar;
