# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import os

count = 0
for base_path, _, files in os.walk('./..'):
    base_path = base_path.replace('\\', '/')
    if '/venv/' in base_path or '/.git/' in base_path:
        continue
    for file in files:
        if not file.endswith('.py') or file == 'lines_count.py':
            continue
        filename = f'{base_path}/{file}'
        with open(filename, 'r', encoding='UTF-8') as f:
            count += len(f.readlines())

print(f'На данный момент в проекте примерно {count} строк кода на Python.')
