from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect

from .models import Drawing, Rectangle

from django.template import loader

def index(request):
    drawings = Drawing.objects.all()

    template = loader.get_template("pictures/index.html")

    return HttpResponse(template.render({'drawings': drawings}, request))

def detail(request, drawing_id):
    drawing = get_object_or_404(Drawing, id=drawing_id)

    template = loader.get_template("pictures/detail.html")

    return HttpResponse(template.render({'drawing': drawing}, request))


def remove_rectangle(request, rectangle_id):
    rectangle = get_object_or_404(Rectangle, id=rectangle_id)
    author = rectangle.author
    rectangle.delete()
    
    return redirect('pictures:detail', drawing_id=author.id)  # Redirect to the detail page of the drawing

def add_rectangle(request, drawing_id):
    if request.method == 'POST':
        # Extract form data from the request
        x = request.POST.get('x')
        y = request.POST.get('y')
        width = request.POST.get('width')
        height = request.POST.get('height')
        color = request.POST.get('color')

        # Create a new rectangle object
        rectangle = Rectangle.objects.create(
            x=x,
            y=y,
            width=width,
            height=height,
            color=color,
            author_id=drawing_id  # Associate the rectangle with the drawing
        )

        # Redirect to the detail page of the drawing
        return redirect('pictures:detail', drawing_id=drawing_id)

    # Render the template with the form
    return redirect('pictures:detail', drawing_id=drawing_id)