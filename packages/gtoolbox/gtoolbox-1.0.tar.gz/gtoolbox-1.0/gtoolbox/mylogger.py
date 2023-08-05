import logging
import os, sys
from collections import OrderedDict
from enum import Enum
import enum
from collections import namedtuple
import copy

class ACTIONS(Enum):

    UPLOAD = "upload"
    DOWNLOAD = "download"
    COPY = "copy"
    CREATE = "create"
    PROCESS = "process"
    REFORMAT ="reformat"
    RECIEVE = "recieve"


class SATTELITES(Enum):
    @classmethod
    def get(cls, stringname):
        if type(cls) is not enum.EnumMeta:
            ex = ImportWarning("Enum should be updated to enum34(backported python3 version)")
            raise(ex)
        for t in SATTELITES:
            if stringname.lower() in map(lambda s: s.lower(), t.value):
                return t

    NPP = ["NPP", "suomi-npp"]
    NOAA20 = ["NOAA20", "JPSS-1", "NO20", "NOAA_20"]
    METEOR_M_2 = ["meteorm-m-2", "meteorm-2", "meteorm_2", "meteorm_m_2"]
    METEOSAT_10 =["Meteosat10", "Meteosat-10"]
    METEOSAT_8 = ["Meteosat8", "Meteosat-8"]
    ELEKTRO_L_2 = ["electro2","elektro-l2", "elektro-l-2", "Electro-l-2", "electro-l2","Electro-l2", "ElectroL2", "ElektroL2","ElektroL-2","ElectroL-2"]
    GOES_16 = ["goes-r", "goesR", "goes-16", "goes_16","goes16"]





class TAGS(Enum):
    RET_CODE = "return_code"
    SRCPATH = "srcpath"
    DSTPATH = "dstpath"
    SATELLITE = "satellite"
    INSTRUMENT = "instrument"
    ACTION = "action"
    SCAN_TIME = "scan_time"


class Mylogger:
    __instances__ = {}

    @staticmethod
    def get_logger(logger_name=os.path.splitext(os.path.basename(os.path.normpath(sys.argv[0])))[0], logpath = None):
        l = Mylogger.__instances__.get(logger_name)
        if not l:
            if logpath == None:
                logpath = os.path.splitext(os.path.normpath(sys.argv[0]))[0] + ".log"
            l = Mylogger(logger_name, logpath)
            Mylogger.__instances__[l.logger_name] = l
        return l


    def format(self):
        base = self.base
        for k, v in self.TAGS.items():
            base = base + " {}={}".format(str(k), str(v))
        return base + " --- message=<%(message)s>"




    def __init__(self, logger_name=os.path.splitext(os.path.basename(os.path.normpath(sys.argv[0])))[0], logpath=os.path.splitext(os.path.normpath(sys.argv[0]))[0] + ".log"):
            self.base = '%(asctime)s - {} - %(levelname)s'.format(os.path.normpath(sys.argv[0]))
            self.TAGS = OrderedDict()
            self.logger_name = logger_name
            self.init_logger(logger_name, logpath)
            self.logpath = logpath
            self.errFlag = False
            Mylogger.__instances__[logger_name] = self
            print("hey")



    def mylog(self, message, level=logging.INFO, tags = {}):
        _t = None
        if tags:
            _t = copy.deepcopy(self.TAGS)
            formatter = self.file_handler.formatter
            self.update_tags(tags)
        self.logger.log(level, message)
        if _t:
            self.TAGS = _t

            self.file_handler.setFormatter(formatter)
            self.stream_handler.setFormatter(formatter)

    def update_tags(self, tagdict = {}):

        self.TAGS.update(tagdict)
        formatter = logging.Formatter(self.format())

        self.file_handler.setFormatter(formatter)
        self.stream_handler.setFormatter(formatter)

    def set_custom_base(self, base):
        self.base = base
        self.update_tags()



    def init_logger(self, logger_name,logpath):

        logpath = self.touch(logpath)
        logger = logging.getLogger(logger_name)
        self.file_handler = logging.FileHandler(logpath)
        self.stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(self.format())
        self.formatter = formatter
        self.file_handler.setFormatter(formatter)
        self.stream_handler.setFormatter(formatter)
        logger.addHandler(self.file_handler)
        logger.addHandler(self.stream_handler)
        logger.setLevel(logging.INFO)
        self.logger = logger

    def error(self, message, tags = {}, exc_info = None):
        if exc_info:
            _, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            tags.update({"EXC_FILE": fname,"EXC_LINENO" : exc_tb.tb_lineno })

        self.errFlag = True
        self.mylog(message, logging.ERROR, tags)

    def info(self, message, tags={}):
        self.mylog(message, logging.INFO, tags)

    def debug(self, message, tags={}):
        self.mylog(message, logging.DEBUG, tags)

    def warn(self, message, tags={}):
        self.mylog(message, logging.WARNING, tags)

    def touch(self, fname, times=None):
        if not os.path.exists(fname):
            with open(fname, 'a'):
                os.utime(fname, times)
        return fname
