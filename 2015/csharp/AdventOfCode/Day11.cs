using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static void Day11a()
        {
            //string password = "hxbxwxba";
            string password = incrementPassword("hxbxxyzz"); 
            //string password = "ghijklmn";

            while (!validatePassword(password))
                password = incrementPassword(password);

            Console.WriteLine("Santa's new password will be {0}", password);
        }

        private static bool validatePassword(string password)
        {
            if (password.Contains("i") || password.Contains("l") || password.Contains("o"))
                return false;

            if (!hasPairs(password, 2))
                return false;

            if (!hasStraight(password))
                return false;
            return true;
        }

        private static bool hasPairs(string password, int number)
        {
            int pairs = 0;
            for (char c = 'a'; c <= 'z'; c++)
                if (password.Contains(string.Concat(c, c)))
                    pairs++;
            return pairs >= number;
        }

        private static bool hasStraight(string password)
        {
            for (char c = 'a'; c <= 'x'; c++)
                if (password.Contains(string.Concat(c, (char)(c + 1), (char)(c + 2))))
                    return true;
            return false;
        }

        private static string incrementPassword(string password)
        {            
            StringBuilder newPassword = new StringBuilder();
            bool carry = false;

            char nextChar = (char)(password[password.Length - 1] + 1);
            if (nextChar > 'z')
            {
                nextChar = (char)(nextChar - 26);
                carry = true;
            }
            newPassword.Insert(0, nextChar);

            int pos = password.Length - 2;

            while (pos >= 0)
            {
                if (carry)
                {
                    nextChar = (char)(password[pos] + 1);
                }
                else
                    nextChar = password[pos];

                if (nextChar > 'z')
                {
                    nextChar = (char)(nextChar - 26);
                    carry = true;
                }
                else
                {
                    carry = false;
                }

                newPassword.Insert(0, nextChar);
                pos--;
            }            

            return newPassword.ToString();
        }
    }
}
