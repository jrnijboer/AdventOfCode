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
        static void Day5b()
        {
            var strings = File.ReadAllLines("input/day5.input");
            int niceStrings = 0;

            foreach (string s in strings)
            {
                if (isNiceStringB(s))
                    niceStrings++;
            }

            Console.WriteLine("There were {0} nice string in the input", niceStrings);
        }

        private static bool isNiceStringB(string s)
        {
            bool containsDoublePair = hasDoublePair(s);
            bool containsRepeat = hasRepeat(s);

            return containsDoublePair && containsRepeat;
        }

        private static bool hasRepeat(string s)
        {
            int pos = 0;
            while (pos < s.Length - 2)
            {
                if (s[pos] == s[pos + 2])
                    return true;
                pos++;
            }

            return false;
        }

        private static bool hasDoublePair(string s)
        {
            int pos = 0;
            while (pos < s.Length - 3)
            {
                if (s.Substring(pos + 2).Contains(s.Substring(pos, 2)))
                    return true;
                pos++;
            }
            return false;
        }

        static void Day5a()
        {
            var strings = File.ReadAllLines("input/day5.input");
            int niceStrings = 0;

            foreach (string s in strings)
            {
                if (isNiceStringA(s))
                    niceStrings++;
            }

            Console.WriteLine("There were {0} nice string in the input", niceStrings);
        }

        private static bool isNiceStringA(string s)
        {
            if (s.Contains("ab") || s.Contains("cd") || s.Contains("pq") || s.Contains("xy"))
                return false;
            int pos = 0;
            bool hasDouble = false;

            int vowels = 0;
            while (pos < s.Length)
            {
                if (pos < s.Length - 1 && s[pos + 1] == s[pos])
                    hasDouble = true;
                if (s[pos] == 'a' || s[pos] == 'e' || s[pos] == 'i' || s[pos] == 'o' || s[pos] == 'u')
                    vowels++;
                pos++;
            }

            return hasDouble && vowels >= 3;
        }
    }
}
