import React from "react";
import "../App.css"; // Make sure your styles include `.match-card`

function MatchCard({ match }) {
  return (
    <div className="match-card">
      <h3> Match Details</h3>
      <p><strong>Date:</strong> {match.date}</p>
      <p><strong>Time:</strong> {match.time}</p>
      <p><strong>Venue:</strong> {match.venue}</p>
      <p><strong>Status:</strong> {match.status}</p>
      {match.status === "completed" && (
        <p><strong>Score:</strong> {match.score || "N/A"}</p>
      )}
    </div>
  );
}

export default MatchCard;
