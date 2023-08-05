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

class Benefits(BaseObject):
    """
    
    """

    __config = {
        
        "d473a1cd-5a7c-44a0-8367-af0eea042d5a" : OperationConfig("/loyalty/v1/benefits/assigned", "query", ["x-client-correlation-id"], ["ica","userId","panLastFourDigits","channel","preferredLanguage"]),
        
        "6fdf737d-6e77-4b61-add6-7cfcdf40cc4e" : OperationConfig("/loyalty/v1/benefits/{benefitId}/detail", "query", ["x-client-correlation-id"], ["ica","channel","preferredLanguage"]),
        
        "9cbb6183-7f65-4e72-9e98-b20ae1636756" : OperationConfig("/loyalty/v1/benefits", "query", ["x-client-correlation-id"], ["ica","cardProductType","channel","preferredLanguage"]),
        
        "c8e58df9-6a9b-4cae-a04a-57afb702c830" : OperationConfig("/loyalty/v1/benefits", "create", ["x-client-correlation-id"], []),
        
        "287f0aec-8380-4307-816c-28dc0f9aa174" : OperationConfig("/loyalty/v1/benefits/programterms", "query", ["x-client-correlation-id"], ["ica","preferredLanguage"]),
        
        "3538c731-dfad-44c7-8e70-ab9a806217a4" : OperationConfig("/loyalty/v1/users/{userId}/benefits", "query", ["x-client-correlation-id"], ["panLastFourDigits"]),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())







    @classmethod
    def getAssignedBenefits(cls,criteria):
        """
        Query objects of type Benefits by id and optional criteria
        @param type criteria
        @return Benefits object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("d473a1cd-5a7c-44a0-8367-af0eea042d5a", Benefits(criteria))






    @classmethod
    def getBenefitDetail(cls,criteria):
        """
        Query objects of type Benefits by id and optional criteria
        @param type criteria
        @return Benefits object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("6fdf737d-6e77-4b61-add6-7cfcdf40cc4e", Benefits(criteria))






    @classmethod
    def getBenefits(cls,criteria):
        """
        Query objects of type Benefits by id and optional criteria
        @param type criteria
        @return Benefits object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("9cbb6183-7f65-4e72-9e98-b20ae1636756", Benefits(criteria))

    @classmethod
    def selectBenefits(cls,mapObj):
        """
        Creates object of type Benefits

        @param Dict mapObj, containing the required parameters to create a new object
        @return Benefits of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("c8e58df9-6a9b-4cae-a04a-57afb702c830", Benefits(mapObj))











    @classmethod
    def getProgramTerms(cls,criteria):
        """
        Query objects of type Benefits by id and optional criteria
        @param type criteria
        @return Benefits object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("287f0aec-8380-4307-816c-28dc0f9aa174", Benefits(criteria))






    @classmethod
    def userBenefitsRegistrationStatus(cls,criteria):
        """
        Query objects of type Benefits by id and optional criteria
        @param type criteria
        @return Benefits object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("3538c731-dfad-44c7-8e70-ab9a806217a4", Benefits(criteria))


