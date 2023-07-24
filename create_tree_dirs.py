import os
from tree_file import films_titles
from create_award_films import awards
import json
from genres_film import *
from pprint import pprint
import csv


def create_tree_dirs():
    dir_main = 'Harry_Potter'
    if not os.path.exists(dir_main):
        os.mkdir(dir_main)
        print("Створена директорія")
    else:
        print("Директорія вже існує")

    os.chdir(dir_main)

    title_film = []
    for i in films_titles['results']:
        update_title = i['title'].replace(' ', '_').replace(':', '')
        title_film.append(update_title)
        os.makedirs(update_title, exist_ok=True)

    os.chdir('..')
    path_sub_list = []
    y = []
    for title in title_film:
        for i in range(ord('A'), ord('Z')):
            path_sub_dir = dir_main + '/' + title + '/' + chr(i)
            os.makedirs(path_sub_dir, exist_ok=True)

            for j in awards:
                if path_sub_dir[-1:] == j['award_name'][:1] and j['title_film'] == path_sub_dir[(len(dir_main)):-2].replace('/', ''):
                    path_sub_list.append(os.path.join(path_sub_dir, j['award_name']))

    for i in path_sub_list:
        with open(i + '.txt', 'w', encoding='UTF-8') as file_award:
            for j in awards:
                if j['award_name'] == i[i.rfind('\\')+1:] and \
                        j['title_film'] == i[(len(dir_main)):i.rfind('\\')-2].replace('/', ''):
                    file_award.write(j['award'] + '\n')


#create_tree_dirs()


dict_genres = json.loads(genres)
create_genres_dir = [(os.makedirs(*genre.values(), exist_ok=True), *genre.values()) for genre in dict_genres['results']]
title_genres_dir = [create_genres_dir[i][1] for i in range(len(create_genres_dir))]

film_info = []
title_genre = []

for i in films_data:
    film_info.append({
        'title': i['title'],
        'year': i['year'],
        'rating': i['rating'],
        'type': i['type'],
        'genres': [g['genre'] for g in i['gen']]
    })

for t in title_genres_dir:
    with open(os.path.join(t, t + '_film_info.csv'), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['title', 'year', 'rating', 'type', 'genres'])
        for f in film_info:
            for g in f['genres']:
                if g in os.path.join(t, 'film_info.csv'):
                    writer.writerow(f.values())