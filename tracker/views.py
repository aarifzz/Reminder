from django.shortcuts import render, redirect, get_object_or_404
from .models import ProblemRevision
from django.http import JsonResponse
from check_reminders import run_check  # if used
from django.contrib.auth.decorators import login_required

@login_required
def revision_view(request):
    if request.method == 'POST':
        for key in request.POST:
            if key.startswith("update_"):
                pk = int(key.split("_")[1])
                problem = get_object_or_404(ProblemRevision, pk=pk,user = request.user)
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
                get_object_or_404(ProblemRevision, pk=pk,user = request.user).delete()

            elif key == "add_new":
                problem = request.POST.get("new_problem", "").strip()
                link = request.POST.get("new_link", "").strip()
                date = request.POST.get("new_date", "").strip()
                difficulty = request.POST.get("new_difficulty", "").strip()
                notes = request.POST.get("new_notes", "").strip()

                # ✅ Backend validation: only add if all required fields are filled
                if problem and link and date and difficulty:
                    ProblemRevision.objects.create(
                        user = request.user,
                        problem=problem,
                        link=link,
                        date=date,
                        difficulty=difficulty,
                        notes=notes,
                    )   

        return redirect('revision_view')

    problems = ProblemRevision.objects.filter(user  = request.user).order_by('date')
    return render(request, 'revision.html', {'problems': problems})


def check_reminders_view(request):
    run_check()

