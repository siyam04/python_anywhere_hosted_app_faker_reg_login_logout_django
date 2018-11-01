import os, django, random

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_source.settings')
django.setup()


from first_app.models import Topic, WebPage, AccessRecord
from faker import Faker


fake_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    # Create n Entries of Dates Accessed
    for entry in range(n):
        # Get Topic for Entry
        top = add_topic()
        # Create Fake Data for entry
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()
        # Create new WebPage Entry
        web_pg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        acc_rec = AccessRecord.objects.get_or_create(name=web_pg, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the database...Please Wait")
    populate(20)
    print('Populating Complete')
