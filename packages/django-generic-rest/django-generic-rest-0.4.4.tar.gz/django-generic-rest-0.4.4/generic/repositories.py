import re

from django.core.exceptions import ObjectDoesNotExist

from generic.exceptions import ObjectNotFoundError
from generic.helpers import contains_char_classes


class ValidatorMixin:
    """
    Provides validators for generic repositories.
    """

    def is_unique(self, instance, field):
        """
        :arg: instance: Instance that should be validated
        :arg: field: Field that should be checked for uniqueness
        :returns: True if the value stored in field is unique; False otherwise

        Checks the uniqueness of the value stored in field.
        Cannot be used as an argument validator.
        """
        try:
            value = getattr(instance, field)
        except KeyError:
            return True

        if value is None:
            return True

        kwargs = {field: str(value)}
        pk = getattr(instance, 'id')
        conflict = self.model_class.objects.exclude(id=pk).filter(**kwargs).count()

        if conflict is 0:
            return True

        return False

    def search_by(self, instance, *fields):
        """
        :arg: instance: Instance that should be validated
        :arg: fields: Fields that should be used as filter criteria
        :returns: Queryset matching the filter criteria

        Returns queryset matching the filter criteria, excluding the passed
        instance.
        Cannot be used as an argument validator.
        """
        search_filter = {}

        def _get_value(field):
            try:
                value = getattr(instance, field)
            except KeyError:
                return

            search_filter[field] = value

        [_get_value(f) for f in fields]
        pk = getattr(instance, 'id')
        instances = self.model_class.objects.exclude(id=pk).filter(**search_filter)
        return instances

    @staticmethod
    def is_none(instance, field):
        """
        :arg: instance: Instance that should be validated
        :arg: field: field: Field that should be checked for None
        :returns: True if the value stored in field is None; False otherwise

        Checks if the value stored in field is None.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return True

        if value is None:
            return True

        return False

    @staticmethod
    def is_too_long(instance, field, length):
        """
        :arg: instance: Instance that should be validated
        :arg: field: field: Field that should be checked for length
        :returns: True if the value stored in field if longer than length;
        False otherwise

        Checks if the value stored in field is longer then max_length.
        Only applicable to CharFields.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return False

        if value is None:
            return False

        if len(value) > length:
            return True

        return False

    @staticmethod
    def is_too_short(instance, field, length):
        """
        :arg: instance: Instance that should be validated
        :arg: field: field: Field that should be checked for length
        :returns: True if the value stored in field if shorter than length;
        False otherwise

        Checks if the value stored in field is shorter then length.
        Only applicable to CharFields.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return False

        if value is None:
            return False

        if len(value) < length:
            return True

        return False

    @staticmethod
    def contains_arg(instance, field):
        """
        :arg: instance: Instance that should be validated
        :arg: field: field: Field that should be checked for presence
        :returns: True if the argument is present; False otherwise

        Checks if field is present in the args dictionary or instance.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                instance[field]
            else:
                getattr(instance, field)

        except KeyError:
            return False

        return True

    @staticmethod
    def contains_char_classes(instance, field, char_classes):
        """
        :arg: instance: Instance that should be validated
        :arg: field: Field that should be checked for character classes
        :arg: char_classes: Number of character classes that must be present
        :returns: True if the value stored in field contains sufficient
        character classes, False otherwise

        Checks if the value stored in field contains the demanded number of
        different character classes.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return True

        if value is None:
            return True

        if contains_char_classes(value, char_classes):
            return True

        return False

    @staticmethod
    def is_valid_email(instance, field):
        """
        :arg: instance: Instance that should be validated
        :arg: field: Field that should be checked for a valid email address
        :returns: True if the value stored in field is a valid email address;
        False otherwise

        Checks if the value stored in field is a valid email address.
        Can be used as an argument validator.
        """
        try:
            if type(instance) is dict:
                value = instance[field]
            else:
                value = getattr(instance, field)

        except KeyError:
            return True

        if value is None:
            return True

        reg_ex = r"[^@]+@[^@]+\.[^@]+"
        if re.match(reg_ex, value):
            return True

        return False


class GenericRepository(ValidatorMixin):
    """
    Provides a generic database abstraction layer for all model classes.
    """

    def __init__(self, model_class):
        """
        :arg: model_class: Class of the model that this repository should
        work on.

        Constructor that initializes the repository with a specific
        model class.
        """
        self.model_class = model_class

    def find_by_user(self, user=None):
        """
        :raises: NotImplementedError
        """
        raise NotImplementedError("""GenericRepository does not provide
                                  function find_by_user.""")

    def find_by_id(self, pk, user=None):
        """
        :arg: pk: Primary key of the instance that should be returned
        :returns: Queryset representing the instance with id=pk

        Provides generic get by id function. Returns queryset representing
        exactly one instance or an empty queryset.
        """
        return self.model_class.objects.filter(id=pk)

    def get_by_id(self, pk, user=None):
        """
        :arg: pk: Primary key of the instance that should be returned
        :returns: Requested instance with id=pk
        :raises: ObjectNotFoundError if the requested object was not found

        Provides generic get by id function. Returns exactly one instance or
        raises error.
        """
        try:
            return self.model_class.objects.get(id=pk)
        except ObjectDoesNotExist:
            raise ObjectNotFoundError('Object not found.',
                                      modelclass=self.model_class)

    def list_all(self, user=None):
        """
        :returns: Queryset of all instances

        Provides generic list all function.
        """
        return self.model_class.objects.all()

    def delete_by_id(self, pk, user=None):
        """
        :arg: pk: Primary key of the instance that should be deleted
        :returns: True if the instance was deleted
        :raises: ObjectNotFoundError if the requested object was not found

        Provides generic delete function.
        """
        try:
            self.model_class.objects.get(id=pk).delete()
            return True
        except ObjectDoesNotExist:
            raise ObjectNotFoundError('Object not found.',
                                      modelclass=self.model_class)

    @staticmethod
    def persist(instance):
        """
        :arg: instance: Instance that should be persisted.
        :returns: The persisted instance

        Provides generic persist function.
        """
        return instance.save()


class OwnershipRepository(ValidatorMixin):
    """
    Provides a generic database abstraction layer for all model classes
    that have an owner field, writing and reading of these model classes is
    limited to the owner. At time of creation the ownership information is
    automatically inserted.
    """

    def __init__(self, model_class):
        """
        :arg: model_class: Class of the model that this repository should
        work on.

        Constructor that initializes the repository with a specific
        model class.
        """
        self.model_class = model_class

    def find_by_user(self, user):
        """
        :arg: user: Requesting user
        :returns: Queryset representing all instances owned by user

        Provides generic find by user function.
        """
        if hasattr(self.model_class, 'owner'):
            return self.model_class.objects.filter(owner=user)

        return self.model_class.objects.filter(id=user.id)

    def find_by_id(self, pk, user):
        """
        :arg: pk: Primary key of the instance that should be returned
        :arg: user: Requesting user
        :returns: Queryset representing the instance owned by user with id=pk

        Provides generic get by id function. Only matches instances that are
        owned by the user. If there is no owner field, id is used for
        determining ownership instead. Returns queryset representing exactly
        one instance or an empty queryset.
        """
        if hasattr(self.model_class, 'owner'):
            return self.model_class.objects.filter(owner=user).filter(id=pk)

        return self.model_class.objects.filter(id=user.id).filter(id=pk)

    def get_by_id(self, pk, user):
        """
        :arg: pk: Primary key of the instance that should be returned
        :arg: user: Requesting user
        :returns: Requested instance owned by user with id=pk
        :raises: ObjectNotFoundError if the requested object was either not
        found or not owned by user

        Provides generic get by id function. Only matches instances that are
        owned by the user. If there is no owner field, id is used for
        determining ownership instead. Returns exactly one instance or
        raises error.
        """
        if hasattr(self.model_class, 'owner'):
            try:
                return self.model_class.objects.filter(owner=user).get(id=pk)
            except ObjectDoesNotExist:
                raise ObjectNotFoundError('Object not found.',
                                          modelclass=self.model_class)

        try:
            return self.model_class.objects.filter(id=user.id).get(id=pk)
        except (ObjectDoesNotExist, AttributeError):
            raise ObjectNotFoundError('Object not found.',
                                      modelclass=self.model_class)

    def list_all(self, user):
        """
        :arg: user: Requesting user
        :returns: Queryset of instances owned by the user

        Provides generic list all owned by user function. If there is no owner
        field, id is used for determining ownership instead.
        """
        if hasattr(self.model_class, 'owner'):
            return self.model_class.objects.filter(owner=user)

        return self.model_class.objects.filter(id=user.id)

    def delete_by_id(self, pk, user):
        """
        :arg: pk: Primary key of the instance that should be deleted
        :arg: user: Requesting user
        :returns: Instance that was deleted
        :raises: ObjectNotFoundError if the requested object was either not
        found or not owned by user

        Provides generic delete function. Only matches instances that are
        owned by the user. If there is no owner field, id is used for
        determining ownership instead.
        """
        if hasattr(self.model_class, 'owner'):
            try:
                return self.model_class.objects.filter(owner=user).get(id=pk).delete()
            except ObjectDoesNotExist:
                raise ObjectNotFoundError('Object not found.',
                                          modelclass=self.model_class)

        try:
            return self.model_class.objects.filter(id=user.id).get(id=pk).delete()
        except (ObjectDoesNotExist, AttributeError):
            raise ObjectNotFoundError('Object not found.',
                                      modelclass=self.model_class)

    @staticmethod
    def persist(instance):
        """
        :arg: instance: Instance that should be persisted.
        :returns: The persisted instance

        Provides generic persist function.
        """
        return instance.save()
