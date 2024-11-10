const clickbtn = document.querySelector('button');
const clickActive = document.querySelector('span');
const EmojiName = document.getElementById("Emoji-name");

let data = []; 

const api_token = '6606c921320b4b8be815fa8c54c870ae0ca4af17';
const url = `https://emoji-api.com/emojis?access_key=${api_token}`;

fetch(url)
    .then(response => response.json())
    .then(json => {
        for (let i = 0; i < json.length; i++) {
            data.push({
                character: json[i]['character'],
                Emojiname: json[i]['unicodeName']
            });
        }
    })
    .catch(error => console.error("Error fetching data:", error));

clickbtn.addEventListener("click", () => {
    if (data.length >= 0) {
        const randomIndex = Math.floor(Math.random() * data.length);
        
        clickbtn.innerHTML = data[randomIndex]['character'];
        clickbtn.style.fontSize = '100px';
        EmojiName.innerHTML = data[randomIndex]['Emojiname'];
    } else {
        console.log("Data is not loaded yet.");
    }
});
