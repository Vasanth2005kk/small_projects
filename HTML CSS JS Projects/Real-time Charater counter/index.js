const textAreaContent = document.getElementById('text');
const totalcounter = document.getElementById('increes');
const totaldecrees = document.getElementById('decrees');

// declaer the max value
deClearmaxValue = 100

if (typeof(deClearmaxValue) == "number"){
    textAreaContent.setAttribute('maxlength',deClearmaxValue)
}  
let maxCounterLeb = parseInt(textAreaContent.getAttribute('maxlength'));

totaldecrees.innerHTML = maxCounterLeb;
var total = 0
textAreaContent.addEventListener("keyup", () => {
    charaterscounts();
    total ++
    if(total == maxCounterLeb){
        alert("Your Charater Count Is Full!")
    }
});

function charaterscounts() {
    let textValues = textAreaContent.value.length;
    totalcounter.innerHTML = textValues;
    totaldecrees.innerHTML = maxCounterLeb - textValues
}
