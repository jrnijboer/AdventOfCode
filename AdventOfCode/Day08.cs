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
        static void Day8a()
        {
            var input = File.ReadAllLines("input/day8.input").ToList();
            int escapeChars = 0;

            input.ForEach(line =>
            {
                escapeChars += 2;
                for (int pos = 0; pos < line.Length - 1; pos++)
                {
                    if (line[pos] == '\\')
                    {
                        if (line[pos+1] =='x')
                        {
                            escapeChars += 3;
                            pos += 2;
                        }
                        else
                        {
                            escapeChars++; ;
                            pos++;
                        }
                    }
                }
            });           

            Console.WriteLine("There were {0} escaped characters.", escapeChars);            
        }

        static void Day8b()
        {
            int unescapedLength = 0;
            int newLength = 0;
            var input = File.ReadAllLines("input/day8.input").ToList();
            input.ForEach(line => 
            {
                unescapedLength += line.Length;
                var newline = line.Replace("\\", "\\\\");
                newline = "\"" + newline.Replace("\"", "\\\"") + "\""; 
                newLength += newline.Length;
            });
            Console.WriteLine("difference in length: {0}", newLength - unescapedLength);

        }
    }
}