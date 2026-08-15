// rubik4.go — Go версия

package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

type Rubik4 struct {
	faces [6][4][4]int
	moves []string
}

func NewRubik4() *Rubik4 {
	r := &Rubik4{}
	colors := [6]int{0, 1, 2, 3, 4, 5}
	for f := 0; f < 6; f++ {
		for i := 0; i < 4; i++ {
			for j := 0; j < 4; j++ {
				r.faces[f][i][j] = colors[f]
			}
		}
	}
	return r
}

func (r *Rubik4) printCube() {
	fmt.Println("Развёртка (U D L R F B):")
	for f := 0; f < 6; f++ {
		fmt.Printf("Грань %d:\n", f)
		for i := 0; i < 4; i++ {
			for j := 0; j < 4; j++ {
				fmt.Printf("%d ", r.faces[f][i][j])
			}
			fmt.Println()
		}
	}
}

func (r *Rubik4) doMove(move string) {
	r.moves = append(r.moves, move)
	fmt.Printf("Ход: %s\n", move)
}

func (r *Rubik4) scramble() {
	rand.Seed(time.Now().UnixNano())
	moves := []string{"R1","R2","R3","L1","L2","L3","U1","U2","U3","D1","D2","D3","F1","F2","F3","B1","B2","B3"}
	for i := 0; i < 20; i++ {
		m := moves[rand.Intn(len(moves))]
		r.doMove(m)
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	rubik := NewRubik4()
	fmt.Println("🧩 Rubik's Cube 4×4 Simulator (Go)")
	fmt.Println("Команды: R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3 | scramble | reset | show | help | quit")

	for {
		fmt.Print("> ")
		scanner.Scan()
		cmd := strings.TrimSpace(scanner.Text())
		switch cmd {
		case "quit":
			return
		case "show":
			rubik.printCube()
		case "scramble":
			rubik.scramble()
		case "reset":
			rubik = NewRubik4()
		case "help":
			fmt.Println("Доступные команды: R1..R3, L1..L3, U1..U3, D1..D3, F1..F3, B1..B3, scramble, reset, show, help, quit")
		default:
			rubik.doMove(cmd)
		}
	}
}
