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
        static void Day7a()
        {
            var input = File.ReadAllLines("input/day7.input");
            
            Dictionary<string, string> circuits = new Dictionary<string, string>();
            foreach (string circuit in input)
            {
                var x = circuit.Split(new[] { "-> " }, StringSplitOptions.None).ToList();
                circuits[x[1]] = " " + x[0];
            }

            //uncomment for day7b
            //circuits["b"] = "16076"; //== result of day7a

            while (!Regex.IsMatch(circuits["a"], @"\d"))
            {
                Console.WriteLine("");
                Console.WriteLine("-------------");
                Console.WriteLine("");
                foreach (string key in circuits.Keys.ToArray())
                {
                    if (Regex.IsMatch(circuits[key].Trim(), @"^\d+$"))
                    {                        
                        foreach (string k in circuits.Keys.ToArray())
                        {
                            if (Regex.IsMatch(circuits[k], " " + key + " "))
                            {
                                circuits[k] = Regex.Replace(circuits[k], " " + key + " ", circuits[key]);
                                Console.WriteLine("replaced {0} with {1} for key {2}", key, circuits[key], k);
                            }
                        }
                        circuits.Remove(key);
                        Console.WriteLine("removed key {0}", key);
                    }
                    else 
                    {
                        var match = Regex.Match(circuits[key], @"(\d+) ?(AND|OR|RSHIFT|LSHIFT) ?(\d+)");
                        if (match.Success)
                        {
                            ushort op1 = ushort.Parse(match.Groups[1].Value);
                            string oper = match.Groups[2].Value;
                            ushort op2 = ushort.Parse(match.Groups[3].Value);
                            ushort result;
                            switch (oper)
                            {
                                case "AND":
                                    result = (ushort)(op1 & op2);
                                    break;
                                case "OR":
                                    result = (ushort)(op1 | op2);
                                    break;
                                case "RSHIFT":
                                    result = (ushort)(op1 >> (int)op2);
                                    break;
                                case "LSHIFT":
                                    result = (ushort)(op1 << (int)op2);
                                    break;
                                default:
                                    throw new Exception();                                    
                            }
                            Console.WriteLine("replacing {0} with {1} for key {2}", circuits[key], result, key);
                            circuits[key] = result.ToString();

                        }
                        else
                        {
                            match = Regex.Match(circuits[key], @"NOT ?(\d+)");
                            if (match.Success)
                            {
                                ushort op = ushort.Parse(match.Groups[1].Value);
                                Console.WriteLine("replacing {0} with {1} for key {2}", circuits[key], (ushort)~op, key);
                                circuits[key] = ((ushort)(~op)).ToString();
                            }
                        }
                    }                    
                }
            }

            Console.WriteLine("The output of a is {0}", circuits["a"]);
        }

        class Command
        {
            public string input
            {
                get; set;
            }

            public string output
            {
                get; set;
            }
        }
    }
}
