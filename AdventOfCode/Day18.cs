using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static readonly int gridSize = 100;
        static readonly int generations = 100;

        static void Day18b()
        {
            var input = File.ReadAllLines("input/day18.input");
            bool[,] grid = new bool[gridSize, gridSize];
            for (int i = 0; i < input.Length; i++)
                for (int j = 0; j < input[i].Length; j++)
                {
                    grid[i, j] = input[i][j] == '#';
                }

            grid[0, 0] = true;
            grid[0, gridSize - 1] = true;
            grid[gridSize - 1, 0] = true;
            grid[gridSize - 1, gridSize - 1] = true;

            for (int i = 0; i < generations; i++)
            {
                grid = CalculateNextGeneration(grid, false);
                grid[0, 0] = true;
                grid[0, gridSize - 1] = true;
                grid[gridSize - 1, 0] = true;
                grid[gridSize - 1, gridSize - 1] = true;
            }

            int lights = 0;
            for (int i = 0; i < input.Length; i++)
                for (int j = 0; j < input[i].Length; j++)
                    if (grid[i, j])
                        lights++;

            Console.WriteLine("After 100 generations there are {0} lights on", lights);
        }

        static void Day18a()
        {
            var input = File.ReadAllLines("input/day18.input");
            bool[,] grid = new bool[gridSize, gridSize];
            for (int i = 0; i < input.Length; i++)
                for (int j = 0; j < input[i].Length; j++)
                {
                    grid[i, j] = input[i][j] == '#';
                }

            for (int i = 0; i < generations; i++)
                grid = CalculateNextGeneration(grid, false);

            int lights = 0;
            for (int i = 0; i < input.Length; i++)
                for (int j = 0; j < input[i].Length; j++)
                    if (grid[i, j])
                        lights++;

            Console.WriteLine("After 100 generations there are {0} lights on", lights);
        }

        private static bool[,] CalculateNextGeneration(bool[,] grid, bool printToConsole)
        {
            bool[,] newGrid = new bool[gridSize, gridSize];

            for (int i = 0; i < gridSize; i++)
                for (int j = 0; j < gridSize; j++)
                {
                    int neighbours = calculateNeighbours(i, j, grid);
                    if (grid[i, j])
                    {
                        newGrid[i, j] = neighbours == 2 || neighbours == 3;

                    }
                    else
                    {
                        newGrid[i, j] = neighbours == 3;
                    }
                }

            if (printToConsole)
            {
                for (int i = 0; i < gridSize; i++)
                {
                    for (int j = 0; j < gridSize; j++)
                    {
                        Console.Write(newGrid[i, j] ? '#' : '.');
                    }
                    Console.WriteLine();
                }
                Console.WriteLine();
            }
            return newGrid;
        }

        private static int calculateNeighbours(int i, int j, bool[,] grid)
        {
            int neighbours = 0;
            for (int x = -1; x <= 1; x++)
                for (int y = -1; y <= 1; y++)
                    if (i + x >= 0 && j + y >= 0 && i + x <= gridSize - 1 && j + y <= gridSize - 1 && grid[i + x, j + y] && !(x == 0 && y == 0))
                        neighbours++;

            return neighbours;
        }
    }
}
