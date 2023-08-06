import os
import pathlib
import re

from traitlets import Undefined, Unicode

if __package__:
    from delta import DeltaTable
    from pyspark.sql.dataframe import DataFrame

    from pushcart import dbutils, spark


class ExistingSystemPath(Unicode):
    """
    Custom TraitType for storing an existing system path
    """

    def __init__(
        self,
        default_value=Undefined,
        allow_none=False,
        file=False,
        directory=False,
        search_paths=None,
        **kwargs,
    ):
        self.file = file
        self.directory = directory
        self.search_paths = search_paths

        if file and directory:
            raise ValueError("Path cannot be a file and a directory at the same time")

        super(ExistingSystemPath, self).__init__(
            default_value=default_value, allow_none=allow_none, **kwargs
        )

    def validate_system_abs_path(self, path):
        """
        Check whether the path is an existing file, directory, or any kind of path,
        depending on the values of the file and directory attributes. If the path is
        valid, it returns the path, otherwise it returns None
        """
        if (not self.file and not self.directory) and os.path.exists(path):
            return path
        if (self.file and not self.directory) and os.path.isfile(path):
            return path
        if (not self.file and self.directory) and os.path.isdir(path):
            return path

    def validate_system_path(self, value, search_paths=None):
        """
        First normalize path by removing any redundant separators and "." and ".."
        components. If the path is absolute, call the validate_system_abs_path method
        to validate the path. If the path is not absolute, iterate through the search
        paths and append the path to each search path to create an absolute path. Call
        the validate_system_abs_path method to validate each absolute path.
        """
        path = os.path.normpath(value)

        if not search_paths:
            search_paths = [os.getcwd()]

        if os.path.isabs(path):
            return self.validate_system_abs_path(path)
        else:
            for p in search_paths:
                abs_path = os.path.join(os.path.normpath(p), path)

                if found := self.validate_system_abs_path(abs_path):
                    return found

    def validate(self, obj, value):
        value = super(ExistingSystemPath, self).validate(obj, value)

        parsed_value = self.validate_system_path(value, search_paths=self.search_paths)
        if not parsed_value:
            self.error(obj)

        return parsed_value


class ExistingSystemFilePath(ExistingSystemPath):
    """
    Custom TraitType for storing an existing file path on the system
    """

    def __init__(
        self,
        default_value=Undefined,
        allow_none=False,
        search_paths=None,
        **kwargs,
    ):
        super(ExistingSystemFilePath, self).__init__(
            default_value=default_value,
            allow_none=allow_none,
            file=True,
            search_paths=search_paths,
            **kwargs,
        )


class ExistingSystemDirectoryPath(ExistingSystemPath):
    """
    Custom TraitType for storing an existing directory path on the system
    """

    def __init__(
        self,
        default_value=Undefined,
        allow_none=False,
        search_paths=None,
        **kwargs,
    ):
        super(ExistingSystemDirectoryPath, self).__init__(
            default_value=default_value,
            allow_none=allow_none,
            directory=True,
            search_paths=search_paths,
            **kwargs,
        )


class ExistingDataPath(Unicode):
    """
    Custom TraitType for storing an existing path to a file or non-empty directory,
    accessible by Databricks
    """

    default_value = Undefined
    allow_none = False

    def validate_path_exists(self, path):
        path_contents = dbutils.fs.ls(path)

        if path_contents:
            return path

    def validate(self, obj, value):
        value = super(ExistingDataPath, self).validate(obj, value)

        if not self.validate_path_exists(value):
            self.error(obj)

        return value


class ExistingDeltaPath(Unicode):
    """
    Custom TraitType for holding a path to an existing Delta table, accessible from
    Databricks on local storage, DBFS, S3, Azure Storage or Google Storage.
    """

    default_value = Undefined
    allow_none = False

    def validate_path_exists(self, path):
        if DeltaTable.isDeltaTable(spark, path):
            return path

    def validate(self, obj, value):
        value = super(ExistingDeltaPath, self).validate(obj, value)

        if not self.validate_path_exists(value):
            self.error(obj)

        return value


