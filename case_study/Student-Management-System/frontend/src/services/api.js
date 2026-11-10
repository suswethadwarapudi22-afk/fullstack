import axios from "axios";

/**
 * Axios instance configured with base URL and default JSON headers.
 * Base URL dynamically points to VITE_API_URL or defaults to local server.
 */
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:5000/api",
  headers: {
    "Content-Type": "application/json",
  },
});

/**
 * Fetch all students from the database
 * Interacts with: GET /api/students
 */
export const getStudents = async (params = {}) => {
  const response = await api.get("/students", { params });
  return response.data.students;
};

/**
 * Fetch a single student by MongoDB document ID
 * Interacts with: GET /api/students/:id
 */
export const getStudentById = async (id) => {
  const response = await api.get(`/students/${id}`);
  return response.data.student;
};

/**
 * Add a new student record
 * Interacts with: POST /api/students
 */
export const addStudent = async (student) => {
  const response = await api.post("/students", student);
  return response.data;
};

/**
 * Update an existing student record by ID
 * Interacts with: PUT /api/students/:id
 */
export const updateStudent = async (id, student) => {
  const response = await api.put(`/students/${id}`, student);
  return response.data;
};

/**
 * Delete a student record by ID
 * Interacts with: DELETE /api/students/:id
 */
export const deleteStudent = async (id) => {
  const response = await api.delete(`/students/${id}`);
  return response.data;
};

export default api;
