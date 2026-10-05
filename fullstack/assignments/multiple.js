class Tree {
    grow() {
        console.log("Tree can grow - multiple.js:3");
    }
}

class FruitTree extends Tree {
    fruit() {
        console.log("Fruit tree gives fruit - multiple.js:9");
    }
}

class MangoTree extends FruitTree {
    mango() {
        console.log("Mango tree gives mangoes - multiple.js:15");
    }
}

let m = new MangoTree();

m.grow();
m.fruit();
m.mango();