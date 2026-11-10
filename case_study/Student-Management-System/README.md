# STUDIA – Student Management System

A full-stack web application designed to manage student information through a centralized and user-friendly institutional dashboard, built with React, Node.js, Express.js, and MongoDB Atlas.

---

## Project Overview

**STUDIA – Student Management System** is developed as part of the Full-Stack Web Development Case Study (Unit V: MongoDB, Database Operations, and Cloud Deployment).

### Core Problem & Topic
> **Topic:** Consider a Student Management System in which students can be added, viewed, updated, and deleted. Design the required Express.js API routes and explain how each route interacts with MongoDB to perform the corresponding operation.

The application eliminates paper-based student record tracking by offering an intuitive web interface backed by a robust RESTful API and cloud-hosted MongoDB Atlas database. It supports full CRUD operations, advanced multi-criteria searching and filtering, individual profile views, data validation, conflict management, and cloud deployment.

---

## Live Deployment

The system is architected for cloud deployment across Vercel, Render, and MongoDB Atlas:

| Component | Platform | Role / Deployment |
|---|---|---|
| **Frontend** | Vercel | Production React SPA build served via global CDN |
| **Backend** | Render | Node.js / Express.js REST API Web Service |
| **API Endpoints** | Render | `https://studia-backend-orll.onrender.com/api/students` |
| **Database** | MongoDB Atlas | Cloud-hosted document database cluster (`test.students`) |

---

## Technology Stack

### Frontend
- **React.js (v18.3)** – Component-based reactive user interface.
- **Vite** – Next-generation build tool and local development server.
- **Axios** – Promise-based HTTP client for asynchronous REST API communication.
- **Lucide React** – Clean, modern UI iconography.
- **CSS3** – Responsive styling with CSS variables, custom modals, and responsive grid layouts.

### Backend
- **Node.js** – Server-side asynchronous JavaScript runtime environment.
- **Express.js (v4.19)** – Minimalist, robust web application framework for API routing and middleware.
- **Mongoose ODM (v8.4)** – Object Data Modeling library for schema validation, querying, and document lifecycle hooks.
- **CORS & Dotenv** – Cross-origin resource sharing and environment-variable security.

### Database
- **MongoDB Atlas** – Fully-managed multi-cloud document database storing BSON records.

---

## System Architecture

STUDIA follows a clean **Three-Layer (3-Tier) Web Architecture**:

```text
                     +---------------------------------------+
                     |         CLIENT / BROWSER              |
                     +---------------------------------------+
                                         |
                                         v
                     +---------------------------------------+
                     |         REACT FRONTEND (Vite)         |
                     |  - Dashboard Summary & Stats          |
                     |  - Student Directory & Search         |
                     |  - Add / Edit / Delete Modals         |
                     |  - Student Profile View               |
                     +---------------------------------------+
                                         |
                                         | HTTPS / Axios REST Requests
                                         | (JSON Payloads)
                                         v
                     +---------------------------------------+
                     |       EXPRESS.JS REST API BACKEND     |
                     |  - CORS & JSON Body Parsing           |
                     |  - RESTful Route Handlers             |
                     |  - Schema Validation & Conflict Guard |
                     |  - HTTP Status Code Management        |
                     +---------------------------------------+
                                         |
                                         | Mongoose ODM
                                         | (BSON ObjectIds, Queries)
                                         v
                     +---------------------------------------+
                     |         MONGODB ATLAS DATABASE        |
                     |  - Cluster: Cloud-hosted MongoDB      |
                     |  - Database: `test`                   |
                     |  - Collection: `students`             |
                     |  - Unique Indexes on rollNumber/email |
                     +---------------------------------------+
```

---

## MongoDB Document Model

Student records are stored as BSON documents inside the `students` collection in MongoDB Atlas.

### Mongoose Schema (`models/Student.js`)

```javascript
const mongoose = require("mongoose");

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
      trim: true
    },
    department: {
      type: String,
      required: [true, "Department is required"],
      enum: ["CSE", "AI&DS", "CSE-AIML", "IT", "ECE", "EEE", "MECH", "CIVIL"],
      trim: true
    },
    year: {
      type: Number,
      required: [true, "Academic year is required"],
      min: 1,
      max: 4
    },
    phone: { type: String, trim: true, default: "" },
    dateOfBirth: { type: Date, default: null },
    gender: { type: String, default: "" },
    address: { type: String, trim: true, default: "" }
  },
  {
    timestamps: true // Automatically manages createdAt and updatedAt
  }
);

studentSchema.index({ rollNumber: 1 });
studentSchema.index({ email: 1 });

module.exports = mongoose.model("Student", studentSchema);
```

