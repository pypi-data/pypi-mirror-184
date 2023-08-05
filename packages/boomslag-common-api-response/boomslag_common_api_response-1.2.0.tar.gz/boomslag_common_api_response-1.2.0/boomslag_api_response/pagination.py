from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'

    def __init__(self, page_size=None, max_page_size=None):
        self.page_size = page_size
        self.max_page_size = max_page_size