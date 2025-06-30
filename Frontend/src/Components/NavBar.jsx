import { NavLink, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function NavBar() {
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem("access_token"));
  const navigate = useNavigate();

  useEffect(() => {
    const handleStorage = () => {
      setIsLoggedIn(!!localStorage.getItem("access_token"));
    };
    window.addEventListener("storage", handleStorage);
    return () => window.removeEventListener("storage", handleStorage);
  }, []);

  
  useEffect(() => {
    setIsLoggedIn(!!localStorage.getItem("access_token"));
  });

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("user");
    setIsLoggedIn(false);
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <h2 className="navbar-title">High Tackle</h2>
      <div className="nav-links">
        <NavLink to="/" className="nav-link">Home</NavLink>
        {!isLoggedIn && (
          <>
            <NavLink to="/register" className="nav-link">Register</NavLink>
            <NavLink to="/login" className="nav-link">Login</NavLink>
          </>
        )}
        {isLoggedIn && (
          <>
            <NavLink to="/members" className="nav-link">Members</NavLink>
            <NavLink to="/players" className="nav-link">Players</NavLink>
            <NavLink to="/coaches" className="nav-link">Coaches</NavLink>
            <NavLink to="/matches" className="nav-link">Matches</NavLink>
            <button className="nav-link logout-btn" onClick={handleLogout}>
              Logout
            </button>
          </>
        )}
      </div>
    </nav>
  );
}

export default NavBar;




