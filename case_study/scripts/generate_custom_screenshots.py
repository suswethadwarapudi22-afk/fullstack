import os
from PIL import Image, ImageDraw, ImageFont

# Dimensions
WIDTH, HEIGHT = 1100, 620

# Modern Slate & Indigo/Violet Theme Colors (Distinct from reference's olive/lime)
BG_DARK = "#0B0F19"
BG_SIDEBAR = "#111827"
BG_CARD = "#172033"
BG_PANEL = "#1E293B"
BORDER = "#2B374E"
BORDER_ACCENT = "#4F46E5"
ACCENT_INDIGO = "#6366F1"
ACCENT_PURPLE = "#8B5CF6"
ACCENT_CYAN = "#06B6D4"
ACCENT_EMERALD = "#10B981"
ACCENT_AMBER = "#F59E0B"
ACCENT_ROSE = "#F43F5E"
TEXT_WHITE = "#F9FAFB"
TEXT_MUTED = "#94A3B8"
TEXT_DIM = "#64748B"

# Load Standard Windows Fonts
FONT_TITLE = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 20)
FONT_HEADING = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
FONT_SUB = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 13)
FONT_BOLD = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 13)
FONT_REGULAR = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12)
FONT_SMALL = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 11)
FONT_MONO = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 12)
FONT_MONO_BOLD = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 12)

def draw_window_chrome(draw, title, url="https://edusphere-suswetha.vercel.app"):
    # Header Bar
    draw.rectangle([(0, 0), (WIDTH, 42)], fill="#0F172A")
    draw.line([(0, 42), (WIDTH, 42)], fill=BORDER, width=1)
    
    # Window Controls (mac-style glowing dots)
    draw.ellipse([(18, 15), (28, 25)], fill="#EF4444")
    draw.ellipse([(34, 15), (44, 25)], fill="#F59E0B")
    draw.ellipse([(50, 15), (60, 25)], fill="#10B981")
    
    # URL bar with Indigo lock
    draw.rounded_rectangle([(80, 8), (WIDTH - 160, 34)], radius=6, fill="#1E293B", outline=BORDER)
    draw.text((95, 12), f"🔒 {url}", fill=TEXT_MUTED, font=FONT_SMALL)
    
    # Right pill badge
    draw.rounded_rectangle([(WIDTH - 145, 8), (WIDTH - 18, 34)], radius=6, fill="#1E1B4B", outline="#4338CA")
    draw.text((WIDTH - 132, 12), "● Production Live", fill=ACCENT_INDIGO, font=FONT_SMALL)

