/* Bonfire: Chunky Monkey
Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a multidimensional array.*/

function chunk(arr, size) {
  // Break it up.
  ans = [];
  for(i = 0; i < arr.length; i = i + size)
    {
        ans.push(arr.slice(i,i+size));
    }
  return ans;
  
}

chunk(["a", "b", "c", "d"], 2);
