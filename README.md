# Hydraulic
![GitHub last commit](https://img.shields.io/github/last-commit/dell4valt/hydraulic)

Программа предназначена для гидравлических расчетов уровней и скоростей (а так же сопутствующих параметров) воды в русле реки с возможностью разделения русла на участки с индивидуальными параметрами.

Результатом выполнения программы является отчет в формате Microsoft Office содержащий графическую часть: створ поперечного профиля, гидравлическую кривую, кривую скоростей и их вариации; таблицы параметров и результатов расчетов: расчётные уровни воды, расчётные участки и их параметры, параметры расчёта кривой расхода воды, сводные таблицы по всем створам.

Створ поперечного профиля |  Гидравлическая кривая Q(H)     |         
:-------------------------:|:-------------------------:
![Створ поперечного профиля](https://raw.githubusercontent.com/dell4valt/hydraulic/dev/docs/img/profile.png) | ![Гидравлическая кривая Q(H) 3](https://raw.githubusercontent.com/dell4valt/hydraulic/dev/docs/img/QH.png)|

## 📈 Исходные данные
В текущей реализации параметры створов поперечных профилей задаются в специально подготовленном файле Microsoft Excel расположенном в `example/example_profile.xls`. Каждый лист в данном файле представляет собой отдельный створ к которому выполняются расчеты и по которому формируется отчет.

Для выполнения гидравлических расчетов требуется указание следующих обязательных параметров:
 - **Координаты сечения створа поперечного профиля** (колонки *ПК* и *ОТМ*)
 - расчетные участки и параметры **коэффициента шероховатости** и **уклона** (колонки *Участок*, *n* и *i*)
 - расчетные **обеспеченности** и **расходы воды** этих обеспеченностей (колонки *Обеспеченность*)
 - **расчетный шаг** в сантиметрах (ячейка *расчетный шаг*)

Остальные параметры являются необязательными для расчетов и влияют на визуальную и информационную составляющую отчета.

## 🧑🏻‍💻 Пример запуска
Пример запуска расчётов. Входные параметры представлены в файле `example/example_profile.xls`, результирующий отчёт записать в файл `result/hydraulic_results.docx`.

```python
from hydraulic import profile

# Пути к файлу исходных данных
# и к файлу результирующего отчета
IN_FILENAME = 'example/example_profile.xls'
OUT_FILENAME = 'result/hydraulic_results.docx'

# Запуск расчетов и формирования отчета
profile.xls_calculate_hydraulic(IN_FILENAME, OUT_FILENAME)
```

## ⏳ История изменений
### Версия 0.1.0
В программе реализованы все базовые методы и функции для выполнения расчетов и формирования отчета.

## 📚 Использованные источники
1. Железняков Г.В. Пропускная способность русел каналов и рек. Л.: Гидрометеоиздат, 1981. 312 с.
2. СП 33-101-2003. Определение основных расчетных гидрологических характеристик. Издание официальное. М.: Госстрой России, 2004. 73 с.