### Stored Document Representation (BSON / JSON)

```json
{
  "_id": { "$oid": "6730a1b2c3d4e5f6a7b8c9d0" },
  "rollNumber": "A24126552079",
  "name": "Suswetha Dwarapudi",
  "email": "suswetha.dwarapudi@example.com",
  "department": "CSE",
  "year": 3,
  "phone": "+91 9876543210",
  "gender": "Female",
  "createdAt": { "$date": "2026-11-10T10:15:30.000Z" },
  "updatedAt": { "$date": "2026-11-10T10:15:30.000Z" },
  "__v": 0
}
```

---

## Detailed Express.js API Routes & MongoDB Interaction

The REST API implements standard HTTP methods mapping directly to MongoDB operations:

| HTTP Method | Route Path | Operation | Mongoose Method | MongoDB Shell Command | HTTP Status |
|---|---|---|---|---|---|
| **POST** | `/api/students` | Add new student | `new Student(data).save()` | `db.students.insertOne(...)` | `201 Created` / `400` / `409` |
| **GET** | `/api/students` | View all students | `Student.find().sort(...)` | `db.students.find({})` | `200 OK` / `500` |
| **GET** | `/api/students/:id` | View single student | `Student.findById(id)` | `db.students.findOne({_id})` | `200 OK` / `404` |
| **PUT** | `/api/students/:id` | Update student | `Student.findByIdAndUpdate()` | `db.students.findOneAndUpdate(...)` | `200 OK` / `404` / `409` |
| **DELETE** | `/api/students/:id` | Delete student | `Student.findByIdAndDelete()` | `db.students.findOneAndDelete(...)` | `200 OK` / `404` |

### 1. Add Student (`POST /api/students`)
- **Express Handling:** Extracts student JSON from `req.body`.
- **MongoDB Interaction:** Mongoose initializes `new Student(req.body)`, verifies constraints, and executes `.save()`, which sends an `insertOne` command to MongoDB Atlas. MongoDB creates an immutable `_id` and Mongoose attaches `createdAt` and `updatedAt`.
- **Conflict Handling:** If the roll number or email is already in the database, MongoDB returns error code `11000` (duplicate key), which the route converts to `409 Conflict`.
- **Response:** `201 Created` with the newly created document.

### 2. View All Students (`GET /api/students`)
- **Express Handling:** Reads optional query filters (`department`, `year`, `search`) from `req.query`.
- **MongoDB Interaction:** Calls `Student.find(query).sort({ createdAt: -1 })`. MongoDB issues a `find` query to the collection, applies any regex search on `name`/`rollNumber`/`email`, sorts records in descending order of creation, and returns an array of documents.
- **Response:** `200 OK` with JSON containing `count` and `students` array.

### 3. View Single Student Profile (`GET /api/students/:id`)
- **Express Handling:** Extracts document ID from `req.params.id`.
- **MongoDB Interaction:** Calls `Student.findById(id)`, casting the string into a BSON `ObjectId` and performing an indexed `findOne({ _id: ObjectId(id) })` lookup.
- **Response:** `200 OK` with student object, or `404 Not Found` if the student does not exist.

### 4. Update Student (`PUT /api/students/:id`)
- **Express Handling:** Receives document ID via route parameter and updated fields in `req.body`.
- **MongoDB Interaction:** Calls `Student.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true })`. MongoDB translates this to `findOneAndUpdate({ _id: ObjectId(id) }, { $set: updateFields })`.
- **Key Options:** `{ new: true }` ensures MongoDB returns the updated record rather than the stale record; `{ runValidators: true }` re-executes Mongoose schema validation.
- **Conflict Protection:** Handles duplicate-key errors (`code: 11000`) and returns `409 Conflict`.
- **Response:** `200 OK` with the updated student record.

