using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Text.RegularExpressions;

namespace aoc2018
{
    class Day10
    {
        public static void Solve()
        {
            var pixels = new List<Point>();
            var velocities = new List<Point>();
            var lines = File.ReadAllLines(Path.Combine("..", "input", "day10.input"));
            var r = new Regex(@"^position=<\s*(-?\d+),\s*(-?\d+)>\s+velocity=<\s*(-?\d+),\s*(-?\d)>$");
            foreach (var line in lines)
            {
                var m = r.Match(line);
                pixels.Add(new Point(int.Parse(m.Groups[1].Value), int.Parse(m.Groups[2].Value)));
                velocities.Add(new Point(int.Parse(m.Groups[3].Value), int.Parse(m.Groups[4].Value)));
            }

            int seconds = 0;
            while (true)
            {
                seconds++;
                for (int i = 0; i < pixels.Count; i++)
                    pixels[i] = new Point { X = pixels[i].X + velocities[i].X, Y = pixels[i].Y + velocities[i].Y };

                int minx = int.MaxValue, miny = int.MaxValue;
                int maxx = int.MinValue, maxy = int.MinValue;
                foreach (var pixel in pixels)
                {
                    minx = Math.Min(pixel.X, minx); miny = Math.Min(pixel.Y, miny);
                    maxx = Math.Max(pixel.X, maxx); maxy = Math.Max(pixel.Y, maxy);
                }
                if (maxy - miny <= 10)
                {
                    PrintGrid(pixels, minx, miny, maxx, maxy);
                    Console.WriteLine("day 10, answer b: {0}", seconds);
                    break;
                }
            }
        }

        private static void PrintGrid(List<Point> pixels, int minx, int miny, int maxx, int maxy)
        {
            for (int y = miny - 1; y <= 1 + maxy; y++)
            {
                for (int x = minx - 1; x <= 1 + maxx; x++)
                    if (pixels.Contains(new Point { X = x, Y = y }))
                        Console.Write('#');
                    else
                        Console.Write('.');
                Console.Write('\n');
            }
        }
    }
}
