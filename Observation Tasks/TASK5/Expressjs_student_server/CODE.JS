const express = require("express");

const app = express();

const PORT = 3000;


// Home route
app.get("/", (req, res) => {
    res.send("Welcome to the Student Server");
});


// Students route
app.get("/students", (req, res) => {

    const students = [
        {
            id: 1,
            name: "Rahul",
            course: "CSE"
        },
        {
            id: 2,
            name: "Priya",
            course: "AI & ML"
        },
        {
            id: 3,
            name: "Arjun",
            course: "ECE"
        },
        {
            id: 4,
            name: "Sneha",
            course: "CSE"
        },
        {
            id: 5,
            name: "Kiran",
            course: "IT"
        }
    ];

    res.json(students);
});


// About route
app.get("/about", (req, res) => {
    res.send(
        "Student Server is a basic Express.js application created to demonstrate routing and HTTP methods."
    );
});


// Start server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT} - CODE.JS:59`);
});