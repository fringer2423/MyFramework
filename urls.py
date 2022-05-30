from views import Index, About

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/about/': About(),
}
