"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный."""

import sys

# Чтение количества матчей
n = int(input().strip())

# Словарь для хранения статистики команд
teams_stats = {}

for _ in range(n):
    # Читаем строки вида 'Команды;Гол_1;Команды;Гол_2'
    team1, goals1, team2, goals2 = input().split(';')
    
    # Преобразуем голы в целые числа
    goals1 = int(goals1)
    goals2 = int(goals2)
    
    # Если команда ещё не встречалась ранее, инициализируем её статистику
    if team1 not in teams_stats:
        teams_stats[team1] = {'games': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'points': 0}
    if team2 not in teams_stats:
        teams_stats[team2] = {'games': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'points': 0}
        
    # Обновляем статистику обеих команд
    teams_stats[team1]['games'] += 1
    teams_stats[team2]['games'] += 1
    
    # Определяем победителя и присваиваем очки
    if goals1 > goals2:
        teams_stats[team1]['wins'] += 1
        teams_stats[team1]['points'] += 3
        teams_stats[team2]['losses'] += 1
    elif goals1 < goals2:
        teams_stats[team2]['wins'] += 1
        teams_stats[team2]['points'] += 3
        teams_stats[team1]['losses'] += 1
    else:
        teams_stats[team1]['draws'] += 1
        teams_stats[team1]['points'] += 1
        teams_stats[team2]['draws'] += 1
        teams_stats[team2]['points'] += 1

# Вывод таблицы результатов
for team, stats in sorted(teams_stats.items()):
    print(f"{team}: {stats['games']} {stats['wins']} {stats['draws']} {stats['losses']} {stats['points']}")