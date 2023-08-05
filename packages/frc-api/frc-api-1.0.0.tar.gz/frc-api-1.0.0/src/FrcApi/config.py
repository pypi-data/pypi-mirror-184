"""
place holder.

place holder.
place holder.
"""
import base64


BASEURL = "https://frc-api.firstinspires.org/v3.0/"


class Config:
    """This class is used for configuring the FrcApi wrapper."""

    def key(self, api_key: str) -> None:
        """Set the api key."""
        self.api_key = api_key

    def encode_key(self, api_key: str, username: str) -> None:
        """
        Proprly encodes the api key and username.

        self: An instance of the Config class.

        api_key: The api key.

        username: The username.
        """
        encode = base64.b64encode(f"{username}:{api_key}".encode("utf-8"))
        self.api_key = encode.decode("utf-8")
