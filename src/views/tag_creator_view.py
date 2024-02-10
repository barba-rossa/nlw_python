from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''
    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        #return business logic
        print(f"Creating tag for product code {product_code}")
        #return http response
        return HttpResponse(200, {"success": "success"})
