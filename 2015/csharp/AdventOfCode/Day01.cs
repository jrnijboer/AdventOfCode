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
