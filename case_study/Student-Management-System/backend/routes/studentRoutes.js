const express = require("express");
const router = express.Router();
const Student = require("../models/Student");

/**
 * =========================================================================
 * EXPRESS.JS API ROUTES - STUDENT MANAGEMENT SYSTEM
 * =========================================================================
 * This module defines RESTful API routes for performing CRUD operations
 * on the MongoDB 'students' collection via Mongoose ODM.
 */

// -------------------------------------------------------------------------
// 1. CREATE: Add a new student record
// -------------------------------------------------------------------------
/**
 * @route   POST /api/students
 * @desc    Add a new student to the database
 * @access  Public
 * 
 * MongoDB Interaction:
 * 1. Express receives the JSON payload in `req.body`.
 * 2. Mongoose instantiates a new Student document: `new Student(req.body)`.
 * 3. Validation is performed against schema constraints (required, unique, enum, min/max).
 * 4. `student.save()` sends an `insertOne` command to the MongoDB Atlas `students` collection.
 * 5. MongoDB generates an immutable `_id` (BSON ObjectId) and Mongoose generates timestamps.
 * 6. Returns HTTP 201 Created with the saved student document.
 */
router.post("/", async (req, res) => {
    try {
        const student = new Student(req.body);
        const savedStudent = await student.save();

        res.status(201).json({
            success: true,
            message: "Student added successfully",
            student: savedStudent
        });
    } catch (error) {
        // Handle MongoDB duplicate key error (E11000)
        if (error.code === 11000) {
            const duplicateField = Object.keys(error.keyPattern || {})[0] || "field";
            return res.status(409).json({
                success: false,
                message: duplicateField === "rollNumber"
                    ? "A student with this roll number already exists."
                    : duplicateField === "email"
                    ? "A student with this email address is already registered."
                    : `Duplicate value detected for ${duplicateField}.`,
                error: error.message
            });
        }

        // Handle Mongoose validation errors
        if (error.name === "ValidationError") {
            const messages = Object.values(error.errors).map(val => val.message);
            return res.status(400).json({
                success: false,
                message: "Validation failed",
                errors: messages
            });
        }

        res.status(400).json({
            success: false,
            message: "Failed to add student",
            error: error.message
        });
    }
});

// -------------------------------------------------------------------------
// 2. READ: Retrieve all student records (with optional query filters)
// -------------------------------------------------------------------------
/**
 * @route   GET /api/students
 * @desc    Retrieve all students from the database with sorting and optional filtering
 * @access  Public
 * 
 * MongoDB Interaction:
 * 1. Express receives optional query parameters (e.g. department, year, search).
 * 2. Mongoose constructs a query filter object.
 * 3. `Student.find(query).sort({ createdAt: -1 })` executes a `find({})` cursor query 
 *    on the MongoDB `students` collection.
 * 4. MongoDB scans the collection (leveraging indexes where available), sorts the 
 *    documents in reverse chronological order, and returns a BSON cursor.
 * 5. Mongoose hydrates the cursor into JavaScript objects.
 * 6. Returns HTTP 200 OK with the array of student records and count.
 */
router.get("/", async (req, res) => {
    try {
        const { department, year, search } = req.query;
        let query = {};

        if (department && department !== "All") {
            query.department = department;
        }

        if (year && year !== "All") {
            query.year = Number(year);
        }

        if (search) {
            query.$or = [
                { name: { $regex: search, $options: "i" } },
                { rollNumber: { $regex: search, $options: "i" } },
                { email: { $regex: search, $options: "i" } }
            ];
        }

        const students = await Student.find(query).sort({ createdAt: -1 });

        res.status(200).json({
            success: true,
            count: students.length,
            students: students
        });
    } catch (error) {
        res.status(500).json({
            success: false,
            message: "Failed to retrieve student records",
            error: error.message
        });
    }
});

// -------------------------------------------------------------------------
// 3. READ: Retrieve a single student by MongoDB _id
// -------------------------------------------------------------------------
/**
 * @route   GET /api/students/:id
 * @desc    Retrieve single student profile by MongoDB document identifier
 * @access  Public
 * 
 * MongoDB Interaction:
 * 1. Express captures the `:id` parameter from `req.params.id`.
 * 2. `Student.findById(id)` validates and casts the string into a BSON ObjectId.
 * 3. Mongoose executes `findOne({ _id: ObjectId(id) })` against MongoDB.
 * 4. If the document is found, MongoDB returns it via the indexed primary key `_id`.
 * 5. If found, returns HTTP 200 OK; if not found, returns HTTP 404 Not Found.
 */
