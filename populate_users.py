import os, django, random
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_source.settings')
django.setup()


from third_app_forms.models import User
from faker import Faker


fake_gen = Faker()


def populate(n=5):
    # Create n Entries of Dates Accessed
    for entry in range(n):
        # Create Fake Data for entry
        # fake_name = fakegen.name().split()
        # fake_username = fake_gen.username()
        fake_first_name = fake_gen.first_name()
        fake_last_name = fake_gen.last_name()
        fake_email = fake_gen.email()
        # fake_verify_email = fake_gen.verify_email()
        # Create new User Entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name,
                                          email=fake_email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
