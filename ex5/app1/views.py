from django.shortcuts import render
from app1.forms import CylinderForm
def HomePage(request):
    result = None
    if request.method == 'POST':
        form = CylinderForm(request.POST)
        if form.is_valid(): 

            radius = form.cleaned_data['radius']
            height = form.cleaned_data['height']
           
            surface_area = 2 * 3.14 * radius * (radius + height)
            
            result = {
                'radius': radius,
                'height': height,
                'surface_area': surface_area,
            }
    else:
        form = CylinderForm()  

   
    return render(request, 'index.html', {'form': form, 'result': result})
