def arithmetic_arranger(problems, answers = None):
    nums = []
    ans = ""
    if len(problems) > 5 :
        return  'Error: Too many problems.'
    for i in problems :
        split = i.split()
        try :
            first = int(split[0])
            second = int(split[2])
        except :
            return 'Error: Numbers must only contain digits.'
        if first < 0 or second < 0 :
            return 'Error: Numbers must only contain digits.'
        operand = split[1]
        if operand != '+' and operand != '-' :
            return 'Error: Operator must be \'+\' or \'-\'.'
        if first >= 10000 or second >= 10000 :
            return 'Error: Numbers cannot be more than four digits.'
        length = max(len(split[0]), len(split[2])) + 2
        res = 0
        if operand == '+' :
            res = first + second
        else :
            res = first - second
        nums.append([split[0],split[1],split[2],str(res),length])
    for i in nums :
        ans +=" "*(i[4]-len(i[0]))+i[0]+" "*4
    ans = ans[:len(ans)-4]
    ans += '\n'
    for i in nums :
        ans +=i[1]+" "+ " "*(i[4]-len(i[2])-2)+i[2]+" "*4
    ans = ans[:len(ans)-4]
    ans += '\n'
    for i in nums :
        ans += '-'*i[4]+" "*4
    ans = ans[:len(ans)-4]
    if answers ==  True :
        ans += '\n'
        for i in nums :
           ans +=" "*(i[4]-len(i[3]))+i[3]+" "*4
        ans = ans[:len(ans)-4]
    return ans
