using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day9
    {
        public static void Solve()
        {
            var input = File.ReadAllText(Path.Combine("..", "input", "day9.input")).Split(" ");
            int players = int.Parse(input[0]);
            int marbles = int.Parse(input[6]) * 100;
            var circle = new LinkedList<int>();
            circle.AddFirst(0);
            var current = circle.First;
            var scores = new Dictionary<int, long>();
            Enumerable.Range(0, players).ToList().ForEach(i => scores[i] = 0);

            for (int i = 1; i < marbles; i++)
            {
                if (i == marbles / 100)
                    Console.WriteLine("day 9, answer a: {0}", scores.Values.Max());
                if (i % 23 == 0)
                {
                    for (int j = 0; j < 7; j++)
                        current = current.Previous ?? circle.Last;
                    scores[i % players] += current.Value;
                    scores[i % players] += i;
                    var next = current.Next;
                    circle.Remove(current);
                    current = next;
                }
                else
                    current = current.Next == null ? circle.AddAfter(circle.First, i) : circle.AddAfter(current.Next, i);
            }
            Console.WriteLine("day 9, answer b: {0}", scores.Values.Max());
        }
    }
}
