using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    public partial class Program
    {
        static void Day25a()
        {
            long code = 20151125;

            int codeRow = 2978;
            int codeColumn = 3083;
            //int codeRow = 5;
            //int codeColumn = 5;

            int row = 1;
            int column = 1;

            while (true)
            {
                code = (code * 252533) % 33554393;
                row--;
                column++;
                if (row == 0)
                {
                    row = column;
                    column = 1;
                }
                //Console.WriteLine("value on {0}, {1} = {2}", row, column, code);
                if (row == codeRow &&  column == codeColumn)
                    break;


            }
            Console.WriteLine("The code is {0}", code);            
        }
    }
}
