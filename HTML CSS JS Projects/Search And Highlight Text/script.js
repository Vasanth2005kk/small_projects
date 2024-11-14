const p = document.getElementById('p');
const Special = /[\\[{().+*/?^$,]/g;
const originalText = p.innerHTML; 

document.getElementById('input').addEventListener('input', () => {
    search();
});

function search() {
    let input = document.getElementById('input').value;
    p.innerHTML = originalText;
    if (input !== "") {
        if (Special.test(input)) input = input.replace(Special, '\\$&');

        let regExp = new RegExp(input, 'gi');

        p.innerHTML = (p.innerHTML).replace(regExp, "<mark>$&</mark>");
    }
}
