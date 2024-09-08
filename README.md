# The project is created on pure selenium and python+pytest

### Для написания проекта использовался ресурс:

- https://demoqa.com/
- CI/CD - Github actions

## The project includes:

### 1. Добавлен самописный модуль pytest-cmdline-add-args 1.9.5

    - Модуль позволяет изменять аргументы командной строки до запуска тестов
    - Модуль добавляет аргументы командной строки для получения аллюр отчетов
    - В модуле добавлен самописный метод для загрузки системных переменных с файла env.py, 
    что позволяет управлять модулем из самого проекта

https://pypi.org/project/pytest-cmdline-add-args/

### 2. Проект кроссбраузерный

#### 1. Локально:
    - На виндовз работают тесты для Chrome, Edge, Firefox
    - На мак ОС работают тесты Chrome, Edge, Safari

#### 2. Удаленно работают тесты только для Chrome и Edge
    - С Firefox проблемы, т.к. сущестуют конфликты при установке браузера на Ubuntu

### 3. Аллюр отчеты

1. Локально:
    - Нужно указать в файле env.py в папке конфиг:
        * CREATE_ALLURE_REPORT = False

        - Если CREATE_ALLURE_REPORT = True:
            * Аллюр отчет автоматически откроется в браузере

#### 2. Удаленно:
    - Во время автоматического и ручного запуска аллюр отчеты создаются автоматически

#### 3. Отправка аллюр отчетов
    - При автоматическом запуске отчеты отправляются автоматически
    - При ручном запуске можно указать отправлять отчет или нет (локально и удаленно):
        - Для локальной отправки нужно создать файл .env и там указать данные для отправки отчета на имейл

### 4. Запуск тестов через гит хаб экшнс

If you are going to run tests using GitHub actions, you need to specify the name of your project in workflow:

env:
#### PROJECT_NAME: project_name

#### 1. Кастомизация запуска тестов
    - Можно выбрать раздел ресурса, для которого запустятся тесты
    - Можно выбрать браузер для запуска тестов
    - Можно выбрать отправлять репорт на имейл или нет

#### 2. Деплой аллюр отчетов на ресурс https://evgeniy955.github.io/demoqa_com/
    - Отображаются все тесты что были запущены для данного проекта
    - Сохранение истории запусков для каждого теста
    - Сохранение повторных попыток для каждого теста

### 5. Запуск тестов локально

#### 1. Кастомизация запуска тестов
    - Выбрать конкретный тест
        - e.g. -m "C0007"
    - Можно запустить тесты для любого раздела проекта
    - Можно указать браузер для запуска тестов
    - Можно указать нужно ли создавать аллюр отчет
    - Можно указать нужно ли отправлять отчет на имейл

#### 2. Настройка запуска тестов локально в файле config/env.py