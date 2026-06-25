import axios from "axios";

const configuredBaseURL =
  process.env.REACT_APP_API_URL ||
  "http://127.0.0.1:8001";

const normalizedConfiguredBaseURL = configuredBaseURL
  .replace(/\/api\/call-metrics\/?$/, "")
  .replace(/\/api\/?$/, "")
  .replace(/\/+$/, "");

const baseURL =
  process.env.NODE_ENV === "development"
    ? normalizedConfiguredBaseURL
    : process.env.REACT_APP_API_URL || "";

if (!baseURL) {
  console.error("Missing REACT_APP_API_URL. Add it to .env and restart the dev server.");
}

const API = axios.create({
  baseURL,
});

export default API;
