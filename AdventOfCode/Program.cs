using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Security.Cryptography;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AdventOfCode
{
    class Program
    {
        static void Main(string[] args)
        {
            Day6b();
            Console.ReadKey();
        }

        static void Day6b()
        {
            int[,] grid = new int[1000, 1000];

            for (int x = 0; x <= 999; x++)
            {
                for (int y = 0; y <= 999; y++)
                {
                    grid[x, y] = 0;
                }
            }

            var instructions = File.ReadAllLines("input/day6.input");
            string pattern = @"^(.*?)(\d+),(\d+) .* (\d+),(\d+)$";

            foreach (var instruction in instructions)
            {
                var groups = Regex.Match(instruction, pattern).Groups;
                string oper = groups[1].Value.Trim();
                int xStart = int.Parse(groups[2].Value);
                int yStart = int.Parse(groups[3].Value);
                int xStop = int.Parse(groups[4].Value);
                int yStop = int.Parse(groups[5].Value);

                switch (oper)
                {
                    case "toggle":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] += 2;
                            }
                        }
                        break;
                    case "turn off":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] = grid[x, y] > 0 ? grid[x, y]-=1 : 0;
                            }
                        }
                        break;
                    case "turn on":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y]++;
                            }
                        }
                        break;
                }
            }

            long lights = 0;

            for (int x = 0; x <= 999; x++)
            {
                for (int y = 0; y <= 999; y++)
                {
                    lights += (grid[x, y]);
                        
                }
            }

            Console.WriteLine("{0} lights are lit", lights);
        }

        static void Day6a()
        {
            bool[,] grid = new bool[1000, 1000];

            for (int x = 0; x <= 999; x++)
            {
                for (int y = 0; y <= 999; y++)
                {
                    grid[x, y] = false;
                }
            }

            var instructions = File.ReadAllLines("input/day6.input");
            string pattern = @"^(.*?)(\d+),(\d+) .* (\d+),(\d+)$";

            foreach (var instruction in instructions)
            {
                var groups = Regex.Match(instruction, pattern).Groups;
                string oper = groups[1].Value.Trim();
                int xStart = int.Parse(groups[2].Value);
                int yStart = int.Parse(groups[3].Value);
                int xStop = int.Parse(groups[4].Value);
                int yStop = int.Parse(groups[5].Value);

                switch (oper)
                {
                    case "toggle":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] = !grid[x, y];
                            }
                        }
                        break;
                    case "turn off":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] = false;
                            }
                        }
                        break;
                    case "turn on":
                        for (int x = xStart; x <= xStop; x++)
                        {
                            for (int y = yStart; y <= yStop; y++)
                            {
                                grid[x, y] = true;
                            }
                        }
                        break;
                }
            }

            int lights = 0;

            for (int x = 0; x <= 999; x++)
            {
                for (int y = 0; y <= 999; y++)
                {
                    if (grid[x, y])
                        lights++;
                }
            }

            Console.WriteLine("{0} lights are lit", lights);
        }

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

        static void Day4b()
        {
            int i = 0;
            string input = "iwrupvqb";
            string hash = "";

            using (MD5 md5Hash = MD5.Create())
            {
                while (!hash.StartsWith("000000"))
                {
                    hash = GetMd5Hash(md5Hash, input + i.ToString());
                    i++;
                }
            }

            Console.WriteLine("found a hash with i = {0}", --i);
        }

        static void Day4a()
        {
            int i = 0;
            string input = "iwrupvqb";
            string hash = "";

            using (MD5 md5Hash = MD5.Create())
            {
                while (!hash.StartsWith("00000"))
                {
                    hash = GetMd5Hash(md5Hash, input + i.ToString());
                    i++;
                }
            }

            Console.WriteLine("found a hash with i = {0}", --i);
        }

        static void Day3b()
        {
            int xSanta = 0;
            int ySanta = 0;

            int xRobo = 0;
            int yRobo = 0;
            List<string> visitedLocations = new List<string>();

            var directions = File.ReadAllText("input/day3.input");
            int pos = 0;
            do
            {
                visitedLocations.Add(string.Format("{0},{1}", xSanta, ySanta));
                visitedLocations.Add(string.Format("{0},{1}", xRobo, yRobo));
                switch (directions[pos])
                {
                    case '^':
                        ySanta++;
                        break;
                    case '>':
                        xSanta++;
                        break;
                    case '<':
                        xSanta--;
                        break;
                    case 'v':
                        ySanta--;
                        break;
                }
                pos++;

                switch (directions[pos])
                {
                    case '^':
                        yRobo++;
                        break;
                    case '>':
                        xRobo++;
                        break;
                    case '<':
                        xRobo--;
                        break;
                    case 'v':
                        yRobo--;
                        break;
                }
                pos++;


            } while (pos < (directions.Length));
            int result = visitedLocations.Distinct().Count();

            Console.WriteLine("Santa and Robo-Santa visited {0} locations", result);
        }

        static void Day3a()
        {
            int x = 0;
            int y = 0;

            List<string> visitedLocations = new List<string>();

            var directions = File.ReadAllText("input/day3.input");
            int pos = 0;
            do
            {
                visitedLocations.Add(string.Format("{0},{1}", x, y));
                switch (directions[pos])
                {
                    case '^':
                        y++;
                        break;
                    case '>':
                        x++;
                        break;
                    case '<':
                        x--;
                        break;
                    case 'v':
                        y--;
                        break;
                }
                pos++;
            } while (pos < (directions.Length));
            int result = visitedLocations.Distinct().Count();

            Console.WriteLine("Santa visited {0} locations", result);
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

        // Helper functions down here


        //from MSDN
        static string GetMd5Hash(MD5 md5Hash, string input)
        {

            // Convert the input string to a byte array and compute the hash.
            byte[] data = md5Hash.ComputeHash(Encoding.UTF8.GetBytes(input));

            // Create a new Stringbuilder to collect the bytes
            // and create a string.
            StringBuilder sBuilder = new StringBuilder();

            // Loop through each byte of the hashed data 
            // and format each one as a hexadecimal string.
            for (int i = 0; i < data.Length; i++)
            {
                sBuilder.Append(data[i].ToString("x2"));
            }

            // Return the hexadecimal string.
            return sBuilder.ToString();
        }


    }
}
