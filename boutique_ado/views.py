# boutique_ado/views.py

from django.shortcuts import render

def success_view(request):
    return render(request, 'success.html')  # Renders a success template
