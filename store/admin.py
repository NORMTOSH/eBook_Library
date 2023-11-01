from django.contrib import admin
from .models import Category, Writer, Book, Slider
from django.utils.html import format_html


class AddCategory(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, AddCategory)

class AddWriter(admin.ModelAdmin):
	list_display = ['display_pic', 'name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

	def display_pic(self, obj):
			return format_html('<img src="{}" width="35" height="50" />', obj.pic.url if obj.pic else '')

	display_pic.short_description = 'Pic'

admin.site.register(Writer, AddWriter)

class AddBook(admin.ModelAdmin):
	list_display = ['display_coverpage', 'name', 'category', 'writer', 'bookpage', 'price', 'status', 'created', 'updated']
	list_filter = ['status', 'created', 'updated']
	list_editable = ['status']
	prepopulated_fields = {'slug': ('name',)}

	def display_coverpage(self, obj):
			return format_html('<img src="{}" width="35" height="50" />', obj.coverpage.url if obj.coverpage else '')

	display_coverpage.short_description = 'Cover Page'

admin.site.register(Book, AddBook)

class AddSlider(admin.ModelAdmin):
	list_display = ['display_slideimg', 'title', 'created', 'updated']
	#list_editable = ['title']

	def display_slideimg(self, obj):
			return format_html('<img src="{}" width="35" height="50" />', obj.slideimg.url if obj.slideimg else '')

	display_slideimg.short_description = 'Slide Image'

admin.site.register(Slider, AddSlider) 