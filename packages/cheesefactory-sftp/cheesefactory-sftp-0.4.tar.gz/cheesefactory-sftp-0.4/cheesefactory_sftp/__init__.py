# __init__.py
__authors__ = ["tsalazar"]
__version__ = "0.3"

# v0.1 (tsalazar) -- Stand-alone SFTP package, split from cheesefactory package.

import logging
import pysftp
from pathlib import Path


class SFTP:
    """A class that provides methods for interacting with an SFTP server."""

    def __init__(self, host='127.0.0.1', port='22', username=None, password=None):
        """Initialize an instance of the Report class.

        Args:
            host (str): SFTP server hostname or IP.
            port (str): SFTP server port.
            username (str): SFTP server account username.
            password (str): SFTP server account password.
        """

        # Logging

        self.__logger = logging.getLogger(__name__)
        self.__logger.debug('Initializing CSV class object')

        # Initialize instance attributes

        self.__sftp_connection = self.__connect()

        self.host = host
        self.port = int(port)
        self.__username = username
        self.__password = password

        self.__logger.debug('SFTP class object initialized')
        self.__connect()

        self.__local_directory = '/'
        self.__remote_directory = '/'
        self.__new_file_count = 0
        self.__existing_file_count = 0

    def __connect(self):
        """Establish an SFTP connection with a server.

        Returns:
            : SFTP connection
        """

        # Connect
        self.__logger.debug('Establishing a connection to the SFTP server.')

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        sftp_connection = pysftp.Connection(
            self.host,
            port=int(self.port),
            username=self.__username,
            password=self.__password,
            cnopts=cnopts,
        )

        self.__logger.debug('SFTP connection established.')
        return sftp_connection

    def get(self, filename=None, local_directory='/', remote_directory='/'):
        """Download a file from an SFTP server.

        Args:
            filename (str): The name of the file to download.
            local_directory (str): The local directory to download the file into.
            remote_directory (str): Remote SFTP directory.
        """

        try:
            self.__logger.debug(f'Changing directory: {remote_directory}')
            self.__sftp_connection.cd(remote_directory)
            self.__logger.debug(f'Attempting to retrieve file: {filename}')
            self.__sftp_connection.get(
                filename,
                localpath=f'{local_directory}/{filename}'
            )

        except ValueError:
            self.__logger.critical('Problem encountered when retrieving file.')
            exit(1)

    def put(self, filename=None, confirm=True, remote_directory='/'):
        """Upload a file to an SFTP server.

        Args:
            filename (str): The name of the file to upload.
            confirm (bool): Confirm that the transfer was successful using stat().
            remote_directory (str): Remote SFTP directory.
        """

        try:
            self.__logger.debug(f'Changing directory: {remote_directory}')
            with self.__sftp_connection.cd(remote_directory):
                self.__logger.debug(f'Attempting to upload file: {filename}')
                self.__sftp_connection.put(
                    filename,
                    confirm=confirm
                )

        except ValueError:
            self.__logger.critical('Problem encountered when uploading file.')
            exit(1)

    def get_new_files(self, remote_directory='/', local_directory='/'):
        """Get all unretrieved files from remote SFTP directory

        Args:
            remote_directory (str): Remote SFTP directory.
            local_directory (str): Local directory to copy the files to.
        """

        self.__logger.debug(f'Changing directory: {remote_directory}')
        self.__sftp_connection.cd(remote_directory)
        self.__remote_directory = remote_directory

        self.__logger.debug(f'Testing existence of local directory: {str(local_directory)}')

        # Create the directory if it does not exist
        Path(local_directory).mkdir(
            parents=True,
            exist_ok=True
        )
        self.__local_directory = local_directory

        self.__logger.info(f'Retrieving new files from remote directory: {str(remote_directory)}')

        self.__sftp_connection.walktree(
            remote_directory,
            self.__is_this_a_new_file,
            self.__is_this_a_new_file,
            self.__is_this_a_new_file,
        )

    def __is_this_a_new_file(self, filename):
        """Test to see if the current file has been retrieved yet.

        Args:
            filename (str):  File to test for.
        """

        local_file = Path(self.__local_directory, Path(filename).name)

        if local_file.exists():
            self.__logger.debug(f'File exists: {str(local_file)} -- Skipping.')
            self.__existing_file_count += 1
        else:
            self.__logger.debug(f'File not found: {str(local_file)} -- Transferring.')
            self.get(
                filename=filename,
                local_directory=self.__local_directory,
                remote_directory=self.__remote_directory
            )
            self.__new_file_count += 1

    def close(self):
        """Close a connection to an SFTP server."""

        try:
            self.__sftp_connection.close()
        except ValueError:
            self.__logger.critical('Problem closing connection.')
            exit(1)

    def __del__(self):
        """Wrap it up."""

        try:
            self.__sftp_connection.close()
        except ValueError:
            self.__logger.critical('Problem closing connection.')
            exit(1)
