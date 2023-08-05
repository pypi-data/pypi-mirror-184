from rest_framework.pagination import PageNumberPagination

# class CustomPagination(PageNumberPagination):
#     page_query_param = 'p'
#     page_size_query_param = 'page_size'

#     def __init__(self, page_size=None, max_page_size=None):
#         self.page_size = page_size
#         self.max_page_size = max_page_size

#     def paginate_data(self, data, request):
#         """
#         Paginate the data object and return the paginated data
#         """
#         self.page = request.query_params.get(self.page_query_param, 1)
#         self.page_size = request.query_params.get(self.page_size_query_param, self.page_size)
#         if self.page_size > self.max_page_size:
#             self.page_size = self.max_page_size

#         start_index = (self.page - 1) * self.page_size
#         end_index = start_index + self.page_size
#         paginated_data = data[start_index:end_index]
#         return paginated_data

class CustomPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'

    def __init__(self, page_size=None, max_page_size=None):
        self.page_size = page_size
        self.max_page_size = max_page_size

    def paginate_data(self, data, request):
        self.page = request.query_params.get(self.page_query_param, 1)
        self.page_size = self._get_page_size(request)
        return self.paginate_queryset(data, request)