from django.contrib import admin
from .models import UserProfile, Product, Question, Invoice, InvoiceItems, Result, Subscription


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ('user', 'username', 'type')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'type', 'category', 'cost')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    raw_id_fields = ['updated_by']
    list_display = ('updated_by', 'question', 'option')


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ('userprofile', 'updated_by')
    list_display = ('userprofile', 'amount', 'balance', 'updated_by')


@admin.register(InvoiceItems)
class InvoiceItemsAdmin(admin.ModelAdmin):
    raw_id_fields = ('product', 'invoice')
    list_display = ('product', 'invoice', 'amount', 'balance', 'discount', 'cgst', 'sgst', 'igst')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    raw_id_fields = ('product', 'userprofile')
    list_display = ('userprofile', 'product', 'score')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    raw_id_fields = ('userprofile', 'updated_by')
    list_display = ('userprofile', 'start_date', 'end_date', 'updated_by')
