from django.db.models.query import QuerySet

from generic.exceptions import ValidationError


def image_dim_validator(repository, field, width, height):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :arg: width: Maximum image width
    :arg: height: Maximum image height
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks if an image is too tall/wide.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.image_too_tall(instance, field, height):
                msg = "Image is too tall: Maximum height is {0}.".format(height)
                raise ValidationError(msg, field=field)
            if repository.image_too_wide(instance, field, width):
                msg = "Image is too wide: Maximum width is {0}.".format(width)
                raise ValidationError(msg, field=field)
            return True

    return _checker


def image_size_validator(repository, field, size):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :arg: size: Maximum image size in bytes
    :returns: True is validation was successful
    :raises: ValidationError if the validation failed

    Checks if an image is too large.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if repository.image_too_large(instance, field, size):
                msg = "Image is too large: Maximum size is {}B.".format(size)
                raise ValidationError(msg, field=field)
            return True

    return _checker


def image_square_validator(repository, field):
    """
    :arg: repository: Repository that should be used to perform validation
    :arg: field: Field to be validated
    :returns: ValidationError if the validation failed

    Ensures that image is quadratic.
    """

    def _checker(instance):
        if isinstance(instance, QuerySet):
            return all(_checker(i) for i in instance)
        else:
            if not repository.is_square(instance, field):
                msg = 'Image must be quadratic.'
                raise ValidationError(msg, field=field)
            return True

    return _checker