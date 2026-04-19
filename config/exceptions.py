from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import exception_handler


def custom_exception_handler(get_response):

    def middleware(request):

        try:
            response = get_response(request)
            return response

        except ValueError as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )

        except PermissionDenied as e:
            return JsonResponse(
                {"error": str(e)},
                status=403
            )

        except ObjectDoesNotExist:
            return JsonResponse(
                {"error": "Object not found"},
                status=404
            )

        except IntegrityError:
            return JsonResponse(
                {"error": "Database integrity error"},
                status=400
            )

        except Exception:
            return JsonResponse(
                {"error": "Internal server error"},
                status=500
            )

    return middleware
    
def drf_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "status": "error",
            "errors": response.data
        }

    return response