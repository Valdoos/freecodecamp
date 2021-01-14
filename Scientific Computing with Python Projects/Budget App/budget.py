from functools import reduce

class Category:

    def __init__(self, name=""):
        self.__name = name
        self.ledger = []
        self.__balance = 0.0

    def deposit(self,amount,description=""):
        self.__balance+=amount
        self.ledger.append({"amount":amount,"description":description})

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            self.__balance-=amount
            return True
        return False

    def get_balance(self):
        self.__balance = round(self.__balance,2)
        return self.__balance

    def get_name(self):
        return self.__name

    def transfer(self,amount,another):
        if self.withdraw(amount,"Transfer to " + another.get_name()) :
            another.deposit(amount,"Transfer from " + self.get_name())
            return True
        return False

    def check_funds(self,amount):
        return amount <= self.get_balance()

    def __str__(self):
        first = int((30-len(self.get_name()))/2)
        last = int(30-len(self.get_name())-first)
        ans = "*"*first + self.get_name() + "*"*last+"\n"
        for _, pair in enumerate(self.ledger) :
            amount = "{:5.2f}".format(pair["amount"])[:7]
            description = pair["description"][:23]
            ans += description
            ans += " "*(23-len(description))
            ans += " "*(7-len(amount))
            ans += amount + "\n"
        ans+="Total: "+ str(round(self.__balance,2))
        return ans



def create_spend_chart(categories):
    total = []
    all = 0.0
    n=0
    ans ="Percentage spent by category\n"
    for _, x in enumerate(categories):
        amount = [p["amount"]  for _, p in enumerate(x.ledger) if p["amount"] < 0]
        sum = 0.0
        for _, k in enumerate(amount) :
            sum+=k
        sum*=-1
        total.append({"name":x.get_name(),"amount":sum})
        all+=total[-1]["amount"]
        n+=1
    for i, x in enumerate(total):
        total[i]["amount"] = round(x["amount"]*100/all)
    x = 100

    while x >= 0 :
        s = " "*(3-len(str(x)))+str(x)+"|"+" "
        for _, t in enumerate(total):
            if t["amount"]>=x:
                s+="o"+"  "
            else :
                s+=" "+"  "
        ans+=s+"\n"
        x-=10
    ans+="    "+"-"*(1+n*3)
    b = True
    while b :
        ans+="\n"
        b = False
        s=" "*5
        for j, t in enumerate(total):
            if t["name"]!="" :
                b = True
                s+=t["name"][0]
            else :
                s+=" "
            total[j]["name"] = t["name"][1:]
            s+=" "*2
        if b:
            ans+=s
    return ans[:-1]
