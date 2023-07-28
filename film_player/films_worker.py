import os.path
from create_dirs import create_dir


class Film:
    def __init__(self, title, description, running_time, rating, storage_address):
        self.title = title
        self.description = description
        self.running_time = running_time
        self.rating = rating
        self.storage_address = storage_address
        self.get_film_address()

    def upload_file(self):
        adress = create_dir()
        for adr in adress:
            if self.title[:1] and self.storage_address in adr:
                with open(adr + '/' + self.title + '.txt', 'w', encoding='utf-8') as f:
                    line = [f'Назва фільму {self.title}\n Опис фільму {self.description}\n '
                            f'Тривалісь фільму {self.running_time}\n '
                            f'Рейтинг фільму {self.rating}\n']
                    f.writelines(line)

    def get_film_address(self):
        self.storage_address = os.path.abspath(self.storage_address)
        return self.storage_address


film = Film('Seven', "A middle-aged husband's life changes dramatically when his wife asks him for a divorce", '118 minutes', 7.4, 'film_storage/S')
film1 = Film('Oscar', "A changes dramatically when his wife asks him for a divorce", '188 minutes', 7.4, 'film_storage/O')
film.upload_file()
film1.upload_file()
print(film.get_film_address())
