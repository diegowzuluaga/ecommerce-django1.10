from django.contrib import admin

# Register your models here.
from .models import Product, Variation, ProductImage, Category, ProductCategory, ProductFeatured

class ProductImageInLine(admin.TabularInline):
	model = ProductImage
	extra = 0
	max_num = 10


class VariationInLine(admin.TabularInline):
	model = Variation
	extra = 0 #numero de lineas en el formulario de Variation
	max_num = 10


class ProductAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'price']
	inlines = [
	    ProductImageInLine,
	    VariationInLine,

	]
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)
#admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductCategory)
admin.site.register(ProductFeatured)
#admin.site.register(Variation)
