import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from "recharts";

export default function Charts({ data }) {
  return (
    <LineChart width={600} height={300} data={data} className="mt-6">
      <Line type="monotone" dataKey="probability" stroke="#2563eb" />
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="created_at" />
      <YAxis />
      <Tooltip />
    </LineChart>
  );
}
