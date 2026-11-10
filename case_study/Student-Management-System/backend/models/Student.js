const mongoose = require("mongoose");

/**
 * Student Schema definition for MongoDB via Mongoose ODM.
 * Defines the document structure, validation rules, indexes, and timestamps.
 */
const studentSchema = new mongoose.Schema(
    {
        rollNumber: {
            type: String,
            required: [true, "Roll number is required"],
            unique: true,
            uppercase: true,
            trim: true
        },
        name: {
            type: String,
            required: [true, "Student name is required"],
            trim: true
        },
        email: {
            type: String,
            required: [true, "Email address is required"],
            unique: true,
            lowercase: true,
            trim: true,
            match: [
                /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/,
                "Please fill a valid email address"
            ]
        },
        department: {
            type: String,
            required: [true, "Department is required"],
            trim: true,
            enum: {
                values: ["CSE", "AI&DS", "CSE-AIML", "IT", "ECE", "EEE", "MECH", "CIVIL"],
                message: "{VALUE} is not a supported department"
            }
        },
        year: {
            type: Number,
            required: [true, "Academic year is required"],
            min: [1, "Academic year must be between 1 and 4"],
            max: [4, "Academic year must be between 1 and 4"]
        },
        phone: {
            type: String,
            trim: true,
            default: ""
        },
        dateOfBirth: {
            type: Date,
            default: null
        },
        gender: {
            type: String,
            enum: ["Male", "Female", "Other", "Prefer not to say", ""],
            default: ""
        },
        address: {
            type: String,
            trim: true,
            default: ""
        }
    },
    {
        timestamps: true // Automatically manages createdAt and updatedAt
    }
);

// Indexing rollNumber and email for fast lookups and unique constraint enforcement
studentSchema.index({ rollNumber: 1 });
studentSchema.index({ email: 1 });

module.exports = mongoose.model("Student", studentSchema);
