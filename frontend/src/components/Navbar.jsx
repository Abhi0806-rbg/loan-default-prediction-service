import React from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <nav className="bg-white shadow px-6 py-4 flex justify-between">
      <h1 className="text-xl font-bold">Lone-1</h1>

      <div className="flex gap-4">
        <Link to="/dashboard" className="hover:text-blue-500">Dashboard</Link>
        <Link to="/predict" className="hover:text-blue-500">Predict</Link>
        <button
          onClick={logout}
          className="text-red-600 font-semibold hover:underline"
        >
          Logout
        </button>
      </div>
    </nav>
  );
}
