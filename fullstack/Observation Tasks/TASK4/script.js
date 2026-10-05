// Select HTML elements
const taskInput = document.getElementById("taskInput");
const addTaskButton = document.getElementById("addTask");
const taskList = document.getElementById("taskList");
const emptyMessage = document.getElementById("emptyMessage");

// Add Task button event listener
addTaskButton.addEventListener("click", function () {

    const taskText = taskInput.value.trim();

    // Check if input is empty
    if (taskText === "") {
        alert("Please enter a task.");
        return;
    }

    // Create list item
    const li = document.createElement("li");

    // Create task text
    const span = document.createElement("span");
    span.textContent = taskText;
    span.className = "task-text";

    // Create Complete button
    const completeButton = document.createElement("button");
    completeButton.textContent = "Complete";

    // Complete button event
    completeButton.addEventListener("click", function () {
        span.classList.toggle("completed");
    });

    // Create Delete button
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";

    // Delete button event
    deleteButton.addEventListener("click", function () {
        li.remove();
        updateEmptyMessage();
    });

    // Add elements to list item
    li.appendChild(span);
    li.appendChild(completeButton);
    li.appendChild(deleteButton);

    // Add list item to task list
    taskList.appendChild(li);

    // Clear input
    taskInput.value = "";

    // Hide empty message
    updateEmptyMessage();
});

// Function to display empty message
function updateEmptyMessage() {
    if (taskList.children.length === 0) {
        emptyMessage.style.display = "block";
    } else {
        emptyMessage.style.display = "none";
    }
}