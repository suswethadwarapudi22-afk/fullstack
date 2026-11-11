import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, Preformatted
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "FULL-STACK WEB DEVELOPMENT  |  UNIT V CASE STUDY")
            self.drawRightString(558, 750, f"EduSphere – Student Management System  •  {self._pageNumber}")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.6)
            self.line(54, 742, 558, 742)
            
        # Footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.6)
        self.line(54, 46, 558, 46)
        
        self.drawString(54, 34, "ANITS • Dept. of CSE / CSM  |  Reg: A24126552079")
        self.drawRightString(558, 34, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def build_pdf(filename="case_study/A24126552079_FSWD_CASESTUDY_DOCUMENTATION.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    PRIMARY = colors.HexColor("#1B365D")
    SECONDARY = colors.HexColor("#2563EB")
    DARK_TEXT = colors.HexColor("#1E293B")
    MUTED_TEXT = colors.HexColor("#475569")
    LIGHT_BG = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#CBD5E1")
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        alignment=1, # Center
        textColor=PRIMARY,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        alignment=1,
        textColor=SECONDARY,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=16,
        textColor=PRIMARY,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=SECONDARY,
        spaceBefore=9,
        spaceAfter=4,
        keepWithNext=True
    )

    h3_style = ParagraphStyle(
        'CustomH3',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=PRIMARY,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=DARK_TEXT,
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=DARK_TEXT,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=3
    )

    caption_style = ParagraphStyle(
        'CustomCaption',
        parent=styles['Italic'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        alignment=1,
        textColor=MUTED_TEXT,
        spaceAfter=8
    )

    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=7.2,
        leading=9.5,
        textColor=colors.HexColor("#0F172A"),
        backColor=colors.HexColor("#F1F5F9"),
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=6
    )

    story = []

    def p(text):
        return Paragraph(text, body_style)

    def b(text):
        return Paragraph(text, bullet_style)

    # -------------------------------------------------------------------------
    # PAGE 1: COVER PAGE
    # -------------------------------------------------------------------------
    inst_header = Paragraph(
        "<b>ANIL NEERUKONDA INSTITUTE OF TECHNOLOGY & SCIENCES</b><br/>"
        "<font size=8.5 color='#475569'>(AUTONOMOUS)  |  VISAKHAPATNAM</font>",
        ParagraphStyle('InstHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, leading=15, alignment=1, textColor=PRIMARY)
    )
    story.append(inst_header)
    story.append(Spacer(1, 14))

    story.append(Paragraph("UNIT V – CASE STUDY DOCUMENTATION<br/><font size=18>EduSphere</font><br/>Student Management System", title_style))
    story.append(Paragraph("Design of Express.js API Routes, MongoDB Atlas Interaction, and Cloud Deployment", subtitle_style))

    topic_box = Paragraph(
        "<b>Topic:</b> <i>Consider a Student Management System in which students can be added, viewed, updated and deleted. "
        "Design the required Express.js API routes and explain how each route interacts with MongoDB to perform the corresponding operation.</i>",
        ParagraphStyle('TopicBox', parent=body_style, fontSize=8.5, leading=12, alignment=1, textColor=DARK_TEXT)
    )
    story.append(topic_box)
    story.append(Spacer(1, 16))

    # Meta Table
    meta_data = [
        [Paragraph("<b>Course Title</b>", body_style), Paragraph("Full-Stack Web Development", body_style)],
        [Paragraph("<b>Course Code</b>", body_style), Paragraph("23CM4121", body_style)],
        [Paragraph("<b>Unit</b>", body_style), Paragraph("Unit V – MongoDB and Deploying Applications", body_style)],
        [Paragraph("<b>Student Name</b>", body_style), Paragraph("D. Suswetha", body_style)],
        [Paragraph("<b>Registration Number</b>", body_style), Paragraph("A24126552079", body_style)],
        [Paragraph("<b>Academic Year / Semester</b>", body_style), Paragraph("3rd Year – 1st Semester", body_style)],
        [Paragraph("<b>Faculty / Guide</b>", body_style), Paragraph("P. Santosh Kumar", body_style)],
        [Paragraph("<b>Academic Year</b>", body_style), Paragraph("2026–27", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[150, 354])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor("#F1F5F9")),
        ('BACKGROUND', (1, 0), (1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(meta_table)
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # PAGE 2: TABLE OF CONTENTS & SNAPSHOT
    # -------------------------------------------------------------------------
    story.append(Paragraph("TABLE OF CONTENTS", h1_style))
    
    toc_data = [
        [Paragraph("<b>PART A</b>", body_style), Paragraph("Comprehensive Question, Problem Statement and Topic Specification", body_style)],
        [Paragraph("<b>PART B – 1</b>", body_style), Paragraph("Requirement Analysis, Functional Modules, and 3-Tier System Architecture", body_style)],
        [Paragraph("<b>PART B – 2</b>", body_style), Paragraph("MongoDB Document Model, Mongoose Schema, and Database CRUD Operations", body_style)],
        [Paragraph("<b>PART B – 3</b>", body_style), Paragraph("Express.js REST API Route Design and Step-by-Step MongoDB Interaction", body_style)],
        [Paragraph("<b>PART B – 4</b>", body_style), Paragraph("Testing, Systematic Debugging Procedure, and Validation Matrix", body_style)],
        [Paragraph("<b>PART B – 5</b>", body_style), Paragraph("Cloud Deployment Architecture (Vercel, Render, Atlas) and Security", body_style)],
        [Paragraph("<b>PART C</b>", body_style), Paragraph("Output Screenshots and Implementation Evidence (Figures 1 to 9)", body_style)],
        [Paragraph("<b>CONCLUSION</b>", body_style), Paragraph("Project Outcome, Practical Insights, Limitations, and Future Enhancements", body_style)]
    ]
    toc_table = Table(toc_data, colWidths=[90, 414])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(toc_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("PROJECT SNAPSHOT", h1_style))
    
    snap_data = [
        [Paragraph("<b>Architecture Layer</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Technologies / Tools</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Assigned Role & Implementation</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white))],
        [Paragraph("<b>Frontend Client</b>", body_style), Paragraph("React 18, Vite, Axios, CSS3, Lucide", body_style), Paragraph("SPA: dashboard, directory table, search, filters, forms, and profile modal", body_style)],
        [Paragraph("<b>Backend REST API</b>", body_style), Paragraph("Node.js, Express.js (v4.19), Mongoose", body_style), Paragraph("REST API routing, validation, CORS, error handling, and MongoDB transactions", body_style)],
        [Paragraph("<b>Database</b>", body_style), Paragraph("MongoDB Atlas (Cloud Cluster)", body_style), Paragraph("Document-oriented storage of BSON student records in test.students collection", body_style)],
        [Paragraph("<b>Frontend Hosting</b>", body_style), Paragraph("Vercel Cloud Platform", body_style), Paragraph("Production React build hosting with global edge delivery", body_style)],
        [Paragraph("<b>Backend Hosting</b>", body_style), Paragraph("Render Cloud Platform", body_style), Paragraph("Hosts containerized Node.js Web Service with managed secrets", body_style)]
    ]
    snap_table = Table(snap_data, colWidths=[110, 150, 244])
    snap_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(snap_table)
    story.append(Spacer(1, 8))

    story.append(b("<b>• Live Frontend URL:</b> https://edusphere-suswetha.vercel.app"))
    story.append(b("<b>• Live Backend Web Service:</b> https://edusphere-backend-suswetha.onrender.com"))
    story.append(b("<b>• Students API Endpoint:</b> https://edusphere-backend-suswetha.onrender.com/api/students"))
    story.append(b("<b>• Source Repository:</b> https://github.com/suswethadwarapudi22-afk/fullstack/tree/main/case_study"))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # PART A: COMPREHENSIVE QUESTION & PROBLEM STATEMENT
    # -------------------------------------------------------------------------
    story.append(Paragraph("PART A. COMPREHENSIVE QUESTION & PROBLEM STATEMENT", h1_style))
    story.append(Paragraph("Case Study Context: Institutional Student Record Management (EduSphere)", h2_style))
    story.append(p("Educational institutions manage extensive volumes of student information, including registration numbers, names, email contacts, academic departments, year levels, contact numbers, and personal demographics. When handled manually or through fragmented spreadsheet files, institutions inevitably encounter duplicated entries, inconsistent updates across offices, sluggish search capabilities, and the inability to reliably verify academic history. To resolve these challenges, modern educational organizations adopt web-based, centralized Student Management Systems backed by scalable cloud databases and RESTful application programming interfaces (APIs)."))

    story.append(Paragraph("Core Problem Statement & Topic Assignment", h2_style))
    story.append(p("<b>Consider a Student Management System in which students can be added, viewed, updated and deleted. Design the required Express.js API routes and explain how each route interacts with MongoDB to perform the corresponding operation.</b> Implement the system using React, Node.js, Express.js, and MongoDB Atlas, and deploy the application to public cloud platforms."))

    story.append(Paragraph("Key Academic & Technical Objectives:", h3_style))
    story.append(b("<b>1. Data Modeling:</b> Store student details including roll number, full name, email, department, and academic year, alongside personal attributes (phone, date of birth, gender, address)."))
    story.append(b("<b>2. MongoDB Integration:</b> Create and manage a MongoDB database (<code>test</code>) and <code>students</code> collection utilizing an appropriate BSON document structure and indexed constraints."))
    story.append(b("<b>3. Route Architecture:</b> Design RESTful API routes in Express.js supporting complete CRUD operations (Create, Read all, Read single, Update, and Delete) with rigorous error handling and validation."))
    story.append(b("<b>4. Database Interaction Analysis:</b> Provide an in-depth mechanical explanation of how each Express.js route executes Mongoose operations and issues corresponding commands to MongoDB Atlas."))
    story.append(b("<b>5. Client User Interface:</b> Implement client-side search, department filtering, and academic year filtering over the retrieved student records in React."))
    story.append(b("<b>6. Cloud Deployment:</b> Deploy the frontend (Vercel), backend (Render), and database (MongoDB Atlas) to public cloud platforms with secure environment variable isolation."))
    story.append(b("<b>7. Case Study Debugging:</b> Investigate a critical real-world failure mode where student records are successfully added to MongoDB but updated records fail to reflect in the user interface, and provide a systematic debugging workflow."))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # PART B – 1: REQUIREMENT ANALYSIS & SYSTEM DESIGN
    # -------------------------------------------------------------------------
    story.append(Paragraph("PART B – 1. REQUIREMENT ANALYSIS & SYSTEM DESIGN", h1_style))
    story.append(Paragraph("1. Functional Requirements Analysis", h2_style))
    
    req_data = [
        [Paragraph("<b>Requirement Area</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>System Expectation</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>EduSphere Implementation Details</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white))],
        [Paragraph("<b>Student Identity</b>", body_style), Paragraph("Unique institutional identifier", body_style), Paragraph("Roll number (e.g. A24126552079) with unique index; immutable MongoDB _id (ObjectId)", body_style)],
        [Paragraph("<b>Student Info</b>", body_style), Paragraph("Academic & personal capture", body_style), Paragraph("Captures rollNumber, name, email, department, year, phone, dob, gender, address", body_style)],
        [Paragraph("<b>Data Storage</b>", body_style), Paragraph("Fault-tolerant document storage", body_style), Paragraph("MongoDB Atlas cloud cluster (test database, students collection)", body_style)],
        [Paragraph("<b>API Layer</b>", body_style), Paragraph("Standardized RESTful CRUD interface", body_style), Paragraph("Express.js REST API with JSON body parsing and CORS headers", body_style)],
        [Paragraph("<b>Search & Filter</b>", body_style), Paragraph("Fast discovery of student records", body_style), Paragraph("Search by name/rollNo/email; dropdown filtering by department and year", body_style)],
        [Paragraph("<b>Validation</b>", body_style), Paragraph("Duplicate key & invalid input rejection", body_style), Paragraph("Schema validators, unique indexes, and mapping MongoDB error 11000 to HTTP 409", body_style)]
    ]
    req_table = Table(req_data, colWidths=[110, 160, 234])
    req_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(req_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("2. Three-Tier System Architecture", h2_style))
    story.append(p("EduSphere adheres to a clean Three-Tier Web Architecture ensuring separation of concerns, maintainability, and enterprise-grade security:"))
    
    arch_ascii = (
        "       +-------------------------------------------------------+\n"
        "       |             CLIENT TIER (User Browser)                |\n"
        "       |  React 18 Single-Page Application (Hosted on Vercel)  |\n"
        "       |  - Dashboard Overview, Metric Cards, Search & Filters |\n"
        "       |  - Add/Edit Student Forms & Delete Confirmation Modal |\n"
        "       +-------------------------------------------------------+\n"
        "                                   |\n"
        "                                   | HTTPS / Asynchronous Axios Calls\n"
        "                                   | REST Requests (application/json)\n"
        "                                   v\n"
        "       +-------------------------------------------------------+\n"
        "       |             APPLICATION TIER (REST API)               |\n"
        "       |  Node.js + Express.js Web Server (Hosted on Render)   |\n"
        "       |  - CORS Security Middleware & JSON Body Parsing       |\n"
        "       |  - RESTful Route Handlers (/api/students)             |\n"
        "       |  - Mongoose Schema Validation & Business Rules        |\n"
        "       +-------------------------------------------------------+\n"
        "                                   |\n"
        "                                   | Mongoose Object Data Modeling (ODM)\n"
        "                                   | Wire Protocol over TLS/SSL\n"
        "                                   v\n"
        "       +-------------------------------------------------------+\n"
        "       |             DATABASE TIER (Storage Layer)             |\n"
        "       |       MongoDB Atlas Cloud Database Cluster            |\n"
        "       |  - Database: `test` | Collection: `students`          |\n"
        "       |  - BSON Document Storage & Unique Primary Key Indexes |\n"
        "       +-------------------------------------------------------+"
    )
    story.append(Preformatted(arch_ascii, code_style))

    story.append(Paragraph("3. Main Functional Modules", h2_style))
    story.append(b("<b>• Institutional Dashboard:</b> Presents total enrolled student count, active department count, department-wise student distribution cards, and real-time backend operational status."))
    story.append(b("<b>• Student Directory:</b> Displays student records in a structured tabular directory with instant search (name, roll number, email) and department/year filter dropdowns."))
    story.append(b("<b>• Add Student Module:</b> Interactive modal form capturing academic and personal details with client-side and server-side constraint checks."))
    story.append(b("<b>• Student Profile Viewer:</b> Dedicated profile view displaying individual student records, avatar initials, enrollment dates, and audit timestamps."))
    story.append(b("<b>• Edit Student Module:</b> Pre-populates existing student attributes for modification and dispatches PUT requests to update MongoDB documents."))
    story.append(b("<b>• Delete Confirmation Guard:</b> Prevents accidental deletions by presenting a safety modal requiring explicit confirmation prior to issuing DELETE commands."))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # PART B – 2: MONGODB DOCUMENT MODEL & DATABASE OPERATIONS
    # -------------------------------------------------------------------------
    story.append(Paragraph("PART B – 2. MONGODB DOCUMENT MODEL & DATABASE OPERATIONS", h1_style))
    story.append(Paragraph("1. Document-Oriented Data Modeling", h2_style))
    story.append(p("Relational databases enforce rigid tabular schemas requiring complex foreign key joins to represent multidimensional records. In contrast, MongoDB's document model represents each student entity as a self-contained, flexible BSON (Binary JSON) document. This model offers high write throughput, seamless schema extensibility, and direct JSON impedance match with React and Node.js."))

    story.append(Paragraph("2. MongoDB Document Schema Representation (JSON / BSON)", h2_style))
    doc_json = (
        '{\n'
        '  "_id": ObjectId("6730a1b2c3d4e5f6a7b8c9d0"),\n'
        '  "rollNumber": "A24126552079",\n'
        '  "name": "Suswetha Dwarapudi",\n'
        '  "email": "suswetha.dwarapudi@example.com",\n'
        '  "department": "CSE",\n'
        '  "year": 3,\n'
        '  "phone": "+91 9876543210",\n'
        '  "dateOfBirth": ISODate("2004-05-18T00:00:00.000Z"),\n'
        '  "gender": "Female",\n'
        '  "address": "Visakhapatnam, Andhra Pradesh",\n'
        '  "createdAt": ISODate("2026-11-10T10:15:30.000Z"),\n'
        '  "updatedAt": ISODate("2026-11-10T10:15:30.000Z"),\n'
        '  "__v": 0\n'
        '}'
    )
    story.append(Preformatted(doc_json, code_style))

    story.append(Paragraph("3. Document Fields, Data Types, and Constraints", h2_style))
    fld_data = [
        [Paragraph("<b>Field Name</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>BSON / JS Type</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Validation Constraints</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Functional Purpose</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white))],
        [Paragraph("<b>_id</b>", body_style), Paragraph("ObjectId", body_style), Paragraph("Primary Key, Auto-generated", body_style), Paragraph("Unique 12-byte BSON identifier", body_style)],
        [Paragraph("<b>rollNumber</b>", body_style), Paragraph("String", body_style), Paragraph("Required, Unique Index, Trim", body_style), Paragraph("Institutional student ID (A24126552079)", body_style)],
        [Paragraph("<b>name</b>", body_style), Paragraph("String", body_style), Paragraph("Required, Trim, Min length 2", body_style), Paragraph("Student full legal name", body_style)],
        [Paragraph("<b>email</b>", body_style), Paragraph("String", body_style), Paragraph("Required, Unique Index, Regex", body_style), Paragraph("Contact email address", body_style)],
        [Paragraph("<b>department</b>", body_style), Paragraph("String", body_style), Paragraph("Required, Enum (CSE, AI&DS...)", body_style), Paragraph("Academic discipline / branch", body_style)],
        [Paragraph("<b>year</b>", body_style), Paragraph("Number", body_style), Paragraph("Required, Min 1, Max 4", body_style), Paragraph("Current academic year (1-4)", body_style)],
        [Paragraph("<b>phone / dob</b>", body_style), Paragraph("String / Date", body_style), Paragraph("Optional personal attributes", body_style), Paragraph("Emergency contact & birth date", body_style)],
        [Paragraph("<b>createdAt / updatedAt</b>", body_style), Paragraph("Date", body_style), Paragraph("Managed by Mongoose timestamps", body_style), Paragraph("Audit timestamps tracking lifecycle", body_style)]
    ]
    fld_table = Table(fld_data, colWidths=[90, 85, 155, 174])
    fld_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(fld_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("4. Native MongoDB Shell (mongosh) CRUD Queries", h2_style))
    shell_queries = (
        "// Switch database\n"
        "use test;\n\n"
        "// 1. Insert student record (POST)\n"
        "db.students.insertOne({ rollNumber: 'A24126552079', name: 'Suswetha Dwarapudi', department: 'CSE', year: 3 });\n\n"
        "// 2. Query all student records (GET)\n"
        "db.students.find({}).sort({ createdAt: -1 });\n\n"
        "// 3. Find student by unique roll number (GET by roll)\n"
        "db.students.findOne({ rollNumber: 'A24126552079' });\n\n"
        "// 4. Update student department & year (PUT)\n"
        "db.students.updateOne({ rollNumber: 'A24126552079' }, { $set: { department: 'CSE', year: 3, updatedAt: new Date() } });\n\n"
        "// 5. Delete student record (DELETE)\n"
        "db.students.deleteOne({ rollNumber: 'A24126552079' });\n\n"
        "// 6. Verify index execution\n"
        "db.students.find({ rollNumber: 'A24126552079' }).explain('executionStats');"
    )
    story.append(Preformatted(shell_queries, code_style))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # PART B – 3: BACKEND & FRONTEND IMPLEMENTATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("PART B – 3. BACKEND & FRONTEND IMPLEMENTATION", h1_style))
    story.append(Paragraph("1. Express.js REST API Route Design", h2_style))
    story.append(p("The backend exposes a RESTful interface over `/api/students`. Each route corresponds to a standard HTTP verb, URL pattern, controller logic, and database query:"))

    api_data = [
        [Paragraph("<b>HTTP Verb</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Route Endpoint</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Purpose & Action</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>HTTP Status Codes</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white))],
        [Paragraph("<b>POST</b>", body_style), Paragraph("/api/students", body_style), Paragraph("Create and persist new student record", body_style), Paragraph("201 Created | 400 | 409", body_style)],
        [Paragraph("<b>GET</b>", body_style), Paragraph("/api/students", body_style), Paragraph("Retrieve all student records with sorting", body_style), Paragraph("200 OK | 500 Error", body_style)],
        [Paragraph("<b>GET</b>", body_style), Paragraph("/api/students/:id", body_style), Paragraph("Retrieve single student profile by document ID", body_style), Paragraph("200 OK | 400 | 404", body_style)],
        [Paragraph("<b>PUT</b>", body_style), Paragraph("/api/students/:id", body_style), Paragraph("Update student attributes by document ID", body_style), Paragraph("200 OK | 400 | 404 | 409", body_style)],
        [Paragraph("<b>DELETE</b>", body_style), Paragraph("/api/students/:id", body_style), Paragraph("Permanently remove student record by ID", body_style), Paragraph("200 OK | 400 | 404", body_style)]
    ]
    api_table = Table(api_data, colWidths=[65, 120, 194, 125])
    api_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(api_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("2. Detailed Explanation: How Each Route Interacts with MongoDB", h2_style))
    
    story.append(Paragraph("A. Add Student Route (POST /api/students)", h3_style))
    story.append(b("<b>1. Payload Receipt:</b> Express parses JSON into <code>req.body</code>."))
    story.append(b("<b>2. Model Instantiation:</b> Mongoose runs <code>const student = new Student(req.body)</code>, checking schema validations."))
    story.append(b("<b>3. MongoDB Write Command:</b> Executing <code>await student.save()</code> transmits an <code>insertOne</code> command to MongoDB Atlas."))
    story.append(b("<b>4. Conflict Interception:</b> If roll number or email violates a unique index, MongoDB throws error code <code>11000</code>. The handler catches this and returns HTTP 409 Conflict."))
    story.append(b("<b>5. Persistence & Return:</b> MongoDB persists the BSON document, assigns an immutable <code>_id</code> ObjectId, attaches timestamps, and returns HTTP 201 Created."))

    story.append(Paragraph("B. View All Students Route (GET /api/students)", h3_style))
    story.append(b("<b>1. Query Inspection:</b> Express extracts optional parameters (department, year, search) from <code>req.query</code>."))
    story.append(b("<b>2. Query Construction:</b> Mongoose synthesizes query clauses (e.g. regex on name, rollNumber, email)."))
    story.append(b("<b>3. Database Cursor Scan:</b> <code>Student.find(query).sort({ createdAt: -1 })</code> executes a <code>find</code> command on MongoDB Atlas."))
    story.append(b("<b>4. Document Hydration:</b> MongoDB streams matching documents ordered by creation date, which Mongoose hydrates into JavaScript objects."))
    story.append(b("<b>5. Response:</b> Returns HTTP 200 OK with total count and students array."))

    story.append(Paragraph("C. View Single Student Route (GET /api/students/:id)", h3_style))
    story.append(b("<b>1. Parameter Capture:</b> Extracts document ID from <code>req.params.id</code>."))
    story.append(b("<b>2. Key Lookup:</b> <code>Student.findById(id)</code> casts the ID to BSON <code>ObjectId(id)</code> and issues <code>findOne({ _id: ObjectId(id) })</code>."))
    story.append(b("<b>3. Result:</b> MongoDB performs an O(1) indexed lookup. Returns HTTP 200 OK with student record or HTTP 404 Not Found."))

    story.append(Paragraph("D. Update Student Route (PUT /api/students/:id)", h3_style))
    story.append(b("<b>1. Input Ingestion:</b> Captures document ID from parameters and updated fields from body."))
    story.append(b("<b>2. Atomic Database Update:</b> <code>Student.findByIdAndUpdate(id, req.body, { new: true, runValidators: true })</code> triggers MongoDB's atomic <code>findOneAndUpdate({ _id: ObjectId(id) }, { $set: updateFields })</code>."))
    story.append(b("<b>3. Crucial Options:</b> <code>{ new: true }</code> ensures MongoDB returns the updated document rather than the old pre-update document. <code>{ runValidators: true }</code> re-evaluates validation rules."))
    story.append(b("<b>4. Conflict Protection:</b> Detects duplicate roll numbers during updates and responds with HTTP 409. Returns HTTP 200 OK on success."))

    story.append(Paragraph("E. Delete Student Route (DELETE /api/students/:id)", h3_style))
    story.append(b("<b>1. Parameter Capture:</b> Extracts student ID from <code>req.params.id</code>."))
    story.append(b("<b>2. MongoDB Deletion:</b> <code>Student.findByIdAndDelete(id)</code> triggers MongoDB's <code>findOneAndDelete({ _id: ObjectId(id) })</code>."))
    story.append(b("<b>3. Removal:</b> Document is permanently excised from storage. Returns HTTP 200 OK confirming deletion."))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # PART B – 4: TESTING, DEBUGGING & VALIDATION
    # -------------------------------------------------------------------------
    story.append(Paragraph("PART B – 4. TESTING, DEBUGGING & VALIDATION", h1_style))
    story.append(Paragraph("1. In-Depth Analysis of the Case Study Problem", h2_style))
    story.append(p("<b>Problem Scenario:</b> A deployed Student Management System successfully adds new student records to MongoDB Atlas, but after editing a student record, the user interface fails to display the updated information."))
    story.append(p("A successful database write (HTTP 200/201) and a refreshed user interface are separate operations in a multi-tier web application. When an update succeeds in MongoDB but fails to appear on screen, the breakdown can occur across several layers: client-side state management, asynchronous execution timing, backend route parameters, Mongoose return options, browser caching, or database cluster mismatches."))

    story.append(Paragraph("2. Multi-Layer Debugging Failure Matrix", h2_style))
    diag_data = [
        [Paragraph("<b>Architectural Layer</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Root Cause Description</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Diagnostic Procedure & Systematic Resolution</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white))],
        [Paragraph("<b>React State Staleness</b>", body_style), Paragraph("Frontend does not re-fetch list after PUT request", body_style), Paragraph("Ensure `await fetchStudents()` is called immediately after a successful PUT response to reload server state.", body_style)],
        [Paragraph("<b>Async Race Condition</b>", body_style), Paragraph("List refresh query executes before write finishes", body_style), Paragraph("Ensure the Axios PUT request is explicitly awaited before triggering the GET request.", body_style)],
        [Paragraph("<b>Mongoose Options</b>", body_style), Paragraph("Missing `{ new: true }` in `findByIdAndUpdate` returns old document", body_style), Paragraph("Add `{ new: true, runValidators: true }` so Mongoose returns the updated document.", body_style)],
        [Paragraph("<b>Document ID Mismatch</b>", body_style), Paragraph("Backend update route uses `rollNumber` instead of `_id`", body_style), Paragraph("Verify that the PUT request URL is `/api/students/${student._id}` where `_id` is the BSON ObjectId.", body_style)],
        [Paragraph("<b>Environment Disconnect</b>", body_style), Paragraph("Backend connects to a different Atlas database", body_style), Paragraph("Verify Render `MONGO_URI`. Open MongoDB Atlas Data Explorer and confirm writes in `test.students`.", body_style)],
        [Paragraph("<b>CORS / Verb Blocking</b>", body_style), Paragraph("Browser blocks PUT preflight options check", body_style), Paragraph("Configure Express CORS middleware with `app.use(cors())` permitting PUT/DELETE from Vercel domain.", body_style)]
    ]
    diag_table = Table(diag_data, colWidths=[110, 160, 234])
    diag_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(diag_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("3. Step-by-Step Systematic Debugging Sequence", h2_style))
    story.append(b("<b>Step 1: Isolated Reproduction:</b> Select a specific test student (Roll No: A24126552079) and log current values and target values."))
    story.append(b("<b>Step 2: Network Inspection:</b> Open Chrome DevTools -> Network tab. Submit update form and inspect PUT request URL, method, and payload."))
    story.append(b("<b>Step 3: Response Status Validation:</b> Verify that the server returns HTTP 200 OK and inspect the returned JSON body."))
    story.append(b("<b>Step 4: Backend Logs Analysis:</b> Examine Render logs for schema validation errors or duplicate-key conflicts."))
    story.append(b("<b>Step 5: Direct Database Verification:</b> Log into MongoDB Atlas -> Data Explorer -> test.students. Verify that the updated field and `updatedAt` have changed in storage."))
    story.append(b("<b>Step 6: Direct API Query:</b> Send an independent GET request (`curl -s .../api/students`) to verify the REST API returns the updated document."))
    story.append(b("<b>Step 7: State Management Verification:</b> Inspect React component state. Verify that `fetchStudents()` sets the new array into state."))
    story.append(b("<b>Step 8: Persistence Confirmation:</b> Hard refresh browser (Ctrl+F5). Confirm updated values remain visible."))

    story.append(Paragraph("4. Test Case Validation Matrix", h2_style))
    tc_data = [
        [Paragraph("<b>Test ID</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Test Action & Input</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Expected Outcome</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Evidence & Status</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white))],
        [Paragraph("<b>TC-01</b>", body_style), Paragraph("Navigate to root URL", body_style), Paragraph("Dashboard loads with metrics, student count, cards", body_style), Paragraph("<font color='#16A34A'><b>Figure 1 | Passed</b></font>", body_style)],
        [Paragraph("<b>TC-02</b>", body_style), Paragraph("View Student Directory", body_style), Paragraph("Students collection retrieved via GET and listed in table", body_style), Paragraph("<font color='#16A34A'><b>Figure 2 | Passed</b></font>", body_style)],
        [Paragraph("<b>TC-03</b>", body_style), Paragraph("Submit Add Student form", body_style), Paragraph("Record saved to MongoDB via POST; list refreshes", body_style), Paragraph("<font color='#16A34A'><b>Figure 3 | Passed</b></font>", body_style)],
        [Paragraph("<b>TC-04</b>", body_style), Paragraph("Submit duplicate roll number", body_style), Paragraph("Backend rejects insertion; returns HTTP 409 Conflict", body_style), Paragraph("<font color='#16A34A'><b>Conflict Guard | Passed</b></font>", body_style)],
        [Paragraph("<b>TC-05</b>", body_style), Paragraph("Click student profile view", body_style), Paragraph("Student details displayed in profile view via GET /:id", body_style), Paragraph("<font color='#16A34A'><b>Figure 4 | Passed</b></font>", body_style)],
        [Paragraph("<b>TC-06</b>", body_style), Paragraph("Submit Edit Student form", body_style), Paragraph("Attributes updated in MongoDB via PUT; updated in UI", body_style), Paragraph("<font color='#16A34A'><b>Figure 5 | Passed</b></font>", body_style)],
        [Paragraph("<b>TC-07</b>", body_style), Paragraph("Click Delete button", body_style), Paragraph("Safety confirmation dialog displayed before DELETE", body_style), Paragraph("<font color='#16A34A'><b>Figure 6 | Passed</b></font>", body_style)],
        [Paragraph("<b>TC-08</b>", body_style), Paragraph("Inspect MongoDB Atlas", body_style), Paragraph("Student documents verified in test.students collection", body_style), Paragraph("<font color='#16A34A'><b>Figure 7 | Passed</b></font>", body_style)],
        [Paragraph("<b>TC-09</b>", body_style), Paragraph("Verify cloud deployment", body_style), Paragraph("Render backend Live; Vercel frontend Ready", body_style), Paragraph("<font color='#16A34A'><b>Figures 8 & 9 | Passed</b></font>", body_style)]
    ]
    tc_table = Table(tc_data, colWidths=[55, 145, 184, 120])
    tc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(tc_table)
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # PART B – 5: CLOUD DEPLOYMENT & SECURITY
    # -------------------------------------------------------------------------
    story.append(Paragraph("PART B – 5. CLOUD DEPLOYMENT & SECURITY", h1_style))
    story.append(Paragraph("1. Cloud Hosting Architecture", h2_style))
    story.append(p("EduSphere is architected across three industry-standard cloud tiers, ensuring high availability, continuous deployment from GitHub, and complete credential isolation:"))

    dep_data = [
        [Paragraph("<b>Layer</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Cloud Platform</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Project Identifier</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Configuration Details</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white))],
        [Paragraph("<b>Frontend</b>", body_style), Paragraph("Vercel", body_style), Paragraph("edusphere-frontend-suswetha", body_style), Paragraph("Vite build (`dist`), global edge CDN distribution", body_style)],
        [Paragraph("<b>Backend</b>", body_style), Paragraph("Render", body_style), Paragraph("edusphere-backend-suswetha", body_style), Paragraph("Node.js Web Service, `npm install` build, `npm start` start", body_style)],
        [Paragraph("<b>Database</b>", body_style), Paragraph("MongoDB Atlas", body_style), Paragraph("Cluster0 / AURAFIT", body_style), Paragraph("Cloud replica set, database `test`, collection `students`", body_style)]
    ]
    dep_table = Table(dep_data, colWidths=[80, 100, 134, 190])
    dep_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(dep_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("2. Environment Variable Configuration", h2_style))
    env_data = [
        [Paragraph("<b>Variable</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Configured Location</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Sensitivity</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white)),
         Paragraph("<b>Operational Purpose</b>", ParagraphStyle('TH', parent=body_style, fontName='Helvetica-Bold', textColor=colors.white))],
        [Paragraph("<b>MONGO_URI</b>", body_style), Paragraph("Render Backend Service", body_style), Paragraph("<font color='#DC2626'><b>HIGH SECRET</b></font>", body_style), Paragraph("Encrypted connection string with database credentials", body_style)],
        [Paragraph("<b>PORT</b>", body_style), Paragraph("Render Runtime", body_style), Paragraph("Standard", body_style), Paragraph("Port assigned dynamically by Render (defaults to 5000)", body_style)],
        [Paragraph("<b>VITE_API_URL</b>", body_style), Paragraph("Vercel Frontend Project", body_style), Paragraph("Public", body_style), Paragraph("Base URL pointing to the live Render REST API endpoint", body_style)]
    ]
    env_table = Table(env_data, colWidths=[90, 130, 90, 194])
    env_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor("#F8FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(env_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("3. Cloud Security Best Practices", h2_style))
    story.append(b("<b>• Secret Isolation:</b> <code>MONGO_URI</code> is stored exclusively inside Render's environment secret manager and never placed in frontend code, client-side <code>.env</code> files, or committed to GitHub."))
    story.append(b("<b>• Version Control Hygiene:</b> <code>.gitignore</code> explicitly excludes all local <code>.env</code> and <code>node_modules</code> folders to prevent credential leakage."))
    story.append(b("<b>• Origin Validation:</b> The Express.js backend enforces CORS validation to restrict which origins can execute state-changing requests."))
    story.append(b("<b>• HTTPS / TLS Encryption:</b> All production traffic between browser, backend, and MongoDB Atlas runs over TLS/SSL encryption."))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # PART C: OUTPUT SCREENSHOTS AND EVIDENCE
    # -------------------------------------------------------------------------
    story.append(Paragraph("PART C. OUTPUT SCREENSHOTS AND EVIDENCE", h1_style))
    story.append(p("The following figures document the live implementation, responsive user interface workflows, database persistence, and cloud hosting status of EduSphere:"))

    screenshots = [
        ("case_study/output_screenshots/01_dashboard.png", "Figure 1. EduSphere institutional dashboard showing total student count, department metrics, and quick action bar.", 460, 210),
        ("case_study/output_screenshots/02_dashboard_2.png", "Figure 2. Student directory view showing stored student records, roll numbers, departments, and action buttons.", 460, 210),
        ("case_study/output_screenshots/03_add_new_student.png", "Figure 3. Add Student modal form capturing roll number, name, email, department, and academic year.", 460, 210),
        ("case_study/output_screenshots/04_view_student.png", "Figure 4. Student profile viewer displaying detailed academic standing, contact email, and audit timestamps.", 460, 210),
        ("case_study/output_screenshots/05_edit_student.png", "Figure 5. Edit Student modal populated with existing student data, demonstrating field modification workflow.", 460, 210),
        ("case_study/output_screenshots/06_delete_student.png", "Figure 6. Safety deletion confirmation modal displayed prior to permanent document removal.", 460, 210),
        ("case_study/output_screenshots/07_mongodb_atlas.png", "Figure 7. MongoDB Atlas Data Explorer showing test.students collection with stored BSON student documents.", 460, 210),
        ("case_study/output_screenshots/08_render_backend.png", "Figure 8. Render dashboard showing edusphere-backend-suswetha Node.js web service running with Live deployment status.", 460, 210),
        ("case_study/output_screenshots/09_vercel_frontend.png", "Figure 9. Vercel deployment console showing edusphere-frontend-suswetha production deployment with Ready status.", 460, 210)
    ]

    for idx, (img_path, caption, w, h) in enumerate(screenshots):
        if os.path.exists(img_path):
            img_item = Image(img_path, width=w, height=h)
            cap_item = Paragraph(caption, caption_style)
            story.append(KeepTogether([img_item, Spacer(1, 4), cap_item, Spacer(1, 8)]))
            # Put 2 screenshots per page
            if idx % 2 == 1 and idx < len(screenshots) - 1:
                story.append(PageBreak())

    story.append(Paragraph("Evidence Interpretation & Architecture Validation", h2_style))
    story.append(p("The execution evidence verifies end-to-end full-stack integration: Figures 1-6 validate that all student management workflows (create, read, update, delete, view profile) are operational within the browser interface. Figure 7 confirms persistent BSON storage within MongoDB Atlas. Figures 8 and 9 demonstrate that the three-layer architecture has been deployed and operationalized across independent cloud environments."))
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # CONCLUSION, LIMITATIONS & FUTURE ENHANCEMENTS
    # -------------------------------------------------------------------------
    story.append(Paragraph("CONCLUSION, LIMITATIONS & FUTURE ENHANCEMENTS", h1_style))
    story.append(Paragraph("1. Expected Outcome & Project Achievements", h2_style))
    story.append(b("<b>• Full-Stack Integration:</b> Designed and deployed a modern, responsive Single-Page Application using React 18, Vite, and Lucide React."))
    story.append(b("<b>• Robust REST API:</b> Engineered RESTful Express.js API routes under <code>/api/students</code> mapping to MongoDB CRUD operations with Mongoose ODM."))
    story.append(b("<b>• Database Interaction Clarity:</b> Detailed the exact mechanical interactions between Express.js routes and MongoDB write/read commands."))
    story.append(b("<b>• Systematic Debugging:</b> Developed a repeatable, multi-layer debugging procedure solving the critical case-study issue of stale client views after update."))
    story.append(b("<b>• Production Cloud Deployment:</b> Operationalized the frontend on Vercel, the backend on Render, and persistent data on MongoDB Atlas with complete secret isolation."))

    story.append(Paragraph("2. System Limitations", h2_style))
    story.append(b("<b>• Open Public Access:</b> Currently, any user visiting the public URL can perform edit and delete operations. Role-based access control is needed for production."))
    story.append(b("<b>• Client-Side Pagination:</b> The GET endpoint loads all students simultaneously. Datasets exceeding thousands of records would require server-side pagination."))
    story.append(b("<b>• Cold Start Latency:</b> Render's free compute tier spins down after 15 minutes of inactivity, resulting in a 30-50 second latency window upon initial wake-up."))

    story.append(Paragraph("3. Future Enhancements", h2_style))
    story.append(b("<b>• Role-Based Authentication:</b> Implement JSON Web Token (JWT) role-based authentication distinguishing administrators, faculty, and students."))
    story.append(b("<b>• Server-Side Pagination:</b> Incorporate server-side pagination (<code>limit</code> and <code>skip</code>) to optimize query throughput for large institutional datasets."))
    story.append(b("<b>• Data Export Capabilities:</b> Provide one-click export of student records into standard CSV and formatted PDF transcripts."))
    story.append(b("<b>• Audit Trail Logging:</b> Implement an audit logging collection in MongoDB tracking user ID, IP address, timestamp, and field deltas on every record modification."))

    story.append(Paragraph("4. References & Documentation", h2_style))
    story.append(b("<b>• ANITS Course Syllabus:</b> Anil Neerukonda Institute of Technology & Sciences, Syllabus 23CM4121 (Unit V – MongoDB and Deploying Applications)."))
    story.append(b("<b>• MongoDB Manual:</b> MongoDB Atlas and BSON Architecture Documentation (https://www.mongodb.com/docs/)."))
    story.append(b("<b>• Express.js Documentation:</b> Express.js API Reference and Routing Guide (https://expressjs.com/)."))
    story.append(b("<b>• Mongoose Documentation:</b> Mongoose ODM Models, Queries, and Validation (https://mongoosejs.com/docs/)."))
    story.append(b("<b>• React Documentation:</b> React 18 Component State and Hooks Guide (https://react.dev/)."))
    story.append(b("<b>• Cloud Hosting Guides:</b> Render Cloud Web Services & Vercel Global Deployment Documentation."))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated and saved to {filename}")

if __name__ == "__main__":
    build_pdf()
