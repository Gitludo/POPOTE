from django.contrib import admin
from .models import Stock, Consommateur


class StockAdmin(admin.ModelAdmin):
   list_display   = ('produit', 'quantite', 'date')
   list_filter    = ('produit','quantite',)
   date_hierarchy = ('date')
   ordering       = ('produit', 'quantite')
   search_fields  = ('produit', 'quantite')

class ConsommateurAdmin(admin.ModelAdmin):
   list_display   = ('Nom', 'Prenom', 'Carte', 'Cafe')
   list_filter    = ('Nom', 'Prenom', 'Carte', 'Cafe')
   ordering       = ('Nom', 'Prenom', 'Carte', 'Cafe')
   search_fields  = ('Nom', 'Prenom', 'Carte', 'Cafe')

admin.site.register(Stock, StockAdmin)
admin.site.register(Consommateur, ConsommateurAdmin)

# Register your models here.
