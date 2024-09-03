import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from django.utils import timezone
from property.models import Property, ImagesProperty, FloorPlansImages, Features
from django.contrib.auth.models import User


# Initialize faker instance
fake = Faker()

# Predefined locations for Cairo, Alexandria, and Mansoura
locations = {
    'Cairo': '30.0444,31.2357',
    'Alexandria': '31.2001,29.9187',
    'Mansoura': '31.0364,31.3807'
}

# Create dummy data for the Property model using faker
def create_dummy_properties(num_properties=10):
    users = User.objects.all()
    property_types = ['House', 'Apartment', 'Office', 'Land', 'Villa', 'Shop', 'Warehouse']
    statuses = ['Rent', 'Sale', 'Buy']
    image_choices = ['1.jpg', '2.jpg','3.jpg', '4.jpg','5.jpg','6.jpg','7.jpg',
                     '8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg',
                     '16.jpg','17.jpg','18.jpg','19.jpg']

    for _ in range(num_properties):
        # Randomly choose a city and its corresponding location
        city = random.choice(list(locations.keys()))
        location = locations[city]

        property = Property.objects.create(
            title=fake.sentence(nb_words=3),
            price=random.uniform(10000, 1000000),
            status=random.choice(statuses),
            sku=random.randint(1, 10000),
            type=random.choice(property_types),
            bathroom=random.randint(1, 5),
            bedroom=random.randint(1, 5),
            description=fake.paragraph(nb_sentences=4),  # 4 sentences in the description
            parking=fake.boolean(),
            image=f'property/{random.choice(image_choices)}',  # Randomly choose from the image list
            area=random.uniform(50, 500),
            year_built=fake.date_this_century(),
            city=city,  # Set city from predefined cities
            location=location,  # Set location coordinates based on the chosen city
            # video=f'prop/video{_ + 1}.mp4',
            owner=random.choice(users),
            created_at=timezone.now(),
            updated_at=timezone.now(),
            view_count=random.randint(0, 100),
        )

        # Create related ImagesProperty data
        for i in range(random.randint(1, 5)):
            ImagesProperty.objects.create(
                Image=f'property_images/{random.choice(image_choices)}',  # Use the image list here as well
                property=property
            )

        # Create related FloorPlansImages data
        for i in range(random.randint(1, 3)):
            FloorPlansImages.objects.create(
                Image=f'property_images/{random.choice(image_choices)}',  # Use the image list here as well
                property=property
            )

        # Create related Features data
        features_list = ['Swimming Pool', 'Garden', 'Garage', 'Gym', 'Security']
        for feature in random.sample(features_list, random.randint(1, len(features_list))):
            Features.objects.create(
                features=feature,
                property=property
            )
    print(f"Seed Successfully")
# Call the function to create dummy data



# create_dummy_properties(50)
