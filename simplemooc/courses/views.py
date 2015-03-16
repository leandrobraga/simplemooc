from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from simplemooc.courses.models import Course
from simplemooc.courses.models import Enrollment
from .forms import ContactCourse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


@login_required
def enrollment(request, slug):

    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    if created:
        enrollment.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')

    return redirect('accounts:dashboard')
