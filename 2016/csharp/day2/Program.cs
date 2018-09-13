using System;
using System.IO;

namespace day2
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllLines("input.txt");
            SolveA(input);
            SolveB(input);
        }

        static void SolveA(string[] input)
        {
            var code = "";
            int[][] padlock = new int[3][];
            int y = 1;
            int x = 1;
            padlock[0] = new int[3] {1,2,3};
            padlock[1] = new int[3] {4,5,6};
            padlock[2] = new int[3] {7,8,9};

            foreach (var line in input)
            {
                foreach (var c in line)
                {
                    if (c == 'U' && y > 0) y--;
                    else if (c == 'D' && y < 2) y++;
                    else if (c == 'L' && x > 0) x--;
                    else if (c == 'R' && x < 2) x++;
                }
                code += (padlock[y][x]).ToString();
            }
            Console.WriteLine("part 1: {0}", code);
        }

        static void SolveB(string[] input)
        {
            var code = "";
            char[][] padlock = new char[5][];
            int y = 2;
            int x = 0;
            padlock[0] = new char[5] {'0','0','1','0','0'};
            padlock[1] = new char[5] {'0','2','3','4','0'};
            padlock[2] = new char[5] {'5','6','7','8','9'};
            padlock[3] = new char[5] {'0','A','B','C','0'};
            padlock[4] = new char[5] {'0','0','D','0','0'};
            foreach (var line in input)
            {
                foreach (var c in line)
                {
                    if (c == 'U' && y > 0 && padlock[y-1][x] != '0') y--;
                    else if (c == 'D' && y < 4 && padlock[y+1][x] != '0') y++;
                    else if (c == 'L' && x > 0 && padlock[y][x-1] != '0') x--;
                    else if (c == 'R' && x < 4 && padlock[y][x+1] != '0') x++;
                }
                code += (padlock[y][x]).ToString();
            }
            Console.WriteLine("part 2: {0}", code);
        }
    }
}