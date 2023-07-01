from django.db import models
from django_quill.fields import QuillField


class Paciente(models.Model):

    nombre = models.CharField(max_length=200)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    dni = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.dni} - {self.nombre}"


class HistoriaClinica(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    # Cabeceras
    modelo = models.CharField(max_length=200)
    ministerio = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)

    # Body
    motivo = models.CharField(max_length=600)
    historia_enfermedad_actual = QuillField()

    def __str__(self):
        return f"{self.paciente.dni} - {self.titulo}"


class AntecedentePatologicoFamiliar(models.Model):

    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    personal = models.BooleanField()
    padre = models.BooleanField()
    madre = models.BooleanField()
    hijo = models.BooleanField()
    otro = models.BooleanField()

    def __str__(self):
        return self.nombre


class IntervencionQuirurgica(models.Model):

    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    tipo_de_operacion = models.CharField(max_length=200)
    secuelas = models.CharField(max_length=200)
    fecha = models.DateField()

    def __str__(self):
        return self.tipo_de_operacion


class Interrogatorio(models.Model):

    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    # Sistema respiratorio

    respiratorio_disnea = models.BooleanField()
    respiratorio_dolor = models.BooleanField()
    respiratorio_tos = models.BooleanField()
    respiratorio_otros = models.BooleanField()
    respiratorio_hemoptisis = models.BooleanField()
    respiratorio_expectoracion = models.BooleanField()

    # Sistema Cardiovascular

    cardiovascular_disnea = models.BooleanField()
    cardiovascular_dolor = models.BooleanField()
    cardiovascular_tos = models.BooleanField()
    cardiovascular_cianosis = models.BooleanField()
    cardiovascular_claudicacion_intermitente = models.BooleanField()
    cardiovascular_palpitaciones = models.BooleanField()
    cardiovascular_otros = models.BooleanField()
    cardiovascular_apex_visible = models.BooleanField()
    cardiovascular_apex_palpable = models.BooleanField()
    cardiovascular_fremito = models.BooleanField()
    cardiovascular_percusion = models.BooleanField()
    cardiovascular_auscultacion_normal = models.BooleanField()
    cardiovascular_soplo_sistolico = models.BooleanField()
    cardiovascular_soplo_diastolico = models.BooleanField()
    cardiovascular_soplo_sisto_diastolico = models.BooleanField()
    cardiovascular_tono_normal = models.BooleanField()
    cardiovascular_tono_reforzado = models.BooleanField()
    cardiovascular_tono_desdoblamiento = models.BooleanField()
    cardiovascular_tonos = models.BooleanField()
    cardiovascular_pulsos_femorales = models.BooleanField()
    cardiovascular_pulsos_femorales_fuertes = models.BooleanField()
    cardiovascular_pulsos_femorales_debiles = models.BooleanField()
    cardiovascular_frecuencia_cardiaca = models.IntegerField()
    cardiovascular_llene_capilar_normal = models.BooleanField()
    cardiovascular_llene_capilar_lento = models.BooleanField()
    cardiovascular_tension_arterial = models.CharField(max_length=500)
    cardiovascular_percentiles = models.CharField(max_length=500)

    # Sistema urogenital

    urogenital_dolor = models.BooleanField()
    urogenital_orinas_turbias = models.BooleanField()
    urogenital_disuria = models.BooleanField()
    urogenital_hematuria = models.BooleanField()
    urogenital_polaquiluria = models.BooleanField()
    urogenital_impotencia = models.BooleanField()
    urogenital_calculos = models.BooleanField()
    urogenital_nicturias = models.BooleanField()
    urogenital_exudado_uretral = models.BooleanField()
    urogenital_retencion_urinaria = models.BooleanField()
    urogenital_incontinencia = models.BooleanField()
    urogenital_uretrorragia = models.BooleanField()
    urogenital_tumoracion = models.BooleanField()
    urogenital_otros = models.BooleanField()

    # Sistema neurologico

    neurologico_cefaleas = models.BooleanField()
    neurologico_vomitos = models.BooleanField()
    neurologico_vertigo = models.BooleanField()
    neurologico_convulsiones = models.BooleanField()
    neurologico_deficit_motor = models.BooleanField()
    neurologico_deficit_sensitivo = models.BooleanField()
    neurologico_alteracion_conciencia = models.BooleanField()
    neurologico_dolor_facial = models.BooleanField()
    neurologico_dolor_cervical = models.BooleanField()
    neurologico_dolor_lumbar = models.BooleanField()
    neurologico_alteracion_marcha = models.BooleanField()
    neurologico_alteracion_equilibrio = models.BooleanField()
    neurologico_alteracion_visual = models.BooleanField()
    neurologico_deficit_habla_entender = models.BooleanField()
    neurologico_conciencia_normal = models.BooleanField()
    neurologico_somnolencia = models.BooleanField()
    neurologico_coma = models.BooleanField()
    neurologico_grado = models.IntegerField()
    neurologico_postura_normal = models.BooleanField()
    neurologico_epistofanos = models.BooleanField()
    neurologico_movimientos_involuntarios = models.BooleanField()
    neurologico_reflejos_moro_presente = models.BooleanField()
    neurologico_prehension = models.BooleanField()
    neurologico_caminar = models.BooleanField()
    neurologico_tigidez_de_nuca = models.BooleanField()
    neurologico_signo_kemis = models.BooleanField()
    neurologico_signo_brudzinky = models.BooleanField()
    neurologico_trofismo_normal = models.BooleanField()
    neurologico_fuerza_muscular_normal = models.BooleanField()
    neurologico_tono_muzcular_normal = models.BooleanField()
    neurologico_reflejos_osteotendinosos_normales = models.BooleanField()
    neurologico_reflejos_superficiales_normales = models.BooleanField()
    neurologico_sensibilidad_normal = models.BooleanField()

    # Sistema Ginecologico

    ginecologico_menarquia_edad = models.IntegerField()
    ginecologico_menopausia_edad = models.IntegerField()
    ginecologico_formula_menstrual = models.CharField(max_length=200)
    ginecologico_fecha_ultima_menstruacion = models.DateField()
    ginecologico_primeras_relaciones_sexuales = models.IntegerField()
    ginecologico_hiperpolimenorrea = models.BooleanField()
    ginecologico_frigidez = models.BooleanField()
    ginecologico_dolor = models.BooleanField()
    ginecologico_leucorrea = models.BooleanField()
    ginecologico_dispareunia = models.BooleanField()
    ginecologico_numero_embarazos = models.IntegerField()
    ginecologico_numero_partos = models.IntegerField()
    ginecologico_numero_abortos = models.IntegerField()
    ginecologico_espontaneos = models.BooleanField()
    ginecologico_provocados = models.BooleanField()
    ginecologico_diu = models.BooleanField()
    ginecologico_oral = models.BooleanField()
    ginecologico_otros = models.BooleanField()
    ginecologico_numero_macrofetos = models.IntegerField()
    ginecologico_prueba_citologica = models.DateField()
    ginecologico_prueba_citologica_resultado = models.CharField(max_length=200)

    # sistema endocrino

    endocrino_hipofisis = models.BooleanField()
    endocrino_suprarrenal = models.BooleanField()
    endorrino_tiroides = models.BooleanField()
    ondocrino_ovarios = models.BooleanField()
    endocrino_paratiroides = models.BooleanField()
    endocrino_testiculos = models.BooleanField()
    endocrino_pancreas = models.BooleanField()
    endocrino_otros = models.BooleanField()

    # sistema genitourinario

    genitourinario_genitales_externos_normales = models.BooleanField()
    genitourinario_genitales_externos_anormales = models.BooleanField()
    genitourinario_hipospadia = models.BooleanField()
    genitourinario_hidrocele = models.BooleanField()
    genitourinario_fimosis = models.BooleanField()
    genitourinario_testiculos_descendidos = models.BooleanField()
    genitourinario_hernia_inguinal = models.BooleanField()
    genitourinario_tumoracion = models.BooleanField()
    genitourinario_rinones_palpables = models.BooleanField()
    genitourinario_rinones_nopalpables = models.BooleanField()
    genitourinario_rinones_putos_rinopieloureterales = models.BooleanField()
    genitourinario_rinones_dolorosos = models.BooleanField()
    genitourinario_rinones_nodolorsos = models.BooleanField()

    # sistema digestivo

    digestivo_formula_dentaria = QuillField()
    digestivo_encias_normales = models.BooleanField()
    digestivo_paladar_normal = models.BooleanField()
    digestivo_olivar = models.BooleanField()
    digestivo_fisura_palatina = models.BooleanField()
    digestivo_lengua_normal = models.BooleanField()
    digestivo_lengua_depapilada = models.BooleanField()
    digestivo_georafica = models.BooleanField()
    digestivo_caries_dentales = models.BooleanField()
    digestivo_deformidad_de_implantacion_de_dientes = models.BooleanField()
    digestivo_higado_borde_superior_en = QuillField()
    digestivo_higado_borde_inferior_no_rebasa = models.BooleanField()
    digestivo_higado_borde_inferior_rebasa = models.BooleanField()
    digestivo_higado_borde_inferior_rebasa_cm = models.IntegerField()
    digestivo_higado_consistencia = models.BooleanField()
    digestivo_ano_recto_normal = models.BooleanField()
    digestivo_ano_recto_fisura = models.BooleanField()
    digestivo_ano_recto_hemorroides = models.BooleanField()
    digestivo_ano_recto_endurecida = models.BooleanField()
    digestivo_ano_recto_prolapso_rectal = models.BooleanField()

    # Sistema Hemolinfopoyetico

    hemolinfop_adenopatinas_ausentes = models.BooleanField()
    hemolinfo_adenopatinas_presentes = models.BooleanField()
    hemolinfo_cervicales = models.BooleanField()
    hemolinfo_axilares = models.BooleanField()
    hemolinfo_retroauriculares = models.BooleanField()
    hemolinfo_inguinales = models.BooleanField()
    hemolinfo_bazo_palpable = models.BooleanField()
    hemolinfo_bazo_no_palpable = models.BooleanField()
    hemolinfo_bazo_percutible = models.BooleanField()
    hemolinfo_bazo_rebasa = models.BooleanField()
    hemolinfo_bazo_rebasa_cm = models.IntegerField()

    # Sistema Osteomioarticular

    osteo_articulaciones_normales = models.BooleanField()
    osteo_articulaciones_dolorosas = models.BooleanField()
    osteo_articulaciones_inflamadas = models.BooleanField()
    osteo_articulaciones_calientes = models.BooleanField()
    osteo_musculares_normal = models.BooleanField()
    osteo_musculares_no_lesiones_oseas = models.BooleanField()

    # Pares Craneales

    I_N = models.BooleanField()
    I_A = models.BooleanField()

    II_N = models.BooleanField()
    II_A = models.BooleanField()

    III_N = models.BooleanField()
    III_A = models.BooleanField()

    IV_N = models.BooleanField()
    IV_A = models.BooleanField()

    V_N = models.BooleanField()
    V_A = models.BooleanField()

    VI_N = models.BooleanField()
    VI_A = models.BooleanField()

    VII_N = models.BooleanField()
    VII_A = models.BooleanField()

    VIII_N = models.BooleanField()
    VIII_A = models.BooleanField()

    IX_N = models.BooleanField()
    IX_A = models.BooleanField()

    X_N = models.BooleanField()
    X_A = models.BooleanField()

    XI_N = models.BooleanField()
    XI_A = models.BooleanField()

    XII_N = models.BooleanField()
    XII_A = models.BooleanField()

    # otros_datos

    astenia = models.BooleanField()
    anorexia = models.BooleanField()
    epistaxis = models.BooleanField()
    fiebre = models.BooleanField()
    artralgia = models.BooleanField()
    polifagia = models.BooleanField()
    ederna = models.BooleanField()
    prurito = models.BooleanField()
    perdida_de_peso = models.BooleanField()
    ganancia_de_peso = models.BooleanField()
    croparentesias = models.BooleanField()
    otros = models.BooleanField()
    detallar_hallazgo_anormal = QuillField()

    # habitos toxicos

    fuma = models.BooleanField()
    exfumador = models.BooleanField()
    no_fuma = models.BooleanField()
    cantidad_fua = models.IntegerField()
    tiempo_fumando = models.IntegerField()
    alcohol_diario = models.BooleanField()
    alcohol_no = models.BooleanField()
    alcohol_ocasional = models.BooleanField()
    alcohol_semanal = models.BooleanField()
    toxicos_otros = QuillField()

    # datos

    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    sala = models.CharField(max_length=200)
    cama = models.CharField(max_length=200)
    servicio_de = models.CharField(max_length=200)
    medico_asistencia = models.CharField(max_length=200)

    def __str__(self):
        return self.medico_asistencia


