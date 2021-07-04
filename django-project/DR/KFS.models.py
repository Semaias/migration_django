# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActiveCampaigns(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING, blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    contact_share = models.ForeignKey('Numbers', models.DO_NOTHING, db_column='contact_share', blank=True, null=True)
    name = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    media_id = models.CharField(max_length=255, blank=True, null=True)
    media_preview = models.TextField(blank=True, null=True)
    send_date = models.DateTimeField()
    last_sent = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_campaigns'


class ActiveCampaignsHasActiveContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    active_campaigns = models.ForeignKey(ActiveCampaigns, models.DO_NOTHING)
    active_contacts = models.ForeignKey('ActiveContacts', models.DO_NOTHING)
    sent = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_campaigns_has_active_contacts'


class ActiveCampaignsReport(models.Model):
    active_campaigns = models.ForeignKey(ActiveCampaigns, models.DO_NOTHING)
    total = models.IntegerField()
    date = models.DateField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active_campaigns_report'


class ActiveContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    categories = models.ForeignKey('Categories', models.DO_NOTHING, blank=True, null=True)
    companies = models.ForeignKey('Companies', models.DO_NOTHING)
    from_numbers = models.ForeignKey('Numbers', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    number = models.BigIntegerField()
    uploaded = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    sync = models.IntegerField(blank=True, null=True)
    date_sync = models.DateTimeField(blank=True, null=True)
    whats = models.IntegerField(blank=True, null=True)
    type_transaction = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'active_contacts'
        unique_together = (('companies', 'number'),)


class ActiveContactsHasCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    active_contacts = models.ForeignKey(ActiveContacts, models.DO_NOTHING)
    categories = models.ForeignKey('Categories', models.DO_NOTHING)
    created = models.DateTimeField()
    modififed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active_contacts_has_categories'


class Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    support = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AdminHasCompanies(models.Model):
    admin = models.ForeignKey(Admin, models.DO_NOTHING)
    companies = models.ForeignKey('Companies', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_has_companies'


class Answers(models.Model):
    id = models.BigAutoField(primary_key=True)
    questions = models.ForeignKey('Questions', models.DO_NOTHING)
    companies = models.ForeignKey('Companies', models.DO_NOTHING)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    calls = models.ForeignKey('Calls', models.DO_NOTHING)
    researches = models.ForeignKey('Researches', models.DO_NOTHING, blank=True, null=True)
    resposta = models.CharField(max_length=9)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    calls_researches = models.ForeignKey('CallsResearches', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class ArticleReadingControl(models.Model):
    id = models.BigAutoField(primary_key=True)
    articles = models.ForeignKey('Articles', models.DO_NOTHING)
    calls = models.ForeignKey('Calls', models.DO_NOTHING)
    send_article = models.DateTimeField()
    read_article = models.DateTimeField(blank=True, null=True)
    reading = models.IntegerField()
    view_count = models.IntegerField()
    ip_last_view = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'article_reading_control'


class Articles(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey('Companies', models.DO_NOTHING)
    title = models.CharField(max_length=255)
    content = models.TextField()
    send_time = models.DateTimeField()
    last_id = models.BigIntegerField()
    status = models.CharField(max_length=10, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'articles'


class AutoMessages(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    text = models.TextField()
    pos_text = models.TextField(blank=True, null=True)
    position = models.IntegerField()
    start = models.TimeField(blank=True, null=True)
    finish = models.TimeField(blank=True, null=True)
    active = models.IntegerField()
    old_number = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    already_client_text = models.TextField(blank=True, null=True)
    already_client_pos_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_messages'


class AutoMessagesStandards(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers_id = models.BigIntegerField()
    msg_not_horary = models.TextField()
    msg_close_calls = models.TextField()
    msg_close_calls_expired = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auto_messages_standards'


class BorisIntegrationPointer(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_event = models.DateField()
    cod_agenda = models.TextField()

    class Meta:
        managed = False
        db_table = 'boris_integration_pointer'


class Calls(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    name = models.TextField()
    jid = models.CharField(max_length=255)
    no_jid = models.CharField(max_length=255)
    photo = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sync = models.CharField(max_length=45)
    black_flag = models.IntegerField()
    pesquisa = models.DateField(blank=True, null=True)
    pesquisa_realizada = models.IntegerField()
    sync_google = models.IntegerField()
    contact_import_article = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    has_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calls'


class CallsResearches(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey('Companies', models.DO_NOTHING)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    research = models.ForeignKey('Researches', models.DO_NOTHING)
    call = models.ForeignKey(Calls, models.DO_NOTHING)
    history_calls = models.ForeignKey('HistoryCalls', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    date_send_searches = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=18)
    send = models.IntegerField()
    attempt = models.IntegerField()
    last_send = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    schedule = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls_researches'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    companies = models.ForeignKey('Companies', models.DO_NOTHING, blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Changelogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'changelogs'


class Companies(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    has_active = models.IntegerField()
    has_active_contacts = models.IntegerField()
    has_satisfacao = models.IntegerField()
    number_users = models.IntegerField(blank=True, null=True)
    old_number = models.BigIntegerField(blank=True, null=True)
    relatorio_totalizadores = models.TextField(blank=True, null=True)
    version = models.IntegerField()
    active = models.IntegerField()
    integrated_confirmations = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Confirmations(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    calls = models.ForeignKey(Calls, models.DO_NOTHING)
    uras_confirmations = models.ForeignKey('UrasConfirmations', models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    date_event = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=14)
    pre_calls_confirmation = models.ForeignKey('PreCallsConfirmation', models.DO_NOTHING, blank=True, null=True)
    last_send_integration = models.DateTimeField(blank=True, null=True)
    automatic_insert = models.IntegerField(blank=True, null=True)
    integrated = models.IntegerField()
    fail_integrate = models.IntegerField()
    result_integra = models.TextField(blank=True, null=True)
    error_integra = models.TextField(blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    send = models.IntegerField()
    last_send = models.DateTimeField(blank=True, null=True)
    researches = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confirmations'


class ConfirmationsAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    confirmations = models.ForeignKey(Confirmations, models.DO_NOTHING)
    attempts = models.IntegerField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confirmations_attempts'


class ContactsSendArticles(models.Model):
    id = models.BigAutoField(primary_key=True)
    calls = models.ForeignKey(Calls, models.DO_NOTHING)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contacts_send_articles'
        unique_together = (('calls', 'numbers'),)


class CreditHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    credit_plans = models.ForeignKey('CreditPlans', models.DO_NOTHING, blank=True, null=True)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING, blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)
    expired = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_histories'


class CreditPlans(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_plans'


class CrmVyttra(models.Model):
    id = models.BigAutoField(primary_key=True)
    history_calls = models.ForeignKey('HistoryCalls', models.DO_NOTHING)
    crm_vyttra_reasons = models.ForeignKey('CrmVyttraReasons', models.DO_NOTHING)
    client = models.CharField(max_length=18)
    initial_status = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    ocurrence = models.CharField(max_length=40)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'crm_vyttra'


class CrmVyttraReasons(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason = models.CharField(max_length=100)
    option = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'crm_vyttra_reasons'


class Days(models.Model):
    id = models.BigAutoField(primary_key=True)
    times = models.ForeignKey('Times', models.DO_NOTHING)
    day = models.IntegerField()
    created = models.DateTimeField()
    modififed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'days'


class Doctors(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'doctors'


class EventPatterns(models.Model):
    event = models.CharField(max_length=255)
    interval = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event_patterns'


class EventPatternsInNumbers(models.Model):
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    event_patterns = models.ForeignKey(EventPatterns, models.DO_NOTHING)
    time_last = models.DateTimeField()
    data_serve = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'event_patterns_in_numbers'
        unique_together = (('numbers', 'event_patterns'),)


class EventosControl(models.Model):
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    event = models.CharField(max_length=255)
    time_last = models.DateTimeField()
    interval = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eventos_control'


class HistoryCalls(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.ForeignKey('Numbers', models.DO_NOTHING, blank=True, null=True)
    calls = models.ForeignKey(Calls, models.DO_NOTHING)
    last_history_calls = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    uras = models.ForeignKey('Uras', models.DO_NOTHING, blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    last_users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    confirmations = models.ForeignKey(Confirmations, models.DO_NOTHING, blank=True, null=True)
    calls_researches = models.ForeignKey(CallsResearches, models.DO_NOTHING, blank=True, null=True)
    researches = models.ForeignKey('Researches', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=255)
    satisfacao = models.CharField(max_length=45)
    old_number = models.BigIntegerField(blank=True, null=True)
    type_calls = models.CharField(max_length=8)
    ura_start = models.DateTimeField(blank=True, null=True)
    call_start = models.DateTimeField(blank=True, null=True)
    call_end = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    mod_padrao_ans_val = models.CharField(max_length=255, blank=True, null=True)
    massively_closed = models.IntegerField(blank=True, null=True)
    finished_by_inactivity = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history_calls'


class HistoryCallsCustomFields(models.Model):
    id = models.BigAutoField(primary_key=True)
    history_calls = models.ForeignKey(HistoryCalls, models.DO_NOTHING)
    field_name = models.CharField(max_length=255)
    field_value = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history_calls_custom_fields'


class HistoryCallsSatisfacao(models.Model):
    id = models.BigAutoField(primary_key=True)
    history_calls = models.ForeignKey(HistoryCalls, models.DO_NOTHING)
    satisfacao = models.ForeignKey('Satisfacao', models.DO_NOTHING)
    answer = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history_calls_satisfacao'


class HistoryCallsTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    history_calls = models.ForeignKey(HistoryCalls, models.DO_NOTHING)
    tags = models.ForeignKey('Tags', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history_calls_tags'


class ImportBank(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    import_field = models.IntegerField(db_column='import')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'import_bank'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=64)
    parameters = models.TextField()
    content = models.TextField()
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    finished = models.IntegerField()
    executions = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class LogNumbers(models.Model):
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    users_id = models.BigIntegerField(blank=True, null=True)
    history_calls_id = models.BigIntegerField(blank=True, null=True)
    event = models.CharField(max_length=255)
    user_log = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_numbers'


class MessageMediaHash(models.Model):
    id = models.BigAutoField(primary_key=True)
    messages = models.ForeignKey('Messages', models.DO_NOTHING)
    remote_media_hash = models.CharField(max_length=32, blank=True, null=True)
    media_hash = models.CharField(unique=True, max_length=32, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_media_hash'


class Messages(models.Model):
    id = models.BigAutoField(primary_key=True)
    history_calls = models.ForeignKey(HistoryCalls, models.DO_NOTHING)
    users_id = models.BigIntegerField(blank=True, null=True)
    whats_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    message = models.TextField()
    sent_read = models.IntegerField()
    md5_img = models.CharField(max_length=32, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class MessagesConfirmations(models.Model):
    id = models.BigAutoField(primary_key=True)
    confirmations = models.ForeignKey(Confirmations, models.DO_NOTHING)
    message = models.TextField()
    origin = models.CharField(max_length=255)
    sent_read = models.IntegerField()
    whats_id = models.CharField(max_length=255)
    type = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages_confirmations'


class Modules(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modules'


class ModulesHasCompanies(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    modules = models.ForeignKey(Modules, models.DO_NOTHING)
    created = models.DateTimeField()
    modififed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modules_has_companies'


class Montecristo(models.Model):
    base = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'montecristo'


class Negociacoes(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey('Numbers', models.DO_NOTHING)
    products = models.ForeignKey('Products', models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    status = models.CharField(max_length=45)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    calls = models.ForeignKey(Calls, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'negociacoes'


class NegociacoesStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    negociacoes = models.ForeignKey(Negociacoes, models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    log = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    field_field = models.IntegerField(db_column='=')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'negociacoes_status'


class Numbers(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    active = models.IntegerField()
    name = models.CharField(max_length=255)
    number = models.BigIntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    machine = models.BigIntegerField(blank=True, null=True)
    device_uuid = models.CharField(max_length=64, blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)
    credits_prepaid = models.BigIntegerField(blank=True, null=True)
    credit_plans = models.ForeignKey(CreditPlans, models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=255)
    first_login = models.IntegerField()
    profile = models.TextField(blank=True, null=True)
    profile_updated = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    status_updated = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=6, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    share_contacts = models.IntegerField()
    prompt = models.IntegerField()
    is_satisfacao = models.IntegerField(blank=True, null=True)
    satisfacao_number = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    old_number = models.ForeignKey('self', models.DO_NOTHING, db_column='old_number', blank=True, null=True)
    is_active = models.IntegerField()
    main_number = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    main_number_0 = models.CharField(db_column='main_number', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    url_socket = models.CharField(max_length=100)
    ip_socket = models.CharField(max_length=25, blank=True, null=True)
    porta_socket = models.CharField(max_length=25, blank=True, null=True)
    new_call_module = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    close_call_limit = models.IntegerField(blank=True, null=True)
    confirmation_sendtime = models.IntegerField()
    emojis_enabled = models.IntegerField()
    mandatory_tags = models.IntegerField()
    allow_operator_view_credits = models.IntegerField()
    allow_operator_view_history = models.IntegerField()
    show_name_in_title = models.IntegerField()
    confirmation_attempts = models.IntegerField()
    confirmation_interval = models.IntegerField()
    confirm_only_at_business_days = models.IntegerField()
    confirm_early_at_thursday = models.IntegerField()
    dont_close_hcs_on_weekends = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'numbers'


class NumbersFosters(models.Model):
    number_adopted = models.CharField(max_length=30)
    number_active = models.CharField(max_length=255, blank=True, null=True)
    number_passive = models.CharField(max_length=30)
    date_call = models.DateField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'numbers_fosters'


class NumbersInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    contacts_total = models.IntegerField(blank=True, null=True)
    contacts_total_last = models.IntegerField(blank=True, null=True)
    wa_version = models.CharField(max_length=255, blank=True, null=True)
    os_version = models.CharField(max_length=10, blank=True, null=True)
    device_manufacturer = models.CharField(max_length=255, blank=True, null=True)
    device_model = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numbers_info'


class Phinxlog(models.Model):
    version = models.BigIntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'phinxlog'


class PreCallsConfirmation(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    identifier_a = models.CharField(max_length=255, blank=True, null=True)
    identifier_b = models.CharField(max_length=255, blank=True, null=True)
    identifier_c = models.CharField(max_length=255, blank=True, null=True)
    identifier_d = models.CharField(max_length=255, blank=True, null=True)
    name_contact = models.CharField(max_length=255)
    name_store = models.CharField(max_length=25, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    number_store = models.CharField(max_length=25, blank=True, null=True)
    number_alternative = models.CharField(max_length=20, blank=True, null=True)
    number_alternative_store = models.CharField(max_length=25, blank=True, null=True)
    number_whats = models.CharField(max_length=25, blank=True, null=True)
    sync = models.IntegerField(blank=True, null=True)
    date_sync = models.DateTimeField(blank=True, null=True)
    check_whats = models.IntegerField()
    whats = models.IntegerField()
    date_event = models.DateField()
    time_event = models.DateTimeField(blank=True, null=True)
    text_attached = models.TextField()
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING, blank=True, null=True)
    numbers_number = models.CharField(max_length=20, blank=True, null=True)
    type_transaction = models.CharField(max_length=12, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pre_calls_confirmation'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    image = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    old_number = models.ForeignKey(Numbers, models.DO_NOTHING, db_column='old_number', blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    researches = models.ForeignKey('Researches', models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    pergunta = models.TextField()
    ordem = models.IntegerField()
    active = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'questions'


class QuickAnswers(models.Model):
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    quick_answers_groups = models.ForeignKey('QuickAnswersGroups', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    modified = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quick_answers'


class QuickAnswersGroups(models.Model):
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'quick_answers_groups'


class Reminders(models.Model):
    id = models.BigAutoField(primary_key=True)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    calls = models.ForeignKey(Calls, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()
    data = models.DateTimeField()
    complete = models.IntegerField()
    old_number = models.ForeignKey(Numbers, models.DO_NOTHING, db_column='old_number', blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reminders'


class Researches(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    msg_padrao_inicial = models.TextField()
    msg_padrao_fim = models.TextField()
    default_confirm = models.IntegerField()
    active = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    send_on_close = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'researches'


class Satisfacao(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    type = models.CharField(max_length=45)
    text = models.TextField()
    position = models.IntegerField()
    condicao = models.CharField(max_length=45, blank=True, null=True)
    encerrar = models.IntegerField()
    follow = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'satisfacao'


class SatisfacaoOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    satisfacao = models.ForeignKey(Satisfacao, models.DO_NOTHING)
    value = models.CharField(max_length=255)
    position = models.IntegerField()
    follow = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'satisfacao_options'


class Scripts(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    image = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scripts'


class SessionPatternsTime(models.Model):
    minutes = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'session_patterns_time'


class StatusNumberControl(models.Model):
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    date_off = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status_number_control'


class SyonetConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    numbers = models.OneToOneField(Numbers, models.DO_NOTHING)
    url_full = models.CharField(max_length=255)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    dominio = models.CharField(max_length=50)
    grupo_evento = models.CharField(max_length=50)
    tipo_evento = models.CharField(max_length=50)
    origem = models.CharField(max_length=50)
    midia = models.CharField(max_length=50)
    assunto = models.CharField(max_length=50)
    id_empresa = models.CharField(max_length=15)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'syonet_config'


class SyonetSend(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    calls = models.ForeignKey(Calls, models.DO_NOTHING)
    history_calls = models.ForeignKey(HistoryCalls, models.DO_NOTHING)
    email = models.CharField(max_length=255, blank=True, null=True)
    data_syonet_send = models.TextField(blank=True, null=True)
    return_syonet = models.TextField(blank=True, null=True)
    send = models.IntegerField()
    users_syonet_cod = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'syonet_send'


class SyonetUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    syonet_cod = models.IntegerField()
    user_syonet = models.CharField(max_length=255)
    companie_syonet = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'syonet_users'


class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField()
    modififed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class Tickets(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    closed = models.IntegerField()
    uniqid = models.CharField(max_length=255, blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class TicketsFiles(models.Model):
    name = models.CharField(max_length=255)
    tickets = models.ForeignKey(Tickets, models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tickets_files'


class TicketsResponses(models.Model):
    content = models.TextField()
    tickets = models.ForeignKey(Tickets, models.DO_NOTHING)
    admin = models.ForeignKey(Admin, models.DO_NOTHING, blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tickets_responses'


class Times(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    start = models.TimeField()
    finish = models.TimeField()
    old_number = models.ForeignKey(Numbers, models.DO_NOTHING, db_column='old_number', blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'times'


class Uras(models.Model):
    id = models.BigAutoField(primary_key=True)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    uras = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    auto_message = models.TextField(blank=True, null=True)
    position = models.IntegerField()
    old_number = models.ForeignKey(Numbers, models.DO_NOTHING, db_column='old_number', blank=True, null=True)
    created = models.DateTimeField()
    modififed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uras'


class UrasConfirmations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    auto_message_yes = models.TextField()
    auto_message_no = models.TextField(blank=True, null=True)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    direct = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'uras_confirmations'


class UrasDaysOff(models.Model):
    name = models.CharField(max_length=100)
    uras = models.ForeignKey(Uras, models.DO_NOTHING)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'uras_days_off'


class UrasHasUsers(models.Model):
    uras = models.OneToOneField(Uras, models.DO_NOTHING, primary_key=True)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uras_has_users'
        unique_together = (('uras', 'users'),)


class UrasTimes(models.Model):
    uras = models.ForeignKey(Uras, models.DO_NOTHING, blank=True, null=True)
    weekday = models.IntegerField()
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'uras_times'


class UserActivities(models.Model):
    session_patterns_time = models.ForeignKey(SessionPatternsTime, models.DO_NOTHING)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    users = models.ForeignKey('Users', models.DO_NOTHING)
    time_serve = models.DateTimeField(blank=True, null=True)
    time_last = models.DateTimeField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_activities'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    superadmin = models.IntegerField()
    admin = models.IntegerField()
    supervisor = models.IntegerField()
    operador = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    last_number = models.ForeignKey(Numbers, models.DO_NOTHING, blank=True, null=True)
    old_number = models.ForeignKey(Numbers, models.DO_NOTHING, db_column='old_number', blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersHasNumbers(models.Model):
    users = models.OneToOneField(Users, models.DO_NOTHING, primary_key=True)
    numbers = models.ForeignKey(Numbers, models.DO_NOTHING)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_has_numbers'
        unique_together = (('users', 'numbers'),)


class Whatsmigrations(models.Model):
    version = models.BigIntegerField(primary_key=True)
    migration_name = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    breakpoint = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'whatsmigrations'
