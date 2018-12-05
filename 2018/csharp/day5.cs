using System;
using System.IO;

namespace aoc2018
{
    class Day5
    {
        public static void Solve()
        {
            var input = File.ReadAllText("day5.input");
            Console.WriteLine("day5, answer a: {0}", React(input));

            int min = int.MaxValue;
            for (char replaceChar = 'a'; replaceChar <= 'z'; replaceChar++)
            {
                input = File.ReadAllText("day5.input");
                input = input.Replace(replaceChar.ToString(), "").Replace(replaceChar.ToString().ToUpper(), "");
                min = Math.Min(min, React(input));
            }
            Console.WriteLine("day5, answer a: {0}", min);
        }

        static int React(string input)
        {
            bool changed = true;
            while (changed)
            {
                int len = input.Length;
                for (char c = 'a'; c <= 'z'; c++)
                    input = input.Replace(c.ToString().ToUpper() + c, "").Replace(c + c.ToString().ToUpper(), "");
                changed = len != input.Length;
            }
            return input.Length;
        }
    }
}
