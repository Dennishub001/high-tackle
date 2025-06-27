import { useFormik } from "formik";
import Swal from "sweetalert2";
//import axios from "axios";

function RegisterPage() {
  const formik = useFormik({
    initialValues: {
      username: "",
      phone: "",
      email: "",
      role: "", // player, coach, executive, or member
      password: "",
    },

    onSubmit: async (values) => {
      try {
        const res = await axios.post("http://localhost:5555/register", values);
        Swal.fire("Success", res.data.message, "success");
        formik.resetForm();
      } catch (error) {
        Swal.fire("Error", error.response.data.error, "error");
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
