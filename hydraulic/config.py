# -*- coding: utf-8 -*-

PROFILE_LEVELS_TABLE = True  # Отображение уровней воды различных обеспеченностей на графике профиля
PROFILE_LEVELS_TABLE_LINES = False  # Линии сносок от урезов воды к значению в таблицу уровней
PROFILE_WATER_LEVEL_NOTE = False  # Отображение примечания о урезе воды
PROFILE_LEVELS_TITLE = True  # Отображение подписи уровней воды на профилях
PROFILE_SECTOR_LABEL = True  # Отображение названия, длины и разделителя по участкам
PROFILE_SECTOR_FILL = False  # Заливка участков профиля на графике
PROFILE_SECTOR_BOTTOM_LINE = False  # Цвет линии дна по участкам
PROFILE_WATER_FILL = True  # Заливка урезов
PROFILE_WET_PERIMETER = False  # Отрисовка смоченного периметра (для отладки)
PROFILE_EROSION_LIMIT = True  # Отрисовка отметки предельного размыва
PROFILE_EROSION_LIMIT_FULL = False  # Линия предельного размыва во всю длину профиля (если false то только по участкам русла и протоки)
PROFILE_TOP_LIMIT = True  # Отрисовка низа ограничивающее сооружения
PROFILE_SAVE_PICTURES = False  # Сохранение рисунков поперечников в отдельные файлы
HYDRAULIC_CURVE = True  # Отрисовка графика гидравлической кривой
HYDRAULIC_CURVE_LEVELS = True  # Отрисовка расчётных уровней на графике гидравлической кривой
HYDRAULIC_AND_SPEED_CURVE = False  # Отрисовка графика гидравлической кривой с совмещенным графиком скорости
SPEED_CURVE = False  # Отрисовка графика кривой скоростей
SPEED_CURVE_LEVELS = True  # Отрисовка расчётных скоростей на графике кривой скоростей
SPEED_VH_CURVE = True  # Отрисовка графика кривой скоростей от уровня
AREA_CURVE = False  # Отрисовка графика кривой площадей
AREA_FH_CURVE = True  # Отрисовка графика кривой площадей от уровня
CURVE_SAVE_PICTURES = False  # Сохранение рисунков кривой в отдельные файлы
CURVE_HIDE_GRID = False  # Скрыть сетку на графиках кривых
GRAPHICS_TITLES = True  # Отрисовка названия на графиках
GRAPHICS_TITLES_TEXT = False  # Подпись графиков текстом
REWRITE_DOC_FILE = True  # Перезапись экспортируемого файла
DOC_TABLE_SHORT = True  # Укороченный вариант таблицы гидравлической кривой
SITUATION_COLORS = True  # Отрисовка заливки цветом подложки ситуации (в подвале)

ALTITUDE_SYSTEM = ' БС'  # Подпись базовой системы высот (м БС, БС77, абс. и т.д.)

TEMP_DIR_NAME = 'TEMP'  # Название временной папки
GRAPHICS_DIR_NAME = 'Графика'  # Название папки экспорта графики

# Формула расчёта скорости движения
# 1 — Расчёт обычной воды; 2 — Расчёт водокаменного селевого потока; 3 — Расчёт грязекаменного селевого потока
CALC_TYPE = 1  # Выбор типа варианта расчёта

# Расчёт с переливом через бровку (True) или с заполнением всех секторов (False)
OVERFLOW = False

# Разрешение экспортируемых графиков
FIG_DPI = 200

# Размер профиля для вставки в отчет: (16.5, 14); для А3 (28, 14)
PROFILE_SIZE = (16.5, 14)

# Режим отладки (вывод информации о скорости выполнения модулей)
DEBUG = True

COLOR = {
    'text': 'black',  # Основной для текста
    'bottom_text': 'black',  # Основной текст в подвале
    'bottom_text_secondary': 'gray',  # Второстепенный текст в подвале
    'title_text': 'black',  # Заголовок профиля и графика Q(h)
    'border': 'black',   # Основные линии
    'profile_bottom': 'saddlebrown',  # Линия дна
    'profile_point_line': 'black',  # Вертикальные линии от точек до подвала
    'sector_text': 'gray',  # Подписи названия и ширины участков на профиле
    'sector_line': 'gray',  # Линии разграничения участков
    'water_line': 'dodgerblue',  # Линия уреза воды
    'water_reference_line': 'deepskyblue',  # Линий сноски уреза воды
    'water_fill': 'deepskyblue',  # Заливка воды
    'water_level_text': 'navy',  # Подписи уровней воды
    'erosion_limit_line': 'red',  # Линия предельного размыва
    'erosion_limit_text': 'darkred',  # Текст предельного размыва
    'top_limit_line': 'silver',  # Линия ограничения верхнего сооружения
    'top_limit_text': 'gray',  # Текст ограничения верхнего сооружения
    'ax_label_text': 'black',  # Подписи заголовка осей
    'ax_value_text': 'black',  # Подписи значений осей
    'ax_grid': 'silver',  # Сетка профиля, основной цвет
    'ax_grid_sub': 'whitesmoke',  # Сетка профиля, вспомогательный цвет
    'levels_table': 'black',  # Таблица с уровнями
}

FONT_SIZE = {
    'title': 20,  # Заголовок профиля и графика Q(h)
    'ax_label': 16,  # Подписи заголовка осей
    'water_level': 12,  # Урез воды
    'erosion_limit': 12,
    'top_limit': 12,
    'ax_major': 12,  # Значений основных осей
    'ax_minor': 8,  # Значений вспомогательных осей
    'bottom_main': 12,  # Основной для текста в подвале
    'bottom_medium': 10,
    'bottom_small': 8,  # Основной для текста в подвале
    'bottom_description': 14,  # Описание элементов подвала
    'levels_table': 12,  # Таблица уровней различных обеспеченностей
    'legend': 12,  # Легенда на графике гидравлической кривой
}

LINE_WIDTH = {
    'ax_border': 2,  # Основные линии осей
    'water_line': 2,  # Линия уреза воды
    'erosion_limit_line': 3,  # Линия предельного размыва
    'top_limit_line': 2,  # Линия ограничения верхнего сооружения
    'sector_line': 1,  # Линии разделителя участков
    'profile_bottom': 2.5,  # Основные линии в подвале
    'profile_point_line': 1,  # Вертикальные линии от точек до подвала
}

PADDING = {
    'ax_tick_labels': 8,  # Отступ от оси подписей значений осей на графиках кривых
    'ax_profile_tick_labels': 8  # Отступ от оси подписей значений осей на графике профиля
}

STRING = {
    'table': 'Таблица — ',
    'figure': 'Рисунок — '
}
