import { useState } from "react";
import { useNavigate } from "react-router-dom";
// import Swal from "sweetalert2";

function Login({ setIsLoggedIn }) {
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    const isSignedUp = localStorage.getItem("isSignedUp");

    if (isSignedUp && email) {
      localStorage.setItem("isLoggedIn", true);
      setIsLoggedIn(true);

      Swal.fire({
        title: "Welcome!",
        text: "Login successful!",
        icon: "success",
        confirmButtonText: "Continue",
      }).then(() => {
        navigate("/");
      });
    } else {
      Swal.fire({
        title: "Login Failed",
        text: "Email not recognized or not signed up.",
        icon: "error",
        confirmButtonText: "Try Again",
      });
    }
  };

  return (
    <div className="signup-container">
      <h2>Login</h2>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button onClick={handleLogin} className="signup-form">
        Login
      </button>
    </div>
  );
}

export default Login;

// import { useState } from "react";
// import { useNavigate } from "react-router-dom";
// import Swal from "sweetalert2";
// import axios from "axios";

// function Login({ setIsLoggedIn }) {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState(""); // for secure auth
//   const navigate = useNavigate();

//   const handleLogin = async () => {
//     try {
//       const res = await axios.post("http://localhost:5555/login", {
//         email,
//         password,
//       });

//       const token = res.data.token;
//       localStorage.setItem("token", token);
//       setIsLoggedIn(true);

//       Swal.fire("Welcome!", "Login successful!", "success").then(() => {
//         navigate("/");
//       });
//     } catch (error) {
//       Swal.fire("Login Failed", error?.response?.data?.error || "Invalid credentials", "error");
//     }
//   };

//   return (
//     <div className="signup-container">
//       <h2>Login</h2>
//       <input
//         type="email"
//         placeholder="Email"
//         value={email}
//         onChange={(e) => setEmail(e.target.value)}
//       />
//       <input
//         type="password"
//         placeholder="Password"
//         value={password}
//         onChange={(e) => setPassword(e.target.value)}
//       />
//       <button onClick={handleLogin} className="signup-form">
//         Login
//       </button>
//     </div>
//   );
// }

// export default Login;

