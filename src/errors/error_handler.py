from src.views.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequestError

def handle_errors(error: Exception) -> HttpResponse:
  if isinstance(error, HttpBadRequestError):
    return HttpResponse(status_code=error.status_code, body={
      'errors': [{
       'title': error.name,
       'detail': error.message
      }]
    })

  return HttpResponse(status_code=500, body={
    'errors': [{
      'title': 'Internal Server Error',
      'detail': str(error)
    }]
  })