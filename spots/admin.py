from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from spots.models import Book ,Totalspots, Cities

admin.site.register(Book)

class TotalspotsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('name','category','cities','city','address','content')

admin.site.register(Totalspots,TotalspotsAdmin)

class CitiesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('cities','city')

admin.site.register(Cities,CitiesAdmin)
