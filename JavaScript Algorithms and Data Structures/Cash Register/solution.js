function checkCashRegister(price, cash, cid) {
  let cost = [
  ["PENNY", 0.01],
  ["NICKEL",0.05],
  ["DIME", 0.1],
  ["QUARTER", 0.25],
  ["ONE", 1],
  ["FIVE", 5],
  ["TEN", 10],
  ["TWENTY", 20],
  ["ONE HUNDRED", 100]
]
 let money = [
  ["PENNY", 0],
  ["NICKEL",0],
  ["DIME", 0],
  ["QUARTER", 0],
  ["ONE", 0],
  ["FIVE", 0],
  ["TEN", 0],
  ["TWENTY", 0],
  ["ONE HUNDRED",0]
]
  var change = cash - price;
  for (let i = cid.length-1;i>=0;i--) {
    while (cost[i][1] <= change && cid[i][1] >= cost[i][1]) {
      cid[i][1] -=cost[i][1];
      change -= cost[i][1];
      money[i][1] +=cost[i][1];
      change = change.toFixed(2);
      cid[i][1] = cid[i][1].toFixed(2)
    }
  }
  if (change > 0){
    return {status:"INSUFFICIENT_FUNDS", change: []};
  } else if (change == 0) {
    let counter = 0.0;
    for (let i = cid.length-1;i>=0;i--) {
     counter += cid[i][1];
    }
     for (let i = money.length-1;i>=0;i--) {
        money[i][1] = parseFloat(money[i][1].toFixed(2))
    }
    if(counter == 0){
      console.log({status:"CLOSED", change: money})
      return {status:"CLOSED", change: money};
    } else {
      let sortedChange = [];
      for(let i = money.length-1;i>=0;i--) {
        if (money[i][1] != 0) {
          sortedChange.push(money[i])
        }
      }
      return {status:"OPEN", change: sortedChange};
    }
    
  }
}

checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]])