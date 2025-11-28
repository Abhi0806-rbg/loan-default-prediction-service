import React from "react";

export default function PredictionForm({ form, setForm, onSubmit }) {
  const handle = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  return (
    <form onSubmit={onSubmit} className="grid grid-cols-2 gap-4">
      
      {/** Input fields */}
      {[
        ["loan_amount", "Loan Amount"],
        ["income", "Income"],
        ["age", "Age"],
        ["employment_length", "Employment Length"],
        ["credit_score", "Credit Score"],
        ["dti", "Debt-to-Income"]
      ].map(([key, label]) => (
        <input
          key={key}
          name={key}
          value={form[key]}
          onChange={handle}
          placeholder={label}
          className="border p-2 rounded"
          required
        />
      ))}

      <select
        name="loan_purpose"
        className="border p-2 rounded col-span-2"
        onChange={handle}
      >
        <option value="">Select Purpose</option>
        <option>education</option>
        <option>car</option>
        <option>home</option>
        <option>business</option>
      </select>

      <button className="col-span-2 bg-blue-600 text-white py-2 rounded">
        Predict
      </button>
    </form>
  );
}
