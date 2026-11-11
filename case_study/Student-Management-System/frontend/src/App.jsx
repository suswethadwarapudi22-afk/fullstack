import StudentProfile from "./components/StudentProfile";
import { useEffect, useMemo, useState } from "react";
import {
  LayoutDashboard,
  Users,
  Eye,
  GraduationCap,
  Building2,
  Settings,
  Search,
  Plus,
  ArrowUpRight,
  Pencil,
  Trash2,
  X,
  ChevronDown,
  Menu,
  RefreshCw,
} from "lucide-react";

import {
  getStudents,
  addStudent,
  updateStudent,
  deleteStudent,
} from "./services/api";

import "./App.css";

const emptyForm = {
  rollNumber: "",
  name: "",
  email: "",
  department: "CSE",
  year: 1,
};

function App() {
  const [selectedStudent, setSelectedStudent] = useState(null);
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");
  const [departmentFilter, setDepartmentFilter] = useState("All");
  const [yearFilter, setYearFilter] = useState("All");
  const [showForm, setShowForm] = useState(false);
  const [editingId, setEditingId] = useState(null);
  const [form, setForm] = useState(emptyForm);
  const [saving, setSaving] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const fetchStudents = async () => {
    try {
      setLoading(true);
      setError("");
      const data = await getStudents();
      setStudents(data);
    } catch (err) {
      setError(
        err.response?.data?.message ||
        "Unable to load student records. Check your backend."
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  const departments = useMemo(
    () => [...new Set(students.map((s) => s.department))],
    [students]
  );

  const filteredStudents = useMemo(() => {
    return students.filter((student) => {
      const term = search.toLowerCase();

      const matchesSearch =
        student.name?.toLowerCase().includes(term) ||
        student.rollNumber?.toLowerCase().includes(term) ||
        student.email?.toLowerCase().includes(term);

      const matchesDepartment =
        departmentFilter === "All" ||
        student.department === departmentFilter;

      const matchesYear =
        yearFilter === "All" ||
        String(student.year) === yearFilter;

      return matchesSearch && matchesDepartment && matchesYear;
    });
  }, [students, search, departmentFilter, yearFilter]);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setForm((previous) => ({
      ...previous,
      [name]: name === "year" ? Number(value) : value,
    }));
  };

  const openAddForm = () => {
    setEditingId(null);
    setForm(emptyForm);
    setShowForm(true);
  };

  const openEditForm = (student) => {
    setEditingId(student._id);
    setForm({
      rollNumber: student.rollNumber,
      name: student.name,
      email: student.email,
      department: student.department,
      year: Number(student.year),
    });
    setShowForm(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      setSaving(true);
      setError("");

      if (editingId) {
        await updateStudent(editingId, form);
      } else {
        await addStudent(form);
      }

      setShowForm(false);
      setForm(emptyForm);
      setEditingId(null);
      await fetchStudents();
    } catch (err) {
      setError(
        err.response?.data?.message ||
        err.response?.data?.error ||
        "Something went wrong. Please try again."
      );
    } finally {
      setSaving(false);
    }
  };

  const handleDelete = async (id) => {
    const confirmed = window.confirm(
      "Are you sure you want to delete this student?"
    );

    if (!confirmed) return;

    try {
      setError("");
      await deleteStudent(id);
      await fetchStudents();
    } catch (err) {
      setError(
        err.response?.data?.message ||
        "Unable to delete student."
      );
    }
  };

  if (selectedStudent) {
  return (
    <StudentProfile
      student={selectedStudent}
      onBack={() => setSelectedStudent(null)}
      onEdit={(student) => {
        setSelectedStudent(null);
        openEditForm(student);
      }}
    />
  );
}
  return (
    <div className="app-shell">

      {/* SIDEBAR */}

      <aside className={`sidebar ${sidebarOpen ? "sidebar-open" : ""}`}>
        <div className="brand">
          <div className="brand-icon">E</div>
          <div>
            <h2>EDUSPHERE</h2>
            <span>STUDENT MANAGEMENT</span>
          </div>
          <button
            className="mobile-close"
            onClick={() => setSidebarOpen(false)}
          >
            <X size={19} />
          </button>
        </div>

        <div className="sidebar-label">WORKSPACE</div>

        <nav className="navigation">
          <a href="#overview" className="nav-item active">
            <LayoutDashboard size={19} />
            <span>Overview</span>
          </a>

          <a href="#students" className="nav-item">
            <Users size={19} />
            <span>Students</span>
            <span className="nav-count">{students.length}</span>
          </a>

          <a href="#departments" className="nav-item">
            <Building2 size={19} />
            <span>Departments</span>
          </a>
        </nav>

        <div className="sidebar-bottom">
          <div className="sidebar-label">SYSTEM</div>

          <div className="nav-item">
            <Settings size={19} />
            <span>Settings</span>
          </div>

          <div className="admin-card">
            <div className="admin-avatar">S</div>
            <div>
              <strong>D. Suswetha</strong>
              <span>Lead Administrator</span>
            </div>
            <ChevronDown size={16} />
          </div>

          <div className="sidebar-footer">
            <span className="online-dot"></span>
            All systems operational
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT */}

      <main className="main-content" id="overview">

        <header className="topbar">
          <button
            className="mobile-menu"
            onClick={() => setSidebarOpen(true)}
          >
            <Menu size={22} />
          </button>

          <div className="breadcrumb">
            Workspace <span>/</span> Overview
          </div>

          <div className="topbar-right">
            <span className="academic-year">ACADEMIC YEAR 2026–27</span>
            <div className="profile-avatar">S</div>
          </div>
        </header>

        <section className="page-content">

          {/* INTRO */}

          <div className="page-heading">
            <div>
              <div className="eyebrow">
                <span className="online-dot"></span>
                INSTITUTIONAL OVERVIEW
              </div>

              <h1>Your institution,<br />
                <span>in focus.</span>
              </h1>

              <p>
                A clearer picture of your student community.
                Everything in one place.
              </p>
            </div>

            <button className="primary-button" onClick={openAddForm}>
              <Plus size={19} />
              Add student
            </button>
          </div>

          {error && (
            <div className="error-banner">
              <span>{error}</span>
              <button onClick={() => setError("")}>
                <X size={17} />
              </button>
            </div>
          )}

          {/* STATISTICS */}

          <section className="stats-grid">

            <div className="stat-card stat-highlight">
              <div className="stat-top">
                <span>TOTAL STUDENTS</span>
                <Users size={20} />
              </div>
              <h2>{students.length.toString().padStart(2, "0")}</h2>
              <div className="stat-bottom">
                <span>Registered student records</span>
                <ArrowUpRight size={17} />
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-top">
                <span>DEPARTMENTS</span>
                <Building2 size={20} />
              </div>
              <h2>{departments.length.toString().padStart(2, "0")}</h2>
              <div className="stat-bottom">
                <span>Active departments</span>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-top">
                <span>FINAL YEAR</span>
                <GraduationCap size={20} />
              </div>
              <h2>
                {students.filter((s) => Number(s.year) === 4).length
                  .toString().padStart(2, "0")}
              </h2>
              <div className="stat-bottom">
                <span>Fourth-year students</span>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-top">
                <span>ACADEMIC SESSION</span>
                <LayoutDashboard size={20} />
              </div>
              <h2 className="session-number">26/27</h2>
              <div className="stat-bottom">
                <span>Current academic session</span>
              </div>
            </div>

          </section>

          {/* DEPARTMENT SUMMARY */}

          <section className="department-section" id="departments">
            <div className="section-heading">
              <div>
                <span className="section-kicker">CAMPUS STRUCTURE</span>
                <h2>Department overview</h2>
              </div>
              <span className="muted-text">
                {departments.length} departments
              </span>
            </div>

            <div className="department-list">
              {departments.length === 0 ? (
                <p className="empty-inline">
                  Department information will appear here.
                </p>
              ) : (
                departments.map((department) => {
                  const count = students.filter(
                    (s) => s.department === department
                  ).length;

                  const percentage = students.length
                    ? (count / students.length) * 100
                    : 0;

                  return (
                    <div className="department-item" key={department}>
                      <div className="department-info">
                        <span className="department-symbol">
                          {department.slice(0, 2)}
                        </span>
                        <div>
                          <strong>{department}</strong>
                          <span>{count} students</span>
                        </div>
                      </div>

                      <div className="department-progress">
                        <div className="progress-track">
                          <div
                            className="progress-fill"
                            style={{ width: `${percentage}%` }}
                          />
                        </div>
                        <span>{Math.round(percentage)}%</span>
                      </div>
                    </div>
                  );
                })
              )}
            </div>
          </section>

          {/* STUDENT DIRECTORY */}

          <section className="directory-section" id="students">

            <div className="section-heading directory-heading">
              <div>
                <span className="section-kicker">RECORD MANAGEMENT</span>
                <h2>Student directory</h2>
                <p>Manage, search and update student information.</p>
              </div>

              <button
                className="refresh-button"
                onClick={fetchStudents}
                title="Refresh records"
              >
                <RefreshCw size={17} />
              </button>
            </div>

            <div className="filter-bar">

              <div className="search-box">
                <Search size={18} />
                <input
                  type="text"
                  placeholder="Search by name, roll number or email..."
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                />
              </div>

              <select
                value={departmentFilter}
                onChange={(e) => setDepartmentFilter(e.target.value)}
              >
                <option value="All">All departments</option>
                {departments.map((d) => (
                  <option key={d} value={d}>{d}</option>
                ))}
              </select>

              <select
                value={yearFilter}
                onChange={(e) => setYearFilter(e.target.value)}
              >
                <option value="All">All years</option>
                {[1, 2, 3, 4].map((year) => (
                  <option key={year} value={String(year)}>
                    Year {year}
                  </option>
                ))}
              </select>

            </div>

            <div className="table-wrapper">
              <table className="student-table">
                <thead>
                  <tr>
                    <th>STUDENT</th>
                    <th>ROLL NUMBER</th>
                    <th>DEPARTMENT</th>
                    <th>YEAR</th>
                    <th>EMAIL</th>
                    <th>ACTIONS</th>
                  </tr>
                </thead>

                <tbody>
                  {loading ? (
                    <tr>
                      <td colSpan="6" className="empty-state">
                        Loading student records...
                      </td>
                    </tr>
                  ) : filteredStudents.length === 0 ? (
                    <tr>
                      <td colSpan="6" className="empty-state">
                        No student records found.
                      </td>
                    </tr>
                  ) : (
                    filteredStudents.map((student) => (
                      <tr key={student._id}>
                        <td>
                          <div className="student-identity">
                            <div className="student-avatar">
                              {student.name?.charAt(0).toUpperCase()}
                            </div>
                            <strong>{student.name}</strong>
                          </div>
                        </td>

                        <td className="roll-number">
                          {student.rollNumber}
                        </td>

                        <td>
                          <span className="department-tag">
                            {student.department}
                          </span>
                        </td>

                        <td>Year {student.year}</td>

                        <td className="email-cell">{student.email}</td>

                        <td>
                          <div className="action-buttons">
                            <button
                              className="icon-button edit-button"
                              onClick={() => openEditForm(student)}
                              title="Edit student"
                            >
                              <Pencil size={16} />
                            </button>
                            <button
  className="icon-button"
  onClick={() => setSelectedStudent(student)}
  title="View student profile"
>
  <Eye size={16} />
</button>
                            

                            <button
                              className="icon-button delete-button"
                              onClick={() => handleDelete(student._id)}
                              title="Delete student"
                            >
                              <Trash2 size={16} />
                            </button>
                          </div>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>

            <div className="table-footer">
              <span>
                Showing {filteredStudents.length} of {students.length} records
              </span>
              <span>LIVE DATABASE</span>
            </div>

          </section>

          <footer className="page-footer">
            <span>EDUSPHERE © 2026</span>
            <span>STUDENT MANAGEMENT SYSTEM • D. SUSWETHA (A24126552079)</span>
          </footer>

        </section>
      </main>

      {/* ADD / EDIT MODAL */}

      {showForm && (
        <div
          className="modal-overlay"
          onClick={(e) => {
            if (e.target === e.currentTarget) setShowForm(false);
          }}
        >
          <div className="student-modal">

            <div className="modal-header">
              <div>
                <span className="section-kicker">STUDENT RECORDS</span>
                <h2>{editingId ? "Edit student" : "New student"}</h2>
                <p>
                  {editingId
                    ? "Update the student's information."
                    : "Add a new student to your institution."}
                </p>
              </div>

              <button
                className="modal-close"
                onClick={() => setShowForm(false)}
              >
                <X size={20} />
              </button>
            </div>

            <form onSubmit={handleSubmit} className="student-form">
              {error && (
  <div className="error-banner">
    {error}
  </div>
)}

              <label>
                Roll number
                <input
                  name="rollNumber"
                  value={form.rollNumber}
                  onChange={handleChange}
                  placeholder="e.g. A24126552079"
                  required
                />
              </label>

              <label>
                Full name
                <input
                  name="name"
                  value={form.name}
                  onChange={handleChange}
                  placeholder="Enter student name"
                  required
                />
              </label>

              <label>
                Email address
                <input
                  name="email"
                  type="email"
                  value={form.email}
                  onChange={handleChange}
                  placeholder="student@example.com"
                  required
                />
              </label>

              <div className="form-row">
                <label>
                  Department
                  <select
                    name="department"
                    value={form.department}
                    onChange={handleChange}
                  >
                    {["CSE", "ECE", "EEE", "MECH", "CIVIL", "IT", "AI&DS"].map(
                      (d) => <option key={d} value={d}>{d}</option>
                    )}
                  </select>
                </label>

                <label>
                  Academic year
                  <select
                    name="year"
                    value={form.year}
                    onChange={handleChange}
                  >
                    {[1, 2, 3, 4].map((y) => (
                      <option key={y} value={y}>Year {y}</option>
                    ))}
                  </select>
                </label>
              </div>

              <div className="modal-actions">
                <button
                  type="button"
                  className="secondary-button"
                  onClick={() => setShowForm(false)}
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  className="primary-button"
                  disabled={saving}
                >
                  {saving
                    ? "Saving..."
                    : editingId
                      ? "Save changes"
                      : "Add student"}
                </button>
              </div>

            </form>
          </div>
        </div>
      )}

    </div>
  );
}

export default App;
