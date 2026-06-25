import React from "react";
import theme from "../theme";

function DataTable({ filteredCalls }) {
  return (
    <div
      className="chartCard"
      style={{
        background: theme.colors.surface,
        borderRadius: theme.radius.md,
        boxShadow: theme.shadows.card,
        border: `1px solid ${theme.colors.border}`,
        padding: "20px",
      }}
    >
      <h2
        className="chartTitle"
        style={{ color: theme.colors.text }}
      >
        Call Records
      </h2>

      <table className="dataTable" style={{ width: "100%" }}>
        <thead>
          <tr>
            <th>Clinic</th>
            <th>Request</th>
            <th>Month</th>
          </tr>
        </thead>

        <tbody>
          {filteredCalls.map((item, index) => (
            <tr key={index}>
              <td>{item.clinic_name}</td>
              <td>{item.user_request}</td>
              <td>{item.month_name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DataTable;
