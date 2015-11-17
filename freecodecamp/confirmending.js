/* Bonfire: Confirm the Ending
Check if a string (first argument) ends with the given target string (second argument). */

function end(str, target) {
  // "Never give up and good luck will find you."
  // -- Falcor
  substr = str.substr(-target.length, str.length);
  return substr==target;
}

end("Bastian", "n");