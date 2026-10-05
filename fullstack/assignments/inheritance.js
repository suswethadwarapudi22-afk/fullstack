//Single Inheritance
console.log("Single Inheritance - inheritance.js:2");
class Animal {
    constructor(name){
        this.name=name;
    }
    eat(){
        console.log(`${this.name} is eating. - inheritance.js:8`);
    }
}
class Dog extends Animal{
    bark(){
        console.log(`${this.name} is barking. - inheritance.js:13`)
    } 
}
const myDog = new Dog("Buddy");
myDog.eat();
myDog.bark();

//Multilevel Inheritance
console.log("Multilevel Inheritance - inheritance.js:21");
class Vehicle {
    move(){
        console.log("Moving forward - inheritance.js:24");
    }
}
class Bike extends Vehicle{
    wheels(){
        console.log("Bike has 2 Wheels - inheritance.js:29");
    }
}
class Car extends Bike{
    windows(){
        console.log("Car has 4 Windows - inheritance.js:34");
    }
}
const v = new Car();
v.move();
v.wheels();
v.windows();

//Hierarchial Inheritance
console.log("Hierarchial Inheritance - inheritance.js:43");
class User{
    constructor(username){
        this.username = username;
    }
    login(){
        console.log(`${this.username} logged in. - inheritance.js:49`);
    }
}
class Admin extends User{
    deleteUser(){
        console.log(`${this.username} deleted by admin - inheritance.js:54`);
    }
}
class Customer extends User{
    checkout(){
        console.log(`${this.username} checked out successfully. - inheritance.js:59`);
    }
}
const a = new Admin("Anvitha");
const c = new Customer("Sam");
a.login();
c.login();
a.deleteUser();
c.checkout();

//Multiple Inheritance
console.log("Multiple Inheritance - inheritance.js:70");
//Using Mixins
const hall = {
    sofa(){
        console.log("Sofa is placed in Hall. - inheritance.js:74");
    },
    tv(){
        console.log("Tv is placed in Hall. - inheritance.js:77")
    }
}; 
const bedRoom = {
    bed(){
        console.log("Bed is in bedroom. - inheritance.js:82");
    },
    closet(){
        console.log("Closet is in Bedroom. - inheritance.js:85");
    }
};
class Building{
    constructor(houseNo){
        this.houseNo = houseNo;
    }
    house(){
        console.log(`Building House No: ${this.houseNo} - inheritance.js:93`);
    }
}
class Area extends Building{
    constructor(houseNo,area){
        super(houseNo);
        this.area = area;
    }
}
Object.assign(Area.prototype,hall,bedRoom);
const name = new Area("403","Kommadi");
name.house();
name.sofa();
name.bed();