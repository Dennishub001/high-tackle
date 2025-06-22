import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./Components/NavBar";
import HomePage from "./Pages/HomePage";
import MembersPage from "./Pages/MembersPage";
import PlayersPage from "./Pages/PlayersPage";
import CoachesPage from "./Pages/CoachesPage";
import MatchesPage from "./Pages/MatchesPage";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/members" element={<MembersPage />} />
        <Route path="/players" element={<PlayersPage />} />
        <Route path="/coaches" element={<CoachesPage />} />
        <Route path="/matches" element={<MatchesPage />} />
      </Routes>
    </Router>
  );
}

export default App;
