console.log("===== Library Management System ===== - object.js:1");

class Library {

    constructor() {
        this.books = [];
    }

    // Add Book
    addBook(name, price) {
        this.books.push({
            title: name,
            cost: price
        });

        console.log(name + "book added successfully. - object.js:16");
    }

    // Display Books
    displayBooks() {

        console.log("\nBooks in Library: - object.js:22");

        for (let i = 0; i < this.books.length; i++) {

            console.log(
                (i + 1) + ". " +
                this.books[i].title +
                " - ₹" +
                this.books[i].cost
            );

        }

    }

    // Calculate Total Price
    totalPrice() {

        let total = 0;

        for (let i = 0; i < this.books.length; i++) {

            total += this.books[i].cost;

        }

        return total;

    }

    // Remove Last Book
    removeBook() {

        let removedBook = this.books.pop();

        console.log("\nRemoved Book: - object.js:57" + removedBook.title);

    }

}

const lib = new Library();

lib.addBook("Python", 500);
lib.addBook("Java", 600);
lib.addBook("HTML", 300);
lib.addBook("JavaScript", 400);

lib.displayBooks();

console.log("\nTotal Price: ₹ - object.js:72" + lib.totalPrice());

lib.removeBook();

console.log("\nAfter Removing One Book: - object.js:76");

lib.displayBooks();

console.log("\nNew Total Price: ₹ - object.js:80" + lib.totalPrice());