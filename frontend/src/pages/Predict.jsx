import React, { useState } from "react";
import Navbar from "../components/Navbar";
import PredictionForm from "../components/PredictionForm";
import API from "../services/api";

export default function Predict() {
  const [form, setForm] = useState({
    loan_amount: "",
    income: "",
    age: "",
    employment_length: "",
    credit_score: "",
    dti: "",
    loan_purpose: ""
  });

  const [result, setResult] = useState(null);

  const submit = async (e) => {
    e.preventDefault();
    const res = await API.post("/predict", form);
    setResult(res.data);
  };

  return (
    <div>
      <Navbar />

      <div className="p-6 max-w-3xl mx-auto">
        <h1 className="text-xl font-bold mb-4">Make a Prediction</h1>

        <PredictionForm form={form} setForm={setForm} onSubmit={submit} />

        {result && (
          <div className="mt-6 p-4 bg-white shadow rounded">
            <p><b>Prediction:</b> {result.prediction === 1 ? "Default Risk" : "Safe"}</p>
            <p><b>Probability:</b> {result.probability}</p>
            <p><b>Model Version:</b> {result.model_version}</p>
          </div>
        )}
      </div>
    </div>
  );
}
