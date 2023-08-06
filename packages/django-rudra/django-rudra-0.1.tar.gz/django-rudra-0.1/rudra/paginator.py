from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import QuerySet
from rest_framework.serializers import Serializer

class PaginatorService:

    def __init__(self, queryset: QuerySet, serializer: Serializer, serializer_context: dict = None, page: int=1, page_size: int=10, orphans: int=0):
        self.queryset = queryset
        self.serializer = serializer
        self.serializer_context = serializer_context
        self.page_size = page_size
        self.page = page
        self.orphans = orphans
        self.page_obj = None
    
    def get_page(self):
        if self.page_obj:
            return self.page_obj

        paginator = Paginator(self.queryset, self.page_size, orphans=self.orphans)
        try:
            page_obj = paginator.page(self.page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        self.page_obj = page_obj
        return self.page_obj
    
    def get_page_obj_list(self):
        return self.get_page().object_list
    
    def get_page_obj_list_count(self):
        return self.get_page().object_list.count()
    
    def has_next(self):
        return self.get_page().has_next()

    def pages(self):
        return self.get_page().paginator.num_pages
    
    def get_serialized_data(self):
        return self.serializer(self.get_page_obj_list(), many=True, context=self.serializer_context).data
    