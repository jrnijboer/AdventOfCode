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
        static void Day23b()
        {
            uint registerA = 1;
            uint registerB = 0;
            var instructions = File.ReadAllLines("input/day23.input");

            int pos = 0;
            int length = instructions.Length;

            while (pos < length)
            {
                var instructionLine = instructions[pos].Replace("+", "");
                var instruction = instructions[pos].Substring(0, 3);
                switch (instruction)
                {
                    case "hlf":
                        if (instructionLine.Substring(4, 1) == "a")
                            registerA /= 2;
                        else
                            registerB /= 2;
                        pos++;
                        break;

                    case "tpl":
                        if (instructionLine.Substring(4, 1) == "a")
                            registerA *= 3;
                        else
                            registerB *= 3;
                        pos++;
                        break;
                    case "inc":
                        if (instructionLine.Substring(4, 1) == "a")
                            registerA++;
                        else
                            registerB++;
                        pos++;
                        break;
                    case "jmp":
                        var jmpMatch = Regex.Match(instructionLine, @"^jmp (-?\d+)$");
                        pos += int.Parse(jmpMatch.Groups[1].Value);
                        break;
                    case "jie":
                        var jieMatch = Regex.Match(instructionLine, @"^jie (a|b), (-?\d+)$");
                        if (jieMatch.Groups[1].Value == "a" && registerA % 2 == 0)
                            pos += int.Parse(jieMatch.Groups[2].Value);
                        else if (jieMatch.Groups[1].Value == "b" && registerB % 2 == 0)
                            pos += int.Parse(jieMatch.Groups[2].Value);
                        else pos++;
                        break;
                    case "jio":
                        var jioMatch = Regex.Match(instructionLine, @"^jio (a|b), (-?\d+)$");
                        if (jioMatch.Groups[1].Value == "a" && registerA == 1)
                            pos += int.Parse(jioMatch.Groups[2].Value);
                        else if (jioMatch.Groups[1].Value == "b" && registerB == 1)
                            pos += int.Parse(jioMatch.Groups[2].Value);
                        else
                            pos++;
                        break;
                }
            }

            Console.WriteLine("After running al the instructions the value of register B = {0}", registerB);            
        }

        static void Day23a()
        {
            uint registerA = 0;
            uint registerB = 0;
            var instructions = File.ReadAllLines("input/day23.input");

            int pos = 0;
            int length = instructions.Length;

            while (pos < length)
            {
                var instructionLine = instructions[pos].Replace("+", "");
                var instruction = instructions[pos].Substring(0, 3);
                switch (instruction)
                {
                    case "hlf":
                        if (instructionLine.Substring(4, 1) == "a")
                            registerA /= 2;
                        else
                            registerB /= 2;
                        pos++;
                        break;

                    case "tpl":
                        if (instructionLine.Substring(4, 1) == "a")
                            registerA *= 3;
                        else
                            registerB *= 3;
                        pos++;
                        break;
                    case "inc":
                        if (instructionLine.Substring(4, 1) == "a")
                            registerA++;
                        else
                            registerB++;
                        pos++;
                        break;
                    case "jmp":
                        var jmpMatch = Regex.Match(instructionLine, @"^jmp (-?\d+)$");
                        pos += int.Parse(jmpMatch.Groups[1].Value);
                        break;
                    case "jie":
                        var jieMatch = Regex.Match(instructionLine, @"^jie (a|b), (-?\d+)$");
                        if (jieMatch.Groups[1].Value == "a" && registerA % 2 == 0)
                            pos += int.Parse(jieMatch.Groups[2].Value);
                        else if (jieMatch.Groups[1].Value == "b" && registerB % 2 == 0)
                            pos += int.Parse(jieMatch.Groups[2].Value);
                        else pos++;
                        break;
                    case "jio":
                        var jioMatch = Regex.Match(instructionLine, @"^jio (a|b), (-?\d+)$");
                        if (jioMatch.Groups[1].Value == "a" && registerA == 1)
                            pos += int.Parse(jioMatch.Groups[2].Value);
                        else if (jioMatch.Groups[1].Value == "b" && registerB == 1)
                            pos += int.Parse(jioMatch.Groups[2].Value);
                        else
                            pos++;
                        break;                        
                }
            }

            Console.WriteLine("After running al the instructions the value of register B = {0}", registerB);
        }
    }
}
