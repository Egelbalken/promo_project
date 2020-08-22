import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","promo_project.settings")


# To setup in django
import django
django.setup()

# import from "app.models" class name
from promo_app.models import User
from faker import Faker

# create a fake object
fake_generator = Faker()

# default 5 populates
def populate(N=5):
    # Create all the new users
    for entry in range(N):
        fake_name =fake_generator.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake_generator.email()


        # new entry users
        # make fake users, object tuple unpacking from [0]
        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

# If we run this standalone run script
if __name__ == '__main__':
    print("POPULATING DATABASE...")
    populate(20)
    print("COMPLETE!")
