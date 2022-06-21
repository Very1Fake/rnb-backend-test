from django.http import HttpResponse


def tokens_create(request):
    return HttpResponse("/tokens/create endpoint")


# TODO: Add pagination
def tokens_list(request):
    return HttpResponse("/tokens/list endpoint")


def tokens_total_supply(request):
    return HttpResponse("/tokens/total_supply endpoint")