class ExamenFisico(models.Model):

    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    # Examen Fisico General

    aspecto_del_paciente_normal = models.BooleanField()
    aspecto_del_paciente_decaido = models.BooleanField()
    aspecto_del_paciente_septico = models.BooleanField()
    aspecto_del_paciente_desnutrido = models.BooleanField()
    aspecto_del_paciente_grave = models.BooleanField()
    fascies_normal = models.BooleanField()
    fascies_anormal = models.BooleanField()
    temperatura = models.IntegerField()
    peso = models.FloatField()
    edad = models.IntegerField()
    talla = models.FloatField()
    c_cefalica = models.FloatField()
    c_torácica = models.FloatField()
    piel_normal = models.BooleanField()
    piel_livedo_recticularia = models.BooleanField()
    piel_palidez = models.BooleanField()
    piel_eritema = models.BooleanField()
    piel_trauma = models.BooleanField()
    piel_exantema = models.BooleanField()
    piel_pliegue = models.BooleanField()
    piel_nevos = models.BooleanField()
    piel_ictero = models.BooleanField()
    piel_clanosis = models.BooleanField()
    piel_hemorragia = models.BooleanField()
    piel_tcs = models.BooleanField()
    piel_infiltrado = models.BooleanField()
    piel_no_infiltrado = models.BooleanField()
    decubito = models.BooleanField()
    decubito_indiferente = models.BooleanField()
    decubito_obligado = models.BooleanField()

    hallazgo_anormal = QuillField()

    # Examen Físico sitema respiratorio

    orofaringe_normal = models.BooleanField()
    orofaringe_enrojecida = models.BooleanField()
    orofaringe_exudado = models.BooleanField()
    pulmones_normal = models.BooleanField()
    pulmones_tiraje = models.BooleanField()
    pulmones_disnea = models.BooleanField()
    pulmones_palpacion_normal = models.BooleanField()
    pulmones_palpacion_v_v_aumentadas = models.BooleanField()
    pulmones_palpacion_v_v_disminuidas = models.BooleanField()
    pulmones_palpacion_v_v_ausentes = models.BooleanField()
    pulmones_percusion_normal = models.BooleanField()
    pulmones_precusion_hipersonaridad = models.BooleanField()
    pulmones_percusion_matidez = models.BooleanField()
    pulmones_auscultacion_murmullo_vesicular_normal = models.BooleanField()
    pulmones_auscultacion_murmullo_vesicular_disminuido = models.BooleanField()
    pulmones_auscultacion_murmullo_vesicular_ruidos_transitorios = models.BooleanField()
    pulmones_estertores_roncos = models.BooleanField()
    pulmones_estertores_sibilantes = models.BooleanField()
    pulmones_estertores_sub_capilantes = models.BooleanField()
    pulmones_estertores_gruesos = models.BooleanField()
    pulmones_estertores_finos = models.BooleanField()
    pulmones_estertores_crepilantes = models.BooleanField()
    pulmones_estertores_soplo_tubario = models.BooleanField()
    pulmones_otoscopia_normal = models.BooleanField()
    pulmones_otoscopia_anormal = models.BooleanField()
    pulmones_nariz_epistaxis = models.BooleanField()
    pulmones_nariz_obstruccion = models.BooleanField()
    pulmones_nariz_otros = models.BooleanField()

    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    sala = models.CharField(max_length=200)
    cama = models.CharField(max_length=200)
    servicio_de = models.CharField(max_length=200)
    medico_asistencia = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.historia.id}-{self.historia.paciente.dni}"


