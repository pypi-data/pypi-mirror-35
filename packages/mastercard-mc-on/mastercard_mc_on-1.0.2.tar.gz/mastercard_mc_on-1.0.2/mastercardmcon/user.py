#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 MasterCard International Incorporated
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#


from __future__ import absolute_import
from mastercardapicore import BaseObject
from mastercardapicore import RequestMap
from mastercardapicore import OperationConfig
from mastercardapicore import OperationMetadata
from mastercardmcon import ResourceConfig

class User(BaseObject):
    """
    
    """

    __config = {
        
        "7ce4ebff-b2c3-42b9-a66f-8549a83f0987" : OperationConfig("/bundle/profile/v1/users", "create", ["x-client-correlation-id"], []),
        
        "4a603498-6fff-44fc-9502-64a5399ab857" : OperationConfig("/bundle/profile/v1/users/{userId}", "delete", ["x-client-correlation-id"], []),
        
        "57ffa8b1-54b7-4844-83e3-0e8a59632e0d" : OperationConfig("/bundle/profile/v1/users/{userId}/patch", "create", ["x-client-correlation-id"], []),
        
        "4e93251a-5260-437c-a467-d8c92583f4cd" : OperationConfig("/bundle/profile/v1/users/{userId}", "read", ["x-client-correlation-id"], []),
        
        "662f4765-64c6-41fa-8449-d2b500725e21" : OperationConfig("/bundle/profile/v1/users/{userId}", "update", ["x-client-correlation-id"], []),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())


    @classmethod
    def createUser(cls,mapObj):
        """
        Creates object of type User

        @param Dict mapObj, containing the required parameters to create a new object
        @return User of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("7ce4ebff-b2c3-42b9-a66f-8549a83f0987", User(mapObj))









    @classmethod
    def deleteUserById(cls,id,map=None):
        """
        Delete object of type User by id

        @param str id
        @return User of the response of the deleted instance.
        @raise ApiException: raised an exception from the response status
        """

        mapObj =  RequestMap()
        if id:
            mapObj.set("id", id)

        if map:
            if (isinstance(map,RequestMap)):
                mapObj.setAll(map.getObject())
            else:
                mapObj.setAll(map)

        return BaseObject.execute("4a603498-6fff-44fc-9502-64a5399ab857", User(mapObj))

    def deleteUser(self):
        """
        Delete object of type User

        @return User of the response of the deleted instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("4a603498-6fff-44fc-9502-64a5399ab857", self)



    @classmethod
    def patchUser(cls,mapObj):
        """
        Creates object of type User

        @param Dict mapObj, containing the required parameters to create a new object
        @return User of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("57ffa8b1-54b7-4844-83e3-0e8a59632e0d", User(mapObj))










    @classmethod
    def readUser(cls,id,criteria=None):
        """
        Returns objects of type User by id and optional criteria
        @param str id
        @param dict criteria
        @return instance of User
        @raise ApiException: raised an exception from the response status
        """
        mapObj =  RequestMap()
        if id:
            mapObj.set("id", id)

        if criteria:
            if (isinstance(criteria,RequestMap)):
                mapObj.setAll(criteria.getObject())
            else:
                mapObj.setAll(criteria)

        return BaseObject.execute("4e93251a-5260-437c-a467-d8c92583f4cd", User(mapObj))



    def updateUser(self):
        """
        Updates an object of type User

        @return User object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("662f4765-64c6-41fa-8449-d2b500725e21", self)






