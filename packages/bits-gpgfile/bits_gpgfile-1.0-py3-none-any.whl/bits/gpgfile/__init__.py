"""Module for decrypting GPG files."""

# import
import os
import gpgme
import tempfile

# import BytesID from the io module
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO


class GPGFile(object):
    """Class for opening GPG-encrypted files."""

    def __init__(self, keyfiles=None):
        """Initiator."""
        if (not keyfiles) or (type(keyfiles) != list):
            raise ValueError("GPG key file list was not provided")

        # Setup the internal file pointer to nothing
        self.fp = None

        # Testing...probably not needed
        self._gpghome = tempfile.mkdtemp(prefix="tmp.gpghome")
        os.environ["GNUPGHOME"] = self._gpghome

        # Setup GPG context
        self.ctx = gpgme.Context()

        # Check keyfiles
        for k in keyfiles:
            if not os.path.isfile(k):
                raise ValueError("GPG key file `%s` could not be found" % k)

            # open keyfile file pointer
            fp = open(k, "rb")

            # import keyfile file pointer
            self.ctx.import_(fp)

    def open(self, filename=None, mode=None):
        """Return a decrypted file."""
        if (not filename) or (type(filename) != str):
            raise ValueError("Filename not provided")
        if (not mode) or (type(mode) != str):
            raise ValueError("Open mode not provided")

        if not os.path.isfile(filename):
            raise ValueError("File `%s` could not be found" % filename)

        # open encrypted file
        self.fp = open(filename, mode)

        # create a new BytesIO object
        plaintext = BytesIO()

        # decrypt the file into the BytesIO object
        self.ctx.decrypt(self.fp, plaintext)

        # convert the BytesIO object to a string
        string = plaintext.getvalue()

        # initialize new lists for lines and errors
        lines = []
        errors = []

        # check lines for non-ascii characters
        for line in string.split('\n'):

            # see if text can be encoded into ascii
            try:
                encoded = line.encode('ascii')

            # if not, clean it up
            except UnicodeDecodeError:
                errors.append(line)
                decoded = line.decode('utf8', errors='ignore')
                encoded = decoded.encode('ascii', errors='ignore')

            # add the newly encoded ascii line to the array
            lines.append(encoded)

        # print out any errors
        if errors:
            print('ERRORS:')
            print('   - '+'\n   - '.join(sorted(errors)))
            print('')

        return lines
