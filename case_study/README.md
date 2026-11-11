# Unit V Case Study: EduSphere – Student Management System

### Full-Stack Web Development (Course Code: 23CM4121)
**Anil Neerukonda Institute of Technology & Sciences (Autonomous)**  
*Department of Computer Science & Engineering / Machine Learning*  
**Academic Year:** 2026–27 | **Semester:** 3rd Year – 1st Semester  
**Student Name:** D. Suswetha | **Registration Number:** A24126552079  
**Faculty / Guide:** P. Santosh Kumar  

---

## 📌 Case Study Topic & Problem Statement

> **Consider a Student Management System in which students can be added, viewed, updated and deleted. Design the required Express.js API routes and explain how each route interacts with MongoDB to perform the corresponding operation.**

This repository contains the complete worked solution, full-stack source code, cloud deployment configuration, test case validation, and academic case-study documentation for **EduSphere**, an institutional Student Management System.

---

## 🚀 Live Deployment & Public Links

| Platform | Deployment Role | Public Access URL |
|---|---|---|
| **Frontend** | Vercel SPA Deployment | [https://edusphere-suswetha.vercel.app](https://edusphere-suswetha.vercel.app) |
| **Backend** | Render Node.js Web Service | [https://edusphere-backend-suswetha.onrender.com](https://edusphere-backend-suswetha.onrender.com) |
| **REST API** | Live Students Endpoint | [https://edusphere-backend-suswetha.onrender.com/api/students](https://edusphere-backend-suswetha.onrender.com/api/students) |
| **Database** | MongoDB Atlas Cluster | Cloud-hosted MongoDB (`test.students`) |

---

## 📂 Repository Structure

```text
case_study/
├── A24126552079_FSWD_CASESTUDY_DOCUMENTATION.pdf   # Complete 18-page Academic Case Study Report (PDF)
├── A24126552079_FSWD_CASESTUDY_DOCUMENTATION.docx  # Formatted Word Document
├── README.md                                       # Case study overview and topic guide
├── output_screenshots/                             # Execution evidence & deployment screenshots
│   ├── 01_dashboard.png                            # Figure 1: Dashboard overview
│   ├── 02_dashboard_2.png                          # Figure 2: Student directory table
│   ├── 03_add_new_student.png                      # Figure 3: Add student modal form
│   ├── 04_view_student.png                         # Figure 4: Student profile viewer
│   ├── 05_edit_student.png                         # Figure 5: Edit student form
│   ├── 06_delete_student.png                       # Figure 6: Delete confirmation guard
│   ├── 07_mongodb_atlas.png                        # Figure 7: MongoDB Atlas collection view
│   ├── 08_render_backend.png                       # Figure 8: Render backend Live status
│   └── 09_vercel_frontend.png                      # Figure 9: Vercel frontend Ready status
├── Student-Management-System/                      # Full-Stack Application Source Code
│   ├── backend/                                    # Express.js REST API + Mongoose
│   │   ├── models/Student.js                       # Mongoose Schema & Indexes
│   │   ├── routes/studentRoutes.js                 # CRUD API Routes & MongoDB Interaction
│   │   ├── server.js                               # Express Server & DB Connection
│   │   ├── package.json                            # Backend dependencies
│   │   ├── .env.example                            # Backend environment template
│   │   └── .gitignore
│   ├── frontend/                                   # React 18 + Vite SPA Client
│   │   ├── src/
│   │   │   ├── components/StudentProfile.jsx       # Student profile view component
│   │   │   ├── components/StudentProfile.css
│   │   │   ├── services/api.js                     # Axios HTTP REST client
│   │   │   ├── App.jsx                             # Main responsive dashboard UI
│   │   │   ├── App.css                             # Custom responsive CSS
│   │   │   ├── index.css
│   │   │   └── main.jsx
│   │   ├── index.html
│   │   ├── vite.config.js
│   │   ├── package.json                            # Frontend dependencies
│   │   ├── .env.example                            # Frontend environment template
│   │   └── .gitignore
│   └── README.md                                   # Comprehensive application documentation
└── scripts/
    ├── generate_docx.py                            # Script generating the documentation DOCX
    └── generate_pdf.py                             # Script generating the documentation PDF
```

---

## 🛠️ Express.js API Routes & MongoDB Interaction

The application implements RESTful routes that translate HTTP client actions into optimized MongoDB database commands via Mongoose ODM:

### 1. Add Student (`POST /api/students`)
- **HTTP Method:** `POST`
- **Route Endpoint:** `/api/students`
- **Mongoose Execution:** `const student = new Student(req.body); await student.save();`
- **MongoDB Under-the-Hood Command:** `db.students.insertOne(...)`
- **MongoDB Interaction:**
  1. Validates required schema fields (`rollNumber`, `name`, `email`, `department`, `year`).
  2. Issues `insertOne` command to MongoDB Atlas.
  3. MongoDB generates immutable 12-byte BSON `_id` ObjectId and Mongoose attaches `createdAt` and `updatedAt`.
  4. Intercepts MongoDB duplicate key conflict (`code: 11000`) and returns `409 Conflict`.
  5. Returns `201 Created` with saved student JSON.

### 2. View All Students (`GET /api/students`)
- **HTTP Method:** `GET`
- **Route Endpoint:** `/api/students`
- **Mongoose Execution:** `await Student.find(query).sort({ createdAt: -1 });`
- **MongoDB Under-the-Hood Command:** `db.students.find({}).sort({ createdAt: -1 })`
- **MongoDB Interaction:**
  1. Inspects query string parameters for optional filtering (e.g. `department`, `year`, `search`).
  2. MongoDB scans the `students` collection, utilizing indexes for fast sorting.
  3. Hydrates matching BSON documents into JavaScript objects.
  4. Returns `200 OK` with JSON `{ count: N, students: [...] }`.

### 3. View Single Student (`GET /api/students/:id`)
- **HTTP Method:** `GET`
- **Route Endpoint:** `/api/students/:id`
- **Mongoose Execution:** `await Student.findById(req.params.id);`
- **MongoDB Under-the-Hood Command:** `db.students.findOne({ _id: ObjectId(id) })`
- **MongoDB Interaction:**
  1. Casts URL parameter `:id` into a BSON `ObjectId`.
  2. Performs an O(1) primary key index search on `_id`.
  3. Returns `200 OK` with the student profile if found, or `404 Not Found`.

### 4. Update Student (`PUT /api/students/:id`)
- **HTTP Method:** `PUT`
- **Route Endpoint:** `/api/students/:id`
- **Mongoose Execution:** `await Student.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });`
- **MongoDB Under-the-Hood Command:** `db.students.findOneAndUpdate({ _id: ObjectId(id) }, { $set: updateFields }, { returnDocument: "after" })`
- **MongoDB Interaction:**
  1. Finds the document by `_id` and applies atomic `$set` updates.
  2. The option `{ new: true }` instructs MongoDB to return the modified document rather than original.
  3. `{ runValidators: true }` re-executes Mongoose schema validation constraints.
  4. Mongoose automatically updates the `updatedAt` timestamp.
  5. Catches duplicate key conflicts (`code: 11000`) and returns `409 Conflict`.
  6. Returns `200 OK` with the updated student record.

### 5. Delete Student (`DELETE /api/students/:id`)
- **HTTP Method:** `DELETE`
- **Route Endpoint:** `/api/students/:id`
- **Mongoose Execution:** `await Student.findByIdAndDelete(req.params.id);`
- **MongoDB Under-the-Hood Command:** `db.students.findOneAndDelete({ _id: ObjectId(id) })`
- **MongoDB Interaction:**
  1. Locates document by `_id` and permanently removes it from collection storage.
  2. Returns `200 OK` with confirmation message or `404 Not Found`.

---

## 🔍 Case Study Debugging Procedure

**Problem:** *Student records are successfully added to MongoDB Atlas, but after modifying a record, the user interface fails to display updated data.*

**Systematic Debugging Workflow:**
1. **Network Layer:** Open Chrome DevTools -> Network tab. Submit the update form. Verify that the request uses `PUT` with the correct document ID (`/api/students/:id`) and payload.
2. **Backend & Mongoose Verification:** Confirm that `findByIdAndUpdate` uses `{ new: true }`. Without `{ new: true }`, Mongoose returns the stale, un-updated document.
3. **Async Sequencing:** In React, ensure `await updateStudent(id, form)` finishes completely before calling `await fetchStudents()`. Calling re-fetch prematurely causes a race condition.
4. **State Management:** Ensure the React save handler receives the new student array from the server and replaces `students` state using `setStudents(freshData)`.
5. **Database Verification:** Check MongoDB Atlas Data Explorer directly to verify that the field value and `updatedAt` timestamp have changed in `test.students`.

---

## 🏃 Running the Application Locally

### 1. Start Backend:
```bash
cd Student-Management-System/backend
npm install
# Configure MONGO_URI in .env
npm run dev
# Server listening at http://localhost:5000
```

### 2. Start Frontend:
```bash
cd Student-Management-System/frontend
npm install
# Configure VITE_API_URL in .env
npm run dev
# Vite client running at http://localhost:5173
```
