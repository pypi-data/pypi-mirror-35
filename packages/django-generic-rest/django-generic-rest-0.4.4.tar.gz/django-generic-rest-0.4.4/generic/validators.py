from django.core.exceptions import ImproperlyConfigured
from django.db.models.query import QuerySet

from generic.exceptions import ValidationError


def unique_field(repository, field):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks if a field is unique.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if not repository.is_unique(instance, field):
                raise ValidationError('This value has already been used.',
                                      field=field)
            return True

    return _checker


def unique_together_fields(repository, *fields):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: fields: Fields to be validated
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks if a field is unique.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if len(repository.search_by(instance, *fields)) is not 0:
                raise ValidationError('These values have already been used.',
                                      field=fields)
            return True

    return _checker


def required_field(repository, field):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks if a field is present.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.is_none(instance, field):
                raise ValidationError('Mandatory value was not provided.',
                                      field=field)
            return True

    return _checker


def max_length(repository, field, length):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :arg: length: Maximal length for field
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks if the max length of a CharField is exceeded.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.is_too_long(instance, field, length):
                raise ValidationError(("Maximal length of {0} chars "
                                       "exceeded.").format(length),
                                      field=field)
            return True

    return _checker


def min_length(repository, field, length):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :arg: length: Maximal length for field
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks if the min length of a CharField is is met.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.is_too_short(instance, field, length):
                raise ValidationError(("Minimal length of {0} characters "
                                       "not met.").format(length),
                                      field=field)

            return True

    return _checker


def read_only_field(repository, field):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Ensures that read only fields are not written to.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.contains_arg(instance, field):
                raise ValidationError('Attempt to write read only field.',
                                      field=field)
            return True

    return _checker


def min_char_classes(repository, field, char_classes):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :arg: char_classes: Number of different character classes need to be
    present; can be lower/upper case letters, digits or punctuation
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks if field comprises sufficient character classes.
    """
    if char_classes < 0 or char_classes > 4:
        raise ImproperlyConfigured(("Number of character classes "
                                    "must be  in range 0-4."))

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if not repository.contains_char_classes(instance, field, char_classes):
                raise ValidationError(("Field must contain {0} of the "
                                       "following characters: upper case letters, "
                                       "lower case letters, digits and special "
                                       "characters.").format(char_classes),
                                      field='password')

            return True

    return _checker


def email_field(repository, field):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks is a user's email address is valid
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if not repository.is_valid_email(instance, field):
                raise ValidationError('This email address is invalid.', field='email')
            return True

    return _checker


def validate_many(*validators):
    """
    :arg: *validators: List of validators to be applied

    Allows to apply multiple validators.
    """

    def _checker(instance):
        return all(validator(instance) for validator in validators)

    return _checker
