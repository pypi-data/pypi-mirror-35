"""Relation viewset."""
from itertools import zip_longest

from django.db import IntegrityError

from rest_framework import exceptions, permissions, status, viewsets
from rest_framework.response import Response

from resolwe.flow.filters import RelationFilter
from resolwe.flow.models import Relation
from resolwe.flow.models.entity import RelationType
from resolwe.flow.serializers import RelationSerializer


class RelationViewSet(viewsets.ModelViewSet):
    """API view for :class:`Relation` objects."""

    queryset = Relation.objects.all().prefetch_related('contributor')
    serializer_class = RelationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = RelationFilter
    ordering_fields = ('id', 'created', 'modified')
    ordering = ('id',)

    def _filter_queryset(self, queryset):
        """Filter queryset by entity, label and position.

        Due to a bug in django-filter these filters have to be applied
        manually:
        https://github.com/carltongibson/django-filter/issues/883
        """
        entities = self.request.query_params.getlist('entity')
        labels = self.request.query_params.getlist('label')
        positions = self.request.query_params.getlist('position')

        if labels and len(labels) != len(entities):
            raise exceptions.ParseError(
                'If `labels` query parameter is given, also `entities` '
                'must be given and they must be of the same length.'
            )

        if positions and len(positions) != len(entities):
            raise exceptions.ParseError(
                'If `positions` query parameter is given, also `entities` '
                'must be given and they must be of the same length.'
            )

        if entities:
            for entity, label, position in zip_longest(entities, labels, positions):
                filter_params = {'entities__pk': entity}
                if label:
                    filter_params['relationpartition__label'] = label
                if position:
                    filter_params['relationpartition__position'] = position

                queryset = queryset.filter(**filter_params)

        return queryset

    def get_queryset(self):
        """Get queryset and perform custom filtering."""
        return self._filter_queryset(self.queryset)

    def create(self, request, *args, **kwargs):
        """Create a resource."""
        user = request.user
        if not user.is_authenticated:
            raise exceptions.NotFound

        relation_type = request.data.get('type')
        if not relation_type:
            return Response({'type': ['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)

        rel_type_query = RelationType.objects.filter(name=relation_type)
        try:
            request.data['type'] = rel_type_query.last().pk
        except RelationType.DoesNotExist:
            return Response(
                {'type': ['Invalid type name "{}" - object does not exist.'.format(relation_type)]},
                status=status.HTTP_400_BAD_REQUEST)

        request.data['contributor'] = user.pk

        try:
            return super().create(request, *args, **kwargs)

        except IntegrityError as ex:
            return Response({'error': str(ex)}, status=status.HTTP_409_CONFLICT)

    def update(self, request, *args, **kwargs):
        """Update the ``Relation`` object.

        Reject the update if user doesn't have ``EDIT`` permission on
        the collection referenced in the ``Relation``.
        """
        instance = self.get_object()
        if (not request.user.has_perm('edit_collection', instance.collection)
                and not request.user.is_superuser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete the ``Relation`` object.

        Reject the delete if user doesn't have ``EDIT`` permission on
        the collection referenced in the ``Relation``.
        """
        instance = self.get_object()

        if (not request.user.has_perm('edit_collection', instance.collection)
                and not request.user.is_superuser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)
