interface Rect {
    x: number;
    y: number;
    width: number;
    height: number;
    color: string;
}

interface Img {
    data: string;
    width: number;
    height: number;
    rects: Rect[];
}

function render(img: Img): HTMLElement {
    const svg = document.createElement('svg');
    svg.setAttribute('height', img.height.toString());
    svg.setAttribute('width', img.width.toString());
    svg.className = "border border-gray-600 mx-auto";

    img.rects.forEach((rect, index) => {
        const svgRect = document.createElement('rect');
        svgRect.setAttribute('x', rect.x.toString());
        svgRect.setAttribute('y', rect.y.toString());
        svgRect.setAttribute('width', rect.width.toString());
        svgRect.setAttribute('height', rect.height.toString());
        svgRect.setAttribute('fill', rect.color);
        svgRect.setAttribute('data-id', index.toString());
        svg.appendChild(svgRect);
    });

    return svg;
}

function renderLogs(img: Img): HTMLElement {
    const log = document.createElement('p');
    log.innerText = "New img -> date:" + img.data + " rect_cnt:" + img.rects.length.toString();

    return log;
}

function init() {

    console.log("111!!!");
    const imageContainer = document.getElementById('image-container');
    const logsContainer = document.getElementById('logs');
    if (!imageContainer) return;
    if (!logsContainer) return;

    console.log("222!!!");


    var ws = new WebSocket("ws://localhost:8000/ws");

    ws.onopen = function() {
        console.log("WebSocket connection established.");
        ws.send("hello");
    };

    ws.onclose = function() {
        console.log("WebSocket connection closed!!!");
        // window.location.reload();
    };

    ws.onmessage = function(event) {
        console.log("GOT NEW MESSEGE!!!");
        let img: Img =  JSON.parse(event.data);
        logsContainer.appendChild(renderLogs(img));
        imageContainer.appendChild(render(img));
        console.log("Message received:", event.data);
    };

    ws.onerror = function(event) {
        document.body.innerHTML = "websocket error!!" + event.toString();
        console.error("WebSocket error:", event);
    };

    console.log("seding");
}

document.addEventListener("DOMContentLoaded", init);
