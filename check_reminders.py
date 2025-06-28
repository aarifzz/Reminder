import os
import django
import datetime
from django.core.mail import send_mail
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dsatracker.settings")
django.setup()

from tracker.models import ProblemRevision


def run_check():
    today = datetime.date.today()
    problems = ProblemRevision.objects.all()

    for prob in problems:
        days_since = (today - prob.date).days

        # get the associated user email
        user_email = prob.user.email if prob.user and prob.user.email else None

        if not user_email:
            continue  # skip if no email available

        if days_since == 1 and not prob.day_1:
            send_mail(
                "1-Day Revision Reminder",
                f"🧠 You haven't revised '{prob.problem}' (1-day mark). Do it now!",
                settings.EMAIL_HOST_USER,
                [user_email],
            )
        elif days_since == 3 and not prob.day_3:
            send_mail(
                "3-Day Revision Reminder",
                f"⏰ Reminder: Please revise '{prob.problem}' (3-day mark).",
                settings.EMAIL_HOST_USER,
                [user_email],
            )
        elif days_since == 5 and not prob.day_5:
            send_mail(
                "5-Day Revision Reminder",
                f"⚠️ Still pending: Revise '{prob.problem}' (5-day mark).",
                settings.EMAIL_HOST_USER,
                [user_email],
            )
        elif days_since == 7 and not prob.day_7:
            send_mail(
                "7-Day Revision Reminder",
                f"📚 Final Reminder: Revise '{prob.problem}' (7-day mark).",
                settings.EMAIL_HOST_USER,
                [user_email],
            )

if __name__ == "__main__":
    run_check()
