const bodyElement = document.querySelector("body")
bodyElement.addEventListener("mousemove", (event) => {
    const XElSetof = event.offsetX;
    const YElSetof = event.offsetY;

    const createSpan = document.createElement("span")
    createSpan.style.top = YElSetof + "px";
    createSpan.style.left = XElSetof + "px";

    const WHrandom = Math.floor(Math.random() * 101);

    createSpan.style.width = WHrandom + 'px';
    createSpan.style.height = WHrandom + 'px';

    // let a = ['blur(5px)', 'brightness(200%)', 'contrast(200%)', 'drop-shadow(8px 8px 10px gray)', 'grayscale(100%)','hue-rotate(90deg)','hue-rotate(230deg)','hue-rotate(50deg)','hue-rotate(190deg)','hue-rotate(720deg)','invert(100%)','opacity(30%)','saturate(8)','sepia(100%)','contrast(200%) brightness(150%)'];
    // let i = Math.floor(Math.random() * a.length);
    // createSpan.style.filter = a[i];

    bodyElement.appendChild(createSpan)

    setTimeout(() => {
        createSpan.remove();
    }, 3000)

})