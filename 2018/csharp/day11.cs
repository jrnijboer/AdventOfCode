using System;
using System.IO;

namespace aoc2018
{
    class Day11
    {
        public static void Solve()
        {
            int serial = int.Parse(File.ReadAllText(Path.Combine("..", "input", "day11.input")));
            var grid = new int[301, 301];

            for (int i = 0; i <= 300; i++)
            {
                grid[0, i] = 0;
                grid[i, 0] = 0;
            }

            for (int y = 1; y <= 300; y++)
                for (int x = 1; x <= 300; x++)
                    grid[x, y] = GetPowerlevel(x, y, serial) + grid[x - 1, y] + grid[x, y - 1] - grid[x - 1, y - 1];

            int max = int.MinValue, maxX = 0, maxY = 0, bestGridsize = 0;
            for (int size = 2; size < 300; size++)
            {
                for (int y = 1; y + size <= 300; y++)
                    for (int x = 1; x + size <= 300; x++)
                    {
                        int v = 0;
                        v = grid[x, y] + grid[x + size, y + size] - grid[x + size, y] - grid[x, y + size];
                        if (v > max)
                        {
                            max = v;
                            maxX = x;
                            maxY = y;
                            bestGridsize = size;
                        }
                    }
                if (size == 3)
                    Console.WriteLine("day 11, answer a: \"{0},{1}\"", maxX + 1, maxY + 1);
            }
            Console.WriteLine("day 11, answer b: \"{0},{1},{2}\"", maxX + 1, maxY + 1, bestGridsize);
        }
        static int GetPowerlevel(int x, int y, int serial)
        {
            return (((x + 10) * y + serial) * (x + 10) / 100 % 10) - 5;
        }
    }
}
