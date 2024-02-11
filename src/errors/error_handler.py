from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessedEntityError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessedEntityError):
        # send to a logger
        # send a mail to the dev team
        return HttpResponse(
            status_code=422,
            body={
                "errors": [{"title": "Unprocessable Entity", "detail": error.message}]
            },
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [
                {
                    "title": "Internal Server Error",
                    "detail": (
                        str(error) if error else "An unexpected error occurred"
                    ),
                }
            ]
        },
    )
