function convertToRoman(num) {
    let ans = "";
    let strNum = String(num)
    let roman = ['I','V','X','L','C','D','M'];
    let integer = [1, 5, 10, 50, 100, 500, 1000];
    let j = 0;
    for (let i = strNum.length-1;i >= 0 ; i--) {
        let digit = parseInt(strNum[i]);
        switch(digit) {
            case 1: {
                ans = roman[j]+ans;
                break;
            }
            case 2: {
                ans = roman[j]+roman[j] + ans;
                break;
            }
            case 3: {
                ans = roman[j]+roman[j]+roman[j] + ans;
                break;
            }
             case 4: {
                 ans = roman[j]+roman[j+1]+ans;
                 break;
            }
             case 5: {
                 ans = roman[j+1]+ans;
                 break;
            }
             case 6: {
                 ans = roman[j+1]+roman[j]+ans;
                 break;
            }
             case 7: {
                 ans = roman[j+1]+roman[j]+roman[j]+ans;
                 break;
            }
             case 8: {
                 ans = roman[j+1]+roman[j]+roman[j]+roman[j]+ans;
                 break;
            }
             case 9: {
                 ans = roman[j]+roman[j+2]+ans;
                 break;
            }
            default : {

            }
        }
        j+=2
    }
    console.log(ans)
    return ans
}

convertToRoman(891);