import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def build_docx(filename="case_study/A24126552079_FSWD_CASESTUDY_DOCUMENTATION.docx"):
    doc = docx.Document()
    
    # Page setup
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
        # Header & Footer
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("FULL-STACK WEB DEVELOPMENT | UNIT V CASE STUDY")
        hrun.font.name = "Arial"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(120, 120, 120)
        
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("EduSphere – Student Management System • ANITS • Registration No: A24126552079")
        frun.font.name = "Arial"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(120, 120, 120)

    # Styles
    PRIMARY = RGBColor(27, 54, 93)     # Navy Blue
    SECONDARY = RGBColor(41, 128, 185) # Accent Blue
    DARK_TEXT = RGBColor(40, 40, 40)
    MUTED = RGBColor(100, 100, 100)

    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(17)
        run.font.color.rgb = PRIMARY
        p.paragraph_format.space_after = Pt(4)
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(12)
        run.font.color.rgb = SECONDARY
        p.paragraph_format.space_after = Pt(14)
        return p

    def add_heading_1(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(13.5)
        run.font.color.rgb = PRIMARY
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(5)
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(11.5)
        run.font.color.rgb = SECONDARY
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        return p

    def add_heading_3(text):
        p = doc.add_paragraph()
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(10.5)
        run.font.color.rgb = PRIMARY
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        return p

    def add_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Arial"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = DARK_TEXT
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(10)
        run.font.color.rgb = DARK_TEXT
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Arial"
            r_pre.font.size = Pt(9.5)
            r_pre.font.color.rgb = DARK_TEXT
        run = p.add_run(text)
        run.font.name = "Arial"
        run.font.size = Pt(9.5)
        run.font.color.rgb = DARK_TEXT
        return p

    def add_code(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        run.font.name = "Consolas"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(30, 30, 30)
        # Background light gray
        pPr = p._p.get_or_add_pPr()
        pPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F4F6F9"/>'))
        return p

    # -------------------------------------------------------------------------
    # PAGE 1: TITLE & COVER
    # -------------------------------------------------------------------------
    inst_p = doc.add_paragraph()
    inst_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    irun = inst_p.add_run("ANIL NEERUKONDA INSTITUTE OF TECHNOLOGY & SCIENCES\n(AUTONOMOUS) | VISAKHAPATNAM")
    irun.bold = True
    irun.font.name = "Arial"
    irun.font.size = Pt(12)
    irun.font.color.rgb = PRIMARY
    inst_p.paragraph_format.space_after = Pt(18)

    add_title("UNIT V – CASE STUDY DOCUMENTATION\nEduSphere – Student Management System")
    add_subtitle("Design of Express.js API Routes, MongoDB Atlas Interaction, and Cloud Deployment")

    p_topic = doc.add_paragraph()
    p_topic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_topic.paragraph_format.space_before = Pt(8)
    p_topic.paragraph_format.space_after = Pt(18)
    rt = p_topic.add_run("Topic: Consider a Student Management System in which students can be added, viewed, updated and deleted. Design the required Express.js API routes and explain how each route interacts with MongoDB to perform the corresponding operation.")
    rt.italic = True
    rt.font.size = Pt(10)
    rt.font.color.rgb = DARK_TEXT

    # Student metadata table
    meta_table = doc.add_table(rows=8, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(meta_table)
    
    meta_data = [
        ("Course Title", "Full-Stack Web Development"),
        ("Course Code", "23CM4121"),
        ("Unit", "Unit V – MongoDB and Deploying Applications"),
        ("Student Name", "D. Suswetha"),
        ("Registration Number", "A24126552079"),
        ("Academic Year / Semester", "3rd Year – 1st Semester"),
        ("Faculty / Guide", "P. Santosh Kumar"),
        ("Academic Year", "2026–27")
    ]
    
    for idx, (label, val) in enumerate(meta_data):
        row = meta_table.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.5)
        set_cell_background(c0, "F0F4F8")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 100, 100, 150, 150)
        set_cell_margins(c1, 100, 100, 150, 150)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = PRIMARY
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.name = "Arial"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = DARK_TEXT

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # PAGE 2: TABLE OF CONTENTS & PROJECT SNAPSHOT
    # -------------------------------------------------------------------------
    add_heading_1("TABLE OF CONTENTS")
    
    toc_table = doc.add_table(rows=8, cols=2)
    toc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(toc_table)
    
    toc_data = [
        ("PART A", "Comprehensive Question, Problem Statement and Topic Specification"),
        ("PART B – 1", "Requirement Analysis, Functional Modules, and 3-Tier System Architecture"),
        ("PART B – 2", "MongoDB Document Model, Mongoose Schema, and Database CRUD Operations"),
        ("PART B – 3", "Express.js REST API Route Design and Step-by-Step MongoDB Interaction"),
        ("PART B – 4", "Testing, Systematic Debugging Procedure, and Validation Matrix"),
        ("PART B – 5", "Cloud Deployment Architecture (Vercel, Render, Atlas) and Security"),
        ("PART C", "Output Screenshots and Implementation Evidence (Figures 1 to 9)"),
        ("CONCLUSION", "Project Outcome, Practical Insights, Limitations, and Future Enhancements")
    ]
    
    for idx, (sec, title) in enumerate(toc_data):
        row = toc_table.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(1.8)
        c1.width = Inches(4.9)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 80, 80, 120, 120)
        set_cell_margins(c1, 80, 80, 120, 120)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(sec)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = PRIMARY
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(title)
        r1.font.name = "Arial"
        r1.font.size = Pt(9.5)

    add_heading_1("PROJECT SNAPSHOT")
    
    snap_table = doc.add_table(rows=6, cols=3)
    snap_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(snap_table)
    
    snap_headers = ["Architecture Layer", "Technologies / Tools", "Assigned Role & Implementation"]
    for i, h in enumerate(snap_headers):
        c = snap_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 100, 100, 120, 120)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    snap_rows = [
        ("Frontend Client", "React 18, Vite, Axios, CSS3, Lucide React", "Single-Page Application: dashboard stats, directory, search, modals, and profile view"),
        ("Backend REST API", "Node.js, Express.js (v4.19), Mongoose ODM", "REST API routing, request validation, CORS, error handling, and MongoDB transactions"),
        ("Persistent Database", "MongoDB Atlas (Cloud Cluster)", "Document-oriented database storing BSON records in test.students collection"),
        ("Frontend Hosting", "Vercel Cloud Platform", "Builds and delivers high-performance production React application assets"),
        ("Backend Hosting", "Render Cloud Platform", "Hosts containerized Node.js/Express.js web service with managed environment secrets")
    ]
    
    for idx, (l, tech, role) in enumerate(snap_rows, start=1):
        row = snap_table.rows[idx]
        for c_idx, val in enumerate([l, tech, role]):
            cell = row.cells[c_idx]
            if c_idx == 0:
                cell.width = Inches(1.8)
                set_cell_background(cell, "F8FAFC")
            elif c_idx == 1:
                cell.width = Inches(2.2)
                set_cell_background(cell, "FFFFFF")
            else:
                cell.width = Inches(2.7)
                set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, 80, 80, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(9)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = PRIMARY

    add_p("https://edusphere-suswetha.vercel.app", bold_prefix="• Live Frontend URL: ")
    add_p("https://edusphere-backend-suswetha.onrender.com", bold_prefix="• Live Backend Web Service: ")
    add_p("https://edusphere-backend-suswetha.onrender.com/api/students", bold_prefix="• Students API Endpoint: ")
    add_p("https://github.com/suswethadwarapudi22-afk/fullstack/tree/main/case_study", bold_prefix="• GitHub Repository Case Study: ")

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # PART A. COMPREHENSIVE QUESTION & PROBLEM STATEMENT
    # -------------------------------------------------------------------------
    add_heading_1("PART A. COMPREHENSIVE QUESTION & PROBLEM STATEMENT")
    add_heading_2("Case Study Context: Institutional Student Record Management (EduSphere)")
    
    add_p("Educational institutions manage extensive volumes of student information, including registration numbers, names, email contacts, academic departments, year levels, contact numbers, and personal demographics. When handled manually or through fragmented spreadsheet files, institutions inevitably encounter duplicated entries, inconsistent updates across offices, sluggish search capabilities, and the inability to reliably verify academic history. To resolve these challenges, modern educational organizations adopt web-based, centralized Student Management Systems backed by scalable cloud databases and RESTful application programming interfaces (APIs).")

    add_heading_2("Core Problem Statement & Topic Assignment")
    add_p("Consider a Student Management System in which students can be added, viewed, updated and deleted. Design the required Express.js API routes and explain how each route interacts with MongoDB to perform the corresponding operation. Implement the system using React, Node.js, Express.js, and MongoDB Atlas, and deploy the application to public cloud platforms.")

    add_heading_3("Key Academic & Technical Objectives:")
    add_bullet("Store student details including roll number, full name, email, department, and academic year, alongside personal attributes (phone, date of birth, gender, address).", bold_prefix="1. Data Modeling: ")
    add_bullet("Create and manage a MongoDB database (`test`) and `students` collection utilizing an appropriate BSON document structure and indexed constraints.", bold_prefix="2. MongoDB Integration: ")
    add_bullet("Design RESTful API routes in Express.js supporting complete CRUD operations (Create, Read all, Read single, Update, and Delete) with rigorous error handling and validation.", bold_prefix="3. Route Architecture: ")
    add_bullet("Provide an in-depth mechanical explanation of how each Express.js route executes Mongoose operations and issues corresponding commands to MongoDB Atlas.", bold_prefix="4. Database Interaction Analysis: ")
    add_bullet("Implement client-side search, department filtering, and academic year filtering over the retrieved student records.", bold_prefix="5. Client User Interface: ")
    add_bullet("Deploy the frontend (Vercel), backend (Render), and database (MongoDB Atlas) to public cloud platforms with secure environment variable isolation.", bold_prefix="6. Cloud Deployment: ")
    add_bullet("Investigate a critical real-world failure mode where student records are successfully added to MongoDB but updated records fail to reflect in the user interface, and provide a systematic debugging workflow.", bold_prefix="7. Case Study Debugging: ")

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # PART B – 1: REQUIREMENT ANALYSIS & SYSTEM DESIGN
    # -------------------------------------------------------------------------
    add_heading_1("PART B – 1. REQUIREMENT ANALYSIS & SYSTEM DESIGN")
    
    add_heading_2("1. Functional Requirements Analysis")
    req_table = doc.add_table(rows=7, cols=3)
    req_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(req_table)
    
    req_headers = ["Requirement Area", "System Expectation", "EduSphere Implementation Details"]
    for i, h in enumerate(req_headers):
        c = req_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    req_rows = [
        ("Student Identity", "Unique institutional student identifier", "Institutional roll number (e.g. A24126552079) with unique index; immutable MongoDB _id (ObjectId)"),
        ("Student Demographics", "Academic and personal details capture", "Captures rollNumber, name, email, department, year, phone, dateOfBirth, gender, and address"),
        ("Data Persistence", "Fault-tolerant document storage", "MongoDB Atlas cloud cluster (test database, students collection)"),
        ("API Communication", "Standardized RESTful CRUD interface", "Express.js REST API with JSON payload body parsing and CORS headers"),
        ("Search & Filtering", "Fast discovery of student records", "Multi-criteria search by name, roll number, or email; dropdown filters by department and year"),
        ("Data Integrity", "Duplicate key and invalid input rejection", "Schema-level validators, unique indexes, and translation of MongoDB error 11000 to HTTP 409 Conflict")
    ]
    
    for idx, (area, exp, imp) in enumerate(req_rows, start=1):
        row = req_table.rows[idx]
        for c_idx, val in enumerate([area, exp, imp]):
            cell = row.cells[c_idx]
            if c_idx == 0:
                cell.width = Inches(1.8)
                set_cell_background(cell, "F8FAFC")
            elif c_idx == 1:
                cell.width = Inches(2.2)
                set_cell_background(cell, "FFFFFF")
            else:
                cell.width = Inches(2.7)
                set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, 60, 60, 90, 90)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = PRIMARY

    add_heading_2("2. Three-Tier System Architecture")
    add_p("EduSphere adheres to a clean Three-Tier Web Architecture ensuring separation of concerns, maintainability, and enterprise-grade security:")
    
    add_code(
"""       +-------------------------------------------------------+
       |             CLIENT TIER (User Browser)                |
       |  React 18 Single-Page Application (Hosted on Vercel)  |
       |  - Dashboard Overview, Metric Cards, Search & Filters |
       |  - Add/Edit Student Forms & Delete Confirmation Modal |
       +-------------------------------------------------------+
                                   |
                                   | HTTPS / Asynchronous Axios Calls
                                   | REST Requests (application/json)
                                   v
       +-------------------------------------------------------+
       |             APPLICATION TIER (REST API)               |
       |  Node.js + Express.js Web Server (Hosted on Render)   |
       |  - CORS Security Middleware & JSON Body Parsing       |
       |  - RESTful Route Handlers (/api/students)             |
       |  - Mongoose Schema Validation & Business Rules        |
       +-------------------------------------------------------+
                                   |
                                   | Mongoose Object Data Modeling (ODM)
                                   | Wire Protocol over TLS/SSL
                                   v
       +-------------------------------------------------------+
       |             DATABASE TIER (Storage Layer)             |
       |       MongoDB Atlas Cloud Database Cluster            |
       |  - Database: `test` | Collection: `students`          |
       |  - BSON Document Storage & Unique Primary Key Indexes |
       +-------------------------------------------------------+"""
    )
    
    add_p("Architecture Decoupling & Security: The browser client never interacts directly with MongoDB Atlas. Database connection strings, database credentials, and cluster endpoints remain strictly encapsulated within the Node.js backend environment variables on Render. This prevents credential exposure and centralizes validation logic.")

    add_heading_2("3. Main Functional Modules")
    add_bullet("Presents total enrolled student count, active department count, department-wise student distribution cards, and real-time backend operational status.", bold_prefix="• Institutional Dashboard: ")
    add_bullet("Displays student records in a structured tabular directory with instant search (name, roll number, email) and department/year filter dropdowns.", bold_prefix="• Student Directory: ")
    add_bullet("Interactive modal form capturing academic and personal details with client-side and server-side constraint checks.", bold_prefix="• Add Student Module: ")
    add_bullet("Dedicated profile view displaying individual student records, avatar initials, enrollment dates, and audit timestamps.", bold_prefix="• Student Profile Viewer: ")
    add_bullet("Pre-populates existing student attributes for modification and dispatches PUT requests to update MongoDB documents.", bold_prefix="• Edit Student Module: ")
    add_bullet("Prevents accidental deletions by presenting a safety modal requiring explicit confirmation prior to issuing DELETE commands.", bold_prefix="• Delete Confirmation Guard: ")

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # PART B – 2: MONGODB DOCUMENT MODEL & DATABASE OPERATIONS
    # -------------------------------------------------------------------------
    add_heading_1("PART B – 2. MONGODB DOCUMENT MODEL & DATABASE OPERATIONS")
    
    add_heading_2("1. Document-Oriented Data Modeling")
    add_p("Relational databases enforce rigid tabular schemas requiring complex foreign key joins to represent multidimensional records. In contrast, MongoDB's document model represents each student entity as a self-contained, flexible BSON (Binary JSON) document. This model offers high write throughput, seamless schema extensibility, and direct JSON impedance match with React and Node.js.")

    add_heading_2("2. MongoDB Document Schema Representation (JSON / BSON)")
    add_code(
"""{
  "_id": ObjectId("6730a1b2c3d4e5f6a7b8c9d0"),
  "rollNumber": "A24126552079",
  "name": "Suswetha Dwarapudi",
  "email": "suswetha.dwarapudi@example.com",
  "department": "CSE",
  "year": 3,
  "phone": "+91 9876543210",
  "dateOfBirth": ISODate("2004-05-18T00:00:00.000Z"),
  "gender": "Female",
  "address": "Visakhapatnam, Andhra Pradesh",
  "createdAt": ISODate("2026-11-10T10:15:30.000Z"),
  "updatedAt": ISODate("2026-11-10T10:15:30.000Z"),
  "__v": 0
}"""
    )

    add_heading_2("3. Document Fields, Data Types, and Constraints")
    field_table = doc.add_table(rows=11, cols=4)
    field_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(field_table)
    
    field_headers = ["Field Name", "BSON / Schema Type", "Constraints & Validation", "Functional Purpose"]
    for i, h in enumerate(field_headers):
        c = field_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    fields_data = [
        ("_id", "ObjectId", "Primary Key, Immutable, Auto-generated", "Globally unique 12-byte BSON document identifier"),
        ("rollNumber", "String", "Required, Unique Index, Uppercase, Trim", "Human-readable institutional identifier (e.g. A24126552079)"),
        ("name", "String", "Required, Trim, Min length 2", "Student full legal name"),
        ("email", "String", "Required, Unique Index, Lowercase, Regex", "Institutional contact email for notifications"),
        ("department", "String", "Required, Enum (CSE, AI&DS, IT, ECE...)", "Enrolled academic department / discipline"),
        ("year", "Number", "Required, Number, Min 1, Max 4", "Current academic standing (Year 1 to 4)"),
        ("phone", "String", "Optional, Trim", "Personal emergency contact telephone number"),
        ("dateOfBirth", "Date", "Optional, ISO Date", "Student date of birth for institutional records"),
        ("gender", "String", "Optional, Enum (Male, Female, Other)", "Demographic gender designation"),
        ("createdAt / updatedAt", "Date", "Managed automatically via Mongoose timestamps", "Audit trail timestamps tracking record lifecycle")
    ]

    for idx, (fld, tp, constr, purp) in enumerate(fields_data, start=1):
        row = field_table.rows[idx]
        for c_idx, val in enumerate([fld, tp, constr, purp]):
            cell = row.cells[c_idx]
            if c_idx == 0:
                cell.width = Inches(1.5)
                set_cell_background(cell, "F8FAFC")
            elif c_idx == 1:
                cell.width = Inches(1.4)
                set_cell_background(cell, "FFFFFF")
            elif c_idx == 2:
                cell.width = Inches(2.0)
                set_cell_background(cell, "FFFFFF")
            else:
                cell.width = Inches(1.8)
                set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = PRIMARY

    add_heading_2("4. MongoDB Shell (mongosh) CRUD Operations")
    add_p("To illustrate how MongoDB processes CRUD commands directly, the following native shell queries reflect the underlying operations performed by the backend:")
    
    add_code(
"""// 1. Switch to application database
use test;

// 2. Insert a new student record
db.students.insertOne({
  rollNumber: "A24126552079",
  name: "Suswetha Dwarapudi",
  email: "suswetha.dwarapudi@example.com",
  department: "CSE",
  year: 3,
  createdAt: new Date(),
  updatedAt: new Date()
});

// 3. Retrieve all students sorted by most recent
db.students.find({}).sort({ createdAt: -1 });

// 4. Query a student by unique roll number
db.students.findOne({ rollNumber: "A24126552079" });

// 5. Update student details
db.students.updateOne(
  { rollNumber: "A24126552079" },
  { $set: { department: "CSE", year: 3, updatedAt: new Date() } }
);

// 6. Delete a student record
db.students.deleteOne({ rollNumber: "A24126552079" });

// 7. Verify Indexing and Query Performance
db.students.createIndex({ rollNumber: 1 }, { unique: true });
db.students.find({ rollNumber: "A24126552079" }).explain("executionStats");"""
    )

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # PART B – 3: BACKEND & FRONTEND IMPLEMENTATION
    # -------------------------------------------------------------------------
    add_heading_1("PART B – 3. BACKEND & FRONTEND IMPLEMENTATION")
    
    add_heading_2("1. Express.js REST API Route Design")
    add_p("The backend exposes a RESTful interface over the base route `/api/students`. Each route is explicitly mapped to a corresponding HTTP method, URL pattern, controller logic, and database query:")

    api_table = doc.add_table(rows=6, cols=4)
    api_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(api_table)
    
    api_headers = ["HTTP Method", "Route Endpoint", "Purpose & Action", "Success & Error Status Codes"]
    for i, h in enumerate(api_headers):
        c = api_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    api_rows = [
        ("POST", "/api/students", "Create and persist a new student record", "201 Created | 400 Bad Request | 409 Conflict"),
        ("GET", "/api/students", "Retrieve all student records with sorting", "200 OK | 500 Internal Server Error"),
        ("GET", "/api/students/:id", "Retrieve single student profile by document ID", "200 OK | 400 Bad ID | 404 Not Found"),
        ("PUT", "/api/students/:id", "Update student attributes by document ID", "200 OK | 400 Bad Request | 404 Not Found | 409 Conflict"),
        ("DELETE", "/api/students/:id", "Permanently remove student record by document ID", "200 OK | 400 Bad Request | 404 Not Found")
    ]

    for idx, (m, ep, purp, st) in enumerate(api_rows, start=1):
        row = api_table.rows[idx]
        for c_idx, val in enumerate([m, ep, purp, st]):
            cell = row.cells[c_idx]
            if c_idx == 0:
                cell.width = Inches(1.2)
                set_cell_background(cell, "F8FAFC")
            elif c_idx == 1:
                cell.width = Inches(1.8)
                set_cell_background(cell, "FFFFFF")
            elif c_idx == 2:
                cell.width = Inches(2.2)
                set_cell_background(cell, "FFFFFF")
            else:
                cell.width = Inches(1.5)
                set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = PRIMARY

    add_heading_2("2. Detailed Explanation: How Each Route Interacts with MongoDB")
    
    add_heading_3("A. Add Student Route (POST /api/students)")
    add_bullet("Express JSON middleware parses the HTTP request body into `req.body`.", bold_prefix="1. Payload Receipt: ")
    add_bullet("Mongoose creates a new model instance `const student = new Student(req.body)`, verifying required fields and data types against the schema.", bold_prefix="2. Document Instantiation: ")
    add_bullet("Executing `await student.save()` transmits an `insertOne` write command over the MongoDB wire protocol.", bold_prefix="3. MongoDB Command: ")
    add_bullet("MongoDB Atlas validates unique indexes (rollNumber, email). If a violation occurs, MongoDB throws error code `11000`. The catch block intercepts this code and responds with HTTP 409 Conflict.", bold_prefix="4. Conflict Handling: ")
    add_bullet("Upon success, MongoDB persists the document, generates a unique 12-byte `_id` ObjectId, sets `createdAt` and `updatedAt`, and returns HTTP 201 Created with the saved JSON object.", bold_prefix="5. Document Return: ")

    add_heading_3("B. View All Students Route (GET /api/students)")
    add_bullet("Express inspects `req.query` for optional filters such as `department`, `year`, or `search` keywords.", bold_prefix="1. Filter Extraction: ")
    add_bullet("Mongoose constructs a query filter object. If a search keyword is provided, it creates regex clauses: `{ $or: [{ name: /.../i }, { rollNumber: /.../i }] }`.", bold_prefix="2. Query Synthesis: ")
    add_bullet("Executing `Student.find(query).sort({ createdAt: -1 })` sends a `find` command to MongoDB Atlas.", bold_prefix="3. Database Scan: ")
    add_bullet("MongoDB retrieves documents matching the criteria and orders them in reverse chronological order via the `createdAt` index.", bold_prefix="4. Cursor Hydration: ")
    add_bullet("Express returns HTTP 200 OK containing the array of students and the total record count.", bold_prefix="5. Response: ")

    add_heading_3("C. View Single Student Route (GET /api/students/:id)")
    add_bullet("Express extracts the unique document identifier from URL parameters (`req.params.id`).", bold_prefix="1. Parameter Capture: ")
    add_bullet("Mongoose verifies that `id` is a valid 24-character hex string and converts it to BSON `ObjectId(id)`.", bold_prefix="2. Type Casting: ")
    add_bullet("Executing `Student.findById(id)` translates to `db.students.findOne({ _id: ObjectId(id) })`.", bold_prefix="3. Key Lookup: ")
    add_bullet("MongoDB uses the primary key index on `_id` to locate the document with O(1) efficiency.", bold_prefix="4. Index Execution: ")
    add_bullet("If found, returns HTTP 200 OK with the student profile; if absent, returns HTTP 404 Not Found.", bold_prefix="5. Evaluation: ")

    add_heading_3("D. Update Student Route (PUT /api/students/:id)")
    add_bullet("Captures document ID from `req.params.id` and updated attributes from `req.body`.", bold_prefix="1. Input Ingestion: ")
    add_bullet("Mongoose executes `Student.findByIdAndUpdate(id, req.body, { new: true, runValidators: true })`.", bold_prefix="2. Mongoose Method: ")
    add_bullet("MongoDB translates this operation into an atomic `findOneAndUpdate({ _id: ObjectId(id) }, { $set: updateFields })` command.", bold_prefix="3. MongoDB Atomic Operation: ")
    add_bullet("CRITICAL: The `{ new: true }` option instructs MongoDB to return the modified document instead of the original pre-update document. `{ runValidators: true }` re-executes Mongoose validation rules.", bold_prefix="4. Crucial Options: ")
    add_bullet("If the update introduces a duplicate roll number or email, MongoDB throws code `11000`, returned as HTTP 409 Conflict. If successful, returns HTTP 200 OK with the updated document.", bold_prefix="5. Result: ")

    add_heading_3("E. Delete Student Route (DELETE /api/students/:id)")
    add_bullet("Captures document ID from `req.params.id`.", bold_prefix="1. Parameter Capture: ")
    add_bullet("Mongoose executes `Student.findByIdAndDelete(req.params.id)`.", bold_prefix="2. Mongoose Method: ")
    add_bullet("MongoDB translates this to `findOneAndDelete({ _id: ObjectId(id) })`, permanently unlinking and removing the document from the BSON storage engine.", bold_prefix="3. MongoDB Deletion: ")
    add_bullet("If no document matched the ID, returns HTTP 404 Not Found. If removed, returns HTTP 200 OK with a confirmation message.", bold_prefix="4. Response: ")

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # PART B – 4: TESTING, DEBUGGING & VALIDATION
    # -------------------------------------------------------------------------
    add_heading_1("PART B – 4. TESTING, DEBUGGING & VALIDATION")
    
    add_heading_2("1. In-Depth Analysis of the Case Study Problem")
    add_p("Case Study Problem Scenario: A deployed Student Management System successfully adds new student records to MongoDB Atlas, but after editing a student record, the user interface fails to display the updated information.", bold_prefix="• Core Issue: ")
    add_p("A successful database write (HTTP 200/201) and a refreshed user interface are independent steps in a multi-tier web application. When an update succeeds in MongoDB but fails to appear on screen, the breakdown can occur across several layers: client-side state management, asynchronous execution timing, backend route parameters, Mongoose return options, browser caching, or database cluster mismatches.")

    add_heading_2("2. Multi-Layer Debugging Failure Matrix")
    diag_table = doc.add_table(rows=7, cols=3)
    diag_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(diag_table)
    
    diag_headers = ["Architectural Layer", "Root Cause Description", "Diagnostic Procedure & Systematic Resolution"]
    for i, h in enumerate(diag_headers):
        c = diag_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    diag_rows = [
        ("React State Staleness", "Frontend does not trigger a re-fetch of students following the PUT request", "Inspect the form submission handler. Ensure `await fetchStudents()` is called immediately after a successful PUT response to reload server state."),
        ("Asynchronous Race Condition", "List refresh query executes before MongoDB Atlas finishes the write", "Ensure the Axios PUT request is explicitly awaited (`await updateStudent(...)`) before triggering the GET request."),
        ("Mongoose Return Behavior", "Missing `{ new: true }` in `findByIdAndUpdate` causes Mongoose to return old document", "Add `{ new: true, runValidators: true }` to the `findByIdAndUpdate` call in `studentRoutes.js` so the updated document is returned."),
        ("Document ID Mismatch", "Backend update route uses `rollNumber` instead of MongoDB `_id`", "Verify that the PUT request URL is `/api/students/${student._id}` where `_id` is the 24-character BSON ObjectId."),
        ("Environment / Cluster Disconnect", "Backend connects to a different MongoDB Atlas database than expected", "Verify Render environment variable `MONGO_URI`. Open MongoDB Atlas Data Explorer and confirm writes in `test.students`."),
        ("CORS / HTTP Verb Blocking", "Browser blocks PUT request preflight options check", "Configure Express CORS middleware with `app.use(cors())` ensuring PUT and DELETE verbs are permitted from the Vercel domain.")
    ]

    for idx, (lyr, cause, fix) in enumerate(diag_rows, start=1):
        row = diag_table.rows[idx]
        for c_idx, val in enumerate([lyr, cause, fix]):
            cell = row.cells[c_idx]
            if c_idx == 0:
                cell.width = Inches(1.8)
                set_cell_background(cell, "F8FAFC")
            elif c_idx == 1:
                cell.width = Inches(2.3)
                set_cell_background(cell, "FFFFFF")
            else:
                cell.width = Inches(2.6)
                set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = PRIMARY

    add_heading_2("3. Step-by-Step Systematic Debugging Sequence")
    add_bullet("Select a specific test student (e.g. Roll No: A24126552079) and log current values, target update values, and exact timestamp.", bold_prefix="Step 1: Isolated Reproduction: ")
    add_bullet("Open Chrome Developer Tools -> Network tab. Submit the update form and inspect the outgoing request URL, method (PUT), and payload JSON.", bold_prefix="Step 2: Network Inspection: ")
    add_bullet("Verify that the server answers with HTTP 200 OK and inspect the returned JSON body to confirm the field values have changed.", bold_prefix="Step 3: Response Status Validation: ")
    add_bullet("Examine the Render backend deployment console logs for database errors, schema validation errors, or duplicate-key conflicts.", bold_prefix="Step 4: Backend Logs Analysis: ")
    add_bullet("Log into MongoDB Atlas -> Data Explorer -> test.students. Find the student record and verify that the updated field and `updatedAt` have changed in storage.", bold_prefix="Step 5: Direct Database Verification: ")
    add_bullet("Send an independent GET request (`curl -s https://edusphere-backend-suswetha.onrender.com/api/students`) to verify the REST API returns the updated document.", bold_prefix="Step 6: Direct API Query: ")
    add_bullet("Inspect the React component state in React Developer Tools. Verify that `fetchStudents()` sets the new array into `students` state.", bold_prefix="Step 7: State Management Verification: ")
    add_bullet("Perform a hard refresh (`Ctrl + F5`) on the browser. If the updated data remains visible, persistent storage and retrieval are fully functional.", bold_prefix="Step 8: Persistence Confirmation: ")

    add_heading_2("4. Test Case Validation Matrix")
    tc_table = doc.add_table(rows=11, cols=4)
    tc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tc_table)
    
    tc_headers = ["Test ID", "Test Action & Input", "Expected Outcome", "Validation Evidence & Status"]
    for i, h in enumerate(tc_headers):
        c = tc_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    tc_data = [
        ("TC-01", "Navigate to root URL", "Dashboard loads with institutional metrics, student count, and cards", "Figure 1 | Passed"),
        ("TC-02", "View Student Directory", "Students collection is retrieved via GET /api/students and listed in table", "Figure 2 | Passed"),
        ("TC-03", "Submit Add Student form", "Record saved to MongoDB Atlas via POST; list refreshes automatically", "Figure 3 | Passed"),
        ("TC-04", "Submit duplicate roll number", "Backend rejects insertion; returns HTTP 409 Conflict with clear error", "Error banner | Passed"),
        ("TC-05", "Click student profile view", "Selected student details displayed in profile view via GET /:id", "Figure 4 | Passed"),
        ("TC-06", "Submit Edit Student form", "Attributes updated in MongoDB via PUT; updated values visible in UI", "Figure 5 | Passed"),
        ("TC-07", "Click Delete button", "Safety confirmation dialog displayed before issuing DELETE command", "Figure 6 | Passed"),
        ("TC-08", "Confirm student deletion", "Record excised from MongoDB; student removed from UI table", "Directory updated | Passed"),
        ("TC-09", "Inspect MongoDB Atlas console", "Student documents verified in test.students collection", "Figure 7 | Passed"),
        ("TC-10", "Verify cloud deployment status", "Render backend Live; Vercel frontend Ready", "Figures 8 & 9 | Passed")
    ]

    for idx, (tid, act, exp, stat) in enumerate(tc_data, start=1):
        row = tc_table.rows[idx]
        for c_idx, val in enumerate([tid, act, exp, stat]):
            cell = row.cells[c_idx]
            if c_idx == 0:
                cell.width = Inches(1.1)
                set_cell_background(cell, "F8FAFC")
            elif c_idx == 1:
                cell.width = Inches(2.2)
                set_cell_background(cell, "FFFFFF")
            elif c_idx == 2:
                cell.width = Inches(2.2)
                set_cell_background(cell, "FFFFFF")
            else:
                cell.width = Inches(1.2)
                set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = PRIMARY
            if "Passed" in val:
                r.font.color.rgb = RGBColor(34, 139, 34)

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # PART B – 5: CLOUD DEPLOYMENT & SECURITY
    # -------------------------------------------------------------------------
    add_heading_1("PART B – 5. CLOUD DEPLOYMENT & SECURITY")
    
    add_heading_2("1. Cloud Hosting Architecture")
    add_p("EduSphere is architected across three industry-standard cloud tiers, ensuring high availability, continuous deployment from GitHub, and complete credential isolation:")
    
    dep_table = doc.add_table(rows=4, cols=4)
    dep_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(dep_table)
    
    dep_headers = ["Layer", "Cloud Platform", "Project Name / Identifier", "Runtime / Configuration"]
    for i, h in enumerate(dep_headers):
        c = dep_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    dep_rows = [
        ("Frontend", "Vercel", "edusphere-frontend-suswetha", "Vite build (`dist`), global edge CDN distribution"),
        ("Backend", "Render", "edusphere-backend-suswetha", "Node.js Web Service, `npm install` build, `npm start` start"),
        ("Database", "MongoDB Atlas", "AURAFIT / Cluster0", "Cloud-hosted replica set, database `test`, collection `students`")
    ]

    for idx, (lyr, plat, prj, cfg) in enumerate(dep_rows, start=1):
        row = dep_table.rows[idx]
        for c_idx, val in enumerate([lyr, plat, prj, cfg]):
            cell = row.cells[c_idx]
            if c_idx == 0:
                cell.width = Inches(1.2)
                set_cell_background(cell, "F8FAFC")
            elif c_idx == 1:
                cell.width = Inches(1.4)
                set_cell_background(cell, "FFFFFF")
            elif c_idx == 2:
                cell.width = Inches(1.8)
                set_cell_background(cell, "FFFFFF")
            else:
                cell.width = Inches(2.3)
                set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = PRIMARY

    add_heading_2("2. Environment Variable Configuration")
    env_table = doc.add_table(rows=4, cols=4)
    env_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(env_table)
    
    env_headers = ["Variable Name", "Configured Location", "Sensitivity", "Purpose & Operational Role"]
    for i, h in enumerate(env_headers):
        c = env_table.rows[0].cells[i]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    env_rows = [
        ("MONGO_URI", "Render Backend Service", "HIGH SECRET", "Encrypted MongoDB Atlas connection string with database credentials"),
        ("PORT", "Render Runtime Environment", "Standard", "Port assigned dynamically by hosting provider (defaults to 5000)"),
        ("VITE_API_URL", "Vercel Frontend Project", "Public", "Base URL pointing to the live Render backend REST API endpoint")
    ]

    for idx, (v, loc, sens, purp) in enumerate(env_rows, start=1):
        row = env_table.rows[idx]
        for c_idx, val in enumerate([v, loc, sens, purp]):
            cell = row.cells[c_idx]
            if c_idx == 0:
                cell.width = Inches(1.5)
                set_cell_background(cell, "F8FAFC")
            elif c_idx == 1:
                cell.width = Inches(1.8)
                set_cell_background(cell, "FFFFFF")
            elif c_idx == 2:
                cell.width = Inches(1.3)
                set_cell_background(cell, "FFFFFF")
            else:
                cell.width = Inches(2.1)
                set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, 60, 60, 80, 80)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = PRIMARY
            if sens == "HIGH SECRET":
                r.font.color.rgb = RGBColor(178, 34, 34)

    add_heading_2("3. Cloud Security Best Practices")
    add_bullet("`MONGO_URI` is strictly stored inside Render's environment secret manager and never placed in frontend code, client-side `.env` files, or committed to GitHub.", bold_prefix="• Secret Isolation: ")
    add_bullet("`.gitignore` explicitly excludes all local `.env`, `.env.local`, and `node_modules` folders to prevent credential leakage in public repositories.", bold_prefix="• Version Control Hygiene: ")
    add_bullet("The Express.js backend enforces CORS validation to restrict which origins can execute state-changing requests.", bold_prefix="• Origin Validation: ")
    add_bullet("All production traffic between browser, backend, and MongoDB Atlas runs over TLS/SSL encryption.", bold_prefix="• HTTPS / TLS Encryption: ")

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # PART C. OUTPUT SCREENSHOTS AND EVIDENCE
    # -------------------------------------------------------------------------
    add_heading_1("PART C. OUTPUT SCREENSHOTS AND EVIDENCE")
    add_p("The following figures document the live implementation, responsive user interface workflows, database persistence, and cloud hosting status of EduSphere:")

    screenshots_data = [
        ("case_study/output_screenshots/01_dashboard.png", "Figure 1. EduSphere institutional dashboard showing total student count, department metrics, and quick action bar."),
        ("case_study/output_screenshots/02_dashboard_2.png", "Figure 2. Student directory view showing stored student records, roll numbers, departments, and action buttons."),
        ("case_study/output_screenshots/03_add_new_student.png", "Figure 3. Add Student modal form capturing roll number, name, email, department, and academic year."),
        ("case_study/output_screenshots/04_view_student.png", "Figure 4. Student profile viewer displaying detailed academic standing, contact email, and audit timestamps."),
        ("case_study/output_screenshots/05_edit_student.png", "Figure 5. Edit Student modal populated with existing student data, demonstrating field modification workflow."),
        ("case_study/output_screenshots/06_delete_student.png", "Figure 6. Safety deletion confirmation modal displayed prior to permanent document removal."),
        ("case_study/output_screenshots/07_mongodb_atlas.png", "Figure 7. MongoDB Atlas Data Explorer showing test.students collection with stored BSON student documents."),
        ("case_study/output_screenshots/08_render_backend.png", "Figure 8. Render dashboard showing edusphere-backend-suswetha Node.js web service running with Live deployment status."),
        ("case_study/output_screenshots/09_vercel_frontend.png", "Figure 9. Vercel deployment console showing edusphere-frontend-suswetha production deployment with Ready status.")
    ]

    for img_path, caption in screenshots_data:
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(2)
            run_img = p_img.add_run()
            run_img.add_picture(img_path, width=Inches(5.5))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(12)
            r_cap = p_cap.add_run(caption)
            r_cap.font.name = "Arial"
            r_cap.font.size = Pt(8.5)
            r_cap.italic = True
            r_cap.font.color.rgb = DARK_TEXT

    add_heading_2("Evidence Interpretation & Architecture Validation")
    add_p("The execution evidence verifies end-to-end full-stack integration: Figures 1-6 validate that all student management workflows (create, read, update, delete, view profile) are operational within the browser interface. Figure 7 confirms persistent BSON storage within MongoDB Atlas. Figures 8 and 9 demonstrate that the three-layer architecture has been deployed and operationalized across independent cloud environments.")

    doc.add_page_break()

    # -------------------------------------------------------------------------
    # CONCLUSION, LIMITATIONS & FUTURE ENHANCEMENTS
    # -------------------------------------------------------------------------
    add_heading_1("CONCLUSION, LIMITATIONS & FUTURE ENHANCEMENTS")
    
    add_heading_2("1. Expected Outcome & Project Achievements")
    add_bullet("Designed and deployed a modern, responsive Single-Page Application using React 18, Vite, and Lucide React.", bold_prefix="• Full-Stack Integration: ")
    add_bullet("Engineered RESTful Express.js API routes under `/api/students` mapping to MongoDB CRUD operations with Mongoose ODM.", bold_prefix="• Robust REST API: ")
    add_bullet("Detailed the exact mechanical interactions between Express.js routes and MongoDB write/read commands.", bold_prefix="• Database Interaction Clarity: ")
    add_bullet("Developed a repeatable, multi-layer debugging procedure solving the critical case-study issue of stale client views after update.", bold_prefix="• Systematic Debugging: ")
    add_bullet("Operationalized the frontend on Vercel, the backend on Render, and persistent data on MongoDB Atlas with complete secret isolation.", bold_prefix="• Production Cloud Deployment: ")

    add_heading_2("2. System Limitations")
    add_bullet("Currently, any user visiting the public URL can perform edit and delete operations. Role-based access control is needed for production.", bold_prefix="• Open Public Access: ")
    add_bullet("The GET endpoint loads all students simultaneously. Datasets exceeding thousands of records would require server-side pagination.", bold_prefix="• Client-Side Pagination: ")
    add_bullet("Render's free compute tier spins down after 15 minutes of inactivity, resulting in a 30-50 second latency window upon initial wake-up.", bold_prefix="• Cold Start Latency: ")

    add_heading_2("3. Future Enhancements")
    add_bullet("Implement JSON Web Token (JWT) role-based authentication distinguishing administrators, faculty, and students.", bold_prefix="• Role-Based Authentication: ")
    add_bullet("Incorporate server-side pagination (`limit` and `skip`) to optimize query throughput for large institutional datasets.", bold_prefix="• Server-Side Pagination: ")
    add_bullet("Provide one-click export of student records into standard CSV and formatted PDF transcripts.", bold_prefix="• Data Export Capabilities: ")
    add_bullet("Implement an audit logging collection in MongoDB tracking user ID, IP address, timestamp, and field deltas on every record modification.", bold_prefix="• Audit Trail Logging: ")

    add_heading_2("4. References & Documentation")
    add_bullet("Anil Neerukonda Institute of Technology & Sciences, Syllabus 23CM4121 (Unit V – MongoDB and Deploying Applications).", bold_prefix="• ANITS Course Syllabus: ")
    add_bullet("MongoDB Atlas and BSON Architecture Documentation (https://www.mongodb.com/docs/).", bold_prefix="• MongoDB Manual: ")
    add_bullet("Express.js API Reference and Routing Guide (https://expressjs.com/).", bold_prefix="• Express.js Documentation: ")
    add_bullet("Mongoose ODM Models, Queries, and Validation (https://mongoosejs.com/docs/).", bold_prefix="• Mongoose Documentation: ")
    add_bullet("React 18 Component State and Hooks Guide (https://react.dev/).", bold_prefix="• React Documentation: ")
    add_bullet("Render Cloud Web Services & Vercel Global Deployment Documentation.", bold_prefix="• Cloud Hosting Guides: ")

    # Save document
    doc.save(filename)
    print(f"Document successfully created and saved to {filename}")

if __name__ == "__main__":
    build_docx()
