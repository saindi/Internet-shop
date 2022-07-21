from django.http import HttpRequest, HttpResponse
import re
import random


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("""
    <h1 align='center'>Homepage</h1>
    <ol>
        <li>Створити новий репозиторій на GitHub</li>
        <li>Ініціалізувати django проект</li>
        <li>Налаштувати наступні views та структуру urls:</li>
            <ol type='a'>
                <li>/homepage - домашня сторінка, має містити будь який статичний текст</li>
                <li>/home - те саме</li>
                <li>/ - те саме</li>
                <li>/article/&#60;article_id&#62;/&#60;article_slug&#62; - буде повертати інформацію про статю: 
                номер статіта ії залоговок (slug)</li>
                <li>/password/&#60;password&#62; - буде перевіряти переданий пароль: має містити букви латинського 
                алфавіта у будь якому регістрі або цифри (інщі символи вважати забороненими), та бути завдовшки 8 
                символів. Виводи, чи відповідає переданий пароль цим параметрам, чи ні.</li>
                <li>/password/generate/&#60;length&#62; - буде відображати випадково сгенерований пароль 
                заданої довжини</li>
            </ol>
    </ol>
    """)


def article(request: HttpRequest, article_id: int, article_slug: str) -> HttpResponse:
    return HttpResponse(f"<h1 align='center'>Article {article_id}</h1>"
                        f"<h2>{article_slug}</h2>"
                        f"<p>Some text</p>")


def password_check(request: HttpRequest, password: str) -> HttpResponse:
    if re.match(r'[A-Za-z0-9]{8}', password):
        return HttpResponse(f"<h1 align='center'>Password check</h1>"
                            f"<h2>Valid password '{password}'</h2>")
    else:
        return HttpResponse(f"<h1 align='center'>Password check</h1>"
                            f"<h2>Password '{password}' not valid </h2>")


def password_generate(request: HttpRequest, length: int) -> HttpResponse:
    alphabet = 'abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ1234567890'

    password = "".join([random.choice(alphabet) for _ in range(length)])

    return HttpResponse(f"<h1 align='center'>Password generate</h1>"
                        f"<h2>Password generat: {password}</h2>")