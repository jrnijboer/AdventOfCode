using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
namespace day3
{
    class Program
    {
        static void Main(string[] args)
        {
            SolveA();
            SolveB();
        }

        private static void SolveA()
        {
            int result = 0;
            var triangles = GetInput();

            triangles.ForEach(t =>
            {
                t.Sort();
                if (t[0] + t[1] > t[2])
                    result++;
            });
            Console.WriteLine("part 1: {0}", result);
        }

        private static void SolveB()
        {
            int result = 0;
            var triangles = GetInput();

            int i = 0;
            while (i < triangles.Count)
            {
                var t1 = new List<int> { triangles[i][0], triangles[i + 1][0], triangles[i + 2][0] }.OrderBy(n => n).ToList();
                var t2 = new List<int> { triangles[i][1], triangles[i + 1][1], triangles[i + 2][1] }.OrderBy(n => n).ToList();
                var t3 = new List<int> { triangles[i][2], triangles[i + 1][2], triangles[i + 2][2] }.OrderBy(n => n).ToList();

                if (t1[0] + t1[1] > t1[2])
                    result++;
                if (t2[0] + t2[1] > t2[2])
                    result++;
                if (t3[0] + t3[1] > t3[2])
                    result++;
                i += 3;
            }
            Console.WriteLine("part 2: {0}", result);
        }

        private static List<List<int>> GetInput()
        {
            return (from line in File.ReadAllLines("input.txt")
                    let groups = new Regex(@"^\s+(\d+)\s+(\d+)\s+(\d+)$").Match(line).Groups
                    select new List<int>
                        {
                             int.Parse(groups[1].Value),
                             int.Parse(groups[2].Value),
                             int.Parse(groups[3].Value)
                        }).ToList();
        }
    }
}