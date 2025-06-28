import React, { useEffect, useState } from "react";
import MatchCard from "../Components/MatchCard";

function MatchesPage() {
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/matches")
      .then((res) => res.json())
      .then((data) => setMatches(data))
      .catch((err) => console.error("Error fetching matches:", err));
  }, []);

  return (
    <div className="matches-page">
      <h2>Match Results & Fixtures</h2>
      <div className="matches-list">
        {matches?.length > 0 ? (
          matches.map((match) => (
            <MatchCard key={match.id} match={match} />
          ))
        ) : (
          <p>No matches available.</p>
        )}
      </div>
    </div>
  );
}

export default MatchesPage;
