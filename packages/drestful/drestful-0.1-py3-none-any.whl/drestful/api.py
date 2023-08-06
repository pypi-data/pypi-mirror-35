from django.shortcuts import HttpResponse, redirect
from django.views.generic.edit import View, ModelFormMixin, CreateView
import json


class JsonResponse(HttpResponse):
    def __init__(self, content, *args, **kwargs):
        if isinstance(content, (dict, list)):
            content = json.dumps(content)
        kwargs["content_type"] = "application/json"
        super().__init__(content, *args, **kwargs)


class JsonpResponse(HttpResponse):
    def __init__(self, content, callback_fn="callback", **kwargs):
        if isinstance(content, (dict, list)):
            content = json.dumps(content)

        content = "%s(%s)" % (callback_fn, content)
        super().__init__(content, **kwargs)


class DetailAPI(View):
    model = None
    list_display = ()
    default_filter = {}
    filter_fields = ()
    result_name = 'object'
    jsonp = None

    def get_list_display(self):
        return self.list_display

    def get_data(self, obj):
        res = {}

        for k in self.get_list_display():
            fn = None
            if isinstance(k, tuple) or isinstance(k, list):
                fn = k[1]
                k = k[0]

            if fn:
                res[k] = fn(obj)
            else:
                _v = getattr(obj, k, '')
                if not isinstance(_v, bool):
                    _v = str(_v)
                res[k] = _v

        return res

    def get_filter(self):
        _filter = self.default_filter.copy()
        for k in self.filter_fields:
            if k in self.request.GET:
                _v = self.request.GET.get(k)
                _filter[k] = None if _v == 'None' else _v

        return _filter

    def get_result(self):
        obj = self.model.objects.filter(**self.get_filter()).last()

        res = {
            self.result_name: self.get_data(obj)
        }

        return res

    def get(self, request):
        res = self.get_result()
        if self.jsonp:
            fn = request.GET.get(self.jsonp)
            if fn:
                return JsonpResponse(res, fn)

        return JsonResponse(res)


class ListAPI(DetailAPI):
    def get_result(self):
        object_list = self.model.objects.filter(**self.get_filter())
        res_list = []
        for obj in object_list:
            res_list.append(self.get_data(obj))

        res = {
            self.result_name: res_list
        }

        return res


class CreateAPI(View):
    model = None

    default_fields = {}
    fields = []

    def _clean_field(self, k):
        value = None
        if k in self.request.POST:
            value = self.request.POST.get(k)
        elif k in self.request.FILES:
            value = self.request.FILES.get(k)

        if value == 'None':
            value = None
        return value

    def get_create_data(self):
        res = self.default_fields.copy()

        for k in self.fields:
            if k in self.request.POST or k in self.request.FILES:
                clean_fn = getattr(self, 'clean_%s' % k, None)
                if callable(clean_fn):
                    res[k] = clean_fn()
                else:
                    res[k] = self._clean_field(k)

        return res

    def success(self):
        return JsonResponse({'msg': 'ok', 'id': self.object.pk})

    def failed(self):
        content = json.dumps({'msg': 'failed', 'err': str(self.error)})
        return JsonResponse(content)

    def post(self, request, **kwargs):
        data = self.get_create_data()

        try:
            self.object = self.model(**data)
            self.object.save()

        except Exception as e:
            #print('error', e)
            self.error = e
            return self.failed()

        return self.success()


class DeleteAPI(View):
    model = None
    filter_fields = []
    default_filter = {}

    def get_filter(self):
        _filter = self.default_filter.copy()
        for k in self.filter_fields:
            if k in self.request.POST:
                _v = self.request.POST.get(k)
                _filter[k] = None if _v == 'None' else _v

        return _filter

    def post(self, request):
        # print(request)
        _filter = self.get_filter()
        if _filter:
            object_list = self.model.objects.filter(**_filter).delete()
            # print(object_list)
        return JsonResponse({})
