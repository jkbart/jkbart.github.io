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

class SVGEditor {
    private img: Img;
    private svgCanvas: SVGElement;
    private x1Input: HTMLInputElement;
    private y1Input: HTMLInputElement;
    private x2Input: HTMLInputElement;
    private y2Input: HTMLInputElement;
    private colorInput: HTMLInputElement;
    // private deleteRectangleHandler: (e: MouseEvent) => void;
    // private mouseUpFlag: boolean = false;

    constructor() {
        this.svgCanvas = document.getElementById('svgCanvas') as unknown as SVGElement;
        this.colorInput = document.getElementById('color') as HTMLInputElement;
        this.x1Input = document.getElementById('x1') as HTMLInputElement;
        this.y1Input = document.getElementById('y1') as HTMLInputElement;
        this.x2Input = document.getElementById('x2') as HTMLInputElement;
        this.y2Input = document.getElementById('y2') as HTMLInputElement;
        this.img = {
            width: 500,
            height: 500,
            rects: []
        };

        this.svgCanvas.setAttribute('width', this.img.width.toString());
        this.svgCanvas.setAttribute('height', this.img.width.toString());

        document.getElementById('addRectBtn')?.addEventListener('click', () => this.addRectangle());
        document.getElementById('remRectBtn')?.addEventListener('click', () => this.removeRectangle());
        this.svgCanvas.addEventListener('mousedown', (e) => this.startDrawing(e));
    }

    private addRectangle() {
        const x1 = parseInt(this.x1Input.value, 10);
        const y1 = parseInt(this.y1Input.value, 10);
        const x2 = parseInt(this.x2Input.value, 10);
        const y2 = parseInt(this.y2Input.value, 10);
        const color = this.colorInput.value;

        const rect = {
            x: Math.min(x1, x2),
            y: Math.min(y1, y2),
            width: Math.abs(x2 - x1),
            height: Math.abs(y2 - y1),
            color: color
        };

        this.img.rects.push(rect);
        this.render();
    }

    private removeRectangle() {
        console.log("USUN")
        const x1 = parseInt(this.x1Input.value, 10);
        const y1 = parseInt(this.y1Input.value, 10);
        const x2 = parseInt(this.x2Input.value, 10);
        const y2 = parseInt(this.y2Input.value, 10);
        const color = this.colorInput.value;
        console.log(x1,x2,y1,y2, color)

        for (let i = this.img.rects.length - 1; i >= 0; i--) {
            let rx1 = this.img.rects[i].x;
            let rx2 = x1 + this.img.rects[i].width;
            let ry1 = this.img.rects[i].y;
            let ry2 = y1 + this.img.rects[i].height;
            let rcolor = this.img.rects[i].color;
            console.log("comp ",rx1,rx2,ry1,ry2, rcolor)

            if (x1 == rx1 && x2 == rx2 && 
                y1 == ry1 && y2 == ry2 &&
                color == rcolor) {
                this.img.rects.splice(i, 1);
                break;
            }
        }
        this.render();
    }

    private startDrawing(event: MouseEvent) {
        console.log("START DRAWINMG")
        let mouseMoved: boolean = false;

        const startX = event.offsetX;
        const startY = event.offsetY;

        this.x1Input.value = startX.toString();
        this.y1Input.value = startY.toString();
        this.x2Input.value = startX.toString();
        this.y2Input.value = startY.toString();

        let width =  0;
        let height = 0;

        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', startX.toString());
        rect.setAttribute('y', startY.toString());
        rect.setAttribute('width', '0');
        rect.setAttribute('height', '0');
        rect.setAttribute('fill', this.colorInput.value);
        
        this.svgCanvas.appendChild(rect);

        const onMouseMove = (moveEvent: MouseEvent) => {
            mouseMoved = true;

            const currentX = moveEvent.offsetX;
            const currentY = moveEvent.offsetY;


            this.x1Input.value = Math.min(startX, currentX).toString();
            this.y1Input.value = Math.min(startY, currentY).toString();

            this.x2Input.value = Math.max(startX, currentX).toString();
            this.y2Input.value = Math.max(startY, currentY).toString();

            width = Math.abs(currentX - startX);
            height = Math.abs(currentY - startY);

            rect.setAttribute('width', width.toString());
            rect.setAttribute('height', height.toString());
            rect.setAttribute('x', Math.min(currentX, startX).toString());
            rect.setAttribute('y', Math.min(currentY, startY).toString());
        };

        const onMouseUp = () => {
            this.svgCanvas.removeEventListener('mousemove', onMouseMove);
            this.svgCanvas.removeEventListener('mouseup', onMouseUp);
            console.log(rect.getAttribute('x')!, rect.getAttribute('y')!, rect.getAttribute('width')!)

            mouseMoved = (width > 2 && height > 2); 

            if (mouseMoved == true) {
                this.img.rects.push({
                    x: parseInt(rect.getAttribute('x')!, 10),
                    y: parseInt(rect.getAttribute('y')!, 10),
                    width: parseInt(rect.getAttribute('width')!, 10),
                    height: parseInt(rect.getAttribute('height')!, 10),
                    color: rect.getAttribute('fill')!
                });
                this.colorInput.value = '#'+(0x1000000+Math.random()*0xffffff).toString(16).substr(1,6);
            } else {
                for (let i = this.img.rects.length - 1; i >= 0; i--) {
                    let x1 = this.img.rects[i].x;
                    let x2 = x1 + this.img.rects[i].width;
                    let y1 = this.img.rects[i].y;
                    let y2 = y1 + this.img.rects[i].height;

                    let x = startX;
                    let y = startY;
                    
                    console.log(x1, x2, y1, y2)
                    console.log(x, y)
                    if (x1 <= x && x <= x2 && 
                        y1 <= y && y <= y2) {
                        this.x1Input.value = x1.toString();
                        this.y1Input.value = y1.toString();

                        this.x2Input.value = x2.toString();
                        this.y2Input.value = y2.toString();
                        this.colorInput.value = this.img.rects[i].color;

                        break;
                    }
                }
            }
            this.render();
        };

        this.svgCanvas.addEventListener('mousemove', onMouseMove);
        this.svgCanvas.addEventListener('mouseup', onMouseUp);
    }

    private render() {
        while (this.svgCanvas.firstChild) {
            this.svgCanvas.removeChild(this.svgCanvas.firstChild);
        }

        this.img.rects.forEach((rect, index) => {
            const svgRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            svgRect.setAttribute('x', rect.x.toString());
            svgRect.setAttribute('y', rect.y.toString());
            svgRect.setAttribute('width', rect.width.toString());
            svgRect.setAttribute('height', rect.height.toString());
            svgRect.setAttribute('fill', rect.color);
            svgRect.setAttribute('data-id', index.toString());
            this.svgCanvas.appendChild(svgRect);
        });
    }
}

new SVGEditor();
