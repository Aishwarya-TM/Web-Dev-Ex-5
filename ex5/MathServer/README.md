# Ex.05 Design a Website for Server Side Processing
## Date:

## AIM:
To design a website to find surface area of a Right Cylinder in server side.

## FORMULA:
Surface Area = 2Πrh + 2Πr<sup>2</sup>
<br>r --> Radius of Right Cylinder
<br>h --> Height of Right Cylinder

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :


### SERVER SIDE PROCESSING:
#### Views.py:
```
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
```
#### Urls.py:
```
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage)
]
```


#### HomePage.html:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Surface Area of Cylinder</title>
</head>
<body>
    <h1>Calculate Cylinder Surface Area</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Calculate">
    </form>

    {% if result %}
        <h2>Result:</h2>
        <p>Radius: {{ result.radius }}</p>
        <p>Height: {{ result.height }}</p>
        <p>Surface Area: {{ result.surface_area }}</p>
    {% endif %}
</body>
</html>
```

## RESULT:
The program for performing server side processing is completed successfully.
