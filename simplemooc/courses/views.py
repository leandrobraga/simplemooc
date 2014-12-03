from django.shortcuts import render, get_object_or_404
from simplemooc.courses.models import Course
from .forms import ContactCourse


def index(request):

    courses = Course.objects.all()

    context = {"courses": courses}

    return render(request, "courses/index.html", context)


# def detail(request, pk):

#     course = get_object_or_404(Course, pk=pk)

#     context = {
#         'course': course
#     }

#     return render(request, 'courses/detail.html', context)

def detail(request, slug):

    course = get_object_or_404(Course, slug=slug)
    context = {}

    if request.method == "POST":
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()

    context['course'] = course
    context['form'] = form

    return render(request, 'courses/detail.html', context)
