=========================================
Django Rest Framework Common API Response
=========================================

To use the Boomslag Django API Response Views package, follow these steps:

#. Step 1. Install the package in your Django project by running the following command:


    .. code-block:: python

        pip install djangorestframework-api-response


#. Step 2. Add 'api_response' to your Django installed apps in your project's settings.py file:


    .. code-block:: python

        INSTALLED_APPS = [
            ...
            'rest_framework_common_api',
        ]


#. Step 3. In your Django views, import the BaseAPIView class from the package:


    .. code-block:: python

        from rest_framework_common_api.views import BaseAPIView


#. Step 4. Use the BaseAPIView class as the base class for your Django view. You can then use the following methods to send responses to the client:
    Helper Functions
    ================

    * `**send_response(data=None, status=status.HTTP_200_OK)**`: Sends a successful response to the client. The data parameter is optional and can be used to include additional data in the response. The status parameter can be used to specify the HTTP status code of the response.

    * `**send_error(error, status=status.HTTP_400_BAD_REQUEST)**`: Sends an error response to the client. The error parameter is required and should be a string describing the error. The status parameter can be used to specify the HTTP status code of the response.


Example Views
**************

**Here is an example view** that demonstrates how to use the BaseAPIView class:


    .. code-block:: python

        class HelloWorldView(BaseAPIView):
            def get(self, request, format=None):
                your_condition_here = True
                if your_condition_here:
                    dict = {'message':'Hello World!'}
                    return self.send_response(dict)
                else:
                    error_message = 'This is a custom error message.'
                    return self.send_error(error_message)


**Here is an example view** that demonstrates how to use the BaseAPIView class with a *custom success status code*:


    .. code-block:: python

        class HelloWorldView(BaseAPIView):
            def get(self, request, format=None):
                your_condition_here = True
                if your_condition_here:
                    dict = {'message':'Hello World!'}
                    return self.send_response(dict,status=status.HTTP_201_CREATED)
                else:
                    error_message = 'This is a custom error message. I am a String.'
                    return self.send_error(error_message)


When the client sends a request with the success parameter set to true, this view will send a successful response with the message "Hello World!". Otherwise, it will send an error response with the message "Hello Errors!".

The response sent to the client will have the following format:

.. code-block:: python

    {
        "success": true,
        "status": "200"
        "data": {
            "message": "Hello World!"
        },
    }

or

.. code-block:: python

    {
        "success": false,
        "status": "400",
        "error": "This is a custom error message. I am a String."
    }

You can then use the success and data fields in the client to determine the outcome of the request and process the response accordingly.

Paginated Views
****************

To use StandardAPIView, simply inherit it in your view class. You can then use the paginate_data method to easily paginate any data object and return the paginated response.

*Here is an example view* that demonstrates how to use the StandardAPIView class that returns a paginated response:

    .. code-block:: python

        class HelloWorldObjectPaginatedView(StandardAPIView):
            def get(self, request, format=None):
                # Retrieve your data object
                data = MyModel.objects.all()

                # Use the paginate_data method to paginate and return the response
                if data:
                    return self.paginate_data(data, request, serializer_class=MyDataSerializer, page_size=3, max_page_size=5)
                else:
                    return self.send_error('No data found', status=status.HTTP_404_NOT_FOUND)


The response will be a paginated list of courses, with the pagination metadata included in the response. The pagination metadata will include the current page number, the number of results per page, the total number of results, and the total number of pages. For example, if there are 10 courses in total and the page size is 3, the response will include metadata indicating that there are a total of 4 pages, with the first page containing the first 3 courses and the second page containing the next 3 courses, and so on. The data for each course will be included in the 'results' field of the response.

Here is an example of what the response might look like:

    .. code-block:: python

        {
            "count": 10,
            "next": "http://example.com/api/courses?page=2",
            "previous": null,
            "results": [
            {
                "id": 1,
                "name": "Introduction to Python",
                "description": "Learn the basics of Python programming"
            },
            {
                "id": 2,
                "name": "Advanced Python Techniques",
                "description": "Learn advanced techniques for Python programming"
            },
            {
                "id": 3,
                "name": "Data Science with Python",
                "description": "Learn how to use Python for data analysis and visualization"
            }
            ]
        }


To use the StandardAPIView, you will need to subclass it and override the 'paginate_data' method. This method should accept the data object that you want to paginate as well as the request object, and it should return a paginated response. You can customize the pagination behavior by passing additional arguments to the 'paginate_data' method, such as the page size and maximum page size. You can also pass a serializer class to the 'paginate_data' method if you want to serialize the data object before paginating.

    .. code-block:: python

        class StandardAPIView(BaseAPIView):
            pagination_class = CustomPagination

            def paginate_data(self, data, request, serializer_class=None, context=None, **kwargs):
                # Create a paginator instance
                paginator = self.pagination_class(**kwargs)

                # Paginate the data object and return the paginated response
                paginated_data = paginator.paginate_data(data, request)
                if serializer_class:
                    serializer = serializer_class(paginated_data, many=True, context=context)
                    paginated_data = serializer.data

                # Include the count, next, and previous fields in the response
                response = paginator.get_paginated_response(paginated_data)
                response['count'] = paginator.count
                response['next'] = paginator.get_next_link()
                response['previous'] = paginator.get_previous_link()

                return response


Then we can use the StandardAPIView like in the above example:

    .. code-block:: python

        class HelloWorldObjectPaginatedView(StandardAPIView):
            def get(self, request, format=None):
                courses = Courses.objects.all()
                if courses:
                    return self.paginate_data(courses, request, CourseSerializer, page_size=3, max_page_size=5)
                else:
                    return self.send_error('No data found')


The response to the request made to the HelloWorldObjectPaginatedView would be a paginated JSON object containing a list of serialized course objects. The paginated response would include metadata about the pagination, such as the current page, the number of pages, the number of results per page, and the total number of results. The structure of the response would look like this:


    .. code-block:: python


        {
            "count": 6,
            "next": "http://example.com/api/courses?page=2",
            "previous": null,
            "results": [
            {
                "id": 1,
                "name": "Course 1",
                "description": "This is the first course",
                "instructor": "John Smith"
            },
            {
                "id": 2,
                "name": "Course 2",
                "description": "This is the second course",
                "instructor": "Jane Doe"
            },
            {
                "id": 3,
                "name": "Course 3",
                "description": "This is the third course",
                "instructor": "Bob Smith"
            }
            ]
        }