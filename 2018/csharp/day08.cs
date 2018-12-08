using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Linq;

namespace aoc2018
{
    class Day8
    {
        static int sum = 0;
        public static void Solve()
        {
            Queue<int> Q = new Queue<int>();
            File.ReadAllText(Path.Combine("..", "input", "day8.input")).Split(" ").Select(int.Parse).ToList().ForEach(x => Q.Enqueue(x));
            Node root = BuildNode(Q);
            Console.WriteLine("day8, part a: {0}", sum);
            Console.WriteLine("day8, part b: {0}", GetNodeValue(root));
        }

        public static int GetNodeValue(Node node)
        {
            if (node.children.Count > 0)
            {
                int v = 0;
                foreach (var i in node.values)
                    if (i > 0 && i <= node.children.Count)
                        v += GetNodeValue(node.children[i - 1]);
                return v;
            }
            else
                return node.values.Sum();
        }

        public static Node BuildNode(Queue<int> Q)
        {
            var node = new Node { countC = Q.Dequeue(), countV = Q.Dequeue(), children = new List<Node>(), values = new List<int>() };
            for (int i = 0; i < node.countC; i++)
                node.children.Add(BuildNode(Q));
            for (int i = 0; i < node.countV; i++)
            {
                int v = Q.Dequeue();
                sum += v;
                node.values.Add(v);
            }
            return node;
        }
    }

    struct Node
    {
        public List<Node> children;
        public List<int> values;
        public int countC;
        public int countV;
    }
}
