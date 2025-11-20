import React, { useEffect, useState } from "react";
import { API_URL } from "./api";
import "./styles.css";

function App() {
  const [reviews, setReviews] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(API_URL)
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch");
        return res.json();
      })
      .then((data) => setReviews(data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>WhatsApp Product Reviews</h1>

      {error && <p style={{ color: "red" }}>Error: {error}</p>}

      {reviews.length === 0 && !error && <p>No reviews yet.</p>}

      {reviews.length > 0 && (
        <table border="1" cellPadding="10" style={{ marginTop: "20px" }}>
          <thead>
            <tr>
              <th>User</th>
              <th>Product</th>
              <th>Review</th>
              <th>Time</th>
            </tr>
          </thead>

          <tbody>
            {reviews.map((r) => (
              <tr key={r.id}>
                <td>{r.user_name || r.contact_number || "-"}</td>
                <td>{r.product_name || "-"}</td>
                <td>{r.product_review || "-"}</td>
                <td>{r.created_at ? new Date(r.created_at).toLocaleString() : "-"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
