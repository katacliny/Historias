from django.contrib import admin
from hc.models import AntecedentePatologicoFamiliar, Antecedentes, ExamenFisico, HistoriaClinica, HistoriaSocioAmbiental, HojaDeEgreso, Interrogatorio, IntervencionQuirurgica, Paciente


class PacienteAdmin(admin.ModelAdmin):
    model = Paciente

admin.site.register(Paciente, PacienteAdmin)


class IntervencionQuirurgicaAdmin(admin.ModelAdmin):
    model = IntervencionQuirurgica

admin.site.register(IntervencionQuirurgica, IntervencionQuirurgicaAdmin)


class InterrogatorioAdmin(admin.ModelAdmin):
    model = Interrogatorio

admin.site.register(Interrogatorio, InterrogatorioAdmin)


class HojaDeEgresoAdmin(admin.ModelAdmin):
    model = HojaDeEgreso

admin.site.register(HojaDeEgreso, HojaDeEgresoAdmin)


class HistoriaSocioAmbientalAdmin(admin.ModelAdmin):
    model = HistoriaSocioAmbiental

admin.site.register(HistoriaSocioAmbiental, HistoriaSocioAmbientalAdmin)


class HistoriaClinicaAdmin(admin.ModelAdmin):
    model = HistoriaClinica

admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)


class ExamenFisicoAdmin(admin.ModelAdmin):
    model = ExamenFisico

admin.site.register(ExamenFisico, ExamenFisicoAdmin)


class AntecedentesAdmin(admin.ModelAdmin):
    model = Antecedentes

admin.site.register(Antecedentes, AntecedentesAdmin)


class AntecedentePatologicoFamiliarAdmin(admin.ModelAdmin):
    model = AntecedentePatologicoFamiliar

admin.site.register(AntecedentePatologicoFamiliar, AntecedentePatologicoFamiliarAdmin)
