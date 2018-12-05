using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace aoc2018
{
    class Day4
    {
        public static void Solve()
        {
            var lines = File.ReadLines(Path.Combine("..", "input", "day4.input")).ToList().ToList(); ;
            lines.Sort();
            var guards = new Dictionary<int, Dictionary<int, int>>();
            int guard = 0;
            int sleep = 0;
            var r = new Regex(@"^\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (Guard|falls|wakes) (#\d+)?");
            foreach (var line in lines)
            {
                var m = r.Match(line);
                switch (m.Groups[6].Value)
                {
                    case "Guard":
                        guard = int.Parse(m.Groups[7].Value.Substring(1));
                        if (!guards.ContainsKey(guard))
                            guards[guard] = new Dictionary<int, int>();
                        break;
                    case "falls":
                        sleep = int.Parse(m.Groups[5].Value);
                        break;
                    case "wakes":
                        int wakes = int.Parse(m.Groups[5].Value);
                        for (int i = 0; i < wakes - sleep; i++)
                            if (!guards[guard].ContainsKey(i + sleep))
                                guards[guard][i + sleep] = 1;
                            else
                                guards[guard][i + sleep]++;
                        break;
                }
            }

            guard = guards.FirstOrDefault(x => x.Value.Values.Sum() == guards.Max(g => g.Value.Values.Sum())).Key;
            int sleepiestMinute = guards[guard].FirstOrDefault(x => x.Value == guards[guard].Values.Max()).Key;
            Console.WriteLine("day 4, answer a: {0}", guard * sleepiestMinute);

            int max = 0;
            foreach (int key in guards.Keys)
            {
                if (guards[key].Count > 0 && guards[key].Max(x => x.Value) > max)
                {
                    max = (guards[key].Max(x => x.Value));
                    guard = key;
                }
            }
            sleepiestMinute = guards[guard].FirstOrDefault(x => x.Value == max).Key;
            Console.WriteLine("day 4, answer b: {0}", guard * sleepiestMinute);
        }
    }
}
