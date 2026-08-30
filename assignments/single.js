class Bird {
    fly() {
        console.log("Bird can fly - single.js:3");
    }
}

class Parrot extends Bird {
    speak() {
        console.log("Parrot can speak - single.js:9");
    }
}

let p = new Parrot();

p.fly();
p.speak();