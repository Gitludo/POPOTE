from django.contrib import admin
from .models import Stock



class StockAdmin(admin.ModelAdmin):
   list_display   = ('produit', 'quantite', 'date')
   list_filter    = ('produit','quantite',)
   date_hierarchy = 'date'
   ordering       = ('produit', )
   search_fields  = ('produit', 'quantite')

admin.site.register(Stock, StockAdmin)

# Register your models here.
