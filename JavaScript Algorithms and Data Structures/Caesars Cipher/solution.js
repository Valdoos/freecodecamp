function rot13(str) {
  let map = new Map();
  let ans = '';
  let alphabet = "ABCDEFGHIJKLM";
  let rot13Alphabet = "NOPQRSTUVWXYZ";
  for (let i = 0; i < alphabet.length ; i++) {
    map[alphabet[i]] = rot13Alphabet[i];
    map[rot13Alphabet[i]] = alphabet[i];
  }
  for (let i = 0; i < str.length ; i++) {
    if(map[str[i]]!=null) {
      ans += map[str[i]];
    } else {
      ans +=str[i];
    }
  }
  return ans;
}

rot13("SERR PBQR PNZC");