from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect

from .models import Drawing, Rectangle, Tag

from django.template import loader
from django.core.paginator import Paginator

from django.shortcuts import render

def index(request):
    drawings = Drawing.objects.all()

    template = loader.get_template("pictures/index.html")

    return HttpResponse(template.render({'drawings': drawings}, request))

def listing(request):
    drawing_list = Drawing.objects.all()


    tag_name = request.GET.get("tag")
    sort_by_date = request.GET.get("sort_date")

    if tag_name is not None and tag_name != "":
        drawing_list = drawing_list.filter(tags=tag_name)
    else:
        tag_name = ""

    if sort_by_date is not None:
        if sort_by_date == 'ascending':
            drawing_list = drawing_list.order_by('pub_date')
        elif sort_by_date == 'descending':
            drawing_list = drawing_list.order_by('-pub_date')
    else:
        sort_by_date = ""



    paginator = Paginator(drawing_list, 10)

    template = loader.get_template("pictures/list.html")
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {
        "page_obj": page_obj, 
        "tag_value": tag_name, 
        "sort_value": sort_by_date,
        "suffix": "&sort_date=" + sort_by_date + "&tag=" + tag_name,
    })

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