import React from "react";

function PlayerCard({ player }) {
  return (
    <div className="player-card">
        
      <h3>{player.name}</h3>
      <p><strong>Position:</strong> {player.position}</p>
      <p><strong>Height:</strong> {player.height} cm</p>
      <p><strong>Weight:</strong> {player.weight} kg</p>
      <p><strong>age:</strong> {player.age}</p>
    </div>
  );
}

export default PlayerCard;
