using System;
using System.Diagnostics;

namespace aoc2018
{
    class Program
    {
        static void Main(string[] args)
        {
            var sw = new Stopwatch();
            sw.Start();
            //Day1.Solve();
            //Day2.Solve();
            //Day3.Solve();
            //Day4.Solve();
            //Day5.Solve();
            //Day6.Solve();
            //Day7.Solve();
            //Day8.Solve();
            //Day9.Solve();
            //Day10.Solve();
            //Day11.Solve();
            //Day12.Solve();
            //Day13.Solve();
            Day14.Solve();
            sw.Stop();
            Console.WriteLine("day solved in {0}ms", sw.ElapsedMilliseconds);
            Console.ReadKey();
        }
    }
}
