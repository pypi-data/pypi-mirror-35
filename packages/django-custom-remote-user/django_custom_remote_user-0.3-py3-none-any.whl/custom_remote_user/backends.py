from django.contrib.auth.backends import RemoteUserBackend

class CaseInsensitiveRemoteUserBackend(RemoteUserBackend):
    """
    This backend makes sure all users created using an external authentication
    service are created with an all lower-case username to avoid case-sensitivty 
    problems. 
    """
    def clean_username(self, username):
        """
        Returns an all lower-case username
        """
        return username.lower()