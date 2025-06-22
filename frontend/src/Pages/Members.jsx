import React, { useEffect, useState } from "react";
import MemberCard from "../Components/MemberCard";
import "../styles/MembersPage.css";

function MembersPage() {
  const [members, setMembers] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555/members")
      .then((res) => res.json())
      .then((data) => setMembers(data))
      .catch((err) => console.error("Error fetching members:", err));
  }, []);

  return (
    <div className="members-page">
      <h2>Club Members</h2>
      <div className="members-list">
        {members.map((member) => (
          <MemberCard key={member.id} member={member} />
        ))}
      </div>
    </div>
  );
}

export default MembersPage;
