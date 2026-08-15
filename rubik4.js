// rubik4.js — JavaScript версия

const readline = require('readline');

class Rubik4 {
    constructor() {
        this.faces = [];
        const colors = [0,1,2,3,4,5];
        for (let f = 0; f < 6; f++) {
            const face = [];
            for (let i = 0; i < 4; i++) {
                face.push([colors[f], colors[f], colors[f], colors[f]]);
            }
            this.faces.push(face);
        }
        this.moves = [];
    }

    printCube() {
        console.log("Развёртка (U D L R F B):");
        for (let f = 0; f < 6; f++) {
            console.log(`Грань ${f}:`);
            for (let i = 0; i < 4; i++) {
                console.log(this.faces[f][i].join(' '));
            }
        }
    }

    doMove(move) {
        this.moves.push(move);
        console.log(`Ход: ${move}`);
    }

    scramble() {
        const moves = ['R1','R2','R3','L1','L2','L3','U1','U2','U3','D1','D2','D3','F1','F2','F3','B1','B2','B3'];
        for (let i = 0; i < 20; i++) {
            const m = moves[Math.floor(Math.random() * moves.length)];
            this.doMove(m);
        }
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const rubik = new Rubik4();
console.log("🧩 Rubik's Cube 4×4 Simulator (JavaScript)");
console.log("Команды: R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3 | scramble | reset | show | help | quit");

rl.on('line', (input) => {
    const cmd = input.trim().toLowerCase();
    switch (cmd) {
        case 'quit':
            rl.close();
            break;
        case 'show':
            rubik.printCube();
            break;
        case 'scramble':
            rubik.scramble();
            break;
        case 'reset':
            rubik = new Rubik4();
            break;
        case 'help':
            console.log("Доступные команды: R1..R3, L1..L3, U1..U3, D1..D3, F1..F3, B1..B3, scramble, reset, show, help, quit");
            break;
        default:
            rubik.doMove(cmd);
    }
});
