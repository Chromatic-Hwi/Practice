using System;

public class Solution
{
    public int solution(int n)
    {
        int answer = 2;
        long cal = (long)Math.Sqrt(n);
        if (n == cal * cal) { answer = 1; }
        return answer;
    }
}