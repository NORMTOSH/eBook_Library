from django.urls import path
from . import views
from .views import social_links_view


app_name = 'store'

urlpatterns = [
	path('', views.index, name = "index"),
	path('login', views.signin, name="signin"),
	path('logout', views.signout, name="signout"),
	path('registration', views.registration, name="registration"),
	path('book/<int:id>', views.get_book, name="book"),
	path('books', views.get_books, name="books"),
	path('category/<int:id>', views.get_book_category, name="category"),
	path('writer/<int:id>', views.get_writer, name = "writer"),
    path('social-links/', social_links_view, name='social_links'),
    path('pdf_view/<int:book_id>/', views.pdf_view, name='pdf_view'),
]
