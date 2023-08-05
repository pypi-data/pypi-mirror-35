

from json import JSONEncoder

from django.db.models import QuerySet, Model
from django.utils.module_loading import import_string
from rest_framework import serializers


class DefaultModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        exclude = []


class ZmeiReactJsonEncoder(JSONEncoder):
    def __init__(self, *, view=None, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False,
                 indent=None, separators=None, default=None):
        super().__init__(skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular,
                         allow_nan=allow_nan, sort_keys=sort_keys, indent=indent, separators=separators,
                         default=default)
        if not view:
            raise AttributeError('ZmeiReactJsonEncoder: View is required')
        self.view = view

        self.serializers_cache = {}

    def create_default_serializer(self, model):
        serializer = type('_', (DefaultModelSerializer,), {})
        serializer.Meta.model = model

        return serializer

    def get_model_serializer(self, model):
        if model in self.serializers_cache:
            return self.serializers_cache[model]

        serializer = None
        try:
            index_import_path = f"{'.'.join(model.__module__.split('.')[:-1])}.serializers.index"
            serializer_index = import_string(index_import_path)

            if model in serializer_index:
                serializer = serializer_index[model].get('_')
        except ImportError:
            pass

        if not serializer:
            serializer = self.create_default_serializer(model)

        self.serializers_cache[model] = serializer

        return serializer

    def default(self, o):
        # url object
        if hasattr(o, '__name__') and o.__name__ == 'url':
            return self.view.kwargs

        if isinstance(o, QuerySet):
            serializer = self.get_model_serializer(o.model)
            return serializer(o, many=True).data

        if isinstance(o, Model):
            serializer = self.get_model_serializer(o)
            return serializer(o).data

        print(f'WARN: ZmeiReactJsonEncoder -> Do not know how to encode "{o.__class__}"', o)
        return None
