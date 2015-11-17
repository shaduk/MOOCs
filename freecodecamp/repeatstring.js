/* Bonfire: Repeat a string repeat a string
Repeat a given string (first argument) n times (second argument). Return an empty string if n is a negative number.
*/

function repeat(str, num) {
  // repeat after me
  ans = []
  for(i=0; i < num; i++)
    {
      ans.push(str);
    }
  ans = ans.join('');
  return ans;
}

repeat("abc", 3);