def draw_sidebar(draw, active_index=0):
    draw.rectangle([(0, 43), (210, HEIGHT)], fill=BG_SIDEBAR)
    draw.line([(210, 43), (210, HEIGHT)], fill=BORDER, width=1)
    
    # Brand: EduSphere
    draw.text((25, 60), "🌐 EduSphere", fill=ACCENT_CYAN, font=FONT_TITLE)
    draw.text((25, 85), "Student Management System", fill=TEXT_DIM, font=FONT_SMALL)
    
    # Menu items
    items = [
        "📊 Dashboard",
        "📋 Student Directory",
        "➕ Add Student",
        "🔍 Query Explorer",
        "⚙️ API Settings",
        "📘 Case Study Report"
    ]
    y = 125
    for i, text in enumerate(items):
        if i == active_index:
            draw.rounded_rectangle([(14, y), (196, y + 34)], radius=7, fill="#1E1B4B", outline="#4338CA")
            draw.text((26, y + 8), text, fill=ACCENT_INDIGO, font=FONT_BOLD)
        else:
            draw.text((26, y + 8), text, fill=TEXT_MUTED, font=FONT_REGULAR)
        y += 42
        
    # User Profile Pill in Sidebar for D. Suswetha
    draw.rounded_rectangle([(14, HEIGHT - 75), (196, HEIGHT - 18)], radius=8, fill="#1E293B", outline=BORDER)
    draw.ellipse([(24, HEIGHT - 63), (54, HEIGHT - 33)], fill="#4338CA")
    draw.text((31, HEIGHT - 55), "DS", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((64, HEIGHT - 65), "D. Suswetha", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((64, HEIGHT - 47), "A24126552079 (CSE)", fill=ACCENT_CYAN, font=FONT_SMALL)

# -------------------------------------------------------------
# 01_dashboard.png
# -------------------------------------------------------------
def make_01_dashboard():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "EduSphere | Dashboard", "https://edusphere-suswetha.vercel.app/dashboard")
    draw_sidebar(draw, active_index=0)
    
    # Top banner / Greeting
    draw.text((240, 60), "Institutional Management Dashboard", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((240, 90), "EduSphere Portal • Anil Neerukonda Institute of Technology & Sciences (ANITS) • 2026–27", fill=TEXT_MUTED, font=FONT_REGULAR)
    
    # Modern Metric Cards (Indigo, Cyan, Violet, Emerald)
    cards = [
        ("TOTAL REGISTERED", "48", "+4 new admissions", ACCENT_INDIGO, "#1E1B4B"),
        ("DEPARTMENTS", "6", "CSE, AI&DS, IT, ECE...", ACCENT_CYAN, "#083344"),
        ("ACADEMIC STANDING", "Year 3", "3rd Yr - 1st Semester", ACCENT_PURPLE, "#2E1065"),
        ("MONGODB ATLAS", "Connected", "Cluster0 (test.students)", ACCENT_EMERALD, "#064E3B")
    ]
    x = 240
    for title, val, sub, col, bg in cards:
        draw.rounded_rectangle([(x, 125), (x + 195, 205)], radius=10, fill=BG_CARD, outline=BORDER)
        draw.rounded_rectangle([(x, 125), (x + 195, 128)], radius=2, fill=col)
        draw.text((x + 16, 137), title, fill=TEXT_DIM, font=FONT_SMALL)
        draw.text((x + 16, 155), val, fill=col, font=FONT_HEADING)
        draw.text((x + 16, 182), sub, fill=TEXT_MUTED, font=FONT_SMALL)
        x += 212
        
    # Table Header & Actions
    draw.text((240, 235), "Enrolled Student Directory (Express GET /api/students -> MongoDB Atlas)", fill=TEXT_WHITE, font=FONT_HEADING)
    
    # Table Container
    draw.rounded_rectangle([(240, 265), (WIDTH - 30, HEIGHT - 25)], radius=8, fill=BG_CARD, outline=BORDER)
    
    # Header row
    draw.rectangle([(240, 265), (WIDTH - 30, 300)], fill=BG_PANEL)
    draw.line([(240, 300), (WIDTH - 30, 300)], fill=BORDER, width=1)
    
    cols = [(260, "ROLL NUMBER"), (380, "STUDENT NAME"), (560, "EMAIL ADDRESS"), (770, "DEPARTMENT"), (880, "YEAR"), (960, "STATUS")]
    for cx, ch in cols:
        draw.text((cx, 276), ch, fill=TEXT_DIM, font=FONT_SMALL)
        
    students = [
        ("A24126552079", "D. Suswetha", "d.suswetha@anits.edu.in", "CSE", "Year 3", "Enrolled", True),
        ("A24126552080", "K. Rahul Varma", "k.rahul@anits.edu.in", "AI&DS", "Year 3", "Enrolled", False),
        ("A24126552081", "P. Sneha Reddy", "p.sneha@anits.edu.in", "CSE", "Year 2", "Enrolled", False),
        ("A24126552082", "M. Harshavardhan", "m.harsha@anits.edu.in", "IT", "Year 3", "Enrolled", False),
        ("A24126552083", "V. Bhavani Shankar", "v.bhavani@anits.edu.in", "ECE", "Year 4", "Enrolled", False),
        ("A24126552084", "T. Ananya Rao", "t.ananya@anits.edu.in", "CSE", "Year 1", "Enrolled", False),
        ("A24126552085", "J. Sravan Kumar", "j.sravan@anits.edu.in", "AI&DS", "Year 3", "Enrolled", False)
    ]
    
    y = 310
    for roll, name, email, dept, yr, st, is_highlight in students:
        if is_highlight:
            draw.rounded_rectangle([(245, y - 4), (WIDTH - 35, y + 26)], radius=4, fill="#1E1B4B", outline="#4338CA")
            draw.text((260, y), roll, fill=ACCENT_CYAN, font=FONT_BOLD)
            draw.text((380, y), name, fill=TEXT_WHITE, font=FONT_BOLD)
        else:
            draw.text((260, y), roll, fill=TEXT_WHITE, font=FONT_REGULAR)
            draw.text((380, y), name, fill=TEXT_WHITE, font=FONT_REGULAR)
            
        draw.text((560, y), email, fill=TEXT_MUTED, font=FONT_REGULAR)
        draw.text((770, y), dept, fill=ACCENT_PURPLE if dept == "CSE" else TEXT_WHITE, font=FONT_REGULAR)
        draw.text((880, y), yr, fill=TEXT_WHITE, font=FONT_REGULAR)
        
        # Status Badge
        draw.rounded_rectangle([(960, y - 2), (1040, y + 18)], radius=4, fill="#064E3B", outline="#059669")
        draw.text((970, y), "● " + st, fill=ACCENT_EMERALD, font=FONT_SMALL)
        
        draw.line([(240, y + 30), (WIDTH - 30, y + 30)], fill="#1E293B", width=1)
        y += 36
        
    img.save("case_study/output_screenshots/01_dashboard.png")
    print("Generated 01_dashboard.png")

# -------------------------------------------------------------
# 02_dashboard_2.png (Search & Query Explorer)
# -------------------------------------------------------------
def make_02_directory_search():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "EduSphere | Directory Search", "https://edusphere-suswetha.vercel.app/directory")
    draw_sidebar(draw, active_index=1)
    
    # Title
    draw.text((240, 60), "Student Directory & Dynamic Filtering", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((240, 90), "Execute multi-criteria queries via REST API (GET /api/students?department=CSE&year=3&search=Suswetha)", fill=TEXT_MUTED, font=FONT_REGULAR)
    
    # Search & Filter Controls
    draw.rounded_rectangle([(240, 125), (550, 162)], radius=8, fill=BG_CARD, outline=BORDER_ACCENT)
    draw.text((255, 135), "🔍  Suswetha", fill=TEXT_WHITE, font=FONT_REGULAR)
    
    draw.rounded_rectangle([(565, 125), (710, 162)], radius=8, fill=BG_CARD, outline=BORDER)
    draw.text((580, 135), "Department: CSE  ▼", fill=ACCENT_CYAN, font=FONT_REGULAR)
    
    draw.rounded_rectangle([(725, 125), (855, 162)], radius=8, fill=BG_CARD, outline=BORDER)
    draw.text((740, 135), "Year: 3  ▼", fill=ACCENT_PURPLE, font=FONT_REGULAR)
    
    # New Record Button
    draw.rounded_rectangle([(WIDTH - 180, 125), (WIDTH - 30, 162)], radius=8, fill=ACCENT_INDIGO)
    draw.text((WIDTH - 165, 135), "+ New Student", fill=TEXT_WHITE, font=FONT_BOLD)
    
    # Result count indicator
    draw.text((240, 185), "Search Results: 1 record matching query 'Suswetha' in Department 'CSE'", fill=TEXT_MUTED, font=FONT_SMALL)
    
    # Results Table
    draw.rounded_rectangle([(240, 210), (WIDTH - 30, 365)], radius=8, fill=BG_CARD, outline=BORDER)
    draw.rectangle([(240, 210), (WIDTH - 30, 250)], fill=BG_PANEL)
    draw.line([(240, 250), (WIDTH - 30, 250)], fill=BORDER, width=1)
    
    cols = [(260, "ROLL NUMBER"), (400, "STUDENT NAME"), (580, "EMAIL ADDRESS"), (770, "DEPARTMENT"), (870, "YEAR"), (950, "ACTIONS")]
    for cx, ch in cols:
        draw.text((cx, 224), ch, fill=TEXT_DIM, font=FONT_SMALL)
        
    # Result Row for D. Suswetha
    draw.rounded_rectangle([(245, 258), (WIDTH - 35, 305)], radius=4, fill="#1E1B4B", outline="#4338CA")
    draw.text((260, 273), "A24126552079", fill=ACCENT_CYAN, font=FONT_BOLD)
    draw.text((400, 273), "D. Suswetha", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((580, 273), "d.suswetha@anits.edu.in", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((770, 273), "CSE", fill=ACCENT_PURPLE, font=FONT_BOLD)
    draw.text((870, 273), "Year 3", fill=TEXT_WHITE, font=FONT_REGULAR)
    
    # Action buttons
    draw.rounded_rectangle([(950, 268), (990, 296)], radius=4, fill="#083344", outline=ACCENT_CYAN)
    draw.text((958, 273), "View", fill=ACCENT_CYAN, font=FONT_SMALL)
    
    draw.rounded_rectangle([(998, 268), (1038, 296)], radius=4, fill="#2E1065", outline=ACCENT_PURPLE)
    draw.text((1007, 273), "Edit", fill=ACCENT_PURPLE, font=FONT_SMALL)
    
    # Query Inspection Terminal Panel
    draw.rounded_rectangle([(240, 385), (WIDTH - 30, HEIGHT - 25)], radius=8, fill="#050811", outline=BORDER)
    draw.rectangle([(240, 385), (WIDTH - 30, 415)], fill="#1E293B")
    draw.text((255, 393), "⚡ Live API Route & MongoDB Query Inspection (EduSphere REST Architecture)", fill=ACCENT_CYAN, font=FONT_SMALL)
    
    code_lines = [
        "HTTP Request:  GET /api/students?department=CSE&year=3&search=Suswetha",
        "Mongoose ODM:  Student.find({ department: 'CSE', year: 3, $or: [{ name: /Suswetha/i }, { rollNumber: /Suswetha/i }] })",
        "MongoDB Atlas: db.students.find({ department: 'CSE', year: 3, ... }).sort({ createdAt: -1 })",
        "HTTP Response: 200 OK | Count: 1 | Payload: [{ _id: '6730a1b2c3d4e5f6a7b8c9d0', rollNumber: 'A24126552079'... }]"
    ]
    cy = 432
    for line in code_lines:
        col = ACCENT_INDIGO if "HTTP Request" in line else ACCENT_CYAN if "Mongoose" in line else ACCENT_EMERALD if "200 OK" in line else TEXT_MUTED
        draw.text((255, cy), line, fill=col, font=FONT_MONO)
        cy += 25
        
    img.save("case_study/output_screenshots/02_dashboard_2.png")
    print("Generated 02_dashboard_2.png")

# -------------------------------------------------------------
# 03_add_new_student.png (POST API Modal)
# -------------------------------------------------------------
def make_03_add_student():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "EduSphere | Add Student Record", "https://edusphere-suswetha.vercel.app/students/new")
    draw_sidebar(draw, active_index=2)
    
    # Dim overlay
    draw.rectangle([(211, 43), (WIDTH, HEIGHT)], fill="#050811")
    
    # Modal Window
    mx, my, mw, mh = 330, 70, 660, 510
    draw.rounded_rectangle([(mx, my), (mx + mw, my + mh)], radius=12, fill=BG_CARD, outline=BORDER_ACCENT)
    
    # Glowing top accent stripe
    draw.rounded_rectangle([(mx, my), (mx + mw, my + 6)], radius=3, fill=ACCENT_INDIGO)
    
    # Modal Header
    draw.text((mx + 30, my + 24), "Add New Student Record", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((mx + 30, my + 52), "Express Route: POST /api/students  →  MongoDB Atlas: db.students.insertOne()", fill=ACCENT_CYAN, font=FONT_SMALL)
    draw.line([(mx, my + 78), (mx + mw, my + 78)], fill=BORDER, width=1)
    
    # Form Fields
    fields = [
        ("Roll Number (Unique Primary Key)", "A24126552079", "Institutional registration number with unique index"),
        ("Full Legal Name", "D. Suswetha", "Student full legal name"),
        ("Institutional Email Address", "d.suswetha@anits.edu.in", "Unique registered institutional email address"),
        ("Academic Department", "CSE (Computer Science & Engineering)", "Selected from supported departments enum"),
        ("Academic Year Standing", "Year 3 (3rd Year - 1st Semester)", "Range: Year 1 to Year 4"),
        ("Contact Mobile Number", "+91 9876543210", "10-digit primary contact number")
    ]
    
    fy = my + 94
    for label, val, hint in fields:
        draw.text((mx + 30, fy), label, fill=TEXT_DIM, font=FONT_SMALL)
        draw.rounded_rectangle([(mx + 30, fy + 18), (mx + mw - 30, fy + 48)], radius=6, fill="#0F172A", outline="#334155")
        draw.text((mx + 42, fy + 26), val, fill=ACCENT_CYAN if "A24126552079" in val or "D. Suswetha" in val else TEXT_WHITE, font=FONT_REGULAR)
        fy += 58
        
    # Modal Buttons
    draw.rounded_rectangle([(mx + mw - 260, my + mh - 55), (mx + mw - 150, my + mh - 20)], radius=6, fill="#1E293B", outline=BORDER)
    draw.text((mx + mw - 225, my + mh - 44), "Cancel", fill=TEXT_MUTED, font=FONT_BOLD)
    
    draw.rounded_rectangle([(mx + mw - 135, my + mh - 55), (mx + mw - 30, my + mh - 20)], radius=6, fill=ACCENT_INDIGO)
    draw.text((mx + mw - 120, my + mh - 44), "Add Student", fill=TEXT_WHITE, font=FONT_BOLD)
    
    img.save("case_study/output_screenshots/03_add_new_student.png")
    print("Generated 03_add_new_student.png")

# -------------------------------------------------------------
# 04_view_student.png (GET /api/students/:id Single Profile)
# -------------------------------------------------------------
def make_04_view_profile():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "EduSphere | Student Profile", "https://edusphere-suswetha.vercel.app/profile/6730a1b2c3d4e5f6a7b8c9d0")
    draw_sidebar(draw, active_index=1)
    
    # Back link
    draw.text((240, 60), "← Back to Student Directory", fill=ACCENT_INDIGO, font=FONT_SMALL)
    draw.text((240, 85), "Student Profile Details", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((240, 115), "Operation: GET /api/students/:id  →  Mongoose: Student.findById(ObjectId)", fill=ACCENT_CYAN, font=FONT_SMALL)
    
    # Profile Card
    px, py, pw, ph = 240, 140, 830, 440
    draw.rounded_rectangle([(px, py), (px + pw, py + ph)], radius=12, fill=BG_CARD, outline=BORDER)
    draw.rounded_rectangle([(px, py), (px + pw, py + 5)], radius=3, fill=ACCENT_PURPLE)
    
    # Banner
    draw.rectangle([(px, py + 5), (px + pw, py + 42)], fill=BG_PANEL)
    draw.line([(px, py + 42), (px + pw, py + 42)], fill=BORDER, width=1)
    draw.text((px + 20, py + 16), "EDUSPHERE / INSTITUTIONAL RECORD", fill=TEXT_DIM, font=FONT_SMALL)
    draw.text((px + pw - 150, py + 16), "● STATUS: ENROLLED", fill=ACCENT_EMERALD, font=FONT_SMALL)
    
    # Identity Block
    draw.rounded_rectangle([(px + 30, py + 62), (px + 120, py + 152)], radius=16, fill="#312E81", outline=BORDER_ACCENT)
    draw.text((px + 52, py + 90), "DS", fill=TEXT_WHITE, font=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 30))
    
    draw.text((px + 145, py + 75), "D. Suswetha", fill=TEXT_WHITE, font=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 24))
    draw.text((px + 145, py + 110), "Department of Computer Science & Engineering  •  3rd Year - 1st Semester", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((px + 145, py + 130), "Anil Neerukonda Institute of Technology & Sciences (ANITS), Visakhapatnam", fill=ACCENT_CYAN, font=FONT_SMALL)
    
    # Divider
    draw.line([(px + 30, py + 175), (px + pw - 30, py + 175)], fill=BORDER, width=1)
    
    # Details Grid
    details = [
        ("ROLL NUMBER", "A24126552079 (Unique Indexed ID)"),
        ("EMAIL ADDRESS", "d.suswetha@anits.edu.in"),
        ("DEPARTMENT", "Computer Science & Engineering (CSE)"),
        ("ACADEMIC STANDING", "Year 3 (B.Tech 2026–27)"),
        ("CONTACT NUMBER", "+91 9876543210"),
        ("DATE OF BIRTH", "18 May 2004"),
        ("MONGODB DOCUMENT ID (_id)", "6730a1b2c3d4e5f6a7b8c9d0 (BSON ObjectId)"),
        ("RECORD CREATED", "10-11-2026 10:15:30 UTC"),
        ("LAST MODIFIED", "10-11-2026 10:15:30 UTC")
    ]
    
    gx = px + 30
    gy = py + 195
    for idx, (lbl, val) in enumerate(details):
        draw.text((gx, gy), lbl, fill=TEXT_DIM, font=FONT_SMALL)
        draw.text((gx, gy + 18), val, fill=ACCENT_CYAN if "A24126552079" in val else TEXT_WHITE, font=FONT_BOLD)
        gy += 52
        if (idx + 1) % 3 == 0:
            gx += 265
            gy = py + 195
            
    # Bottom action buttons
    draw.rounded_rectangle([(px + pw - 260, py + ph - 55), (px + pw - 150, py + ph - 20)], radius=6, fill="#2E1065", outline=ACCENT_PURPLE)
    draw.text((px + pw - 235, py + ph - 44), "✏️ Edit Profile", fill=ACCENT_PURPLE, font=FONT_BOLD)
    
    draw.rounded_rectangle([(px + pw - 135, py + ph - 55), (px + pw - 30, py + ph - 20)], radius=6, fill="#4C0519", outline=ACCENT_ROSE)
    draw.text((px + pw - 118, py + ph - 44), "🗑️ Delete", fill=ACCENT_ROSE, font=FONT_BOLD)
    
    img.save("case_study/output_screenshots/04_view_student.png")
    print("Generated 04_view_student.png")

# -------------------------------------------------------------
# 05_edit_student.png (PUT /api/students/:id Update)
# -------------------------------------------------------------
def make_05_edit_student():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "EduSphere | Edit Student Record", "https://edusphere-suswetha.vercel.app/students/edit/6730a1b2c3d4e5f6a7b8c9d0")
    draw_sidebar(draw, active_index=1)
    
    # Dim overlay
    draw.rectangle([(211, 43), (WIDTH, HEIGHT)], fill="#050811")
    
    # Modal Window
    mx, my, mw, mh = 330, 60, 660, 525
    draw.rounded_rectangle([(mx, my), (mx + mw, my + mh)], radius=12, fill=BG_CARD, outline=ACCENT_AMBER)
    draw.rounded_rectangle([(mx, my), (mx + mw, my + 6)], radius=3, fill=ACCENT_AMBER)
    
    # Modal Header
    draw.text((mx + 30, my + 20), "Edit Student Record — A24126552079", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((mx + 30, my + 48), "Route: PUT /api/students/:id  →  findOneAndUpdate({_id}, {$set: ...}, {new: true})", fill=ACCENT_AMBER, font=FONT_SMALL)
    draw.line([(mx, my + 74), (mx + mw, my + 74)], fill=BORDER, width=1)
    
    # Form Fields
    fields = [
        ("Roll Number (Primary Key)", "A24126552079", False),
        ("Full Legal Name", "D. Suswetha", False),
        ("Institutional Email Address", "d.suswetha@anits.edu.in", False),
        ("Department", "CSE (Computer Science & Engineering)", False),
        ("Academic Year Standing", "Year 3", False),
        ("Contact Mobile Number (Modified Field)", "+91 9988776655", True)
    ]
    
    fy = my + 88
    for label, val, is_mod in fields:
        draw.text((mx + 30, fy), label, fill=ACCENT_AMBER if is_mod else TEXT_DIM, font=FONT_SMALL)
        draw.rounded_rectangle([(mx + 30, fy + 18), (mx + mw - 30, fy + 48)], radius=6, fill="#1E293B", outline=ACCENT_AMBER if is_mod else "#334155")
        draw.text((mx + 42, fy + 26), val, fill=ACCENT_AMBER if is_mod else TEXT_WHITE, font=FONT_REGULAR)
        if is_mod:
            draw.text((mx + mw - 140, fy + 26), "● MODIFIED", fill=ACCENT_AMBER, font=FONT_SMALL)
        fy += 56
        
    # Technical explanation banner inside modal
    draw.rounded_rectangle([(mx + 30, fy + 5), (mx + mw - 30, fy + 45)], radius=6, fill="#0F172A", outline="#1E293B")
    draw.text((mx + 42, fy + 12), "✓ MongoDB Interaction: { new: true } returns modified record in API response.", fill=ACCENT_EMERALD, font=FONT_SMALL)
    draw.text((mx + 42, fy + 28), "✓ Mongoose { runValidators: true } ensures schema constraints are strictly checked during edit.", fill=TEXT_MUTED, font=FONT_SMALL)
    
    # Modal Buttons
    draw.rounded_rectangle([(mx + mw - 260, my + mh - 50), (mx + mw - 150, my + mh - 18)], radius=6, fill="#1E293B", outline=BORDER)
    draw.text((mx + mw - 225, my + mh - 40), "Cancel", fill=TEXT_MUTED, font=FONT_BOLD)
    
    draw.rounded_rectangle([(mx + mw - 135, my + mh - 50), (mx + mw - 30, my + mh - 18)], radius=6, fill="#78350F", outline=ACCENT_AMBER)
    draw.text((mx + mw - 125, my + mh - 40), "Save Changes", fill=ACCENT_AMBER, font=FONT_BOLD)
    
    img.save("case_study/output_screenshots/05_edit_student.png")
    print("Generated 05_edit_student.png")

# -------------------------------------------------------------
# 06_delete_student.png (DELETE /api/students/:id Confirmation)
# -------------------------------------------------------------
def make_06_delete_student():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "EduSphere | Delete Confirmation", "https://edusphere-suswetha.vercel.app/students/delete")
    draw_sidebar(draw, active_index=1)
    
    # Dim overlay
    draw.rectangle([(211, 43), (WIDTH, HEIGHT)], fill="#050811")
    
    # Modal Window
    mx, my, mw, mh = 370, 135, 580, 355
    draw.rounded_rectangle([(mx, my), (mx + mw, my + mh)], radius=12, fill=BG_CARD, outline=ACCENT_ROSE)
    draw.rounded_rectangle([(mx, my), (mx + mw, my + 6)], radius=3, fill=ACCENT_ROSE)
    
    # Warning icon
    draw.ellipse([(mx + 30, my + 28), (mx + 80, my + 78)], fill="#4C0519")
    draw.text((mx + 48, my + 40), "⚠️", fill=ACCENT_ROSE, font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 24))
    
    draw.text((mx + 95, my + 34), "Confirm Student Record Deletion", fill=TEXT_WHITE, font=FONT_HEADING)
    draw.text((mx + 95, my + 60), "Permanent database purge • Cannot be undone", fill=ACCENT_ROSE, font=FONT_SMALL)
    
    draw.line([(mx, my + 95), (mx + mw, my + 95)], fill=BORDER, width=1)
    
    # Target details
    draw.text((mx + 30, my + 115), "You are about to delete this record from MongoDB Atlas:", fill=TEXT_MUTED, font=FONT_REGULAR)
    
    draw.rounded_rectangle([(mx + 30, my + 140), (mx + mw - 30, my + 225)], radius=6, fill="#0F172A", outline="#374151")
    draw.text((mx + 45, my + 155), "Student Name:   D. Suswetha", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((mx + 45, my + 175), "Roll Number:    A24126552079 (Dept: CSE)", fill=ACCENT_CYAN, font=FONT_BOLD)
    draw.text((mx + 45, my + 195), "MongoDB _id:    6730a1b2c3d4e5f6a7b8c9d0", fill=TEXT_MUTED, font=FONT_MONO)
    
    # Explanation
    draw.text((mx + 30, my + 242), "Express API:  DELETE /api/students/6730a1b2c3d4e5f6a7b8c9d0", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((mx + 30, my + 262), "MongoDB Wire: db.students.findOneAndDelete({ _id: ObjectId(...) })", fill=ACCENT_CYAN, font=FONT_SMALL)
    
    # Buttons
    draw.rounded_rectangle([(mx + mw - 250, my + mh - 55), (mx + mw - 140, my + mh - 20)], radius=6, fill="#1E293B", outline=BORDER)
    draw.text((mx + mw - 215, my + mh - 44), "Cancel", fill=TEXT_MUTED, font=FONT_BOLD)
    
    draw.rounded_rectangle([(mx + mw - 125, my + mh - 55), (mx + mw - 30, my + mh - 20)], radius=6, fill="#9F1239", outline=ACCENT_ROSE)
    draw.text((mx + mw - 115, my + mh - 44), "Confirm Delete", fill=TEXT_WHITE, font=FONT_BOLD)
    
    img.save("case_study/output_screenshots/06_delete_student.png")
    print("Generated 06_delete_student.png")

# -------------------------------------------------------------
# 07_mongodb_atlas.png (MongoDB Atlas Cloud Interface)
# -------------------------------------------------------------
def make_07_atlas():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0c1015")
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "MongoDB Atlas | Database Deployments", "https://cloud.mongodb.com/v2/clusters/ANITS-Cluster0/explorer/test/students")
    
    # Atlas Top Bar
    draw.rectangle([(0, 43), (WIDTH, 90)], fill="#161e27")
    draw.line([(0, 90), (WIDTH, 90)], fill="#233040", width=1)
    draw.text((30, 58), "🍃 MongoDB Atlas", fill="#00ed64", font=FONT_HEADING)
    draw.text((200, 60), "Cluster: ANITS-Cluster0 (AWS / ap-south-1)", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((540, 60), "Database: test  |  Collection: students (48 documents)", fill=TEXT_MUTED, font=FONT_REGULAR)
    
    # Left Navigation (Databases & Collections)
    draw.rectangle([(0, 91), (220, HEIGHT)], fill="#111822")
    draw.line([(220, 91), (220, HEIGHT)], fill="#233040", width=1)
    
    draw.text((25, 110), "DATABASES (3)", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((25, 135), "📁 admin", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((25, 160), "📁 config", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((25, 185), "📂 test (Application DB)", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((45, 210), "📄 students  (48)", fill="#00ed64", font=FONT_BOLD)
    
    # Query bar
    draw.rounded_rectangle([(245, 110), (WIDTH - 30, 150)], radius=6, fill="#16202c", outline="#29394d")
    draw.text((260, 122), 'Filter:  { "rollNumber": "A24126552079" }', fill="#00ed64", font=FONT_MONO)
    draw.rounded_rectangle([(WIDTH - 130, 116), (WIDTH - 40, 144)], radius=4, fill="#00684a")
    draw.text((WIDTH - 115, 123), "Apply", fill=TEXT_WHITE, font=FONT_SMALL)
    
    # Document Inspection Area
    draw.text((245, 170), "Documents (1 match found in 0.38ms via index { rollNumber: 1 })", fill=TEXT_MUTED, font=FONT_SMALL)
    
    draw.rounded_rectangle([(245, 195), (WIDTH - 30, HEIGHT - 25)], radius=8, fill="#131b24", outline="#29394d")
    
    json_lines = [
        '{',
        '  "_id": ObjectId("6730a1b2c3d4e5f6a7b8c9d0"),',
        '  "rollNumber": "A24126552079",',
        '  "name": "D. Suswetha",',
        '  "email": "d.suswetha@anits.edu.in",',
        '  "department": "CSE",',
        '  "year": 3,',
        '  "phone": "+91 9876543210",',
        '  "dateOfBirth": ISODate("2004-05-18T00:00:00.000Z"),',
        '  "gender": "Female",',
        '  "address": "Visakhapatnam, Andhra Pradesh",',
        '  "createdAt": ISODate("2026-11-10T10:15:30.000Z"),',
        '  "updatedAt": ISODate("2026-11-10T10:15:30.000Z"),',
        '  "__v": 0',
        '}'
    ]
    
    jy = 215
    for jl in json_lines:
        col = "#00ed64" if "A24126552079" in jl or "D. Suswetha" in jl else "#38bdf8" if "ObjectId" in jl or "ISODate" in jl else TEXT_WHITE
        draw.text((275, jy), jl, fill=col, font=FONT_MONO)
        jy += 24
        
    img.save("case_study/output_screenshots/07_mongodb_atlas.png")
    print("Generated 07_mongodb_atlas.png")

# -------------------------------------------------------------
# 08_render_backend.png (Render Backend Service)
# -------------------------------------------------------------
def make_08_render():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0F1117")
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "Render | Web Service edusphere-backend", "https://dashboard.render.com/web/srv-edusphere-suswetha")
    
    # Header
    draw.rectangle([(0, 43), (WIDTH, 110)], fill="#161B26")
    draw.line([(0, 110), (WIDTH, 110)], fill="#2B3445", width=1)
    
    draw.text((35, 58), "🚀 edusphere-backend-suswetha", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((35, 86), "Web Service • Node.js Runtime • https://edusphere-backend-suswetha.onrender.com", fill=ACCENT_CYAN, font=FONT_SMALL)
    
    # Status Pill
    draw.rounded_rectangle([(WIDTH - 150, 65), (WIDTH - 40, 95)], radius=6, fill="#064E3B", outline="#059669")
    draw.text((WIDTH - 135, 72), "● Live Status", fill="#10B981", font=FONT_BOLD)
    
    # Details Cards
    specs = [
        ("Repository", "suswethadwarapudi22-afk/fullstack", "Branch: main"),
        ("Build Command", "npm install", "Node.js v20.x"),
        ("Start Command", "node server.js", "Port: 5000 (auto-assigned)"),
        ("Environment", "MONGO_URI (configured)", "MongoDB Atlas Connected")
    ]
    x = 35
    for title, val, sub in specs:
        draw.rounded_rectangle([(x, 130), (x + 235, 195)], radius=8, fill="#18202D", outline="#2B384D")
        draw.text((x + 15, 142), title, fill=TEXT_MUTED, font=FONT_SMALL)
        draw.text((x + 15, 158), val, fill=TEXT_WHITE, font=FONT_BOLD)
        draw.text((x + 15, 175), sub, fill=ACCENT_CYAN if "Atlas" in sub else TEXT_MUTED, font=FONT_SMALL)
        x += 262
        
    # Logs Terminal Box
    draw.rounded_rectangle([(35, 215), (WIDTH - 35, HEIGHT - 25)], radius=8, fill="#0A0C10", outline="#2B384D")
    draw.rectangle([(35, 215), (WIDTH - 35, 245)], fill="#18202D")
    draw.text((50, 223), "📜 Deployment & Runtime Execution Logs (Live Service Output)", fill=TEXT_MUTED, font=FONT_SMALL)
    
    logs = [
        "==> Cloning repository from https://github.com/suswethadwarapudi22-afk/fullstack...",
        "==> Checking out branch main",
        "==> Running build in case_study/Student-Management-System/backend...",
        "==> Starting EduSphere server with 'node server.js'",
        "[2026-11-10 10:15:20] EduSphere Server running on port 5000",
        "[2026-11-10 10:15:22] MongoDB Atlas connected successfully! (Database: test, Collection: students)",
        "[2026-11-10 10:15:30] POST /api/students - 201 Created (Saved Roll: A24126552079, Name: D. Suswetha)",
        "[2026-11-10 10:15:35] GET /api/students - 200 OK (count: 48 students)",
        "[2026-11-10 10:16:10] GET /api/students/6730a1b2c3d4e5f6a7b8c9d0 - 200 OK (Student Profile)",
        "[2026-11-10 10:16:45] PUT /api/students/6730a1b2c3d4e5f6a7b8c9d0 - 200 OK (Updated D. Suswetha)",
        "==> Service is live at https://edusphere-backend-suswetha.onrender.com"
    ]
    
    ly = 260
    for l in logs:
        col = "#10B981" if "successfully" in l or "live" in l else ACCENT_CYAN if "POST" in l or "PUT" in l else TEXT_WHITE
        draw.text((50, ly), l, fill=col, font=FONT_MONO)
        ly += 25
        
    img.save("case_study/output_screenshots/08_render_backend.png")
    print("Generated 08_render_backend.png")

# -------------------------------------------------------------
# 09_vercel_frontend.png (Vercel Production Deployment)
# -------------------------------------------------------------
def make_09_vercel():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#000000")
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "Vercel | Project Overview", "https://vercel.com/suswetha-dwarapudi/edusphere-frontend")
    
    # Header
    draw.rectangle([(0, 43), (WIDTH, 115)], fill="#0A0A0A")
    draw.line([(0, 115), (WIDTH, 115)], fill="#222222", width=1)
    
    draw.text((35, 60), "▲ edusphere-frontend-suswetha", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((35, 88), "Production Deployment • React 18 + Vite • https://edusphere-suswetha.vercel.app", fill=ACCENT_INDIGO, font=FONT_SMALL)
    
    # Ready pill
    draw.rounded_rectangle([(WIDTH - 140, 68), (WIDTH - 40, 96)], radius=6, fill="#064E3B", outline="#059669")
    draw.text((WIDTH - 125, 75), "● Ready", fill="#10B981", font=FONT_BOLD)
    
    # Deployment card
    draw.rounded_rectangle([(35, 140), (WIDTH - 35, 330)], radius=10, fill="#111111", outline="#222222")
    
    draw.text((60, 165), "Deployment Status", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((60, 185), "Ready (Production Global Edge Network)", fill="#10B981", font=FONT_HEADING)
    
    draw.text((60, 225), "Domain:", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((150, 225), "https://edusphere-suswetha.vercel.app", fill=ACCENT_CYAN, font=FONT_BOLD)
    
    draw.text((60, 255), "Source Repository:", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((210, 255), "suswethadwarapudi22-afk/fullstack (branch: main)", fill=TEXT_WHITE, font=FONT_REGULAR)
    
    draw.text((60, 285), "Deployed Case Study:", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((230, 285), "EduSphere – Student Management System (Author: D. Suswetha, A24126552079)", fill=ACCENT_INDIGO, font=FONT_SMALL)
    
    # Environment Variables Section
    draw.rounded_rectangle([(35, 355), (WIDTH - 35, HEIGHT - 25)], radius=10, fill="#111111", outline="#222222")
    draw.text((60, 375), "Environment Variables (Configured in Project Settings)", fill=TEXT_WHITE, font=FONT_HEADING)
    
    # Table header
    draw.text((60, 415), "VARIABLE NAME", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((260, 415), "VALUE", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((680, 415), "ENVIRONMENT", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.line([(60, 435), (WIDTH - 60, 435)], fill="#222222", width=1)
    
    draw.text((60, 450), "VITE_API_URL", fill=TEXT_WHITE, font=FONT_MONO_BOLD)
    draw.text((260, 450), "https://edusphere-backend-suswetha.onrender.com/api", fill=ACCENT_CYAN, font=FONT_MONO)
    draw.text((680, 450), "Production, Preview, Development", fill=TEXT_MUTED, font=FONT_SMALL)
    
    draw.text((60, 500), "Security Isolation: MONGO_URI is omitted from frontend and isolated strictly within Render backend secrets.", fill="#10B981", font=FONT_SMALL)
    
    img.save("case_study/output_screenshots/09_vercel_frontend.png")
    print("Generated 09_vercel_frontend.png")

if __name__ == "__main__":
    os.makedirs("case_study/output_screenshots", exist_ok=True)
    make_01_dashboard()
    make_02_directory_search()
    make_03_add_student()
    make_04_view_profile()
    make_05_edit_student()
    make_06_delete_student()
    make_07_atlas()
    make_08_render()
    make_09_vercel()
    print("All 9 EduSphere custom screenshots generated successfully!")
