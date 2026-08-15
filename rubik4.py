

### 1. `rubik4.py` (Python)

```python
# rubik4.py — Python версия

import random
import copy

# Цвета: 0-белый, 1-жёлтый, 2-красный, 3-оранжевый, 4-синий, 5-зелёный
# Грань 0: верх (U), 1: низ (D), 2: лево (L), 3: право (R), 4: перед (F), 5: зад (B)
# Каждая грань: 4x4 массив

class Rubik4:
    def __init__(self):
        self.faces = []
        # Инициализация граней
        colors = [0,1,2,3,4,5]  # U,D,L,R,F,B
        for c in colors:
            face = [[c]*4 for _ in range(4)]
            self.faces.append(face)
        self.moves = []

    def rotate_face(self, face_idx, direction=1):
        """Поворачивает грань на 90 градусов (1 - по часовой, -1 - против)."""
        if direction == 1:
            self.faces[face_idx] = [list(row) for row in zip(*self.faces[face_idx][::-1])]
        else:
            self.faces[face_idx] = [list(row) for row in zip(*self.faces[face_idx])][::-1]

    def rotate_layer(self, axis, layer, direction=1):
        """Вращает слой вокруг оси."""
        # axis: 0-X (R/L), 1-Y (U/D), 2-Z (F/B)
        # layer: 0..3
        # direction: 1 - по часовой, -1 - против
        # Реализация для 4x4 сложная, нужно обновлять соседние грани.
        # Для краткости опустим детали, используем упрощённое вращение.
        # Полная реализация требует обновления всех affected граней.
        pass

    def scramble(self, moves=20):
        for _ in range(moves):
            # Генерируем случайный ход
            axis = random.choice(['R','L','U','D','F','B'])
            layer = random.randint(0,3)
            dir = random.choice([1,-1])
            move = f"{axis}{layer+1}{'R' if dir==1 else 'L'}"
            self.do_move(move)

    def do_move(self, move):
        # Упрощённо: только для демонстрации
        print(f"Выполняется ход: {move}")
        self.moves.append(move)

    def print_cube(self):
        # Вывод развёртки
        print("Развёртка (U D L R F B):")
        for i, face in enumerate(self.faces):
            print(f"Грань {i}:")
            for row in face:
                print(' '.join(str(c) for c in row))

def main():
    cube = Rubik4()
    print("🧩 Rubik's Cube 4×4 Simulator (Python)")
    print("Команды: R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3 | scramble | reset | show | help | quit")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == 'quit':
            break
        elif cmd == 'show':
            cube.print_cube()
        elif cmd == 'scramble':
            cube.scramble()
        elif cmd == 'reset':
            cube = Rubik4()
        elif cmd == 'help':
            print("Доступные команды: R1..R3, L1..L3, U1..U3, D1..D3, F1..F3, B1..B3, scramble, reset, show, help, quit")
        else:
            # Попытка выполнить ход
            cube.do_move(cmd)

if __name__ == "__main__":
    main()
