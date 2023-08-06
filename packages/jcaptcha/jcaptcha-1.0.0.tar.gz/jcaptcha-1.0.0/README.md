# jcaptcha
```
def create_code(request):
    text, result, file_path, image_data = jcaptcha()
    request.session['v_code'] = result
    return HttpResponse(image_data, content_type="image/png")

```