from django.shortcuts import render, redirect
from .models import ProblemRevision
from .forms import ProblemRevisionForm

def revision_view(request):
    if request.method == 'POST':
        form = ProblemRevisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('revision_view')
    else:
        form = ProblemRevisionForm()

        problems = ProblemRevision.objects.all().order_by('problem')
    return render(request, 'revision.html', {'form': form, 'problems': problems})

from django.shortcuts import get_object_or_404

def update_problem(request, pk):
    problem = get_object_or_404(ProblemRevision, pk=pk)

    if request.method == 'POST':
        problem.day_1 = 'day_1' in request.POST
        problem.day_3 = 'day_3' in request.POST
        problem.day_5 = 'day_5' in request.POST
        problem.day_7 = 'day_7' in request.POST
        problem.save()
    
    return redirect('revision_view')

from django.http import JsonResponse
from tracker.check_reminders import run_check  # import your logic function

def check_reminders_view(request):
    run_check()
    return JsonResponse({'status': 'Reminder check completed'})
