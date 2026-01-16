from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel)
        spiderman = User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=spiderman, type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=batman, type='swim', duration=25, date=timezone.now().date())
        Activity.objects.create(user=superman, type='run', duration=60, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        w2 = Workout.objects.create(name='Situps', description='Do 30 situps')
        w1.suggested_for.set([ironman, batman])
        w2.suggested_for.set([spiderman, superman])

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=spiderman, score=90)
        Leaderboard.objects.create(user=batman, score=95)
        Leaderboard.objects.create(user=superman, score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
