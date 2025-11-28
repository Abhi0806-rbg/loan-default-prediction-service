import React, { useState } from "react";
import API from "../services/api";
import { Link, useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const nav = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    try {
      const res = await API.post("/auth/login", { email, password });
      localStorage.setItem("token", res.data.access_token);
      nav("/dashboard");
    } catch (err) {
      alert("Invalid Credentials");
    }
  };

  return (
    <div className="h-screen flex justify-center items-center">
      <form onSubmit={submit} className="bg-white p-6 shadow rounded w-96">
        <h1 className="font-bold text-xl mb-4 text-center">Login</h1>

        <input className="border p-2 w-full mb-3" placeholder="Email" type="email"
          onChange={(e) => setEmail(e.target.value)} />

        <input className="border p-2 w-full mb-4" placeholder="Password" type="password"
          onChange={(e) => setPassword(e.target.value)} />

        <button className="bg-blue-600 text-white w-full py-2 rounded">Login</button>
        <p className="text-sm text-center mt-3">
          No account? <Link className="text-blue-500" to="/register">Register</Link>
        </p>
      </form>
    </div>
  );
}
