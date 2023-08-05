import os
import shutil
from hashlib import sha512
from unittest.mock import patch

from aletheia.aletheia import Aletheia

from .base import TestCase


class StackTestCase(TestCase):
    """
    Test the entire stack: key generation, and the signing/verifying of every
    file type.
    """

    TEST_FILES = ("html", "jpg", "mkv", "mp3", "mp4", "webm")

    @patch.dict("os.environ", {"HOME": TestCase.SCRATCH})
    @patch.dict("os.environ", {"ALETHEIA_HOME": TestCase.SCRATCH})
    def test_stack(self):

        aletheia = Aletheia()

        self.assertEqual(
            aletheia.public_key_path,
            os.path.join(self.SCRATCH, "aletheia.pub")
        )
        self.assertEqual(
            aletheia.private_key_path,
            os.path.join(self.SCRATCH, "aletheia.pem")
        )
        self.assertEqual(
            aletheia.public_key_cache,
            os.path.join(self.SCRATCH, "public-keys")
        )

        # Generate the keys

        self.assertFalse(
            os.path.exists(os.path.join(self.SCRATCH, "aletheia.pem")))
        self.assertFalse(
            os.path.exists(os.path.join(self.SCRATCH, "aletheia.pub")))

        aletheia.generate()

        self.assertTrue(
            os.path.exists(os.path.join(self.SCRATCH, "aletheia.pem")))
        self.assertTrue(
            os.path.exists(os.path.join(self.SCRATCH, "aletheia.pub")))

        for suffix in self.TEST_FILES:

            filename = "test.{}".format(suffix)
            source_path = os.path.normpath(
                os.path.join(os.path.dirname(__file__), "data", filename))

            # Copy our test file to SCRATCH so we can fiddle with it

            file_path = os.path.join(self.SCRATCH, filename)
            shutil.copyfile(source_path, file_path)

            # Sign the file

            public_key_url = "https://example.com/aletheia.pub"
            aletheia.sign(file_path, public_key_url)
            with open(source_path, "rb") as original:
                with open(file_path, "rb") as modified:
                    self.assertNotEqual(
                        sha512(original.read()),
                        sha512(modified.read())
                    )

            # Put the public key in the cache so we don't try to fetch it.

            shutil.copyfile(
                os.path.join(self.SCRATCH, "aletheia.pub"),
                os.path.join(
                    self.SCRATCH,
                    "public-keys",
                    sha512(public_key_url.encode("utf-8")).hexdigest()
                )
            )

            # Verify the file

            self.assertTrue(aletheia.verify(file_path))