router.get("/:id", async (req, res) => {
    try {
        const student = await Student.findById(req.params.id);

        if (!student) {
            return res.status(404).json({
                success: false,
                message: "Student not found with the specified ID"
            });
        }

        res.status(200).json({
            success: true,
            student: student
        });
    } catch (error) {
        if (error.name === "CastError") {
            return res.status(400).json({
                success: false,
                message: "Invalid student document ID format"
            });
        }

        res.status(500).json({
            success: false,
            message: "Error fetching student details",
            error: error.message
        });
    }
});

// -------------------------------------------------------------------------
// 4. UPDATE: Modify an existing student record by MongoDB _id
// -------------------------------------------------------------------------
/**
 * @route   PUT /api/students/:id
 * @desc    Update student details using MongoDB document identifier
 * @access  Public
 * 
 * MongoDB Interaction:
 * 1. Express receives document `:id` in URL parameters and modified fields in `req.body`.
 * 2. Mongoose executes `Student.findByIdAndUpdate(id, req.body, { new: true, runValidators: true })`.
 * 3. Under the hood, MongoDB executes `findOneAndUpdate({ _id: ObjectId(id) }, { $set: req.body })`.
 * 4. The option `{ new: true }` instructs MongoDB to return the modified document rather than original.
 * 5. `{ runValidators: true }` ensures that schema validation rules are re-evaluated during the update.
 * 6. Mongoose automatically updates the `updatedAt` timestamp.
 * 7. If the update introduces a duplicate roll number or email, MongoDB rejects with code 11000, 
 *    which the route maps to HTTP 409 Conflict.
 * 8. Returns HTTP 200 OK with the updated student document.
 */
router.put("/:id", async (req, res) => {
    try {
        const updatedStudent = await Student.findByIdAndUpdate(
            req.params.id,
            req.body,
            { new: true, runValidators: true }
        );

        if (!updatedStudent) {
            return res.status(404).json({
                success: false,
                message: "Student not found with the specified ID"
            });
        }

        res.status(200).json({
            success: true,
            message: "Student updated successfully",
            student: updatedStudent
        });
    } catch (error) {
        // Handle unique constraint conflict during update
        if (error.code === 11000) {
            const duplicateField = Object.keys(error.keyPattern || {})[0] || "field";
            return res.status(409).json({
                success: false,
                message: duplicateField === "rollNumber"
                    ? "This roll number already exists for another student. Please use a unique roll number."
                    : duplicateField === "email"
                    ? "This email address is already registered to another student."
                    : `Duplicate value detected for ${duplicateField}.`,
                error: error.message
            });
        }

        // Handle validation errors during update
        if (error.name === "ValidationError") {
            const messages = Object.values(error.errors).map(val => val.message);
            return res.status(400).json({
                success: false,
                message: "Validation failed during update",
                errors: messages
            });
        }

        res.status(400).json({
            success: false,
            message: "Failed to update student",
            error: error.message
        });
    }
});

// -------------------------------------------------------------------------
// 5. DELETE: Remove a student record by MongoDB _id
// -------------------------------------------------------------------------
/**
 * @route   DELETE /api/students/:id
 * @desc    Delete student record from database by MongoDB document identifier
 * @access  Public
 * 
 * MongoDB Interaction:
 * 1. Express extracts the student `:id` from `req.params.id`.
 * 2. Mongoose executes `Student.findByIdAndDelete(req.params.id)`.
 * 3. Under the hood, MongoDB executes `findOneAndDelete({ _id: ObjectId(id) })`.
 * 4. The matching document is permanently excised from the `students` collection in MongoDB Atlas.
 * 5. If the document did not exist, returns HTTP 404 Not Found.
 * 6. If deletion is successful, returns HTTP 200 OK confirming deletion.
 */
router.delete("/:id", async (req, res) => {
    try {
        const deletedStudent = await Student.findByIdAndDelete(req.params.id);

        if (!deletedStudent) {
            return res.status(404).json({
                success: false,
                message: "Student not found with the specified ID"
            });
        }

        res.status(200).json({
            success: true,
            message: `Student record with Roll Number ${deletedStudent.rollNumber} deleted successfully`,
            deletedStudentId: req.params.id
        });
    } catch (error) {
        if (error.name === "CastError") {
            return res.status(400).json({
                success: false,
                message: "Invalid student document ID format"
            });
        }

        res.status(400).json({
            success: false,
            message: "Failed to delete student",
            error: error.message
        });
    }
});

module.exports = router;
