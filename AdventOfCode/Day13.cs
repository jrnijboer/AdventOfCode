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
        private static List<List<string>> allCombinations = new List<List<string>>();

        static void Day13b()
        {
            //ugh horribly slow for 9!
            var input = File.ReadAllLines("input/day13.input");
            int happiness = 0;
            Dictionary<string, int> happyDict = new Dictionary<string, int>();
            List<string> persons = new List<string>();
            foreach (string s in input)
            {
                var match = Regex.Match(s, @"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.$");
                happyDict[match.Groups[1] + "," + match.Groups[4]] = int.Parse(match.Groups[3].Value) * (match.Groups[2].Value == "gain" ? 1 : -1);
                persons.Add(match.Groups[1].Value);
            }

            persons = persons.Distinct().ToList();
            persons.ForEach(p =>
            {
                happyDict[p + ",Santa"] = 0;
                happyDict["Santa," + p] = 0;
            });

            persons.Add("Santa");

            List<string> temp = new List<string>();
            GetCombinations(persons.ToArray(), temp);

            foreach (var combination in allCombinations)
            {
                int combHappiness = 0;
                for (int i = 0; i < persons.Count; i++)
                {
                    combHappiness += happyDict[combination[i] + "," + combination[(i + 1) % persons.Count]];
                    combHappiness += happyDict[combination[(i + 1) % persons.Count] + "," + combination[i]];
                }

                if (combHappiness > happiness)
                    happiness = combHappiness;

            }
            Console.WriteLine("The best seating will give {0} happiness", happiness);
        }

        static void Day13a()
        {
            var input = File.ReadAllLines("input/day13.input");
            int happiness = 0;
            Dictionary<string, int> happyDict = new Dictionary<string, int>();
            List<string> persons = new List<string>();
            foreach (string s in input)
            {
                var match = Regex.Match(s, @"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.$");
                happyDict[match.Groups[1] + "," + match.Groups[4]] = int.Parse(match.Groups[3].Value) * (match.Groups[2].Value == "gain" ? 1 : -1);
                persons.Add(match.Groups[1].Value);
            }

            persons = persons.Distinct().ToList();

            List<string> temp = new List<string>();
            GetCombinations(persons.ToArray(), temp);

            foreach (var combination in allCombinations)
            {
                int combHappiness = 0;
                for (int i = 0; i < persons.Count; i++)
                {
                    combHappiness += happyDict[combination[i] + "," + combination[(i + 1) % persons.Count]];
                    combHappiness += happyDict[combination[(i + 1) % persons.Count] + "," + combination[i]];
                }

                if (combHappiness > happiness)
                    happiness = combHappiness;

            }
            Console.WriteLine("The best seating will give {0} happiness", happiness);
        }

        //http://stackoverflow.com/a/5129280
        private static void GetCombinations(string[] words, List<string> temp)
        {
            if (temp.Count == words.Length)
            {
                List<string> clone = temp.ToList();
                if (clone.Distinct().Count() == clone.Count)
                {
                    allCombinations.Add(clone);
                }
                return;
            }

            for (int i = 0; i < words.Length; i++)
            {
                temp.Add(words[i]);
                GetCombinations(words, temp);
                temp.RemoveAt(temp.Count - 1);
            }

        }
    }
}
