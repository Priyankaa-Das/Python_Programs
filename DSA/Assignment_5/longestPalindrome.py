'''Find the longest palindrome
As we all know, a palindrome is a word that equals its reverse. 
Here are some examples of palindromes: malayalam, gag, appa, amma. 
We consider any sequence consisting of the letters of the English alphabet to be aword. 
So axxb, abbba and bbbccddx are words for our purpose. And aaabbaaa, abbba and bbb are examples of palindromes.
By a subword of a word, we mean a contiguous subsequence of the word. 
For example: the subwords of the word abbba are a, b, ab, bb, ba, abb, bbb, bba, abbb, bbba and abbba.
In this task you will given a word and you must find the longest subword of this word that is also a palindrome.
For example if the given word is abbba then the answer is abbba.
If the given word is abcbcabbacba then the answer is bcabbacb.
Solution hint: Any subword of w that is a palindrome is also a subword when w is reversed.
Input format: The first line of the input contains a single integer N indicating the length of the word. 
The following line contains a single word of length N, made up of the letters a,b,..., z.
Output format:
The first line of the output must contain a single integer indicating the length of the longest subword of the given word that is a palindrome. 
The second line must contain a subword that is a palindrome and which of maximum length. 
If there is more than one subword palindrome of maximum length, print the one that is lexicographically smallest (i.e., smallest in dictionary order).
Test Data:You may assume that 1 ≤ N ≤ 5000. You may further assume that in 30% of the inputs 1 ≤ N ≤ 300.
Example: We illustrate the input and output format using the above examples:
Sample Input 1: 5 abbba
Sample Output 1: 5 abbba'''