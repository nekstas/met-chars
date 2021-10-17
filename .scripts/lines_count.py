# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import os


def lines_filter2(s):
    return s.strip() != '' and s[0] != '#'


count1, count2 = 0, 0
for base_path, _, files in os.walk('./..'):
    base_path = base_path.replace('\\', '/')
    if '/venv/' in base_path or '/.git/' in base_path:
        continue
    for file in files:
        if not file.endswith('.py') or file == 'lines_count.py':
            continue
        filename = f'{base_path}/{file}'
        with open(filename, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            lines2 = [*filter(lines_filter2, lines)]
            count1 += len(lines)
            count2 += len(lines2)

print(f'На данный момент в проекте примерно {count1} строк кода на Python.')
print(f'Из них {count2} строк непустые и без комментариев.')
