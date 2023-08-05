from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import APIResponseSerializer
from .pagination import CustomPagination

def paginate_queryset(queryset, paginator_class, request, serializer_class, context=None, **kwargs):
    paginator = paginator_class(**kwargs)
    results = paginator.paginate_queryset(queryset, request)
    serializer = serializer_class(results, many=True, context=context)
    return paginator.get_paginated_response(serializer.data)


class BaseAPIView(APIView):
    def send_response(self, data=None, status=status.HTTP_200_OK):
        serializer = APIResponseSerializer({
            'success': True,
            'status': status,
            'data': data
        })
        return Response(serializer.data, status=status)

    def send_error(self, error, status=status.HTTP_400_BAD_REQUEST):
        serializer = APIResponseSerializer({
            'success': False,
            'status': status,
            'error': error
        })
        return Response(serializer.data, status=status)



class StandardAPIView(BaseAPIView):
    pagination_class = CustomPagination

    def send_paginated_response(self, data, status=status.HTTP_200_OK, next_url=None, previous_url=None, count=None):
        serializer = APIResponseSerializer({
            'success': True,
            'status': status,
            'next': next_url,
            'previous': previous_url,
            'count': count,
            'data': data
        })
        return Response(serializer.data, status=status)

    def paginate_data(self, data, request):
        paginator = self.pagination_class()
        paginated_data = paginator.paginate_data(data, request)
        return self.send_paginated_response(
            data=paginated_data.data,
            next_url=paginated_data.get('next'),
            previous_url=paginated_data.get('previous'),
            count=paginated_data.count
        )


# ============= Demo Views ============= #

class HelloWorldView(BaseAPIView):
    def get(self, request, format=None):
        your_condition_here = True
        if your_condition_here:
            dict = {'message':'Hello World!'}
            return self.send_response(dict,status=status.HTTP_201_CREATED)
        else:
            error_message = 'This is a custom error message. I am a String.'
            return self.send_error(error_message)


class HelloWorldViewFakeData(BaseAPIView):
    fake_data = [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Jane'},
        {'id': 3, 'name': 'Bob'},
        {'id': 4, 'name': 'Alice'},
        {'id': 5, 'name': 'Eve'},
    ]

    def get(self, request, format=None):
        return self.send_response(self.fake_data)


class MyPaginatedView(StandardAPIView):
    def get(self, request):
        data = [
            {'id': 1, 'content': 'Hello'},
            {'id': 2, 'content': 'World'},
            {'id': 3, 'content': 'This'},
            {'id': 4, 'content': 'Is'},
            {'id': 5, 'content': 'A'},
            {'id': 6, 'content': 'Paginated'},
            {'id': 7, 'content': 'Response'},
        ]
        # data = get_data()  # Replace this with your own data
        return self.paginate_data(data, request)

# class HelloWorldPaginatedView(StandardAPIView):
#     def get(self, request, format=None):
#         data = [
#             {'id': 1, 'content': 'Hello'},
#             {'id': 2, 'content': 'World'},
#             {'id': 3, 'content': 'This'},
#             {'id': 4, 'content': 'Is'},
#             {'id': 5, 'content': 'A'},
#             {'id': 6, 'content': 'Paginated'},
#             {'id': 7, 'content': 'Response'},
#         ]
#         if data:
#             return self.paginate_data(data, request, page_size=3, max_page_size=5)
#         else:
#             return self.send_error('No data found')


# class HelloWorldObjectPaginatedView(StandardAPIView):
#     def get(self, request, format=None):
#         courses = Courses.objects.all()
#         if courses:
#             serializer_class = CourseSerializer
#             return self.paginate_data(courses, request, serializer_class)
#         else:
#             return self.send_error('No data found')