function telephoneCheck(str) {
  let regexes = [
    /^(1\s)?[0-9]{3}-[0-9]{3}-[0-9]{4}$/g,
    /^(1\s?)?\([0-9]{3}\)(\s)?[0-9]{3}-[0-9]{4}$/g,
    /^(1\s)?[0-9]{3}\s[0-9]{3}\s[0-9]{4}$/g,
    /^(1\s)?[0-9]{10}$/g,
  ];
  for (let i = 0;i<regexes.length;i++) {
    if(regexes[i].test(str)) {
        return true
    }
  }
  return false;

}

telephoneCheck("1(555)555-5555");