import React from "react";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Cell,
  LabelList,
} from "recharts";
import theme from "../theme";
import styles from "../styles";
import { getIntentBucket } from "../utils/intentMetrics";

function RequestPieChart({ filteredCalls = [] }) {
  const isLaptop =
    typeof window !== "undefined" && window.innerWidth <= 1440;

  const formatRequestLabel = (value) =>
    String(value || "Unknown")
      .replace(/_/g, " ")
      .replace(/\b\w/g, (char) => char.toUpperCase())
      .replace(/ /g, "\u00A0");

  const requestMap = {};

  filteredCalls.forEach((item) => {
    const request = getIntentBucket(item.primary_intent);
    requestMap[request] = (requestMap[request] || 0) + 1;
  });

  const chartData = Object.keys(requestMap)
    .map((key) => ({
      name: formatRequestLabel(key),
      value: requestMap[key],
    }))
    .sort((a, b) => b.value - a.value);

  const totalRequests = chartData.reduce(
    (sum, item) => sum + item.value,
    0
  );

  return (
    <div
      style={{
        background: theme.colors.surface,
        borderRadius: theme.radius.lg,
        padding: "20px",
        boxShadow: theme.shadows.card,
        height: "100%",
        border: `1px solid ${theme.colors.border}`,
      }}
    >
      <div style={styles.chartHeaderRow}>
        <h2
          style={{
            margin: 0,
            color: theme.colors.text,
            fontWeight: 700,
            fontSize: "18px",
          }}
        >
          Calls by Request Type
        </h2>

        <div style={styles.chartHeaderPill}>
          Total Requests: {totalRequests}
        </div>
      </div>

      <ResponsiveContainer width="100%" height={isLaptop ? 420 : 540}>
        <BarChart
          data={chartData}
          layout="vertical"
          margin={{
            top: 10,
            right: 30,
            left: isLaptop ? 100 : 112,
            bottom: 10,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="#E6EDF5" />

          <XAxis
            type="number"
            tick={{ fontSize: 12, fill: "#93A4BE" }}
            axisLine={{ stroke: "rgba(148, 163, 184, 0.2)" }}
            tickLine={{ stroke: "rgba(148, 163, 184, 0.2)" }}
          />

          <YAxis
            type="category"
            dataKey="name"
            width={isLaptop ? 104 : 110}
            tick={{
              fontSize: isLaptop ? 9 : 11,
              fill: "#10233E",
              fontWeight: 600,
            }}
            axisLine={{ stroke: "rgba(148, 163, 184, 0.2)" }}
            tickLine={false}
          />

          <Tooltip
            formatter={(value, name) => [`${value} Calls`, name]}
            contentStyle={{
              borderRadius: "12px",
              border: `1px solid ${theme.colors.border}`,
              boxShadow: theme.shadows.card,
              background: "rgba(255,255,255,0.98)",
              color: theme.colors.text,
            }}
          />

          <Bar dataKey="value" radius={[0, 10, 10, 0]}>
            <LabelList dataKey="value" position="right" />

            {chartData.map((entry, index) => (
              <Cell
                key={`cell-${entry.name}`}
                fill={
                  theme.chartColors[
                    index % theme.chartColors.length
                  ]
                }
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>

    </div>
  );
}

export default RequestPieChart;
