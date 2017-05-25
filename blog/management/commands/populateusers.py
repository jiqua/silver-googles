from django.core.management import BaseCommand
from django.contrib.auth.models import User

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
#Show this when the user types help
    help = "My test command"
    def handle(self, *args, **options):
        users = []
        for i in range(100):
            user = User(username = 'User%dFakeName' % i,
                        password = "pbkdf2_sha256$30000$cIk1DLFC1gBS$I8puHshroZAPr8Eu4kbrHE6XoDmK6RuHQcAMgyks+KU=",
                        email = "user%dfakeemail@fakeemail.com" % i)
            users.append(user)
        User.objects.bulk_create(users)
