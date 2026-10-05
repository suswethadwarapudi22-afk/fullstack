// MongoDB Student Management System

// Select database
use collegeDB;

// Create collection if it does not exist
if (!db.getCollectionNames().includes("students")) {
    db.createCollection("students");
}

// Display all students
db.students.find().pretty();

// Display students from CSE-AIML
db.students.find({ branch: "CSE-AIML" }).pretty();

// Students scoring more than 75
db.students.find({ marks: { $gt: 75 } }).pretty();

// Search using rollNo
db.students.find({ rollNo: "23CM001" }).pretty();

// Students in 3rd year
db.students.find({ year: 3 }).pretty();

// Students scoring above 80
db.students.find({ marks: { $gt: 80 } }).pretty();

// Students scoring below 50
db.students.find({ marks: { $lt: 50 } }).pretty();

// Update marks
db.students.updateOne(
    { rollNo: "23CM001" },
    { $set: { marks: 90 } }
);

// Update email
db.students.updateOne(
    { rollNo: "23CM001" },
    { $set: { email: "ravi.kumar@example.com" } }
);

// Sort students by marks
db.students.find().sort({ marks: -1 }).pretty();

// Create index
db.students.createIndex({ rollNo: 1 });

// Display indexes
db.students.getIndexes();

// Highest-scoring student
db.students.find().sort({ marks: -1 }).limit(1).pretty();

// Demonstrate index usage
db.students.find(
    { rollNo: "23CM001" }
).explain("executionStats");