using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static void Day2b()
        {
            var ribbonLength = 0;
            var presents = File.ReadAllLines("input/day2.input");
            foreach (var present in presents)
            {
                var dims = present.Split('x').Select(int.Parse).OrderBy(d => d).ToArray();
                ribbonLength += 2 * dims[0] + 2 * dims[1] + dims[0] * dims[1] * dims[2];
            }
            Console.WriteLine("Santa needs to order {0} feet of ribbon", ribbonLength);
        }

        static void Day2a()
        {
            var sqrft = 0;
            var presents = File.ReadAllLines("input/day2.input");

            foreach (var present in presents)
            {
                var dims = present.Split('x').Select(int.Parse).OrderBy(d => d).ToArray();
                var slack = dims[0] * dims[1];
                sqrft += slack + 2 * (dims[0] * dims[1] + dims[1] * dims[2] + dims[0] * dims[2]);
            }
            Console.WriteLine("Santa needs to order {0} square feet of paper", sqrft);
        }
    }
}
