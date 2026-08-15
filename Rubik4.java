// Rubik4.java — Java версия

import java.util.*;

public class Rubik4 {
    private int[][][] faces = new int[6][4][4];
    private List<String> moves = new ArrayList<>();

    public Rubik4() {
        int[] colors = {0,1,2,3,4,5};
        for (int f = 0; f < 6; f++) {
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    faces[f][i][j] = colors[f];
                }
            }
        }
    }

    public void printCube() {
        System.out.println("Развёртка (U D L R F B):");
        for (int f = 0; f < 6; f++) {
            System.out.println("Грань " + f + ":");
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    System.out.print(faces[f][i][j] + " ");
                }
                System.out.println();
            }
        }
    }

    public void doMove(String move) {
        moves.add(move);
        System.out.println("Ход: " + move);
    }

    public void scramble() {
        String[] movesList = {"R1","R2","R3","L1","L2","L3","U1","U2","U3","D1","D2","D3","F1","F2","F3","B1","B2","B3"};
        Random rand = new Random();
        for (int i = 0; i < 20; i++) {
            String m = movesList[rand.nextInt(movesList.length)];
            doMove(m);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Rubik4 rubik = new Rubik4();
        System.out.println("🧩 Rubik's Cube 4×4 Simulator (Java)");
        System.out.println("Команды: R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3 | scramble | reset | show | help | quit");

        while (true) {
            System.out.print("> ");
            String cmd = scanner.nextLine().trim().toLowerCase();
            if (cmd.equals("quit")) break;
            switch (cmd) {
                case "show":
                    rubik.printCube();
                    break;
                case "scramble":
                    rubik.scramble();
                    break;
                case "reset":
                    rubik = new Rubik4();
                    break;
                case "help":
                    System.out.println("Доступные команды: R1..R3, L1..L3, U1..U3, D1..D3, F1..F3, B1..B3, scramble, reset, show, help, quit");
                    break;
                default:
                    rubik.doMove(cmd);
            }
        }
        scanner.close();
    }
}
