class Instrument {
    play() {
        console.log("Instrument can play - hierarchical.js:3");
    }
}

class Guitar extends Instrument {
    strum() {
        console.log("Guitar is strumming - hierarchical.js:9");
    }
}

class Piano extends Instrument {
    press() {
        console.log("Piano is playing - hierarchical.js:15");
    }
}

let g = new Guitar();
let p = new Piano();

g.play();
g.strum();

p.play();
p.press();