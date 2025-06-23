// import { Link } from "react-router-dom";

// function NavBar() {
//   return (
//     <nav>
//       <Link to="/">Home</Link> |{" "}
//       <Link to="/members">Members</Link> |{" "}
//       <Link to="/players">Players</Link> |{" "}
//       <Link to="/coaches">Coaches</Link> |{" "}
//       <Link to="/matches">Matches</Link> |{" "}
//       <Link to="/register">Register</Link> |{" "}
//       <Link to="/login">Login</Link>
//     </nav>
//   );
// }

// export default NavBar;

import { NavLink } from "react-router-dom";
//import "./NavBar.css"; // Optional: for styling

function NavBar() {
  return (
    <nav className="navbar">
      <h2 className="navbar-title">High Tackle Rugby</h2>
      <div className="nav-links">
        <NavLink to="/" className="nav-link">Home</NavLink>
        <NavLink to="/members" className="nav-link">Members</NavLink>
        <NavLink to="/players" className="nav-link">Players</NavLink>
        <NavLink to="/coaches" className="nav-link">Coaches</NavLink>
        <NavLink to="/matches" className="nav-link">Matches</NavLink>
        <NavLink to="/register" className="nav-link">Register</NavLink>
        <NavLink to="/login" className="nav-link">Login</NavLink>
      </div>
    </nav>
  );
}

export default NavBar;

