using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day2
    {
        public static void Solve()
        {
            var lines = File.ReadLines(Path.Combine("..", "input", "day2.input")).ToList();
            solveA(lines);
            solveB(lines);
        }

        public static void solveA(List<string> lines)
        {
            var twos = 0;
            var threes = 0;

            foreach (var line in lines)
            {
                var letters = new Dictionary<char, int>();
                foreach (var c in line)
                {
                    if (letters.ContainsKey(c))
                    {
                        letters[c]++;
                    }
                    else
                    {
                        letters[c] = 1;
                    }
                }

                if (letters.Values.Contains(2))
                    twos++;

                if (letters.Values.Contains(3))
                    threes++;
            }

            Console.WriteLine("day2, answer a: {0}", twos * threes);
        }

        public static void solveB(List<string> lines)
        {
            lines.Sort();
            for (int i = 0; ; i++)
            {
                int diffs = 0;
                int j = 0;
                string s = "";
                while (diffs < 2 && j < lines[i].Length)
                {
                    if (lines[i][j] != lines[i + 1][j])
                        diffs++;
                    else
                        s += lines[i][j];
                    j++;
                }

                if (diffs == 1)
                {
                    Console.WriteLine("day2, answer b: {0}", s);
                    return;
                }
            }
        }
    }
}

