from views import Index, About, StudyPrograms, CoursesList, \
    CreateCourse, CreateCategory, CategoryList

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/about/': About(),
    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList()
}
