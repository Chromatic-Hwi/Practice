using System;

public class Solution
{
    public int solution(int n)
    {
        int answer = 0;
        var word = n.ToString();
        for (int i = 0; i < word.Length; i++)
        {
            answer += (int)char.GetNumericValue(word[i]);
        }
        return answer;
    }
}