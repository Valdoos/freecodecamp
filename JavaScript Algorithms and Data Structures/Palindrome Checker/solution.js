function palindrome(str) {
  str = str.toLowerCase();
  let alphabetRegex = /[A-Za-z0-9]/g;
  let newStr = str.match(alphabetRegex);
  let j = newStr.length-1;
  let i = 0;
  while(i < j) {
    if (newStr[i] != newStr[j]) {
      return false;
    }
    i++;
    j--;
  }
  return true;
}



palindrome("eye");