from django.shortcuts import render, get_object_or_404
from simplemooc.courses.models import Course


def index(request):

    courses = Course.objects.all()

    context = {"courses": courses}

    return render(request, "courses/index.html", context)


def detail(request, pk):

    course = get_object_or_404(Course, pk=pk)

    context = {
        'course': course
    }

    return render(request, 'courses/detail.html', context)
