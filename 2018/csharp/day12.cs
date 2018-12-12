using System;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day12
    {
        public static void Solve()
        {
            var lines = File.ReadAllLines(Path.Combine("..", "input", "day12.input")).ToList();
            int prevSum = 0, zeroPotOffset = 0, sum = 0, gen = 1;
            string state = PadPots(lines[0].Split(" ")[2], ref zeroPotOffset);
            var patterns = lines.Where(l => l.Contains("=>")).Select(part => part.Split(" => ")).ToDictionary(arr => arr[0], arr => arr[1][0]);
            string prevState = "";

            while (state != prevState)
            {
                prevState = state;
                prevSum = sum;
                string newState = "";
                for (int pos = 2; pos < state.Length - 2; pos++)
                    newState += patterns[state.Substring(pos - 2, 5)];

                zeroPotOffset -= 2;
                state = PadPots(newState, ref zeroPotOffset);
                sum = 0;
                for (int i = 0; i < state.Length; i++)
                    if (state[i] == '#')
                        sum += i - zeroPotOffset;

                if (gen == 20)
                    Console.WriteLine("day 12, part a: {0}", sum);

                gen++;
            }
            Console.WriteLine("day 12, part b: {0}", (5000000000 - gen + 1) * (sum - prevSum) + sum);
        }

        private static string PadPots(string state, ref int pot)
        {
            while (!state.StartsWith("....."))
            {
                state = '.' + state;
                pot++;
            }
            while (!state.EndsWith("....."))
                state += '.';
            return state;
        }
    }
}
