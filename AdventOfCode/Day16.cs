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
        static void Day16b()
        {
            var aunts = new List<Dictionary<string, int>>();
            var auntProps = File.ReadAllLines("input/day16.input");

            foreach (var auntProp in auntProps)
            {
                var aunt = new Dictionary<string, int>();
                var pattern = @"^Sue (\d+):(.*)";
                var match = Regex.Match(auntProp, pattern);

                var properties = match.Groups[2].Value.Split(',');
                foreach (var property in properties)
                {
                    var kvp = property.Split(':');
                    aunt[kvp[0].Trim()] = int.Parse(kvp[1]);
                    aunt["id"] = int.Parse(match.Groups[1].Value);
                }
                aunts.Add(aunt);
            }

            var auntsWith3Children = aunts.Where(d => !d.ContainsKey("children") || (d.ContainsKey("children") && d["children"] == 3)).ToList();
            var auntsWith7Cats = auntsWith3Children.Where(d => !d.ContainsKey("cats") || (d.ContainsKey("cats") && d["cats"] > 7)).ToList();
            var auntsWith2Samoyeds = auntsWith7Cats.Where(d => !d.ContainsKey("samoyeds") || (d.ContainsKey("samoyeds") && d["samoyeds"] == 2)).ToList();
            var auntSue = auntsWith2Samoyeds.Where(d => !d.ContainsKey("pomeranians") || (d.ContainsKey("pomeranians") && d["pomeranians"] < 3))
                .Where(d => (d.ContainsKey("akitas") && d["akitas"] == 0) || !d.ContainsKey("akitas"))
                .Where(d => (d.ContainsKey("vizslas") && d["vizslas"] == 0) || !d.ContainsKey("vizslas"))
                .Where(d => (d.ContainsKey("goldfish") && d["goldfish"] < 5) || !d.ContainsKey("goldfish"))
                .Where(d => (d.ContainsKey("trees") && d["trees"] > 3) || !d.ContainsKey("trees"))
                .Where(d => (d.ContainsKey("cars") && d["cars"] == 2) || !d.ContainsKey("cars"))
                .Where(d => (d.ContainsKey("perfumes") && d["perfumes"] == 1) || !d.ContainsKey("perfumes")).ToList();

            Console.WriteLine("The remaining aunt has number {0}", auntSue[0]["id"]);

        }
        static void Day16a()
        {
            var aunts = new List<Dictionary<string, int>>();
            var auntProps = File.ReadAllLines("input/day16.input");

            foreach (var auntProp in auntProps)
            {
                var aunt = new Dictionary<string, int>();
                var pattern = @"^Sue (\d+):(.*)";
                var match = Regex.Match(auntProp, pattern);

                var properties = match.Groups[2].Value.Split(',');
                foreach (var property in properties)
                {
                    var kvp = property.Split(':');
                    aunt[kvp[0].Trim()] = int.Parse(kvp[1]);
                    aunt["id"] = int.Parse(match.Groups[1].Value);
                }
                aunts.Add(aunt);
            }

            var auntsWith3Children = aunts.Where(d => !d.ContainsKey("children") || (d.ContainsKey("children") && d["children"] == 3)).ToList();
            var auntsWith7Cats = auntsWith3Children.Where(d => !d.ContainsKey("cats") || (d.ContainsKey("cats") && d["cats"] == 7)).ToList();
            var auntsWith2Samoyeds = auntsWith7Cats.Where(d => !d.ContainsKey("samoyeds") || (d.ContainsKey("samoyeds") && d["samoyeds"] == 2)).ToList();
            var auntSue = auntsWith2Samoyeds.Where(d => !d.ContainsKey("pomeranians") || (d.ContainsKey("pomeranians") && d["pomeranians"] == 3))
                .Where(d => (d.ContainsKey("akitas") && d["akitas"] == 0) || !d.ContainsKey("akitas"))
                .Where(d => (d.ContainsKey("vizslas") && d["vizslas"] == 0) || !d.ContainsKey("vizslas"))
                .Where(d => (d.ContainsKey("goldfish") && d["goldfish"] == 5) || !d.ContainsKey("goldfish"))
                .Where(d => (d.ContainsKey("trees") && d["trees"] == 3) || !d.ContainsKey("trees"))
                .Where(d => (d.ContainsKey("cars") && d["cars"] == 2) || !d.ContainsKey("cars"))
                .Where(d => (d.ContainsKey("perfumes") && d["perfumes"] == 1) || !d.ContainsKey("perfumes")).ToList();

            Console.WriteLine("The remaining aunt has number {0}", auntSue[0]["id"]);
        }
    }
}
