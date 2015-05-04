from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from simplemooc.courses.models import Course
from simplemooc.courses.models import Enrollment
from simplemooc.courses.models import Announcement
from simplemooc.courses.models import Lesson
from .forms import ContactCourse
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import enrollment_required


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


@login_required
def undo_enrollment(request, slug):

    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)

    if request.method == "POST":
        enrollment.delete()
        messages.success(request, "Sua inscrição foi cancelada com sucesso!")
        return redirect("accounts:dashboard")

    context = {}
    context['enrollment'] = enrollment
    context['course'] = course

    return render(request, "courses/undo_enrollment.html", context)


@login_required
@enrollment_required
def announcements(request, slug):

    course = request.course
    context = {}
    context['course'] = course
    context['announcements'] = course.announcements.all()

    return render(request, "courses/announcements.html", context)


@login_required
@enrollment_required
def show_announcement(request, slug, pk):

    course = request.course
    announcement = get_object_or_404(course.announcements.all(), pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        form = CommentForm()
        messages.success(request, "Seu comentário foi enviado com sucesso!")

    template = "courses/show_announcement.html"

    context = {}
    context['course'] = course
    context['announcement'] = announcement
    context['form'] = form

    return render(request, template, context)


@login_required
@enrollment_required
def lessons(request, slug):
    course = request.course
    template = "courses/lessons.html"
    lessons = course.relase_lessons()
    if request.user.is_staff:
        lessons = course.lessons.all()
    context = {
        "course": course,
        "lessons": lessons
    }
    return render(request, template, context)


@login_required
@enrollment_required
def lesson(request, slug, pk):

    course = request.course
    lesson = get_object_or_404(Lesson, pk=pk, course=course)
    if not request.user.is_staff or not lesson.is_available():
        messages.error(request, "Esta aula não está disponível")
        return redirect("courses:lessons", slug=course.slug)
    template = "courses/lesson.html"
    context = {
        "course": course,
        "lesson": lesson
    }
    return render(request, template, context)
