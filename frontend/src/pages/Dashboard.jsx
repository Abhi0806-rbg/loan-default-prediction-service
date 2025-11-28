import React, { useEffect, useState } from "react";
import API from "../services/api";
import Navbar from "../components/Navbar";
import Charts from "../components/Charts";

export default function Dashboard() {
  const [predictions, setPredictions] = useState([]);

  useEffect(() => {
    API.get("/predict/history")
      .then(res => setPredictions(res.data))
      .catch(() => {});
  }, []);

  return (
    <div>
      <Navbar />
      <div className="p-6">
        <h1 className="text-2xl font-bold">Dashboard</h1>

        <Charts data={predictions} />
      </div>
    </div>
  );
}
