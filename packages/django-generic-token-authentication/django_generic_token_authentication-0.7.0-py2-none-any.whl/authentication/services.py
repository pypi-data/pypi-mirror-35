from django.contrib.auth.hashers import make_password


def retrieve_token_service(repository):
    """
    Creates a new token for the given user.
    """

    def _retrieve(user):
        (token, refresh_token) = repository.create_token(user)
        return token, refresh_token

    return _retrieve


def logout_service(repository):
    """
    Deletes a single token.
    """

    def _logout(token):
        return repository.logout(token)

    return _logout


def logout_all_service(repository):
    """
    Deletes all tokens of user.
    """

    def _logout(user):
        repository.delete_by_user(user)

    return _logout


def refresh_token_service(repository):
    """
    Refreshes a user's token.
    """

    def _refresh(user, token, refresh_token):
        return repository.refresh_token(user, token, refresh_token)

    return _refresh


def reset_password_service(repository):
    """
    Send password reset email to users' email.
    """

    def _reset(email):
        return repository.reset_password(email)

    return _reset


def validate_reset_password_service(repository):
    """
    Checks validity of the password reset token.
    """

    def _test(reset_token):
        return repository.validate_token_and_get_user(reset_token)

    return _test


def confirm_reset_password_service(repository):
    """
    Checks validity of the password reset token and sets new password.
    """

    def _confirm(reset_token, new_password):
        instance = repository.validate_token_and_get_user(reset_token)
        instance.password = make_password(new_password)
        instance.save()
        return instance

    return _confirm


def validate_email_service(repository):
    """
    Sends an email validation email.
    """

    def _validate(instance):
        return repository.send_email_validation(instance)

    return _validate


def confirm_email_service(repository):
    """
    Checks the validation token and flags the email address as validated.
    """

    def _confirm(val_token):
        instance = repository.validate_token_and_get_user(val_token)
        instance.validated_email = True
        instance.save()
        return instance

    return _confirm


def store_profile_image_service(repository, validator):
    """
    Stores the profile image of a user.
    """

    def _store(user, image):
        instance = repository.store_image(user, image, 'image')
        validator(instance)
        instance.save()
        return instance

    return _store

def remove_profile_image_service(repository):
    """
    Removes the profile image of a user.
    """
    def _remove(pk, requesting_user):
        instance = repository.get_by_id(pk, requesting_user)
        instance.image.delete(save=True)
        return instance

    return _remove
