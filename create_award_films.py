from film_award import films_awards
import json


def create_awards_list(path_json):
    awards_list = []
    title_f = ''
    with open(path_json) as f:
        json_award = json.load(f)

        for i in json_award:
            for j in i['results']:
                title_f = j['movie']['title'].replace(' ', '_').replace(':', '')
                if title_f:
                    awards_list.append({
                                        'type': j['type'],
                                        'award_name': j['award_name'],
                                        'award': j['award'],
                                        'title_film': title_f
                      })

        # pp(awards_list)

        awards = sorted(awards_list, key=lambda award: award['award_name'])
        return awards




