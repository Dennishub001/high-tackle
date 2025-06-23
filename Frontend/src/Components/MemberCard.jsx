import React from "react";
import "../App.css"; // Assuming you have a CSS file for styling
function MemberCard({ member }) {
  return (

    <div className="member-card">
      
      <h3>{member.name}</h3>
      <p><strong>Email:</strong> {member.email}</p>
      <p><strong>Phone:</strong> {member.phone}</p>
      <p><strong>Role:</strong> {member.role}</p>
      <p><strong>Status:</strong> {member.status}</p>
    </div>
  );
}

export default MemberCard;