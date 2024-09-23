import axios from "axios";
import camelcaseKeys from "camelcase-keys";

const API_URL =
  `${process.env.NEXT_PUBLIC_API_PROTOCOL}://${process.env.NEXT_PUBLIC_API_HOST}:${process.env.NEXT_PUBLIC_API_PORT}/api` ||
  "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_URL,
  timeout: 1000,
  headers: { "Content-Type": "application/json" },
});

api.interceptors.request.use(
  function (config) {
    const token = localStorage.getItem("authToken");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  function (response) {
    if (response.data && typeof response.data === "object") {
      response.data = camelcaseKeys(response.data, { deep: true });
    }
    return response;
  },
  function (error) {
    return Promise.reject(error);
  }
);

export default api;
