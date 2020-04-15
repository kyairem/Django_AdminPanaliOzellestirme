from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):

	list_display = ['title','publishing_date'] #içeriği görüntülemek için 
	list_display_links = ['publishing_date'] #içeriğin link gibi görünmesi için 
	list_filter = ['publishing_date'] #değişken türüne göre kenarda filtreleme seçenekleri gelir- filtreleme yapmak için 
	search_fields = ['title','content'] #arama çubuğu gelir değişkene göre aranılan kayıtları getirir	
	list_editable = ['title'] #içerisindeki alanlar link olarak tanımlanmamalıdır - güncellemek için kullanılır.
	
	class Meta:
		model = Post

admin.site.register(Post,PostAdmin)


