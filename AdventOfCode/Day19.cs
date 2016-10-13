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
            var moleculeVariants = new List<string>();

            var startElement = input[input.Length - 1];

            string pattern = @"^(\w+) => (\w+)$";
            for (int i = 0; i < input.Length - 2; i++)
            {
                var match = Regex.Match(input[i], pattern);
                replacements.Add(new Tuple<string, string>(match.Groups[1].Value, match.Groups[2].Value));
            }

            var ArReplacements = new Dictionary<string, string>(); 
            foreach (var replacement in replacements.ToArray())
            {
                if (replacement.Item2.EndsWith("Ar"))
                {
                    ArReplacements[replacement.Item2] = replacement.Item1;
                    replacements.Remove(replacement);
                }
            }

            int pos = 1;

            while (pos > 0)
            {
                pos = startElement.IndexOf("Ar");
                startElement = GetArReplacement(startElement.Substring(0, pos)) + startElement.Substring(pos + 2);
            }

            Console.WriteLine("cleaned startelemen: {0}", startElement);

            //int count = startElement.Split(new[] { "SiRnFYFAr" }, StringSplitOptions.None).Count() - 1;
            //startElement = startElement.Replace("SiRnFYFAr", "Ca");
            
        }

        private static string GetArReplacement(string molecule)
        {
            while (molecule.IndexOf("Ar") > 0)
            {


                break;
            }

            return molecule;
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