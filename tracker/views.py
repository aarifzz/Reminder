# from django.shortcuts import render, redirect
# from .models import ProblemRevision
# from .forms import ProblemRevisionForm

# def revision_view(request):
#     if request.method == 'POST':
#         form = ProblemRevisionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('revision_view')
#     else:
#         form = ProblemRevisionForm()

#         problems = ProblemRevision.objects.all().order_by('date')
#     return render(request, 'revision.html', {'form': form, 'problems': problems})

# from django.shortcuts import get_object_or_404

# def update_problem(request, pk):
#     problem = get_object_or_404(ProblemRevision, pk=pk)

#     if request.method == 'POST':
#         problem.day_1 = 'day_1' in request.POST
#         problem.day_3 = 'day_3' in request.POST
#         problem.day_5 = 'day_5' in request.POST
#         problem.day_7 = 'day_7' in request.POST
#         problem.save()
    
#     return redirect('revision_view')

# from django.http import JsonResponse
# from tracker.check_reminders import run_check  # import your logic function

# def check_reminders_view(request):
#     run_check()
#     return JsonResponse({'status': 'Reminder check completed'})

# def edit_problem(request, pk):
#     problem = get_object_or_404(ProblemRevision, pk=pk)
#     if request.method == 'POST':
#         form = ProblemRevisionForm(request.POST, instance=problem)
#         if form.is_valid():
#             form.save()
#             return redirect('revision_view')
#     else:
#         form = ProblemRevisionForm(instance=problem)
#     return render(request, 'edit_problem.html', {'form': form})


# def delete_problem(request, pk):
#     problem = get_object_or_404(ProblemRevision, pk=pk)
#     problem.delete()
#     return redirect('revision_view')

from django.shortcuts import render, redirect, get_object_or_404
from .models import ProblemRevision
from django.http import JsonResponse
from tracker.check_reminders import run_check  # if used

def revision_view(request):
    if request.method == 'POST':
        for key in request.POST:
            if key.startswith("update_"):
                pk = int(key.split("_")[1])
                problem = get_object_or_404(ProblemRevision, pk=pk)
                problem.problem = request.POST.get(f"problem_{pk}")
                problem.link = request.POST.get(f"link_{pk}")
                problem.date = request.POST.get(f"date_{pk}")
                problem.difficulty = request.POST.get(f"difficulty_{pk}")
                problem.notes = request.POST.get(f"notes_{pk}")
                problem.day_1 = f"day_1_{pk}" in request.POST
                problem.day_3 = f"day_3_{pk}" in request.POST
                problem.day_5 = f"day_5_{pk}" in request.POST
                problem.day_7 = f"day_7_{pk}" in request.POST
                problem.save()

            elif key.startswith("delete_"):
                pk = int(key.split("_")[1])
                get_object_or_404(ProblemRevision, pk=pk).delete()

            elif key == "add_new":
                ProblemRevision.objects.create(
                    problem=request.POST.get("new_problem"),
                    link=request.POST.get("new_link"),
                    date=request.POST.get("new_date"),
                    difficulty=request.POST.get("new_difficulty"),
                    notes=request.POST.get("new_notes"),
                )
        return redirect('revision_view')

    problems = ProblemRevision.objects.all().order_by('date')
    return render(request, 'revision.html', {'problems': problems})


def check_reminders_view(request):
    run_check()
    return JsonResponse({'status': 'Reminder check completed'})

