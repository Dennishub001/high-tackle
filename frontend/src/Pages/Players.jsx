import React, { useEffect, useState } from "react";
import PlayerCard from "../Components/PlayerCard";
import "../styles/PlayersPage.css";

function PlayersPage() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555/players")
      .then((res) => res.json())
      .then((data) => setPlayers(data))
      .catch((err) => console.error("Error fetching players:", err));
  }, []);

  return (
    <div className="players-page">
      <h2>Team Players</h2>
      <div className="players-list">
        {players.map((player) => (
          <PlayerCard key={player.id} player={player} />
        ))}
      </div>
    </div>
  );
}

export default PlayersPage;
