from django.core.management.base import BaseCommand

from stripe_app.models import Item


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Формируем список из объектов Item и записываем в базу данных  """
        try:
            Item.objects.all().delete()
            print('DB clear')
        except Exception as ex:
            print('Error clear DB', ex)

        object_list_to_db = [Item(
            id=item,
            name=f'Item {item}',
            description=f'Desc {item}',
            price=f'{item}000')
            for item in range(1, 10)]
        print(object_list_to_db)

        try:
            Item.objects.bulk_create(object_list_to_db)
            print('Импорт в БД выполнен успешно')
        except Exception as ex:
            print('Во время заполнения БД произошла ошибка:', ex)
