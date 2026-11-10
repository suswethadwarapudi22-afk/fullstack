const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
require("dotenv").config();

const studentRoutes = require("./routes/studentRoutes");

const app = express();

// ==========================================
// Middleware Configuration
// ==========================================
// Enable Cross-Origin Resource Sharing (CORS) for frontend client
app.use(cors());

// Parse incoming JSON request bodies
app.use(express.json());

// Parse URL-encoded bodies
app.use(express.urlencoded({ extended: true }));

// Request logging middleware
app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
    next();
});

// ==========================================
// Database Connection (MongoDB Atlas)
// ==========================================
const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017/studentDB";

mongoose.connect(MONGO_URI)
    .then(() => {
        console.log("==========================================");
        console.log("MongoDB Atlas connected successfully!");
        console.log(`Database: ${mongoose.connection.name}`);
        console.log("==========================================");
    })
    .catch((error) => {
        console.error("MongoDB Atlas connection error:", error.message);
    });

// ==========================================
// API Routes
// ==========================================
// Root endpoint
app.get("/", (req, res) => {
    res.status(200).json({
        message: "STUDIA - Student Management System REST API is operational!",
        author: "Suswetha Dwarapudi (A24126552079)",
        documentation: "/api/students",
        status: "Active"
    });
});

// Health check endpoint
app.get("/api/health", (req, res) => {
    res.status(200).json({
        status: "OK",
        uptime: process.uptime(),
        database: mongoose.connection.readyState === 1 ? "Connected" : "Disconnected",
        timestamp: new Date().toISOString()
    });
});

// Mount Student CRUD API routes
app.use("/api/students", studentRoutes);

// 404 Route Not Found handler
app.use((req, res) => {
    res.status(404).json({
        success: false,
        message: `Endpoint ${req.originalUrl} not found on this server.`
    });
});

// Global Error Handler
app.use((err, req, res, next) => {
    console.error("Unhandled Server Error:", err.stack);
    res.status(500).json({
        success: false,
        message: "Internal server error occurred",
        error: process.env.NODE_ENV === "production" ? "Internal error" : err.message
    });
});

// ==========================================
// Server Listener
// ==========================================
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
    console.log(`API URL: http://localhost:${PORT}/api/students`);
});