class Antecedentes(models.Model):

    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    # Historia del embarazo parto y post natales

    embarazo_hipertension_arterial = models.BooleanField()
    embarazo_infeccion_urinaria = models.BooleanField()
    embarazo_enfermedad_venerea = models.BooleanField()
    embarazo_diabetes_melitus = models.BooleanField()
    embarazo_ingestion_medicamentos_droga_alcohol = models.BooleanField()
    embarazo_exposicion_rayos_x = models.BooleanField()
    embarazo_amenaza_de_aborto = models.BooleanField()
    embarazo_parto_prematuro = models.BooleanField()
    embarazo_ciur = models.BooleanField()

    numero_embarazos = models.IntegerField()
    numero_de_orden_de_este_embarazo = models.IntegerField()
    numero_de_abortos = models.IntegerField()
    abortos_provocados = models.IntegerField()

    duracion_del_embarazo_en_semanas = models.IntegerField()

    parto_normal = models.BooleanField()
    parto_instrumental = models.BooleanField()
    parto_cesarea = models.BooleanField()
    conteo_apgar_1_minuto = models.CharField(max_length=200)
    conteo_apgar_5_minuto = models.CharField(max_length=200)
    peso_al_nacer = models.FloatField()
    talla = models.FloatField()
    circunferencia_cefalica = models.FloatField()
    oxigenoterpia = models.BooleanField()
    rotura_de_membrana = models.BooleanField()
    uso_de_bicarbonato = models.BooleanField()
    cateter_umbilical = models.BooleanField()
    hospital_nacimiento = models.CharField(max_length=200)

    post_natales_bronco_aspiracion = models.BooleanField()
    post_natales_hipoglicemia = models.BooleanField()
    post_natales_sepsis_rn = models.BooleanField()
    post_natales_onfalitis = models.BooleanField()
    post_natales_tranfusion = models.BooleanField()
    post_natales_anemia = models.BooleanField()
    post_natales_memb_hilina = models.BooleanField()
    post_natales_t_obstetrico = models.BooleanField()
    post_natales_ictericia = models.BooleanField()
    post_natales_fototerapia = models.BooleanField()
    post_natales_trnferencia_sangre = models.BooleanField()
    post_natales_hemorragia = models.BooleanField()
    post_natales_hipotonia = models.BooleanField()

    post_natales_caida_del_cordon_umbilical = models.IntegerField()
    post_natales_dias_en_el_hospital_nino = models.IntegerField()
    post_natales_dias_en_el_hospital_madre = models.IntegerField()

    post_natales_lactancia_materna_inmediata = models.BooleanField()

    # Desarrollo Psicomotoro Y Adolescencia

    la_madre_piensa_que_ha_adquirido_habilidades_igual_que_otros_niños = (
        models.BooleanField()
    )
    sonrio_a_los = models.IntegerField()
    sostuvo_la_cabeza_a_los = models.IntegerField()
    se_sento_a_los = models.IntegerField()
    primeras_palabras_a_los = models.IntegerField()
    caimino_a_los = models.IntegerField()
    control_de_la_defecacion = models.IntegerField()
    control_vesical_nocturno = models.IntegerField()
    control_vesical_diurno = models.IntegerField()
    grado_escolar_actual = models.IntegerField()
    ha_perdido_grados = models.IntegerField()
    dificultades_escolares = models.BooleanField()
    fuma_cigarrillos = models.BooleanField()
    sin_llegar_a_repetir = models.BooleanField()
    ingiere_bebidas_alcoholicas = models.BooleanField()
    tiene_problemas_disciplina = models.BooleanField()
    edad_de_menarquia = models.IntegerField()
    practica_ejercicios_regularmente = models.BooleanField()
    antecedentes_de_pica = models.BooleanField()

    # Alimentacion

    recibio_lactancia_materna_exclusiva = models.BooleanField()
    durante = models.IntegerField()
    lactancia_artificial = models.BooleanField()
    tipo_de_leche = models.CharField(max_length=200)
    edad_del_destete_antes_del_mes = models.IntegerField()
    ablactacion_lactante_jugos = models.IntegerField()
    ablactacion_lactante_cereales = models.IntegerField()
    ablactacion_lactante_vianda = models.IntegerField()
    ablactacion_lactante_huevos = models.IntegerField()
    ablactacion_lactante_vegetales_verdes = models.IntegerField()
    ablactacion_lactante_carnes = models.IntegerField()
    ablactacion_lactante_pescados = models.IntegerField()
    ablactacion_lactante_quesos = models.IntegerField()
    ablactacion_lactante_legumi = models.IntegerField()

    tipo_de_leche_que_consume = models.CharField(max_length=200)
    cantidad_ingerida_diariamente_litros = models.IntegerField()

    ablactacion_mayor_jugos = models.IntegerField()
    ablactacion_mayor_cereales = models.IntegerField()
    ablactacion_mayor_vianda = models.IntegerField()
    ablactacion_mayor_huevos = models.IntegerField()
    ablactacion_mayor_vegetales_verdes = models.IntegerField()
    ablactacion_mayor_carnes = models.IntegerField()
    ablactacion_mayor_pescados = models.IntegerField()
    ablactacion_mayor_quesos = models.IntegerField()
    ablactacion_mayor_legumi = models.IntegerField()


