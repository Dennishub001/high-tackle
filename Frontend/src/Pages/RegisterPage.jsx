import { useFormik } from "formik";
import Swal from "sweetalert2";
import { useNavigate } from "react-router-dom";

function RegisterPage() {
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: {
      username: "",
      phone: "",
      email: "",
      role: "",
      password: "",
    },

    onSubmit: async (values) => {
      try {
        const response = await fetch("http://localhost:5000/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(values),
        });
        const data = await response.json();
        if (!response.ok) {
          throw new Error(data.error || "An unexpected error occurred.");
        }
        Swal.fire("Success", data.message || "Registered successfully", "success");
        formik.resetForm();
        navigate("/login"); // Redirect to login page after successful registration
      } catch (error) {
        console.error("Registration Error:", error);
        Swal.fire("Error", error.message, "error");
      }
    },
  });

  return (
    <div className="register-container">
      <h2>Register</h2>
      <form onSubmit={formik.handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          onChange={formik.handleChange}
          value={formik.values.username}
        />
        <input
          type="text"
          name="phone"
          placeholder="Phone"
          onChange={formik.handleChange}
          value={formik.values.phone}
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          onChange={formik.handleChange}
          value={formik.values.email}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
        <select
          name="role"
          onChange={formik.handleChange}
          value={formik.values.role}
        >
          <option value="">Select Role</option>
          <option value="player">Player</option>
          <option value="coach">Coach</option>
          <option value="executive">Executive</option>
          <option value="member">Member</option>
        </select>
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default RegisterPage;

