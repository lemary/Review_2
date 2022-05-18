# WikiMIPT

Это программа для студентов МФТИ. Каждый студент может зайти и, (1) либо оценить и сделать комментарию для своего учителя, либо (2) знать средную оценку и комментарии учителя, которые оставили другие студенты.

1. Надо войти в нужный раздел (выбрать "Comment", если запущена браузерная версия, или написать "comment" в консоле) и написать имя своего учителя, комментарий и оценку(от 0 до 10) в соответственных полях.
2. Надо войти в нужный раздел (выбрать "Archive", если запущена браузерная версия, или написать "get_characters" в консоле) и написать имя своего учителя. После этого отображается топ-5 использованных комментариев, средняя оценка и сколько людей оставили отзывы.

## Запуск Сервера

### Для ОС Linux

Откройте терминал в корневом директории репозитория.

Наберите 
```bat
./run_server.sh
```

---

### Для ОС Windows

Устанавите flask

Откройте коммандную строку в директории *Server*

Наберите
```bat
python app.py
```

---

После этого можно в браузере открыть страницу по адресу http://localhost:8000/. Там будут две кнопки ("Comment" и "Archive"), о которых говорили выше.

## Запуск Клиента

### Для ОС Linux

Откройте терминал в корневом директории репозитория.

Наберите 
```bat
./run_client.sh
```

---

### Для ОС Windows

Устанавите requests, lxml

Откройте коммандную строку в директории *Client*

Наберите
```bat
python client.py
```

---

### Пример использования клиента.

```console
Enter command(comment, get_characters, exit)
comment
Teacher Full Name: Maria Leontieva
Comment: clever
Mark(number from 0 to 10): 10
Enter command(comment, get_characters, exit)
comment
Teacher Full Name: Maria Leontieva
Comment: beautiful
Mark(number from 0 to 10): 9
Enter command(comment, get_characters, exit)
get_characters
Teacher Full Name: Maria Leontieva
 Comments:  clever, beautiful  
 Average Mark:  9.5  
 Gave Mark:  2 
Enter command(comment, get_characters, exit)
exit
Are you sure you want to leave (Y/N)?Y
Goodbye!
```

---

## Важные замечания
1. **Включите сервер, потом только клиент.**
2. **Данных пока что мало.**