class HistoriaSocioAmbiental(models.Model):

    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    madre_edad = models.IntegerField()
    madre_escolaridad = models.CharField(max_length=200)
    madre_ocupacion = models.CharField(max_length=200)

    padre_edad = models.IntegerField()
    padre_escolaridad = models.CharField(max_length=200)
    padre_ocupacion = models.CharField(max_length=200)

    el_nino_vive_con = models.CharField(max_length=200)
    padres_separados = models.BooleanField()
    el_nino_asiste_a = models.CharField(max_length=200)
    composicion_del_nucleo_familiar = models.CharField(max_length=200)
    numero_de_personas = models.IntegerField()
    vivienda = models.CharField(max_length=200)
    procedencia_del_agua = models.CharField(max_length=200)
    toma_el_agua_hervida = models.BooleanField()
    toma_el_agua_sin_hervir = models.BooleanField()
    servicio_sanitarios_interior_casa = models.BooleanField()
    servicio_sanitarios_fuera_casa = models.BooleanField()
    presencia_de_animales_en_la_vivienda = models.BooleanField()
    que_animales = QuillField()
    higiene_de_la_vivienda = models.CharField(max_length=200)
    higiene_de_la_personal = models.CharField(max_length=200)
    higiene_de_la_familiar = models.CharField(max_length=200)
    agentes_irritantes_en_la_vivienda = models.CharField(max_length=200)

    # Inmunizaciones

    bgg_primera_docis = models.BooleanField()
    bgg_dejo_huella = models.BooleanField()
    bgg_reactivacion_1ro = models.BooleanField()
    bgg_reactivacion_5to = models.BooleanField()
    antipoliomielitica_1ra = models.BooleanField()
    antipoliomielitica_2da = models.BooleanField()

    dpt_1ra = models.BooleanField()
    dpt_2da = models.BooleanField()
    dpt_3ra = models.BooleanField()
    dpt_reactivacion = models.BooleanField()

    hvb_1ra = models.BooleanField()
    hvb_2da = models.BooleanField()
    hvb_3ra = models.BooleanField()
    hvb_reactivacion = models.BooleanField()

    antimeningococcica_1ra = models.BooleanField()
    antimeningococcicab_2da = models.BooleanField()

    psr_unica = models.BooleanField()

    toxidetetanico_reactivacion = models.BooleanField()

    antifodica_1ra = models.BooleanField()
    antifodica_2da = models.BooleanField()
    antifodica_3ra = models.BooleanField()
    antifodica_reactivacion = models.BooleanField()

    otas_vacunas = QuillField()


