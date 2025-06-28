import React, { useEffect, useState } from "react";
import CoachCard from "../Components/CoachCard";

function CoachesPage() {
  const [coaches, setCoaches] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/coaches")
      .then((res) => res.json())
      .then((data) => setCoaches(data))
      .catch((err) => console.error("Error fetching coaches:", err));
  }, []);

  return (
    <div className="coaches-page">
      <h2>Our Coaches</h2>
      <div className="coaches-list">
        {coaches.map((coach) => (
          <CoachCard key={coach.id} coach={coach} />
        ))}
      </div>
    </div>
  );
}

export default CoachesPage;



