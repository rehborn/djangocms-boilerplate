from cms.api import create_page, create_title
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from base.config import config
from base.models import UserSettings


class Command(BaseCommand):
    def handle(self, *args, **options):

        # create demo user and content if there's no user
        if User.objects.all().count() == 0:
            user, email, password = ['demo', 'demo@demo.demo', 'demo']
            user = User.objects.create_superuser(user, email, password)
            user.save()
            print(f"User: {user} created")

            for i in range(1, 3):
                _user, _created = User.objects.get_or_create(username=f"demo-{i}",
                                                             first_name=f"demo{i}",
                                                             last_name=f"demo{i}",
                                                             email=f"demo{i}@demo.demo",
                                                             )
            home = create_page(f'Home {settings.LANGUAGES[0][0]}',
                               template='default.html',
                               language=settings.LANGUAGES[0][0],
                               in_navigation=True, published=True, parent=None,  slug='home')

            for lang in settings.LANGUAGES[1:]:
                create_title(lang[0], f'Home {lang[0]}', slug='home', page=home)
                home.publish(language=lang[0])

            home.set_as_homepage()

        # update UserSettings according to config.yml
        self.update_user_settings()

    @staticmethod
    def update_user_settings() -> None:
        user_settings = config('user_settings')

        # user_settings.get('name')
        # user_settings.get('url')

        # Create User Settings
        for key, descr in user_settings.items():
            obj, created = UserSettings.objects.get_or_create(key=key)
            if created:
                obj.value = key
                obj.save()
                print(f"UserSettings: created: {obj.key}")

        # Remove unused User Settings
        for obj in UserSettings.objects.all():
            if obj.key not in user_settings.keys():
                obj.delete()
                print(f"UserSettings: deleted: {obj.key}")
