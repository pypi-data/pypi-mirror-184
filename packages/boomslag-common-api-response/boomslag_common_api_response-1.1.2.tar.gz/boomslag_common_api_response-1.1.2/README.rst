==================================
Boomslag Common API Response
==================================

To use the Boomslag Django API Response Views package, follow these steps:

#. Install the package in your Django project by running the following command:


    .. code-block:: python

        pip install boomslag-common-api-response


#. Add 'api_response' to your Django installed apps in your project's settings.py file:


    .. code-block:: python

        INSTALLED_APPS = [
            ...
            'boomslag_api_response',
        ]


#. In your Django views, import the BaseAPIView class from the package:


    .. code-block:: python

        from boomslag_api_response.views import BaseAPIView


#. Use the BaseAPIView class as the base class for your Django view. You can then use the following methods to send responses to the client:

    * `**send_response(data=None, status=status.HTTP_200_OK)**`: Sends a successful response to the client. The data parameter is optional and can be used to include additional data in the response. The status parameter can be used to specify the HTTP status code of the response.

    * `**send_error(error, status=status.HTTP_400_BAD_REQUEST)**`: Sends an error response to the client. The error parameter is required and should be a string describing the error. The status parameter can be used to specify the HTTP status code of the response.

**Here is an example view** that demonstrates how to use the BaseAPIView class:


    .. code-block:: python

        class HelloWorldView(BaseAPIView):
            def get(self, request, format=None):
                your_condition_here = True
                if your_condition_here:
                    dict = {'message':'Hello World!'}
                    return self.send_response(dict)
                else:
                    error_message = 'This is a custom error message. I am a String.'
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
        "data": "Hello World!"
    }

or

.. code-block:: python

    {
        "success": false,
        "data": "Hello Errors!"
    }

You can then use the success and data fields in the client to determine the outcome of the request and process the response accordingly.