class ExistingTableName(Unicode):
    """
    Custom TraitType for holding the name of an existing Databricks table or view.
    """

    default_value = Undefined
    allow_none = False

    def validate_table_exists(self, table_name):
        if isinstance(spark.table(table_name), DataFrame):
            return table_name

    def validate(self, obj, value):
        value = super(ExistingTableName, self).validate(obj, value)

        if not self.validate_table_exists(value):
            self.error(obj)

        return value


class DataPath(Unicode):
    """
    Custom TraitType for holding a path to data, locally, on DBFS, S3, Azure Storage or
    Google Storage. The path does not necessarily already exist.
    """

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        self.path_regex = [
            re.compile(
                r"^(abfss:\/\/[a-z0-9-]{2,62}@[a-z0-9]{3,24}\.dfs\.core\.windows\.net)\/.*$"
            ),
            re.compile(r"^(s3:\/\/[a-z0-9][a-z0-9.-]{1,61}[a-z0-9])\/.*$"),
            re.compile(r"^(gs://(?:[a-z0-9][a-z0-9-_.]{0,61}[a-z0-9])+)\/.*$"),
            re.compile(r"^(dbfs:)\/.*$"),
            re.compile(r"^(file:)\/.*$"),
        ]
        super(DataPath, self).__init__(
            default_value=default_value, allow_none=allow_none, **kwargs
        )

    def validate_path_syntax(self, path):
        """
        Use a regular expression to check whether the path is in one of file:/,
        dbfs:/, s3:/ or abfss:/ locations. If it is, it split the prefix from the rest
        of the path, then attempt to create a pathlib.Path object from the rest of the
        path. Check whether it is an absolute path and if true, return the path (with
        the prefix added back)
        """
        if not isinstance(path, str):
            return

        prefix = ""
        for regex in self.path_regex:
            if match := regex.match(path):
                prefix, path = match.groups()
                break

        try:
            path = os.path.normpath(path)

            p = pathlib.Path(path)
            if p.is_absolute():
                return prefix + path
        except ValueError:
            pass

    def validate(self, obj, value):
        value = super(DataPath, self).validate(obj, value)

        parsed_value = self.validate_path_syntax(value)
        if not parsed_value:
            self.error(obj)

        return value


class TableName(Unicode):
    """
    Custom TraitType for storing the name of a Spark table, optionally including
    metastore and database. The actual table does not necessarily already exist
    """

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        self.regex_starts_with = re.compile(r"[A-Za-z_]")
        self.regex_allowed_chars = re.compile(r"^[A-Za-z0-9_.]*$")
        self.regex_ends_with = re.compile(r"\.$")

        super(TableName, self).__init__(
            default_value=default_value, allow_none=allow_none, **kwargs
        )

    def validate_table_name(self, value):
        """
        Checks:
        - that the value starts with a letter or underscore
        - that the value only contains letters, digits, underscores, and periods
        - that the value does not end with a period
        - that the length of the value after the last period character is max 64
          characters
        """

        if not isinstance(value, str):
            return

        if not self.regex_starts_with.match(value):
            return

        if not self.regex_allowed_chars.match(value):
            return

        if self.regex_ends_with.match(value):
            return

        if len(value.split(".")[-1]) > 64:
            return

        return value

    def validate(self, obj, value):
        value = super(TableName, self).validate(obj, value)

        if not self.validate_table_name(value):
            self.error(obj)

        return value


class ViewName(Unicode):
    """
    Custom TraitType for storing the name of a Spark view. The actual view does not
    necessarily already exist.
    """

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        self.regex_starts_with = re.compile(r"[A-Za-z_]")
        self.regex_allowed_chars = re.compile(r"^[A-Za-z0-9_]*$")

        super(ViewName, self).__init__(
            default_value=default_value, allow_none=allow_none, **kwargs
        )

    def validate_view_name(self, value):
        """
        Checks:
        - that the value starts with a letter or underscore
        - that the value only contains letters, digits or underscores
        - that the value does not end with a period
        - that the length of the value is max 64 characters
        """

        if not isinstance(value, str):
            return

        if not self.regex_starts_with.match(r"[A-Za-z_]"):
            return

        if not self.regex_allowed_chars.match(r"^[A-Za-z0-9_]*$"):
            return

        if len(value) > 64:
            return

        return value

    def validate(self, obj, value):
        value = super(ViewName, self).validate(obj, value)

        if not self.validate_view_name(value):
            self.error(obj)

        return value
