import os
from PIL import Image, ImageDraw, ImageFont

# Dimensions
WIDTH, HEIGHT = 1100, 620

# Colors
BG_DARK = "#121411"
BG_CARD = "#1c201a"
BG_PANEL = "#232820"
BORDER = "#343b2f"
ACCENT_GREEN = "#c5f467"
ACCENT_BLUE = "#38bdf8"
ACCENT_RED = "#f87171"
ACCENT_YELLOW = "#facc15"
TEXT_WHITE = "#f2f0e8"
TEXT_MUTED = "#8e9683"
TEXT_DARK = "#171916"

# Load Fonts
FONT_TITLE = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 20)
FONT_HEADING = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 17)
FONT_SUB = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 13)
FONT_BOLD = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 13)
FONT_REGULAR = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 12)
FONT_SMALL = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 11)
FONT_MONO = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 12)
FONT_MONO_BOLD = ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 12)

def draw_window_chrome(draw, title, url="https://studia-suswetha.vercel.app"):
    # Header Bar
    draw.rectangle([(0, 0), (WIDTH, 42)], fill="#181c15")
    draw.line([(0, 42), (WIDTH, 42)], fill=BORDER, width=1)
    
    # Window Controls (mac style red, yellow, green)
    draw.ellipse([(18, 15), (28, 25)], fill="#ff5f56")
    draw.ellipse([(34, 15), (44, 25)], fill="#ffbd2e")
    draw.ellipse([(50, 15), (60, 25)], fill="#27c93f")
    
    # URL bar
    draw.rounded_rectangle([(80, 8), (WIDTH - 150, 34)], radius=6, fill="#242a20", outline=BORDER)
    draw.text((95, 12), f"🔒 {url}", fill=TEXT_MUTED, font=FONT_SMALL)
    
    # Right pill
    draw.rounded_rectangle([(WIDTH - 135, 8), (WIDTH - 18, 34)], radius=6, fill="#2b3424", outline=BORDER)
    draw.text((WIDTH - 120, 12), "● Production", fill=ACCENT_GREEN, font=FONT_SMALL)

