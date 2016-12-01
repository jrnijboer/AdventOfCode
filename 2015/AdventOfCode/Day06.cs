using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static void Day6b()
        {
            int[,] grid = new int[1000, 1000];

            for (int x = 0; x <= 999; x++)
            {
                for (int y = 0; y <= 999; y++)
                {
                    grid[x, y] = 0;
                }
            }

            var instructions = File.ReadAllLines("input/day6.input");
            string pattern = @"^(.*?)(\d+),(\d+) .* (\d+),(\d+)$";

            foreach (var instruction in instructions)
            {
                var groups = Regex.Match(instruction, pattern).Groups;
                string oper = groups[1].Value.Trim();
                int xStart = int.Parse(groups[2].Value);
                int yStart = int.Parse(groups[3].Value);
                int xStop = int.Parse(groups[4].Value);
                int yStop = int.Parse(groups[5].Value);

                switch (oper)
                {
                    case "toggle":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] += 2;
                            }
                        }
                        break;
                    case "turn off":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] = grid[x, y] > 0 ? grid[x, y] -= 1 : 0;
                            }
                        }
                        break;
                    case "turn on":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y]++;
                            }
                        }
                        break;
                }
            }

            long lights = 0;

            for (int x = 0; x <= 999; x++)
            {
                for (int y = 0; y <= 999; y++)
                {
                    lights += (grid[x, y]);

                }
            }

            Console.WriteLine("{0} brightness by all lights", lights);
        }

        static void Day6a()
        {
            bool[,] grid = new bool[1000, 1000];

            for (int x = 0; x <= 999; x++)
            {
                for (int y = 0; y <= 999; y++)
                {
                    grid[x, y] = false;
                }
            }

            var instructions = File.ReadAllLines("input/day6.input");
            string pattern = @"^(.*?)(\d+),(\d+) .* (\d+),(\d+)$";

            foreach (var instruction in instructions)
            {
                var groups = Regex.Match(instruction, pattern).Groups;
                string oper = groups[1].Value.Trim();
                int xStart = int.Parse(groups[2].Value);
                int yStart = int.Parse(groups[3].Value);
                int xStop = int.Parse(groups[4].Value);
                int yStop = int.Parse(groups[5].Value);

                switch (oper)
                {
                    case "toggle":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] = !grid[x, y];
                            }
                        }
                        break;
                    case "turn off":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] = false;
                            }
                        }
                        break;
                    case "turn on":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] = true;
                            }
                        }
                        break;
                }
            }

            int lights = 0;

            for (int x = 0; x <= 999; x++)
            {
                for (int y = 0; y <= 999; y++)
                {
                    if (grid[x, y])
                        lights++;
                }
            }

            Console.WriteLine("{0} lights are lit", lights);
        }
    }
}
