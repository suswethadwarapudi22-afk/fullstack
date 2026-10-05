// Function
function add(a, b) {
    return a + b;
}

console.log(add(10, 20));


// Class
class Student {

    constructor(name, course) {
        this.name = name;
        this.course = course;
    }

    introduce() {
        console.log("I am - code.js:18" + this.name +
                    " studying " + this.course);
    }
}

// Creating multiple objects
const student1 = new Student("suswetha", "CSE");
const student2 = new Student("Rahul", "AI & ML");

student1.introduce();
student2.introduce();