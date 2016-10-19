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
        static void Day19b()
        {
            var input = File.ReadAllLines("input/day19.input");
            var replacements = new List<Tuple<string, string>>();

            var startElement = input[input.Length - 1];

            string pattern = @"^(\w+) => (\w+)$";
            for (int i = 0; i < input.Length - 2; i++)
            {
                var match = Regex.Match(input[i], pattern);
                if (match.Success)
                    replacements.Add(new Tuple<string, string>(match.Groups[1].Value, match.Groups[2].Value));
            }
                        
            List<string> elementList = new List<string>();
            
            //elements in reversed list
            startElement = new string(startElement.Reverse().ToArray());
            int pos = 0;
            while (pos < startElement.Length)
            {
                if (startElement[pos] >= 'a' && startElement[pos] <= 'z')
                {
                    elementList.Add(new string(startElement.Substring(pos, 2).Reverse().ToArray()));
                    pos++;
                }
                else
                {
                    elementList.Add(startElement[pos].ToString());
                }
                pos++;
            }
          
            int yElements = elementList.Where(e => e == "Y").Count();
            int RnArElements = elementList.Where(e => e == "Ar" || e == "Rn").Count();

            int solution = elementList.Count - RnArElements - (2 * yElements) - 1;
            Console.WriteLine("Found answer: {0}", solution);
        }
        
        static void Day19a()
        {
            var input = File.ReadAllLines("input/day19.input");
            var replacements = new List<Tuple<string, string>>();
            var moleculeVariants = new List<string>();
            var startElement = input[input.Length - 1];

            string pattern = @"^(\w+) => (\w+)$";
            for (int i = 0; i < input.Length - 2; i++)
            {
                var match = Regex.Match(input[i], pattern);
                replacements.Add(new Tuple<string, string>(match.Groups[1].Value, match.Groups[2].Value));
            }

            foreach (var replacement in replacements)
            {
                //todo: correct pattern maken
                var matches = Regex.Matches(startElement, replacement.Item1);

                foreach (Match match in matches)
                {
                    moleculeVariants.Add(startElement.Substring(0, match.Index) + replacement.Item2 + startElement.Substring(match.Index + replacement.Item1.Length));
                }
            }

            Console.WriteLine("After testing there are {0} distinct molecules", moleculeVariants.Distinct().Count());
        }
    }
}