### 5. Delete Student (`DELETE /api/students/:id`)
- **Express Handling:** Extracts student ID from `req.params.id`.
- **MongoDB Interaction:** Calls `Student.findByIdAndDelete(req.params.id)`. MongoDB executes `findOneAndDelete({ _id: ObjectId(id) })`, removing the document permanently from the collection.
- **Response:** `200 OK` with success confirmation, or `404 Not Found`.

---

## Case Study: Debugging Student Records Not Displaying After Updates

### Problem Statement
A deployed Student Management System successfully adds new student records but fails to display updated student records in the UI after editing.

### Root Cause Analysis & Verification

| Layer | Potential Cause | Verification & Systematic Fix |
|---|---|---|
| **Frontend State** | React state not re-fetched after PUT request | Await the update API call, then trigger `fetchStudents()` to pull the fresh array from the server. |
| **Asynchronous Race** | Re-fetch called before MongoDB finishes write | Ensure `await updateStudent(id, form)` completes before calling `await getStudents()`. |
| **API Path & Method** | Incorrect URL or HTTP method in Axios service | Inspect Developer Tools Network tab; verify `PUT /api/students/:id` with HTTP 200/204 response. |
| **Document Identifier** | Backend updating wrong ID or using `rollNumber` instead of `_id` | Ensure route uses `req.params.id` matching `student._id` from MongoDB. |
| **Mongoose Return Option** | Missing `{ new: true }` in `findByIdAndUpdate` | Add `{ new: true }` so Mongoose returns the modified document instead of original pre-update document. |
| **Database Mismatch** | Frontend connects to dev server, while backend writes to Atlas cluster | Check `VITE_API_URL` and `MONGO_URI` environment variables across environments. |
| **CORS / Preflight** | Browser blocking PUT requests due to CORS headers | Ensure Express has `app.use(cors())` enabled for all HTTP verbs including PUT. |
| **Browser Caching** | Browser caching GET response | Verify API responses include appropriate headers (`no-cache`) or use unique timestamps. |

---

## Local Installation & Setup

### Prerequisites
- Node.js (v18+) & npm
- Git
- MongoDB Atlas cluster or local MongoDB instance

### 1. Backend Setup
```bash
cd backend
npm install
```
Create a `.env` file in `backend/`:
```env
MONGO_URI=your_mongodb_atlas_connection_string
PORT=5000
NODE_ENV=development
```
Start the backend server:
```bash
npm run dev
# Server will run at http://localhost:5000
```

### 2. Frontend Setup
Open a separate terminal:
```bash
cd frontend
npm install
```
Create a `.env` file in `frontend/`:
```env
VITE_API_URL=http://localhost:5000/api
```
Start the Vite development server:
```bash
npm run dev
# Application will run at http://localhost:5173
```

---

## Test Cases & Validation Matrix

| Test ID | Test Scenario | Expected Outcome | Status |
|---|---|---|---|
| **TC-01** | Open Dashboard | Dashboard loads with metrics, student count, and department breakdown | Passed |
| **TC-02** | View All Students | Students collection fetched and displayed in sortable directory table | Passed |
| **TC-03** | Add New Student | Valid form payload saved in MongoDB; refreshed list shows new student | Passed |
| **TC-04** | Duplicate Roll Number | Backend detects unique index violation; returns HTTP 409 Conflict | Passed |
| **TC-05** | View Student Profile | Detailed student information and timestamps retrieved by MongoDB `_id` | Passed |
| **TC-06** | Update Student Details | Record updated via PUT request; UI reflects updated values immediately | Passed |
| **TC-07** | Delete Student Record | Confirmation modal shown; record excised from MongoDB on confirm | Passed |
| **TC-08** | Search & Filter | Dynamic filter by department and search by name/rollNo/email | Passed |
| **TC-09** | Cloud Deployment | Backend live on Render, Frontend ready on Vercel, DB on Atlas | Passed |

---

## Project Metadata

- **Project:** STUDIA – Student Management System
- **Course:** Full-Stack Web Development (23CM4121)
- **Unit:** Unit V – MongoDB and Deploying Applications
- **Student Name:** Suswetha Dwarapudi
- **Registration Number:** A24126552079
- **Institution:** Anil Neerukonda Institute of Technology & Sciences (Autonomous), Visakhapatnam
- **Faculty / Guide:** P. Santosh Kumar
- **Academic Year:** 2026–27
