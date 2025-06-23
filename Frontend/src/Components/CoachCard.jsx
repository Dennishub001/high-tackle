import React from "react";

function CoachCard({ coach }) {
  return (
    <div className="coach-card">
      <h3>{coach.member?.name}</h3>
      <p><strong>Specialty:</strong> {coach.specialty}</p>
      <p><strong>Experience:</strong> {coach.experience_years} years</p>
      <p><strong>Certification:</strong> {coach.certification}</p>
    </div>
  );
}

export default CoachCard;
