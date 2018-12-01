using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {

        static void Day4b()
        {
            int i = 0;
            string input = "iwrupvqb";
            string hash = "";

            using (MD5 md5Hash = MD5.Create())
            {
                while (!hash.StartsWith("000000"))
                {
                    hash = GetMd5Hash(md5Hash, input + i.ToString());
                    i++;
                }
            }

            Console.WriteLine("found a hash with i = {0}", --i);
        }

        static void Day4a()
        {
            int i = 0;
            string input = "iwrupvqb";
            string hash = "";

            using (MD5 md5Hash = MD5.Create())
            {
                while (!hash.StartsWith("00000"))
                {
                    hash = GetMd5Hash(md5Hash, input + i.ToString());
                    i++;
                }
            }

            Console.WriteLine("found a hash with i = {0}", --i);
        }

        // Helper functions down here


        //from MSDN
        static string GetMd5Hash(MD5 md5Hash, string input)
        {

            // Convert the input string to a byte array and compute the hash.
            byte[] data = md5Hash.ComputeHash(Encoding.UTF8.GetBytes(input));

            // Create a new Stringbuilder to collect the bytes
            // and create a string.
            StringBuilder sBuilder = new StringBuilder();

            // Loop through each byte of the hashed data 
            // and format each one as a hexadecimal string.
            for (int i = 0; i < data.Length; i++)
            {
                sBuilder.Append(data[i].ToString("x2"));
            }

            // Return the hexadecimal string.
            return sBuilder.ToString();
        }
    }
}
