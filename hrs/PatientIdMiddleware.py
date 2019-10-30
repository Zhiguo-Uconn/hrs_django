from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve


class PatientIdMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        print("------------\n")
        print(hasattr(request, 'pid'))
        if not hasattr(request, 'pid'):
            request._cached_pid = 0
        
        print(request.pid)
        print(resolve(request.path_info).url_name)
        
