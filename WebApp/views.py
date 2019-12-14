from django.shortcuts import render

def HomeView(request):
    return render(request, 'WebApp/Home_Page.html')

def CoursesView(request):
    return render(request, 'WebApp/Courses.html')

def NewsView(request):
    return render(request, 'WebApp/News.html')

def SportsView(request):
    return render(request, 'WebApp/Sports.html')

def AboutView(request):
    return render(request, 'WebApp/About.html')
