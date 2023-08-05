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

class Airport(BaseObject):
    """
    
    """

    __config = {
        
        "ac23bf7b-ebfb-4da7-b6f1-41ce785b342e" : OperationConfig("/loyalty/v1/airport/dmc", "query", ["x-client-correlation-id"], ["userId","panLastFourDigits"]),
        
        "24917d2d-8f24-4e61-ad29-e8bf82b596af" : OperationConfig("/loyalty/v1/airport/history", "query", ["x-client-correlation-id"], ["userId","panLastFourDigits","transactionDateFrom","transactionDateTo"]),
        
        "173d465c-509c-4068-895d-818089f319a3" : OperationConfig("/loyalty/v1/airport/lounges", "query", ["x-client-correlation-id"], ["userId","panLastFourDigits","searchText","preferredLanguage"]),
        
        "d8050e1a-f704-4dd3-8b1c-a4a23a0a722d" : OperationConfig("/loyalty/v1/airport/lounges/{loungeId}/detail", "query", ["x-client-correlation-id"], ["userId","panLastFourDigits","preferredLanguage"]),
        
        "6ae8cf60-28ba-420d-b682-78be28de9453" : OperationConfig("/loyalty/v1/users/{userId}/airport", "query", ["x-client-correlation-id"], ["panLastFourDigits"]),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())







    @classmethod
    def getDMC(cls,criteria):
        """
        Query objects of type Airport by id and optional criteria
        @param type criteria
        @return Airport object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("ac23bf7b-ebfb-4da7-b6f1-41ce785b342e", Airport(criteria))






    @classmethod
    def getLoungeHistory(cls,criteria):
        """
        Query objects of type Airport by id and optional criteria
        @param type criteria
        @return Airport object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("24917d2d-8f24-4e61-ad29-e8bf82b596af", Airport(criteria))






    @classmethod
    def getLounges(cls,criteria):
        """
        Query objects of type Airport by id and optional criteria
        @param type criteria
        @return Airport object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("173d465c-509c-4068-895d-818089f319a3", Airport(criteria))






    @classmethod
    def getLoungeDetail(cls,criteria):
        """
        Query objects of type Airport by id and optional criteria
        @param type criteria
        @return Airport object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("d8050e1a-f704-4dd3-8b1c-a4a23a0a722d", Airport(criteria))






    @classmethod
    def userAirportRegistrationStatus(cls,criteria):
        """
        Query objects of type Airport by id and optional criteria
        @param type criteria
        @return Airport object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("6ae8cf60-28ba-420d-b682-78be28de9453", Airport(criteria))