class HojaDeEgreso(models.Model):

    historia = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    unidad = models.CharField(max_length=200)
    motivo_de_inreso = QuillField()
    resumen_sindromico = QuillField()
    resumen_examen_fisico = QuillField()
    tratamiento = QuillField()
    operaciones_completo = models.BooleanField()
    operaciones_incompleto = models.BooleanField()
    operaciones_no_practicado = models.BooleanField()
    evolucion_satisfactoria = models.BooleanField()
    evolucion_no_satisfactoria = models.BooleanField()
    evolucion_complicaciones = models.BooleanField()
    diagnostico_definitivo_egreso = QuillField()
    otros_diagnosticos = QuillField()

    resultado_curado = models.BooleanField()
    resultado_igual = models.BooleanField()
    resultado_sin_especificar = models.BooleanField()
    resultado_mejorado = models.BooleanField()
    resultado_empeorado = models.BooleanField()

    resultado_muerto_antes_48_horas = models.BooleanField()
    resultado_muerto_despues_48_horas = models.BooleanField()

    autopsia = models.BooleanField()

    observaciones = QuillField()

    fecha = models.DateTimeField()
    medico_que_da_el_alta = models.CharField(max_length=200)

    sala = models.CharField(max_length=200)
    servicio_de = models.CharField(max_length=200)
    medico_de_asistencia = models.CharField(max_length=200)