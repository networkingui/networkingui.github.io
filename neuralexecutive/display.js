 var a = console.log(myNetwork.activate([0,0]));   
// -> [0.015020775950893527]

var b = console.log(myNetwork.activate([0,1]));  
// -> [0.9815816381088985]

var  c = console.log(myNetwork.activate([1,0]));  
// ->  [0.9871822457132193]

 var d = console.log(myNetwork.activate([1,1]));  
// -> [0.012950087641929467]

var computerChoice = concat(a,b,c,d);



getoutput() {
document.getElementById('content').innerHTML = computerChoice
};
