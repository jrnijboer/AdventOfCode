using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day7
    {
        public static void Solve()
        {
            var input = File.ReadAllLines(Path.Combine("..", "input", "day7.input"));
            var requirements = new Dictionary<char, HashSet<char>>();
            var startNodes = new HashSet<char>();
            foreach (var line in input)
            {
                var steps = line.ToLower().Split("step ");
                startNodes.Add(steps[1][0]);
                startNodes.Add(steps[2][0]);
                if (!requirements.ContainsKey(steps[2][0]))
                    requirements[steps[2][0]] = new HashSet<char> { steps[1][0] };
                else
                    requirements[steps[2][0]].Add(steps[1][0]);
            }
            startNodes.ExceptWith(requirements.Keys);

            SolveA(requirements.ToDictionary(k => k.Key, k => k.Value.ToHashSet()), startNodes.OrderBy(x => x).ToList());
            SolveB(requirements, startNodes.OrderBy(x => x).ToList());
        }

        private static void SolveA(Dictionary<char, HashSet<char>> requirements, List<char> sequence)
        {
            while (requirements.Count > 0)
            {
                char next = (char)('z' + 1);
                foreach (var key in requirements.Keys.OrderBy(x => x).ToList())
                {
                    if (key > next)
                        break;
                    if (requirements[key].ToList().Intersect(sequence).Count() == requirements[key].Count)
                        next = key;
                }
                sequence.ForEach(c => requirements[next].Remove(c));
                if (requirements[next].Count == 0)
                    requirements.Remove(next);
                sequence.Add(next);
            }
            Console.WriteLine("day7, part a: {0}", new string(sequence.ToArray()));
        }

        private static void SolveB(Dictionary<char, HashSet<char>> requirements, List<char> sequence)
        {
            const int WORK = 60, MAX_QUEUE = 5;
            int time = -1;
            var queue = new Dictionary<char, int>();
            sequence.ForEach(c => queue[c] = 1 + c - 'a' + WORK);
            sequence = new List<char>();
            var availableChars = new List<char>();

            while (queue.Keys.Count > 0)
            {
                time++;
                if (queue.Values.Min() == 0)
                {
                    char handledKey = queue.First(x => x.Value == 0).Key;
                    sequence.Add(handledKey);
                    queue.Remove(handledKey);
                    foreach (var key in requirements.Keys.OrderBy(x => x).ToList())
                        if (requirements[key].ToList().Intersect(sequence).Count() == requirements[key].Count)
                        {
                            availableChars.Add(key);
                            requirements.Remove(key);
                        }
                }
                availableChars.Sort();

                while (queue.Keys.Count < MAX_QUEUE && availableChars.Count > 0)
                {
                    queue[availableChars[0]] = availableChars[0] - 'a' + 1 + WORK;
                    availableChars.RemoveAt(0);
                }
                queue.Keys.ToList().ForEach(k => queue[k]--);                
            }
            Console.WriteLine("day7, part b: {0}", time);
        }
    }
}