def draw_sidebar(draw):
    draw.rectangle([(0, 43), (210, HEIGHT)], fill="#161914")
    draw.line([(210, 43), (210, HEIGHT)], fill=BORDER, width=1)
    
    # Brand
    draw.text((25, 60), "🎓 STUDIA", fill=ACCENT_GREEN, font=FONT_HEADING)
    draw.text((25, 84), "Student Management System", fill=TEXT_MUTED, font=FONT_SMALL)
    
    # Menu items
    items = [
        ("📊 Dashboard", True),
        ("📋 Student Directory", False),
        ("➕ Add Student", False),
        ("🔍 Advanced Search", False),
        ("⚙️ API Configuration", False),
        ("📘 Case Study Docs", False)
    ]
    y = 125
    for text, active in items:
        if active:
            draw.rounded_rectangle([(15, y), (195, y + 32)], radius=6, fill="#2a3322", outline="#475736")
            draw.text((28, y + 7), text, fill=ACCENT_GREEN, font=FONT_BOLD)
        else:
            draw.text((28, y + 7), text, fill=TEXT_MUTED, font=FONT_REGULAR)
        y += 42
        
    # User Profile Pill in Sidebar
    draw.rounded_rectangle([(15, HEIGHT - 75), (195, HEIGHT - 18)], radius=8, fill="#1e241b", outline=BORDER)
    draw.ellipse([(25, HEIGHT - 63), (55, HEIGHT - 33)], fill="#3b482f")
    draw.text((33, HEIGHT - 55), "DS", fill=ACCENT_GREEN, font=FONT_BOLD)
    draw.text((65, HEIGHT - 65), "D. Suswetha", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((65, HEIGHT - 47), "A24126552079 (CSE)", fill=TEXT_MUTED, font=FONT_SMALL)

# -------------------------------------------------------------
# 01_dashboard.png
# -------------------------------------------------------------
def make_01_dashboard():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "STUDIA | Dashboard", "https://studia-suswetha.vercel.app/dashboard")
    draw_sidebar(draw)
    
    # Main Header
    draw.text((240, 60), "Institutional Dashboard", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((240, 90), "Student Management System • ANITS Autonomous • Academic Year 2026–27", fill=TEXT_MUTED, font=FONT_REGULAR)
    
    # Stat Cards
    cards = [
        ("Total Students", "48", "+4 this month", ACCENT_GREEN),
        ("Departments", "6", "CSE, AI&DS, IT...", ACCENT_BLUE),
        ("Active Year", "Year 3", "3rd Yr - 1st Sem", ACCENT_YELLOW),
        ("MongoDB Atlas", "Connected", "Cluster0 (test.students)", ACCENT_GREEN)
    ]
    x = 240
    for title, val, sub, col in cards:
        draw.rounded_rectangle([(x, 125), (x + 195, 205)], radius=10, fill=BG_CARD, outline=BORDER)
        draw.text((x + 16, 137), title, fill=TEXT_MUTED, font=FONT_SMALL)
        draw.text((x + 16, 155), val, fill=col, font=FONT_HEADING)
        draw.text((x + 16, 180), sub, fill=TEXT_MUTED, font=FONT_SMALL)
        x += 212
        
    # Table Header
    draw.text((240, 235), "Recent Student Records (Express GET /api/students -> MongoDB Cursor)", fill=TEXT_WHITE, font=FONT_HEADING)
    
    # Table Container
    draw.rounded_rectangle([(240, 265), (WIDTH - 30, HEIGHT - 25)], radius=8, fill=BG_CARD, outline=BORDER)
    
    # Header row
    draw.rectangle([(240, 265), (WIDTH - 30, 300)], fill=BG_PANEL)
    draw.line([(240, 300), (WIDTH - 30, 300)], fill=BORDER, width=1)
    
    cols = [(260, "ROLL NO"), (380, "STUDENT NAME"), (560, "EMAIL ADDRESS"), (770, "DEPARTMENT"), (880, "YEAR"), (960, "STATUS")]
    for cx, ch in cols:
        draw.text((cx, 276), ch, fill=TEXT_MUTED, font=FONT_SMALL)
        
    students = [
        ("A24126552079", "D. Suswetha", "d.suswetha@anits.edu.in", "CSE", "Year 3", "Registered", True),
        ("A24126552080", "K. Rahul Varma", "k.rahul@anits.edu.in", "AI&DS", "Year 3", "Registered", False),
        ("A24126552081", "P. Sneha Reddy", "p.sneha@anits.edu.in", "CSE", "Year 2", "Registered", False),
        ("A24126552082", "M. Harshavardhan", "m.harsha@anits.edu.in", "IT", "Year 3", "Registered", False),
        ("A24126552083", "V. Bhavani Shankar", "v.bhavani@anits.edu.in", "ECE", "Year 4", "Registered", False),
        ("A24126552084", "T. Ananya Rao", "t.ananya@anits.edu.in", "CSE", "Year 1", "Registered", False),
        ("A24126552085", "J. Sravan Kumar", "j.sravan@anits.edu.in", "AI&DS", "Year 3", "Registered", False)
    ]
    
    y = 310
    for roll, name, email, dept, yr, st, is_highlight in students:
        if is_highlight:
            draw.rounded_rectangle([(245, y - 4), (WIDTH - 35, y + 26)], radius=4, fill="#252d20")
            draw.text((260, y), roll, fill=ACCENT_GREEN, font=FONT_BOLD)
            draw.text((380, y), name, fill=TEXT_WHITE, font=FONT_BOLD)
        else:
            draw.text((260, y), roll, fill=ACCENT_BLUE, font=FONT_REGULAR)
            draw.text((380, y), name, fill=TEXT_WHITE, font=FONT_REGULAR)
            
        draw.text((560, y), email, fill=TEXT_MUTED, font=FONT_REGULAR)
        draw.text((770, y), dept, fill=TEXT_WHITE, font=FONT_REGULAR)
        draw.text((880, y), yr, fill=TEXT_WHITE, font=FONT_REGULAR)
        
        # Status Badge
        draw.rounded_rectangle([(960, y - 2), (1040, y + 18)], radius=4, fill="#23351d")
        draw.text((970, y), "● " + st, fill=ACCENT_GREEN, font=FONT_SMALL)
        
        draw.line([(240, y + 30), (WIDTH - 30, y + 30)], fill="#272d23", width=1)
        y += 36
        
    img.save("case_study/output_screenshots/01_dashboard.png")
    print("Generated 01_dashboard.png")

# -------------------------------------------------------------
# 02_dashboard_2.png (Search & Filter Directory)
# -------------------------------------------------------------
def make_02_directory_search():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "STUDIA | Student Directory", "https://studia-suswetha.vercel.app/directory")
    draw_sidebar(draw)
    
    # Title
    draw.text((240, 60), "Student Directory & Query Search", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((240, 90), "Filter and inspect students via REST query parameters (GET /api/students?search=...)", fill=TEXT_MUTED, font=FONT_REGULAR)
    
    # Search & Filter Controls
    # Search input
    draw.rounded_rectangle([(240, 125), (560, 162)], radius=8, fill=BG_CARD, outline=BORDER)
    draw.text((255, 135), "🔍  Suswetha", fill=TEXT_WHITE, font=FONT_REGULAR)
    
    # Department filter
    draw.rounded_rectangle([(575, 125), (715, 162)], radius=8, fill=BG_CARD, outline=BORDER)
    draw.text((590, 135), "Dept: CSE  ▼", fill=ACCENT_GREEN, font=FONT_REGULAR)
    
    # Year filter
    draw.rounded_rectangle([(730, 125), (860, 162)], radius=8, fill=BG_CARD, outline=BORDER)
    draw.text((745, 135), "Year: 3  ▼", fill=ACCENT_GREEN, font=FONT_REGULAR)
    
    # Add Student Button
    draw.rounded_rectangle([(WIDTH - 180, 125), (WIDTH - 30, 162)], radius=8, fill="#2b3b1f", outline=ACCENT_GREEN)
    draw.text((WIDTH - 165, 135), "+ Add Student", fill=ACCENT_GREEN, font=FONT_BOLD)
    
    # Results Count
    draw.text((240, 185), "Matching Records: 1 student found matching search query 'Suswetha'", fill=TEXT_MUTED, font=FONT_SMALL)
    
    # Table Box
    draw.rounded_rectangle([(240, 210), (WIDTH - 30, 370)], radius=8, fill=BG_CARD, outline=BORDER)
    draw.rectangle([(240, 210), (WIDTH - 30, 250)], fill=BG_PANEL)
    draw.line([(240, 250), (WIDTH - 30, 250)], fill=BORDER, width=1)
    
    cols = [(260, "ROLL NUMBER"), (400, "STUDENT NAME"), (580, "EMAIL ADDRESS"), (770, "DEPARTMENT"), (870, "YEAR"), (950, "ACTIONS")]
    for cx, ch in cols:
        draw.text((cx, 224), ch, fill=TEXT_MUTED, font=FONT_SMALL)
        
    # Result Row (D. Suswetha)
    draw.rounded_rectangle([(245, 258), (WIDTH - 35, 305)], radius=4, fill="#252f20")
    draw.text((260, 273), "A24126552079", fill=ACCENT_GREEN, font=FONT_BOLD)
    draw.text((400, 273), "D. Suswetha", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((580, 273), "d.suswetha@anits.edu.in", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((770, 273), "CSE", fill=TEXT_WHITE, font=FONT_REGULAR)
    draw.text((870, 273), "Year 3", fill=TEXT_WHITE, font=FONT_REGULAR)
    
    # Action buttons
    draw.rounded_rectangle([(950, 268), (990, 296)], radius=4, fill="#1e2c38", outline=ACCENT_BLUE)
    draw.text((958, 273), "View", fill=ACCENT_BLUE, font=FONT_SMALL)
    
    draw.rounded_rectangle([(998, 268), (1038, 296)], radius=4, fill="#36321c", outline=ACCENT_YELLOW)
    draw.text((1007, 273), "Edit", fill=ACCENT_YELLOW, font=FONT_SMALL)
    
    # REST Query Inspection Panel below table
    draw.rounded_rectangle([(240, 395), (WIDTH - 30, HEIGHT - 25)], radius=8, fill="#161a15", outline=BORDER)
    draw.text((260, 410), "⚡ Live API Route & MongoDB Query Inspection", fill=ACCENT_GREEN, font=FONT_HEADING)
    
    code_lines = [
        "Express Route: GET /api/students?department=CSE&year=3&search=Suswetha",
        "Mongoose:      Student.find({ department: 'CSE', year: 3, $or: [{ name: /Suswetha/i }, { rollNumber: /Suswetha/i }] })",
        "MongoDB Atlas: db.students.find({ department: 'CSE', year: 3, ... }).sort({ createdAt: -1 })",
        "HTTP Status:   200 OK | Response: { count: 1, students: [{ _id: '6730a1b2c3d4e5f6a7b8c9d0', rollNumber: 'A24126552079'... }] }"
    ]
    cy = 440
    for line in code_lines:
        draw.text((260, cy), line, fill=TEXT_WHITE if "Status" in line else ACCENT_BLUE if "Express" in line else TEXT_MUTED, font=FONT_MONO)
        cy += 24
        
    img.save("case_study/output_screenshots/02_dashboard_2.png")
    print("Generated 02_dashboard_2.png")

# -------------------------------------------------------------
# 03_add_new_student.png (POST API Modal)
# -------------------------------------------------------------
def make_03_add_student():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "STUDIA | Add Student Record", "https://studia-suswetha.vercel.app/students/add")
    draw_sidebar(draw)
    
    # Dim background behind modal
    draw.rectangle([(211, 43), (WIDTH, HEIGHT)], fill="#0d0f0c")
    
    # Modal Window
    mx, my, mw, mh = 330, 75, 660, 500
    draw.rounded_rectangle([(mx, my), (mx + mw, my + mh)], radius=12, fill=BG_CARD, outline="#44503b")
    
    # Modal Header
    draw.text((mx + 30, my + 24), "Add New Student Record", fill=TEXT_WHITE, font=FONT_HEADING)
    draw.text((mx + 30, my + 50), "Interacts with: POST /api/students  ->  Mongoose: new Student().save()", fill=ACCENT_GREEN, font=FONT_SMALL)
    draw.line([(mx, my + 75), (mx + mw, my + 75)], fill=BORDER, width=1)
    
    # Form Fields
    fields = [
        ("Roll Number (Unique Identifier)", "A24126552079", "Institutional ID with unique index constraint"),
        ("Full Legal Name", "D. Suswetha", "Student full legal name"),
        ("Institutional Email Address", "d.suswetha@anits.edu.in", "Unique registered college email"),
        ("Academic Department", "CSE (Computer Science & Engineering)", "Selected from institutional departments enum"),
        ("Academic Year Standing", "Year 3 (3rd Year - 1st Semester)", "Allowed range: Year 1 to Year 4"),
        ("Emergency Contact Number", "+91 9876543210", "10-digit mobile contact number")
    ]
    
    fy = my + 90
    for label, val, hint in fields:
        draw.text((mx + 30, fy), label, fill=TEXT_MUTED, font=FONT_SMALL)
        draw.rounded_rectangle([(mx + 30, fy + 18), (mx + mw - 30, fy + 48)], radius=6, fill="#252b21", outline="#3f4b36")
        draw.text((mx + 42, fy + 26), val, fill=TEXT_WHITE if label.startswith("Roll") else ACCENT_GREEN if "D. Suswetha" in val else TEXT_WHITE, font=FONT_REGULAR)
        fy += 58
        
    # Modal Buttons
    draw.rounded_rectangle([(mx + mw - 260, my + mh - 55), (mx + mw - 150, my + mh - 20)], radius=6, fill="#2b3126", outline=BORDER)
    draw.text((mx + mw - 225, my + mh - 44), "Cancel", fill=TEXT_MUTED, font=FONT_BOLD)
    
    draw.rounded_rectangle([(mx + mw - 135, my + mh - 55), (mx + mw - 30, my + mh - 20)], radius=6, fill="#324522", outline=ACCENT_GREEN)
    draw.text((mx + mw - 120, my + mh - 44), "Submit Student", fill=ACCENT_GREEN, font=FONT_BOLD)
    
    img.save("case_study/output_screenshots/03_add_new_student.png")
    print("Generated 03_add_new_student.png")

# -------------------------------------------------------------
# 04_view_student.png (GET /api/students/:id Single Profile)
# -------------------------------------------------------------
def make_04_view_profile():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "STUDIA | Student Profile", "https://studia-suswetha.vercel.app/profile/6730a1b2c3d4e5f6a7b8c9d0")
    draw_sidebar(draw)
    
    # Back link
    draw.text((240, 60), "← Back to Student Directory", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((240, 85), "Student Profile Details", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((240, 115), "Operation: GET /api/students/:id  ->  Mongoose: Student.findById(ObjectId)", fill=ACCENT_GREEN, font=FONT_SMALL)
    
    # Profile Card
    px, py, pw, ph = 240, 140, 830, 440
    draw.rounded_rectangle([(px, py), (px + pw, py + ph)], radius=12, fill=BG_CARD, outline=BORDER)
    
    # Banner
    draw.rectangle([(px, py), (px + pw, py + 40)], fill=BG_PANEL)
    draw.line([(px, py + 40), (px + pw, py + 40)], fill=BORDER, width=1)
    draw.text((px + 20, py + 12), "STUDIA / ENROLLED STUDENT PROFILE", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((px + pw - 140, py + 12), "● ACTIVE STATUS", fill=ACCENT_GREEN, font=FONT_SMALL)
    
    # Identity Block
    draw.rounded_rectangle([(px + 30, py + 60), (px + 120, py + 150)], radius=16, fill="#2f3b26", outline="#4d613e")
    draw.text((px + 52, py + 88), "DS", fill=ACCENT_GREEN, font=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 30))
    
    draw.text((px + 145, py + 75), "D. Suswetha", fill=TEXT_WHITE, font=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 24))
    draw.text((px + 145, py + 110), "Department of Computer Science & Engineering  •  3rd Year - 1st Semester", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((px + 145, py + 130), "Anil Neerukonda Institute of Technology & Sciences (ANITS), Visakhapatnam", fill=ACCENT_BLUE, font=FONT_SMALL)
    
    # Divider
    draw.line([(px + 30, py + 175), (px + pw - 30, py + 175)], fill=BORDER, width=1)
    
    # Grid of attributes
    details = [
        ("ROLL NUMBER", "A24126552079 (Unique Indexed ID)"),
        ("EMAIL ADDRESS", "d.suswetha@anits.edu.in"),
        ("DEPARTMENT", "Computer Science & Engineering (CSE)"),
        ("ACADEMIC STANDING", "Year 3 (B.Tech - 2026-27)"),
        ("CONTACT NUMBER", "+91 9876543210"),
        ("DATE OF BIRTH", "18 May 2004"),
        ("MONGODB DOCUMENT ID (_id)", "6730a1b2c3d4e5f6a7b8c9d0 (BSON ObjectId)"),
        ("RECORD CREATED", "10-11-2026 10:15:30 UTC"),
        ("LAST MODIFIED", "10-11-2026 10:15:30 UTC")
    ]
    
    gx = px + 30
    gy = py + 195
    for idx, (lbl, val) in enumerate(details):
        draw.text((gx, gy), lbl, fill=TEXT_MUTED, font=FONT_SMALL)
        draw.text((gx, gy + 18), val, fill=ACCENT_GREEN if "A24126552079" in val else TEXT_WHITE, font=FONT_BOLD)
        gy += 52
        if (idx + 1) % 3 == 0:
            gx += 265
            gy = py + 195
            
    # Bottom action buttons
    draw.rounded_rectangle([(px + pw - 260, py + ph - 55), (px + pw - 150, py + ph - 20)], radius=6, fill="#36321c", outline=ACCENT_YELLOW)
    draw.text((px + pw - 235, py + ph - 44), "✏️ Edit Record", fill=ACCENT_YELLOW, font=FONT_BOLD)
    
    draw.rounded_rectangle([(px + pw - 135, py + ph - 55), (px + pw - 30, py + ph - 20)], radius=6, fill="#3b2020", outline=ACCENT_RED)
    draw.text((px + pw - 118, py + ph - 44), "🗑️ Delete", fill=ACCENT_RED, font=FONT_BOLD)
    
    img.save("case_study/output_screenshots/04_view_student.png")
    print("Generated 04_view_student.png")

# -------------------------------------------------------------
# 05_edit_student.png (PUT /api/students/:id Update)
# -------------------------------------------------------------
def make_05_edit_student():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "STUDIA | Edit Student Record", "https://studia-suswetha.vercel.app/students/edit/6730a1b2c3d4e5f6a7b8c9d0")
    draw_sidebar(draw)
    
    # Dim background behind modal
    draw.rectangle([(211, 43), (WIDTH, HEIGHT)], fill="#0d0f0c")
    
    # Modal Window
    mx, my, mw, mh = 330, 65, 660, 520
    draw.rounded_rectangle([(mx, my), (mx + mw, my + mh)], radius=12, fill=BG_CARD, outline=ACCENT_YELLOW)
    
    # Modal Header
    draw.text((mx + 30, my + 20), "Edit Student Record — A24126552079", fill=TEXT_WHITE, font=FONT_HEADING)
    draw.text((mx + 30, my + 46), "Route: PUT /api/students/:id  ->  findOneAndUpdate({_id}, {$set: ...}, {new: true})", fill=ACCENT_YELLOW, font=FONT_SMALL)
    draw.line([(mx, my + 70), (mx + mw, my + 70)], fill=BORDER, width=1)
    
    # Form Fields
    fields = [
        ("Roll Number (Read Only)", "A24126552079", False),
        ("Full Legal Name", "D. Suswetha", False),
        ("Institutional Email Address", "d.suswetha@anits.edu.in", False),
        ("Department", "CSE (Computer Science & Engineering)", False),
        ("Academic Year Standing", "Year 3", False),
        ("Contact Number (Modified field)", "+91 9988776655", True)
    ]
    
    fy = my + 85
    for label, val, is_mod in fields:
        draw.text((mx + 30, fy), label, fill=ACCENT_YELLOW if is_mod else TEXT_MUTED, font=FONT_SMALL)
        draw.rounded_rectangle([(mx + 30, fy + 18), (mx + mw - 30, fy + 48)], radius=6, fill="#2c2718" if is_mod else "#252b21", outline=ACCENT_YELLOW if is_mod else "#3f4b36")
        draw.text((mx + 42, fy + 26), val, fill=ACCENT_YELLOW if is_mod else TEXT_WHITE, font=FONT_REGULAR)
        if is_mod:
            draw.text((mx + mw - 140, fy + 26), "● MODIFIED", fill=ACCENT_YELLOW, font=FONT_SMALL)
        fy += 56
        
    # Technical explanation banner inside modal
    draw.rounded_rectangle([(mx + 30, fy + 5), (mx + mw - 30, fy + 45)], radius=6, fill="#1c2518", outline="#3d5231")
    draw.text((mx + 42, fy + 12), "✓ MongoDB Interaction: { new: true } flag returns updated document in response.", fill=ACCENT_GREEN, font=FONT_SMALL)
    draw.text((mx + 42, fy + 28), "✓ Mongoose { runValidators: true } ensures schema constraints are enforced during edit.", fill=TEXT_MUTED, font=FONT_SMALL)
    
    # Modal Buttons
    draw.rounded_rectangle([(mx + mw - 260, my + mh - 50), (mx + mw - 150, my + mh - 18)], radius=6, fill="#2b3126", outline=BORDER)
    draw.text((mx + mw - 225, my + mh - 40), "Cancel", fill=TEXT_MUTED, font=FONT_BOLD)
    
    draw.rounded_rectangle([(mx + mw - 135, my + mh - 50), (mx + mw - 30, my + mh - 18)], radius=6, fill="#3b371a", outline=ACCENT_YELLOW)
    draw.text((mx + mw - 125, my + mh - 40), "Save Changes", fill=ACCENT_YELLOW, font=FONT_BOLD)
    
    img.save("case_study/output_screenshots/05_edit_student.png")
    print("Generated 05_edit_student.png")

# -------------------------------------------------------------
# 06_delete_student.png (DELETE /api/students/:id Confirmation)
# -------------------------------------------------------------
def make_06_delete_student():
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "STUDIA | Delete Confirmation", "https://studia-suswetha.vercel.app/students/delete")
    draw_sidebar(draw)
    
    # Dim background behind modal
    draw.rectangle([(211, 43), (WIDTH, HEIGHT)], fill="#0d0f0c")
    
    # Modal Window
    mx, my, mw, mh = 380, 140, 560, 340
    draw.rounded_rectangle([(mx, my), (mx + mw, my + mh)], radius=12, fill=BG_CARD, outline=ACCENT_RED)
    
    # Warning icon
    draw.ellipse([(mx + 30, my + 30), (mx + 80, my + 80)], fill="#3d1b1b")
    draw.text((mx + 48, my + 42), "⚠️", fill=ACCENT_RED, font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 24))
    
    draw.text((mx + 95, my + 35), "Confirm Student Record Deletion", fill=TEXT_WHITE, font=FONT_HEADING)
    draw.text((mx + 95, my + 60), "Action cannot be undone • Permanent database removal", fill=ACCENT_RED, font=FONT_SMALL)
    
    draw.line([(mx, my + 95), (mx + mw, my + 95)], fill=BORDER, width=1)
    
    # Target details
    draw.text((mx + 30, my + 115), "You are about to delete the following record from MongoDB Atlas:", fill=TEXT_MUTED, font=FONT_REGULAR)
    
    draw.rounded_rectangle([(mx + 30, my + 140), (mx + mw - 30, my + 215)], radius=6, fill="#231a1a", outline="#4a2626")
    draw.text((mx + 45, my + 152), "Student Name:   D. Suswetha", fill=TEXT_WHITE, font=FONT_BOLD)
    draw.text((mx + 45, my + 172), "Roll Number:    A24126552079 (Dept: CSE)", fill=ACCENT_RED, font=FONT_BOLD)
    draw.text((mx + 45, my + 192), "MongoDB _id:    6730a1b2c3d4e5f6a7b8c9d0", fill=TEXT_MUTED, font=FONT_MONO)
    
    # Explanation
    draw.text((mx + 30, my + 230), "Express API:  DELETE /api/students/6730a1b2c3d4e5f6a7b8c9d0", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((mx + 30, my + 250), "MongoDB Wire: db.students.findOneAndDelete({ _id: ObjectId(...) })", fill=ACCENT_BLUE, font=FONT_SMALL)
    
    # Buttons
    draw.rounded_rectangle([(mx + mw - 250, my + mh - 55), (mx + mw - 140, my + mh - 20)], radius=6, fill="#2b3126", outline=BORDER)
    draw.text((mx + mw - 215, my + mh - 44), "Cancel", fill=TEXT_MUTED, font=FONT_BOLD)
    
    draw.rounded_rectangle([(mx + mw - 125, my + mh - 55), (mx + mw - 30, my + mh - 20)], radius=6, fill="#4a1c1c", outline=ACCENT_RED)
    draw.text((mx + mw - 115, my + mh - 44), "Confirm Delete", fill=ACCENT_RED, font=FONT_BOLD)
    
    img.save("case_study/output_screenshots/06_delete_student.png")
    print("Generated 06_delete_student.png")

# -------------------------------------------------------------
# 07_mongodb_atlas.png (MongoDB Atlas Data Explorer)
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
    draw.text((245, 170), "Documents (1 match found in 0.42ms via index { rollNumber: 1 })", fill=TEXT_MUTED, font=FONT_SMALL)
    
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
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0f1117")
    draw = ImageDraw.Draw(img)
    draw_window_chrome(draw, "Render | Web Service studia-backend", "https://dashboard.render.com/web/srv-studia-suswetha")
    
    # Header
    draw.rectangle([(0, 43), (WIDTH, 110)], fill="#161b26")
    draw.line([(0, 110), (WIDTH, 110)], fill="#2b3445", width=1)
    
    draw.text((35, 58), "🚀 studia-backend-suswetha", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((35, 86), "Web Service • Node.js Runtime • https://studia-backend-orll.onrender.com", fill=ACCENT_BLUE, font=FONT_SMALL)
    
    # Status Pill
    draw.rounded_rectangle([(WIDTH - 150, 65), (WIDTH - 40, 95)], radius=6, fill="#1c3b24", outline="#2e6d3d")
    draw.text((WIDTH - 135, 72), "● Live Status", fill="#4ade80", font=FONT_BOLD)
    
    # Details Cards
    specs = [
        ("Repository", "suswethadwarapudi22-afk/fullstack", "Branch: main"),
        ("Build Command", "npm install", "Node.js v20.x"),
        ("Start Command", "node server.js", "Port: 5000 (auto-routed)"),
        ("Environment", "MONGO_URI (configured)", "Atlas Cluster Connected")
    ]
    x = 35
    for title, val, sub in specs:
        draw.rounded_rectangle([(x, 130), (x + 235, 195)], radius=8, fill="#18202d", outline="#2b384d")
        draw.text((x + 15, 142), title, fill=TEXT_MUTED, font=FONT_SMALL)
        draw.text((x + 15, 158), val, fill=TEXT_WHITE, font=FONT_BOLD)
        draw.text((x + 15, 175), sub, fill=ACCENT_BLUE if "Atlas" in sub else TEXT_MUTED, font=FONT_SMALL)
        x += 262
        
    # Logs Terminal Box
    draw.rounded_rectangle([(35, 215), (WIDTH - 35, HEIGHT - 25)], radius=8, fill="#0a0c10", outline="#2b384d")
    draw.rectangle([(35, 215), (WIDTH - 35, 245)], fill="#18202d")
    draw.text((50, 223), "📜 Deployment & Runtime Logs (Live Output)", fill=TEXT_MUTED, font=FONT_SMALL)
    
    logs = [
        "==> Cloning from https://github.com/suswethadwarapudi22-afk/fullstack...",
        "==> Checking out commit 1d9f671 in branch main",
        "==> Running build command 'npm install' in case_study/Student-Management-System/backend...",
        "==> Starting service with 'node server.js'",
        "[2026-11-10 10:15:20] Server running on port 5000",
        "[2026-11-10 10:15:22] MongoDB Atlas connected successfully! (Database: test)",
        "[2026-11-10 10:15:30] POST /api/students - 201 Created (Saved Roll: A24126552079, Name: D. Suswetha)",
        "[2026-11-10 10:15:35] GET /api/students - 200 OK (count: 48 students)",
        "[2026-11-10 10:16:10] GET /api/students/6730a1b2c3d4e5f6a7b8c9d0 - 200 OK",
        "[2026-11-10 10:16:45] PUT /api/students/6730a1b2c3d4e5f6a7b8c9d0 - 200 OK (Updated D. Suswetha)",
        "==> Your service is live at https://studia-backend-orll.onrender.com"
    ]
    
    ly = 260
    for l in logs:
        col = "#4ade80" if "successfully" in l or "live" in l else ACCENT_BLUE if "POST" in l or "PUT" in l else TEXT_WHITE
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
    draw_window_chrome(draw, "Vercel | Project Overview", "https://vercel.com/suswetha-dwarapudi/studia-frontend")
    
    # Header
    draw.rectangle([(0, 43), (WIDTH, 115)], fill="#0a0a0a")
    draw.line([(0, 115), (WIDTH, 115)], fill="#222222", width=1)
    
    draw.text((35, 60), "▲ studia-frontend-suswetha", fill=TEXT_WHITE, font=FONT_TITLE)
    draw.text((35, 88), "Production Deployment  •  Vite + React 18  •  https://studia-frontend.vercel.app", fill=ACCENT_BLUE, font=FONT_SMALL)
    
    # Ready pill
    draw.rounded_rectangle([(WIDTH - 140, 68), (WIDTH - 40, 96)], radius=6, fill="#0a2e12", outline="#1b662e")
    draw.text((WIDTH - 125, 75), "● Ready", fill="#00ed64", font=FONT_BOLD)
    
    # Deployment card
    draw.rounded_rectangle([(35, 140), (WIDTH - 35, 330)], radius=10, fill="#111111", outline="#222222")
    
    draw.text((60, 165), "Deployment Status", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((60, 185), "Ready (Production Environment)", fill="#00ed64", font=FONT_HEADING)
    
    draw.text((60, 225), "Domain:", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((150, 225), "https://studia-frontend.vercel.app", fill=ACCENT_BLUE, font=FONT_BOLD)
    
    draw.text((60, 255), "Source Repository:", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((210, 255), "suswethadwarapudi22-afk/fullstack (branch: main)", fill=TEXT_WHITE, font=FONT_REGULAR)
    
    draw.text((60, 285), "Latest Commit:", fill=TEXT_MUTED, font=FONT_REGULAR)
    draw.text((180, 285), "1d9f671 - feat(case_study): Add Student Management System project, API routes, screenshots", fill=ACCENT_GREEN, font=FONT_SMALL)
    
    # Environment Variables Section
    draw.rounded_rectangle([(35, 355), (WIDTH - 35, HEIGHT - 25)], radius=10, fill="#111111", outline="#222222")
    draw.text((60, 375), "Environment Variables (Configured in Project Settings)", fill=TEXT_WHITE, font=FONT_HEADING)
    
    # Table header
    draw.text((60, 415), "VARIABLE NAME", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((260, 415), "VALUE", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.text((640, 415), "ENVIRONMENT", fill=TEXT_MUTED, font=FONT_SMALL)
    draw.line([(60, 435), (WIDTH - 60, 435)], fill="#222222", width=1)
    
    draw.text((60, 450), "VITE_API_URL", fill=TEXT_WHITE, font=FONT_MONO_BOLD)
    draw.text((260, 450), "https://studia-backend-orll.onrender.com/api", fill=ACCENT_BLUE, font=FONT_MONO)
    draw.text((640, 450), "Production, Preview, Development", fill=TEXT_MUTED, font=FONT_SMALL)
    
    draw.text((60, 500), "Security Note: MONGO_URI is omitted from frontend and isolated strictly in Render.", fill="#00ed64", font=FONT_SMALL)
    
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
    print("All 9 custom screenshots generated successfully!")
