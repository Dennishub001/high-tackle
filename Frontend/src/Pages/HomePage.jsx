import React from "react";

function HomePage() {
  return (
    <div className="home-container">
      <h1>Welcome to High Tackle</h1>
      <p>Your trusted rugby club management app for grassroots and community teams.</p>

      <section className="home-intro">
        <h2>What You Can Do:</h2>
        <ul>
          <li>View team members and player profiles</li>
          <li>Learn more about our coaches</li>
          <li>Explore past and upcoming matches</li>
          <li> Check match performance and results</li>
        </ul>
      </section>

      <p className="footer-note">Navigate using the menu above to get started.</p>
    </div>
  );
}

export default HomePage;
