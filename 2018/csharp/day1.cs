using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day1
    {
        public static void Solve()
        {
            var values = File.ReadAllLines(Path.Combine("..", "input", "day1.input")).Select(line => int.Parse(line));
            Console.WriteLine("Day 1, answer a: {0}", values.Sum());

            var f = 0;
            var freqs = new Dictionary<int, int>();

            while (true)
            {
                foreach (var value in values)
                {
                    f += value;

                    if (!freqs.ContainsKey(f))
                    {
                        freqs[f] = 0;
                    }
                    else
                    {
                        Console.WriteLine("Day 1, answer b: {0}", f);
                        return;
                    }
                }
            }
        }
    }
}
