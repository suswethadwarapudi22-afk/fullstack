import { ArrowLeft, Mail, GraduationCap, Hash, Building2, CalendarDays, Pencil } from "lucide-react";
import "./StudentProfile.css";

function StudentProfile({ student, onBack, onEdit }) {
  if (!student) return null;

  const initials = student.name
    .split(" ")
    .map((word) => word[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();

  return (
    <div className="profile-page">
      <button className="profile-back" onClick={onBack}>
        <ArrowLeft size={17} /> Back to dashboard
      </button>

      <div className="profile-heading">
        <span className="section-kicker">STUDENT RECORD / PROFILE</span>
        <h1>Student <span>profile.</span></h1>
        <p>Personal and academic information.</p>
      </div>

      <section className="profile-card">
        <div className="profile-banner">
          <span>EDUSPHERE / STUDENT DIRECTORY</span>
          <span className="profile-status">
            <span className="online-dot"></span> REGISTERED
          </span>
        </div>

        <div className="profile-identity">
          <div className="profile-large-avatar">{initials}</div>

          <div className="profile-name">
            <h2>{student.name}</h2>
            <p>{student.department} · Year {student.year}</p>
          </div>

          <button className="primary-button" onClick={() => onEdit(student)}>
            <Pencil size={16} /> Edit profile
          </button>
        </div>

        <div className="profile-divider"></div>

        <div className="profile-details">
          <div className="profile-detail">
            <span><Hash size={16} /> ROLL NUMBER</span>
            <strong>{student.rollNumber}</strong>
          </div>

          <div className="profile-detail">
            <span><Mail size={16} /> EMAIL ADDRESS</span>
            <strong>{student.email}</strong>
          </div>

          <div className="profile-detail">
            <span><Building2 size={16} /> DEPARTMENT</span>
            <strong>{student.department}</strong>
          </div>

          <div className="profile-detail">
            <span><GraduationCap size={16} /> ACADEMIC YEAR</span>
            <strong>Year {student.year}</strong>
          </div>

          <div className="profile-detail">
            <span><CalendarDays size={16} /> RECORD CREATED</span>
            <strong>
              {student.createdAt
                ? new Date(student.createdAt).toLocaleDateString("en-IN")
                : "Not available"}
            </strong>
          </div>

          <div className="profile-detail">
            <span><CalendarDays size={16} /> LAST UPDATED</span>
            <strong>
              {student.updatedAt
                ? new Date(student.updatedAt).toLocaleDateString("en-IN")
                : "Not available"}
            </strong>
          </div>
        </div>
      </section>
    </div>
  );
}

export default StudentProfile;
