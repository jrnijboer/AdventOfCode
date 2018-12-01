using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static void Day12a()
        {
            var input = File.ReadAllText("input/day12.input");
            int sum = 0;
            foreach (Match match in Regex.Matches(input, @"(-?\d+)"))
            {
                sum += int.Parse(match.Groups[1].Value);
            }
            Console.WriteLine("The sum of all numbers is {0}", sum);
        }

        static void Day12b()
        {
            var input = File.ReadAllText("input/day12.input");
            input = cleanInput(input);
            int sum = 0;
            foreach (Match match in Regex.Matches(input, @"(-?\d+)"))
            {
                sum += int.Parse(match.Groups[1].Value);
            }
            Console.WriteLine("The sum of all numbers is {0}", sum);
        }

        private static string cleanInput(string input)
        {
            Stack<int> openBraces = new Stack<int>();
            Stack<int> openBrackets = new Stack<int>();
            int pos = 0;

            while (pos < input.Length)
            {
                if (input[pos] == '{')
                    openBraces.Push(pos);

                else if (input[pos] == '}')
                {
                    int subpos = openBraces.Peek();
                    while (subpos < pos)
                    {
                        if (input[subpos] == '[')
                            openBrackets.Push(subpos);
                        else if (input[subpos] == ']')
                        {
                            string substring = input.Substring(openBrackets.Peek(), subpos - openBrackets.Peek());
                            substring = substring.Replace("red", "xxx");
                            input = input.Substring(0, openBrackets.Peek()) + substring + input.Substring(subpos);

                            openBrackets.Pop();
                        }
                        subpos++;
                    }

                    if (input.Substring(openBraces.Peek(), pos - openBraces.Peek()).Contains("red"))
                    {
                        string copy = input;
                        input = copy.Substring(0, openBraces.Peek() + 1);
                        int count = pos - openBraces.Peek();
                        for (int i = 0; i < count - 1; i++)
                            input += 'x';
                        input += copy.Substring(pos);
                    }
                    openBraces.Pop();
                }

                pos++;
            }
            return input;
        }
    }
}
