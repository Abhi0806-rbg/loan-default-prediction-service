import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Predict from "./pages/Predict";

import Protected from "./components/Protected";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* Public */}
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected */}
        <Route path="/dashboard" element={
          <Protected>
            <Dashboard />
          </Protected>
        }/>

        <Route path="/predict" element={
          <Protected>
            <Predict />
          </Protected>
        }/>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
