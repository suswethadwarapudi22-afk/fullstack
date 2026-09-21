class Student {
    constructor(name, rollNo, department, cgpa) {
        this.name = name;
        this.rollNo = rollNo;
        this.department = department;
        this.cgpa = cgpa;
    }
}

const button = document.getElementById("createProfile");//dom function to get the button element with the id "createProfile" and assign it to the variable "button".

button.addEventListener("click", function () { //event listner is added to the button element that listens for a click event. When the button is clicked, the function inside the event listener will be executed.

    const name = document.getElementById("name").value;
    const rollNo = document.getElementById("rollNo").value;
    const department = document.getElementById("department").value;
    const cgpa = document.getElementById("cgpa").value;

    const student = new Student(name, rollNo, department, cgpa);

    const profileContainer = document.getElementById("profileContainer");

    profileContainer.innerHTML = "";

    const profile = document.createElement("div");
    profile.className = "profile";

    const title = document.createElement("h2");
    title.textContent = "Student Profile";

    const nameElement = document.createElement("p");
    nameElement.textContent = `Name : ${student.name}`;

    const rollElement = document.createElement("p");
    rollElement.textContent = `Roll No : ${student.rollNo}`;

    const departmentElement = document.createElement("p");
    departmentElement.textContent = `Department : ${student.department}`;

    const cgpaElement = document.createElement("p");
    cgpaElement.textContent = `CGPA : ${student.cgpa}`;

    profile.appendChild(title);
    profile.appendChild(nameElement);
    profile.appendChild(rollElement);
    profile.appendChild(departmentElement);
    profile.appendChild(cgpaElement);

    profileContainer.appendChild(profile);
});