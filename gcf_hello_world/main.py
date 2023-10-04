import functions_framework

@functions_framework.http
def helloGET(request):
    print('Hello world')