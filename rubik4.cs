// rubik4.cs — C# версия

using System;
using System.Collections.Generic;

class Rubik4
{
    private int[,,] faces = new int[6,4,4];
    private List<string> moves = new List<string>();

    public Rubik4()
    {
        int[] colors = {0,1,2,3,4,5};
        for (int f = 0; f < 6; f++)
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++)
                    faces[f,i,j] = colors[f];
    }

    public void PrintCube()
    {
        Console.WriteLine("Развёртка (U D L R F B):");
        for (int f = 0; f < 6; f++)
        {
            Console.WriteLine($"Грань {f}:");
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                    Console.Write(faces[f,i,j] + " ");
                Console.WriteLine();
            }
        }
    }

    public void DoMove(string move)
    {
        moves.Add(move);
        Console.WriteLine($"Ход: {move}");
    }

    public void Scramble()
    {
        string[] movesList = {"R1","R2","R3","L1","L2","L3","U1","U2","U3","D1","D2","D3","F1","F2","F3","B1","B2","B3"};
        Random rand = new Random();
        for (int i = 0; i < 20; i++)
        {
            string m = movesList[rand.Next(movesList.Length)];
            DoMove(m);
        }
    }

    public static void Main()
    {
        Rubik4 rubik = new Rubik4();
        Console.WriteLine("🧩 Rubik's Cube 4×4 Simulator (C#)");
        Console.WriteLine("Команды: R1 R2 R3 L1 L2 L3 U1 U2 U3 D1 D2 D3 F1 F2 F3 B1 B2 B3 | scramble | reset | show | help | quit");

        while (true)
        {
            Console.Write("> ");
            string cmd = Console.ReadLine().Trim().ToLower();
            if (cmd == "quit") break;
            switch (cmd)
            {
                case "show": rubik.PrintCube(); break;
                case "scramble": rubik.Scramble(); break;
                case "reset": rubik = new Rubik4(); break;
                case "help":
                    Console.WriteLine("Доступные команды: R1..R3, L1..L3, U1..U3, D1..D3, F1..F3, B1..B3, scramble, reset, show, help, quit");
                    break;
                default: rubik.DoMove(cmd); break;
            }
        }
    }
}
