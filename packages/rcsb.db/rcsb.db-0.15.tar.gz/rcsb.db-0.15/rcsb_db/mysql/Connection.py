##
# File:  Connection.py
# Date:  25-Mar-2018 J. Westbrook
#
# Update:
#   31-Mar-2018 jdw add context methods
##
"""
Derived class for managing database credentials from a generic configuration file object.

"""
__docformat__ = "restructuredtext en"
__author__ = "John Westbrook"
__email__ = "jwest@rcsb.rutgers.edu"
__license__ = "Apache 2.0"


import logging
import platform

import MySQLdb

from rcsb_db.mysql.ConnectionBase import ConnectionBase

logger = logging.getLogger(__name__)
#
#
if platform.system() == "Linux":
    try:
        import sqlalchemy.pool as pool
        MySQLdb = pool.manage(MySQLdb, pool_size=12, max_overflow=12, timeout=30, echo=False, use_threadlocal=False)
    except Exception as e:
        logger.exception("Creating MYSQL connection pool failing")


class Connection(ConnectionBase):

    def __init__(self, cfgOb=None, infoD=None, resourceName=None, verbose=False):
        super(Connection, self).__init__(verbose=verbose)
        #
        self.__cfgOb = cfgOb
        #
        if infoD:
            self.setPreferences(infoD)
        #
        if resourceName:
            self.assignResource(resourceName)
        #

    def assignResource(self, resourceName=None):
        """
        """
        #
        defaultPort = 3306
        dbServer = 'mysql'
        self._assignResource(resourceName)
        infoD = {}
        # if not self.__cfgOb:
        #    return infoD
        #
        if (resourceName == "PRD"):
            infoD["DB_NAME"] = self.__cfgOb.get("SITE_REFDATA_PRD_DB_NAME")
            infoD["DB_HOST"] = self.__cfgOb.get("SITE_REFDATA_DB_HOST_NAME")
            infoD["DB_SOCKET"] = self.__cfgOb.get("SITE_REFDATA_DB_SOCKET", default=None)
            infoD["DB_PORT"] = self.__cfgOb.get("SITE_REFDATA_DB_PORT_NUMBER", default=defaultPort)

            infoD["DB_USER"] = self.__cfgOb.get("SITE_REFDATA_DB_USER_NAME")
            infoD["DB_PW"] = self.__cfgOb.get("SITE_REFDATA_DB_PASSWORD")

        elif (resourceName == "CC"):
            infoD["DB_NAME"] = self.__cfgOb.get("SITE_REFDATA_CC_DB_NAME")
            infoD["DB_HOST"] = self.__cfgOb.get("SITE_REFDATA_DB_HOST_NAME")
            infoD["DB_SOCKET"] = self.__cfgOb.get("SITE_REFDATA_DB_SOCKET", default=None)
            infoD["DB_PORT"] = self.__cfgOb.get("SITE_REFDATA_DB_PORT_NUMBER", default=defaultPort)

            infoD["DB_USER"] = self.__cfgOb.get("SITE_REFDATA_DB_USER_NAME")
            infoD["DB_PW"] = self.__cfgOb.get("SITE_REFDATA_DB_PASSWORD")

        elif (resourceName == "RCSB_INSTANCE"):
            infoD["DB_NAME"] = self.__cfgOb.get("SITE_INSTANCE_DB_NAME")
            infoD["DB_HOST"] = self.__cfgOb.get("SITE_INSTANCE_DB_HOST_NAME")
            infoD["DB_SOCKET"] = self.__cfgOb.get("SITE_INSTANCE_DB_SOCKET", default=None)
            infoD["DB_PORT"] = self.__cfgOb.get("SITE_INSTANCE_DB_PORT_NUMBER", default=defaultPort)

            self.__dbUser = self.__cfgOb.get("SITE_INSTANCE_DB_USER_NAME")
            infoD["DB_PW"] = self.__cfgOb.get("SITE_INSTANCE_DB_PASSWORD")

        elif (resourceName == "DA_INTERNAL"):
            infoD["DB_NAME"] = self.__cfgOb.get("SITE_DA_INTERNAL_DB_NAME")
            infoD["DB_HOST"] = self.__cfgOb.get("SITE_DA_INTERNAL_DB_HOST_NAME")
            infoD["DB_PORT"] = self.__cfgOb.get("SITE_DA_INTERNAL_DB_PORT_NUMBER", default=defaultPort)
            infoD["DB_SOCKET"] = self.__cfgOb.get("SITE_DA_INTERNAL_DB_SOCKET", default=None)

            infoD["DB_USER"] = self.__cfgOb.get("SITE_DA_INTERNAL_DB_USER_NAME")
            infoD["DB_PW"] = self.__cfgOb.get("SITE_DA_INTERNAL_DB_PASSWORD")

        elif (resourceName == "DA_INTERNAL_COMBINE"):
            infoD["DB_NAME"] = self.__cfgOb.get("SITE_DA_INTERNAL_COMBINE_DB_NAME")
            infoD["DB_HOST"] = self.__cfgOb.get("SITE_DA_INTERNAL_COMBINE_DB_HOST_NAME")
            infoD["DB_PORT"] = self.__cfgOb.get("SITE_DA_INTERNAL_COMBINE_DB_PORT_NUMBER", default=defaultPort)
            infoD["DB_SOCKET"] = self.__cfgOb.get("SITE_DA_INTERNAL_COMBINE_DB_SOCKET", default=None)

            infoD["DB_USER"] = self.__cfgOb.get("SITE_DA_INTERNAL_COMBINE_DB_USER_NAME")
            infoD["DB_PW"] = self.__cfgOb.get("SITE_DA_INTERNAL_COMBINE_DB_PASSWORD")
        elif (resourceName == "DISTRO"):
            infoD["DB_NAME"] = self.__cfgOb.get("SITE_DISTRO_DB_NAME")
            infoD["DB_HOST"] = self.__cfgOb.get("SITE_DISTRO_DB_HOST_NAME")
            infoD["DB_PORT"] = self.__cfgOb.get("SITE_DISTRO_DB_PORT_NUMBER", default=defaultPort)
            infoD["DB_SOCKET"] = self.__cfgOb.get("SITE_DISTRO_DB_SOCKET", default=None)

            infoD["DB_USER"] = self.__cfgOb.get("SITE_DISTRO_DB_USER_NAME")
            infoD["DB_PW"] = self.__cfgOb.get("SITE_DISTRO_DB_PASSWORD")

        elif (resourceName == "STATUS"):
            infoD["DB_NAME"] = self.__cfgOb.get("SITE_DB_DATABASE_NAME")
            infoD["DB_HOST"] = self.__cfgOb.get("SITE_DB_HOST_NAME")
            infoD["DB_PORT"] = self.__cfgOb.get("SITE_DB_PORT_NUMBER", default=defaultPort)
            infoD["DB_SOCKET"] = self.__cfgOb.get("SITE_DB_SOCKET", default=None)

            infoD["DB_USER"] = self.__cfgOb.get("SITE_DB_USER_NAME")
            infoD["DB_PW"] = self.__cfgOb.get("SITE_DB_PASSWORD")
        elif (resourceName == "MYSQL_DB"):
            infoD["DB_NAME"] = self.__cfgOb.get("MYSQL_DB_DATABASE_NAME")
            infoD["DB_HOST"] = self.__cfgOb.get("MYSQL_DB_HOST_NAME")
            infoD["DB_PORT"] = self.__cfgOb.get("MYSQL_DB_PORT_NUMBER", default=defaultPort)
            infoD["DB_SOCKET"] = self.__cfgOb.get("MYSQL_DB_SOCKET", default=None)

            infoD["DB_USER"] = self.__cfgOb.get("MYSQL_DB_USER_NAME")
            infoD["DB_PW"] = self.__cfgOb.get("MYSQL_DB_PASSWORD")
        else:
            pass

        infoD['DB_PORT'] = int(str(infoD['DB_PORT']))
        infoD['DB_SERVER'] = dbServer

        self.setPreferences(infoD)
        #
        return infoD

        #
    def __enter__(self):
        self.openConnection()
        return self.getClientConnection()

    def __exit__(self, *args):
        return self.closeConnection()
