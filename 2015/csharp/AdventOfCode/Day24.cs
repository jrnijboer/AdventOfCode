using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    public static class Combinator
    {
        public static IEnumerable<IEnumerable<T>> Combinations<T>(this IEnumerable<T> elements, int k)
        {
            return k == 0 ? new[] { new T[0] } :
              elements.SelectMany((e, i) =>
                elements.Skip(i + 1).Combinations(k - 1).Select(c => (new[] { e }).Concat(c)));
        }
    }
    partial class Program
    {
        static List<int> weights;
        static List<List<int>> weightCombinations;
        static int averageWeight;
        static int minCount = 999999;

        static void Day24a()
        {
            readWeights();
            averageWeight = weights.Sum() / 3;
            Console.WriteLine("average weight = {0}", averageWeight);
            //var result = Combinator.Combinations(weights, 24).ToList();
            combinations = new List<List<int>>();
            while (weights.Count > 0 && weights[0] <= averageWeight)
            {
                GetCombinations(new List<int> { weights[0] });
                weights.RemoveAt(0);
            }
            combinations.ForEach(c => { if (c.Count < minCount) minCount = c.Count; });
            //todo build dictionary
            combinations = combinations.Where(c => c.Count == minCount).ToList();
            
            //todo: return dictonary ordered by value desc
            var products = QE(combinations);
            long minQE = products.Values.Min();
            int key = products.Keys.ToList().First(k => products[k] == minQE);
            Console.WriteLine("lowest QE = {0}", products[key]);
        }

        static void Day24b()
        {
            readWeights();
            averageWeight = weights.Sum() / 4;
            Console.WriteLine("average weight = {0}", averageWeight);
            //var result = Combinator.Combinations(weights, 24).ToList();
            combinations = new List<List<int>>();
            while (weights.Count > 0 && weights[0] <= averageWeight)
            {
                GetCombinations(new List<int> { weights[0] });
                weights.RemoveAt(0);
            }
            combinations.ForEach(c => { if (c.Count < minCount) minCount = c.Count; });
            //todo build dictionary
            combinations = combinations.Where(c => c.Count == minCount).ToList();

            //todo: return dictonary ordered by value desc
            var products = QE(combinations);
            long minQE = products.Values.Min();
            int key = products.Keys.ToList().First(k => products[k] == minQE);
            Console.WriteLine("lowest QE = {0}", products[key]);
        }

        static Dictionary<int, long> QE (List<List<int>> combinations)
        {
            int key = 0;
            Dictionary<int, long> qe = new Dictionary<int, long>();
            foreach (var combination in combinations)
            {
                long product = 1;
                combination.ForEach(i => product *= i);
                qe[key] = product;
                key++;
            }
            return qe;
        }

        private static void GetCombinations(List<int> currentAttempt)
        {
            if (currentAttempt.Sum() == averageWeight)
            {
                //Console.WriteLine("found combination: ");
                //currentAttempt.ForEach(p => Console.Write("{0}, ", p));

                //Console.WriteLine();
                combinations.Add(currentAttempt);
                return;
            }

            var packagesLeft = weights.Where(w => w > currentAttempt.Max()).ToList();
            foreach (var package in packagesLeft)
            {
                List<int> nextAttempt = currentAttempt.Select(s => s).ToList();
                nextAttempt.Add(package);

                if (nextAttempt.Sum() > averageWeight)
                {
                    break;
                }
                GetCombinations(nextAttempt);
            }
        }

        private static void readWeights()
        {
            weights = new List<int>();
            foreach (var line in File.ReadAllLines(@"input\day24.input").Where(l => !l.StartsWith("#")))
            {
                weights.Add(int.Parse(line));
            }
        }
    }
}
