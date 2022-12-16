// let quantitie=document.getElementById("selection").textContent

function calc(price)
{
 
  var e = document.getElementById("selection");
  var value = e.options[e.selectedIndex].value;
  amount=price*value
  document.getElementById('6').innerHTML=value+" kg:"+amount
  console.log(amount)

}