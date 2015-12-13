using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static void Day10a()
        {
            string input = "1321131112";
                        
            for (int n = 0; n < 50; n++)
            {
                input = lookAndSay(input);
            }
            Console.WriteLine("length after 50 iterations: {0}", input.Length);
        }

        private static string lookAndSay(string input)
        {
            StringBuilder sb = new StringBuilder();
            int counter;            
            for (int pos = 0; pos < input.Length; )
            {
                counter = 1;                
                while (pos + counter < input.Length && input[pos + counter] == input[pos])
                    counter++;
                sb.Append(counter.ToString() + input[pos]);                
                pos += counter;
            }
            return sb.ToString();
        }
    }
}
