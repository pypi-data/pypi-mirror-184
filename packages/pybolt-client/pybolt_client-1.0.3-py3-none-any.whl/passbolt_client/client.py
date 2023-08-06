import json
import os.path
import uuid

import requests
from gnupg import GPG
from requests_gpgauthlib.gpgauth_session import GPGAuthSession
from requests_gpgauthlib.utils import import_user_private_key_from_file


class Client:
    """
    Client for making Passbolt API requests.
    """

    def __init__(
        self,
        url: str,
        gpg_path: str = "~/.gnupg/",
        private_key_path: str = "~/.gnupg/private.key",
    ):
        self.private_key_path = private_key_path
        self.base_url = url
        self.server_pub_key, self.server_finger_print = self.get_server_details()
        self.session: GPGAuthSession = self._create_session(key_path=gpg_path)

    def _create_session(self, key_path: str) -> GPGAuthSession:
        """
        Initialise a GPG Auth Session.
        """
        gpg = GPG(gnupghome=os.path.expanduser(key_path))
        import_user_private_key_from_file(
            gpg, os.path.expanduser(self.private_key_path)
        )

        session = GPGAuthSession(
            gpg=GPG(gnupghome=os.path.expanduser(key_path)),
            server_url=self.base_url,
        )
        assert session.server_fingerprint == self.server_finger_print
        return session

    def authenticate(self):
        """
        Authenticate the server's public key and finger print.
        """
        self.session.authenticate()

    def get(self, endpoint: str) -> requests.Response:
        """
        Make a GET request to the specified endpoint.

        TODO: Add exception handling for responses other than 200.
        """
        return requests.get(f"{self.base_url}/{endpoint}")

    def create_nonce(self):
        """
        Create a nonce token according to the specified format.
        """
        return f"gpgauthv1.3.0|36|{uuid.uuid4()}|gpgauthv1.3.0"

    def get_server_details(self):
        """
        Get server's public key with fingerprint.

        Returns a tuple with the first element being the public key and the second being
        the fingerprint.
        """
        endpoint = "auth/verify.json"
        response = self.get(endpoint).json()
        response_body = response.get("body")
        server_pub_key = response_body.get("keydata")
        server_finger_print = response_body.get("fingerprint")
        return server_pub_key, server_finger_print

    def get_password_by_name(self, name: str):
        """
        Given the name of a resource, get the corresponding password.
        """
        all_resources = self.get_all_resources().json().get("body")
        resource_id = ""
        for resource in all_resources:
            if resource.get("name") == name:
                resource_id = resource.get("id")
                break
        else:
            return

        return self.get_secret(resource_id)

    def get_all_resources(self):
        """
        Get all resources from passbolt.
        """
        return self.session.get(self.base_url + "/resources.json")

    def get_secret(self, resource_id: str):
        """
        Get a password given the resource id.
        """
        uri = f"{self.base_url}/secrets/resource/{resource_id}.json"

        response = self.session.get(uri)

        encrypted = response.json().get("body").get("data")

        decrypted = self.session.gpg.decrypt(encrypted, always_trust=True)

        loaded = json.loads(decrypted.data.decode())

        return loaded.get("password")
