using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    class Program
    {
        static void Main(string[] args)
        {
            Day3a();
            Console.ReadKey();
        }

        static void Day3a()
        {

        }

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

        static void Day1b()
        {
            var input = File.ReadAllText("input/day1.input");
            int floor = 0;
            int position = 0;
            while (floor >= 0)
            {
                if (input[position] == '(')
                    floor++;
                else floor--;

                position++;
            }
            Console.WriteLine("Santa went to the basement in position {0}", position);
        }

        static void Day1a()
        {
            var input = File.ReadAllText("input/day1.input");
            var floor = input.Count(c => c == '(') - input.Count(c => c == ')');
            Console.WriteLine("Santa should go to floor {0}", floor);
        }
    }
}
