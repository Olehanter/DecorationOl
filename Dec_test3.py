import os
from datetime import datetime
import requests


def logger(old_function):
    new_functions = old_function
    print(new_functions.__name__)

    def new_function(*args, **kwargs):
        print(args, kwargs)
        date_time = datetime.now()
        func_name = old_function.__name__
        result = new_functions(*args, **kwargs)
        with open('maining.log', 'a', encoding='utf-8') as f:
            f.write(f'Дата/время: {date_time}\n'
                    f'Имя функции: {func_name}\n'
                    f'Аргумент {args} - {kwargs}\n'
                    f'Результат {result}\n')
            return result

    return new_function


def test_3():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    resp = response.json()

    @logger
    def simile_mind(heros):
        club = {}
        for next_h in heros:
            for act_ in resp:
                if act_['name'] == next_h:
                    club[next_h] = act_['powerstats']['intelligence']
                    max_intel = max(club.items())
        return (max_intel)

    print(simile_mind(['Hulk', 'Captain America', 'Thanos']))


if __name__ in '__main__':
    test_3()
