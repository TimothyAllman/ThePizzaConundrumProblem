import datetime as dt


class EnvFileData:
    def __init__(
        self,
        myDate: str,
        myPrefix: str = "Prefix",
        mySuffix: str = "Suffix",
    ):
        self.MY_PREFIX = myPrefix
        self.MY_SUFFIX = mySuffix
        self.MY_DATE = myDate
        self.MY_FOLDER = f"{self.MY_PREFIX}_{self.MY_DATE}_{self.MY_SUFFIX}_folder"
