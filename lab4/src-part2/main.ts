interface Rect {
    x: number;
    y: number;
    width: number;
    height: number;
    color: string;
}

interface Img {
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

async function fetchImage(imageId: number): Promise<Img> {
    try {
        const response = await fetch(`http://localhost:8000/randomimg`);
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        
        const data = await response.json();
        if (new Blob([JSON.stringify(data)]).size > 1000 * 500) {
            throw new Error("JSON too big!!!");
        }

        let img: Img = data;
        return img;
    } catch (error) {
        throw error;
    }
}

function createLoadingElement(): HTMLElement {
    // Create the div element
    const div = document.createElement('div');
    div.className = 'inline-block h-8 w-8 animate-spin rounded-full border-4 border-solid border-current border-e-transparent align-[-0.125em] text-neutral-50 motion-reduce:animate-[spin_1.5s_linear_infinite]';
    div.setAttribute('role', 'status');

    // Create the span element
    const span = document.createElement('span');
    span.className = '!absolute !-m-px !h-px !w-px !overflow-hidden !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]';
    span.textContent = '';

    // Append span to div
    div.appendChild(span);

    return div;
}


function createErrorElement(e: unknown, retryCallback: () => void): HTMLElement {
    const errorElement = document.createElement("div");
    errorElement.className = "text-red-500";

    const textElement = document.createElement("p");
    textElement.innerText = 'Błąd podczas ładowania obrazka: ' + e;

    const buttonElement = document.createElement("button");
    buttonElement.className = "bg-red-500 text-white px-2 py-1 rounded";
    buttonElement.innerText = "Spróbuj ponownie"
    buttonElement.addEventListener("click", retryCallback);

    errorElement.appendChild(textElement);
    errorElement.appendChild(buttonElement);
    // errorElement.innerHTML = `<p>Błąd podczas ładowania obrazka: ${e} </p><button class="bg-red-500 text-white px-2 py-1 rounded">Spróbuj ponownie</button>`;
    return errorElement;
}

async function loadImage(imageId: number): Promise<void> {
    const imageContainer = document.getElementById(`image-${imageId}`);
    if (!imageContainer) return;

    imageContainer.innerHTML = "";

    const loadingElement = createLoadingElement();
    imageContainer.appendChild(loadingElement);

    try {
        const img = await fetchImage(imageId);
        imageContainer.removeChild(loadingElement);

        const svg = render(img);

        imageContainer.appendChild(svg);

        // svg.offsetHeight;
        // imageContainer.offsetHeight;
        // svg.classList.toggle('force-repaint');
        // svg.classList.toggle('force-repaint');

    } catch (error) {
        imageContainer.innerHTML = '';
        const errorElement = createErrorElement(error, () => loadImage(imageId));
        imageContainer.appendChild(errorElement);
    }
}

function init() {
    const imageContainer = document.getElementById('image-container');
    if (!imageContainer) return;

    for (let i = 0; i < 10; i++) {
        const imageSlot = document.createElement("div");
        imageSlot.id = `image-${i}`;
        imageSlot.className = "bg-gray-200 flex items-center justify-center m-5";
        imageContainer.appendChild(imageSlot);
        loadImage(i);
    }
}

document.addEventListener("DOMContentLoaded", init);
