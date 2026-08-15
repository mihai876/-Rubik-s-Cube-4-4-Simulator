<?php
// rubik4.php — PHP версия

class Rubik4 {
    private $faces = [];
    private $moves = [];

    public function __construct() {
        $colors = [0,1,2,3,4,5];
        for ($f = 0; $f < 6; $f++) {
            $face = [];
            for ($i = 0; $i < 4; $i++) {
                $row = [];
                for ($j = 0; $j < 4; $j++) {
                    $row[] = $colors[$f];
                }
                $face[] = $row;
            }
            $this->faces[] = $face;
        }
    }

    public function printCube() {
        echo "Развёртка (U D L R F B):\n";
        for ($f = 0; $f < 6; $f++) {
            echo "Грань $f:\n";
            foreach ($this->faces[$f] as $row) {
                echo implode(' ', $row) . "\n";
            }
        }
    }

    public function doMove($move) {
        $this->moves[] = $move;
        echo "Ход: $move\n";
    }

    public function scramble() {
        $movesList = ['R1','R2','R3','L1','L2','L3','U1','U2','U3','D1','D2','D3','F1','F2','F3','B1','B2','B3'];
        for ($i = 0; $i < 20; $i++) {
            $m = $movesList[array_rand($movesList)];
            $this->doMove($m);
        }
    }
}

$rubik = new Rubik4();
echo "🧩 Rubik's Cube 4×4 Simulator (PHP)\n";
echo "Команды: R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3 | scramble | reset | show | help | quit\n";

while (true) {
    echo "> ";
    $cmd = trim(fgets(STDIN));
    $cmd = strtolower($cmd);
    if ($cmd == 'quit') break;
    switch ($cmd) {
        case 'show': $rubik->printCube(); break;
        case 'scramble': $rubik->scramble(); break;
        case 'reset': $rubik = new Rubik4(); break;
        case 'help':
            echo "Доступные команды: R1..R3, L1..L3, U1..U3, D1..D3, F1..F3, B1..B3, scramble, reset, show, help, quit\n";
            break;
        default: $rubik->doMove($cmd);
    }
}
?>
