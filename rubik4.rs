// rubik4.rs — Rust версия

use rand::seq::SliceRandom;
use rand::thread_rng;
use std::io::{self, Write};

struct Rubik4 {
    faces: [[[i32; 4]; 4]; 6],
    moves: Vec<String>,
}

impl Rubik4 {
    fn new() -> Self {
        let colors = [0, 1, 2, 3, 4, 5];
        let mut faces = [[[0; 4]; 4]; 6];
        for f in 0..6 {
            for i in 0..4 {
                for j in 0..4 {
                    faces[f][i][j] = colors[f];
                }
            }
        }
        Rubik4 { faces, moves: Vec::new() }
    }

    fn print_cube(&self) {
        println!("Развёртка (U D L R F B):");
        for f in 0..6 {
            println!("Грань {}:", f);
            for i in 0..4 {
                for j in 0..4 {
                    print!("{} ", self.faces[f][i][j]);
                }
                println!();
            }
        }
    }

    fn do_move(&mut self, m: &str) {
        self.moves.push(m.to_string());
        println!("Ход: {}", m);
    }

    fn scramble(&mut self) {
        let moves = ["R1","R2","R3","L1","L2","L3","U1","U2","U3","D1","D2","D3","F1","F2","F3","B1","B2","B3"];
        let mut rng = thread_rng();
        for _ in 0..20 {
            let m = moves.choose(&mut rng).unwrap();
            self.do_move(m);
        }
    }
}

fn main() {
    let mut rubik = Rubik4::new();
    println!("🧩 Rubik's Cube 4×4 Simulator (Rust)");
    println!("Команды: R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3 | scramble | reset | show | help | quit");

    loop {
        print!("> ");
        io::stdout().flush().unwrap();
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let cmd = input.trim().to_lowercase();
        match cmd.as_str() {
            "quit" => break,
            "show" => rubik.print_cube(),
            "scramble" => rubik.scramble(),
            "reset" => rubik = Rubik4::new(),
            "help" => println!("Доступные команды: R1..R3, L1..L3, U1..U3, D1..D3, F1..F3, B1..B3, scramble, reset, show, help, quit"),
            _ => rubik.do_move(&cmd),
        }
    }
}
