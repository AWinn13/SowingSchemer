from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

def login(request):
    return render(request, "login.html")

# ! EXAMPLES
# def one_method(request):                # no values passed via URL
#     pass                                
    
# def another_method(request, my_val):	# my_val would be a number from the URL
#     pass                                # given the example above, my_val would be 23
    
# def yet_another(request, name):	        # name would be a string from the URL
#     pass                                # given the example above, name would be 'pooh'
    
# def one_more(request, id, color): 	# id would be a number, and color a string from the URL
#     pass                                # given the example above, id would be 17 and color would be 'brown'

# from django.shortcuts import render, redirect
# def some_function(request):
#     if request.method == "GET":
#     	print("a GET request is being made to this route")
#     	return render(request, "some_template.html")
#     if request.method == "POST":
#         print("a POST request is being made to this route")
#     	return redirect("/")