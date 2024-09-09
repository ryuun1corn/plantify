from django.shortcuts import render

# Create your views here.
def show_main(request):
  context = {
    'app_name': 'Plantify Shop',
    'name': 'Yudayana Arif Prasojo',
    'class': 'PBP-D',
    'npm': '2306215160'
  }
  
  return render(request, "main.html", context)