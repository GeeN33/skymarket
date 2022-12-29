import os
import json
from django.core.management.base import BaseCommand
from users.models import User
from ads.models import Comment, Ad


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('fixtures/users.json', "r", encoding='utf-8') as f:
            data = json.load(f)
            for row in data:
                user = User()
                user.last_login = row['fields']['last_login']
                user.first_name = row['fields']['first_name']
                user.last_name = row['fields']['last_name']
                user.password = row['fields']['password']
                user.role = row['fields']['role']
                user.email = row['fields']['email']
                user.phone = row['fields']['phone']
                user.is_active = row['fields']['is_active']
                user.username = row['fields']['email']

                user.save()
        print("Command load_data users.json")

        with open('fixtures/ad.json', "r", encoding='utf-8') as f:
            data = json.load(f)
            for row in data:
                ad = Ad()
                ad.image = row['fields']['image']
                ad.title = row['fields']['title']
                ad.price = row['fields']['price']
                ad.author = User.objects.get(id=row['fields']['author'])
                ad.created_at = row['fields']['created_at']

                ad.save()
        print("Command load_data ad.json")

        with open('fixtures/comments.json', "r", encoding='utf-8') as f:
            data = json.load(f)
            for row in data:
                comment = Comment()
                comment.text = row['fields']['text']
                comment.author = User.objects.get(id=row['fields']['author'])
                comment.ad = Ad.objects.get(id=row['fields']['ad'])
                comment.created_at = row['fields']['created_at']
                comment.save()
        print("Command load_data comments.json")
