import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import NavBar from "./Components/NavBar";
import HomePage from "./Pages/HomePage";
import MembersPage from "./Pages/MembersPage";
import PlayersPage from "./Pages/PlayersPage";
import CoachesPage from "./Pages/CoachesPage";
import MatchesPage from "./Pages/MatchesPage";
import PlayerCard from "./Components/PlayerCard";
import RegisterPage from "./Pages/RegisterPage";
import LoginPage from "./Pages/LoginPage";

// Protected Route wrapper
function ProtectedRoute({ children }) {
  const token = localStorage.getItem("access_token");
  return token ? children : <Navigate to="/login" replace />;
}

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        {/* Public Routes */}
        <Route path="/" element={<HomePage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />

        {/* Protected Routes */}
        <Route
          path="/members"
          element={
            <ProtectedRoute>
              <MembersPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/players"
          element={
            <ProtectedRoute>
              <PlayersPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/players/:id"
          element={
            <ProtectedRoute>
              <PlayerCard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/coaches"
          element={
            <ProtectedRoute>
              <CoachesPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/matches"
          element={
            <ProtectedRoute>
              <MatchesPage />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;