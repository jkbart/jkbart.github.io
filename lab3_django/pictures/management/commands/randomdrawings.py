from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from pictures.models import Drawing, Rectangle, Tag
from random import choice, randint, sample, choices
import string
from django.utils import timezone

class Command(BaseCommand):
    help = "Creates random drawings."

    def handle(self, *args, **kwargs):
        # Drawing.objects.all().delete()

        users = list(User.objects.all())
        all_tags = list(Tag.objects.all())

        suffix = ''.join(choices(string.ascii_uppercase + string.digits, k=5))

        for _ in range(10):  # Generate 10 random drawings
            # Choose a random user as the author
            author = []

            # Choose a random subset of tags for the drawing
            tags = []

            if len(all_tags) > 0:
                tags = sample(all_tags, randint(1, len(all_tags)))
            if len(users) > 0:
                author = sample(users, randint(1, len(users)))

            # Generate a random drawing
            drawing = Drawing.objects.create(
                width=randint(100, 1000),
                height=randint(100, 1000),
                name=f"Random drawing {_ + 1} " + suffix,
                description=f"Description for Drawing {_ + 1}",
                pub_date=timezone.now()
            )

            # Add tags to the drawing
            drawing.tags.set(tags)
            drawing.author.set(author)

            # Generate random rectangles for the drawing
            for _ in range(randint(4, 20)):
                x1 = randint(0, drawing.width - 10)
                y1 = randint(0, drawing.height - 10)
                Rectangle.objects.create(
                    x=x1,
                    y=y1,
                    width=randint(10, drawing.width - x1),
                    height=randint(10, drawing.height - y1),
                    color=choice(["red", "green", "blue", "purple", "yellow", "black", "pink",
                         "aquamarine", "cyan", "darkblue", "gold", "indigo", "lavender",
                         "magenta", "orange", "silver", "tan", "violet", "white", "coral", 
                         "fuchsia", "lime", "maroon", "navy", "olive", "teal"]),
                    author=drawing
                )

            self.stdout.write(self.style.SUCCESS(f'Successfully generated drawing: {drawing.name}'))
