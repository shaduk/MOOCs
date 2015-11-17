/* Bonfire: Find the Longest Word in a String
Return the length of the longest word in the provided sentence.

Your response should be a number. */

function findLongestWord(str) {
  str = str.split(' ');
  var maxlen = 0;
  for(i=0; i < str.length; i++)
    {
      if(str[i].length > maxlen)
        {
          maxlen = str[i].length;
        }
    }
  return maxlen;
}

findLongestWord("The quick brown fox jumped over the lazy dog");