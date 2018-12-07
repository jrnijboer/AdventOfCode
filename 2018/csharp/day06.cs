using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day6
    {
        public static void Solve()
        {            
            var input = File.ReadLines(Path.Combine("..", "input", "day6.input")).ToList();
            var coords = new Dictionary<char, Point>();
            int minx = int.MaxValue, miny = int.MaxValue;
            int maxx = 0, maxy = 0;
            var areas = new Dictionary<char, int>();
            int safePositions = 0;            

            for (int i = 0; i < input.Count; i++)
            {
                var s = input[i].Split(",");
                var p = new Point(int.Parse(s[0]), int.Parse(s[1]));
                coords[(char)('a' + i)] = p;
                minx = Math.Min(int.Parse(s[0]), minx);
                miny = Math.Min(int.Parse(s[1]), miny);
                maxx = Math.Max(int.Parse(s[0]), maxx);
                maxy = Math.Max(int.Parse(s[1]), maxy);
                areas[(char)('a' + i)] = 0;
            }

            for (int y = miny; y <= maxy; y++)
                for (int x = minx; x <= maxx; x++)
                {
                    int minDistance = int.MaxValue;
                    List<char> closestNodes = new List<char>();
                    int sumDistance = 0;
                    foreach (var p in coords.Keys)
                    {
                        int distance = Math.Abs(x - coords[p].X) + Math.Abs(y - coords[p].Y);
                        if (distance < minDistance)
                        {
                            minDistance = distance;
                            closestNodes = new List<char> { p };
                        }
                        else if (distance == minDistance)
                            closestNodes.Add(p);
                        sumDistance += distance;
                    }

                    if (closestNodes.Count == 1)
                        areas[closestNodes.Single()]++;
                    if (sumDistance < 10000)
                        safePositions++;                   
                }
            coords
                .Where((kvp) => kvp.Value.X == minx || kvp.Value.X == maxx || kvp.Value.Y == miny || kvp.Value.Y == maxy)
                .Select(x => x.Key).ToList()
                .ForEach(x => areas.Remove(x));
            Console.WriteLine("day6, part a: {0}", areas.Values.Max());
            Console.WriteLine("day6, part b: {0}", safePositions);
        }
    }
}
