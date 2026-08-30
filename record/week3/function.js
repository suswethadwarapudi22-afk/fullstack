// Array
let marks = [85, 90, 78, 88, 95];

// Function to display marks
function displayMarks(arr) {
    console.log("Student Marks: - function.js:6", arr);
}

// Function to calculate total
function totalMarks(arr) {
    let total = 0;

    for (let i = 0; i < arr.length; i++) {
        total += arr[i];
    }

    return total;
}

// Function to calculate average
function averageMarks(arr) {
    return totalMarks(arr) / arr.length;
}

// Function to add a new mark
function addMark(arr, mark) {
    arr.push(mark);
    return arr;
}

displayMarks(marks);

console.log("Total Marks: - function.js:33", totalMarks(marks));

console.log("Average Marks: - function.js:35", averageMarks(marks));

console.log("After Adding New Mark: - function.js:37");

addMark(marks, 92);

displayMarks(marks);

console.log("New Total: - function.js:43", totalMarks(marks));