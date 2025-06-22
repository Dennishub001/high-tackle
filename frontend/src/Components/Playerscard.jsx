import React from "react";
import "../styles/PlayerCard.css";

function PlayerCard({ player }) {
  return (
    <div className="player-card">
        
      <h3>{player.member?.name}</h3>
      <p><strong>Position:</strong> {player.position}</p>
      <p><strong>Height:</strong> {player.height_cm} cm</p>
      <p><strong>Weight:</strong> {player.weight_kg} kg</p>
      <p><strong>age:</strong> {player.age}</p>
    </div>
  );
}

export default PlayerCard;
