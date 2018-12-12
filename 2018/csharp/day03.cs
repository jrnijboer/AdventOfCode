using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace aoc2018
{
    class Day3
    {
        public static void Solve()
        {
            var lines = File.ReadLines(Path.Combine("..", "input", "day3.input")).ToList();
            var pattern = @"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$";
            var r = new Regex(pattern);
            var claims = new Dictionary<Point, List<int>>();
            foreach (var line in lines)
            {
                var m = r.Match(line);
                int id = int.Parse(m.Groups[1].Value);
                int left = int.Parse(m.Groups[2].Value);
                int top = int.Parse(m.Groups[3].Value);
                int width = int.Parse(m.Groups[4].Value);
                int height = int.Parse(m.Groups[5].Value);
                for (int i = top; i < height + top; i++)
                {
                    for (int j = left; j < width + left; j++)
                    {
                        Point p = new Point(i, j);
                        if (claims.ContainsKey(p))
                            claims[p].Add(id);
                        else
                            claims[p] = new List<int> { id };
                    }
                }
            }

            int overlapSize = 0;
            HashSet<int> overlaps = new HashSet<int>();
            foreach (var key in claims.Keys)
                if (claims[key].Count > 1)
                {
                    overlapSize++;
                    foreach (var i in claims[key])
                    {
                        overlaps.Add(i);
                    }
                }

            Console.WriteLine("day3, answer a: {0}", overlapSize);
            Console.WriteLine("day3, answer b: {0}", Enumerable.Range(1, lines.Count).Except(overlaps).First());
        }
    }
}
