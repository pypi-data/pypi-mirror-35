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

class Offers(BaseObject):
    """
    
    """

    __config = {
        
        "78bceb6f-d1a9-4b1d-83ff-fe33d3825ff1" : OperationConfig("/loyalty/v1/offers", "query", ["x-client-correlation-id"], ["userId","preferredLanguage","sort","category","featured","favorite","partner","latitude","longitude","searchRadius"]),
        
        "29ee5afc-430a-4516-b877-95ba37cbe7fb" : OperationConfig("/loyalty/v1/offers/{offerId}/activate", "create", ["x-client-correlation-id"], []),
        
        "1691d4d2-83eb-4aa5-b586-2a569e700e94" : OperationConfig("/loyalty/v1/offers/{offerId}/detail", "query", ["x-client-correlation-id"], ["userId","preferredLanguage"]),
        
        "eba51ec1-c3f8-42b2-97c6-3cc4de1f4980" : OperationConfig("/loyalty/v1/offers/{offerId}/favorite", "create", ["x-client-correlation-id"], []),
        
        "5ff409d1-a5c0-4ffa-89cb-ccb590cb6ada" : OperationConfig("/loyalty/v1/offers/{offerId}/redeem", "create", ["x-client-correlation-id"], []),
        
        "b01435b7-4a30-4565-add4-b1a07a121972" : OperationConfig("/loyalty/v1/offers/{offerId}/unfavorite", "create", ["x-client-correlation-id"], []),
        
        "9d01ea5f-5310-480f-96b7-97b4fdc1f28b" : OperationConfig("/loyalty/v1/offers/promo", "create", ["x-client-correlation-id"], []),
        
        "33f817b3-c538-4286-8dfd-9c298c563aca" : OperationConfig("/loyalty/v1/offers/redeemed", "query", ["x-client-correlation-id"], ["userId","preferredLanguage"]),
        
        "ef8538b1-c137-46da-bb7a-a54a8064cbcd" : OperationConfig("/loyalty/v1/points/expiring", "query", ["x-client-correlation-id"], ["userId"]),
        
        "71325c24-5083-45dc-9adc-44774ad2050a" : OperationConfig("/loyalty/v1/points", "query", ["x-client-correlation-id"], ["userId"]),
        
        "cf01e37d-80e6-4779-b1e1-3f13b1d4346a" : OperationConfig("/loyalty/v1/users/{userId}/offers", "query", ["x-client-correlation-id"], []),
        
        "58eeb20d-66b7-49b7-9200-5f39d8366e0b" : OperationConfig("/loyalty/v1/vouchers", "query", ["x-client-correlation-id"], ["userId"]),
        
        "1fd5912b-0e42-440e-b99c-67829f27aa6f" : OperationConfig("/loyalty/v1/vouchers/{voucherId}/detail", "query", ["x-client-correlation-id"], ["userId"]),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())







    @classmethod
    def getOffers(cls,criteria):
        """
        Query objects of type Offers by id and optional criteria
        @param type criteria
        @return Offers object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("78bceb6f-d1a9-4b1d-83ff-fe33d3825ff1", Offers(criteria))

    @classmethod
    def activateOffer(cls,mapObj):
        """
        Creates object of type Offers

        @param Dict mapObj, containing the required parameters to create a new object
        @return Offers of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("29ee5afc-430a-4516-b877-95ba37cbe7fb", Offers(mapObj))











    @classmethod
    def getOfferDetail(cls,criteria):
        """
        Query objects of type Offers by id and optional criteria
        @param type criteria
        @return Offers object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("1691d4d2-83eb-4aa5-b586-2a569e700e94", Offers(criteria))

    @classmethod
    def favoriteOffer(cls,mapObj):
        """
        Creates object of type Offers

        @param Dict mapObj, containing the required parameters to create a new object
        @return Offers of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("eba51ec1-c3f8-42b2-97c6-3cc4de1f4980", Offers(mapObj))






    @classmethod
    def redeemOffer(cls,mapObj):
        """
        Creates object of type Offers

        @param Dict mapObj, containing the required parameters to create a new object
        @return Offers of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("5ff409d1-a5c0-4ffa-89cb-ccb590cb6ada", Offers(mapObj))






    @classmethod
    def unfavoriteOffer(cls,mapObj):
        """
        Creates object of type Offers

        @param Dict mapObj, containing the required parameters to create a new object
        @return Offers of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("b01435b7-4a30-4565-add4-b1a07a121972", Offers(mapObj))






    @classmethod
    def submitOfferPromo(cls,mapObj):
        """
        Creates object of type Offers

        @param Dict mapObj, containing the required parameters to create a new object
        @return Offers of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("9d01ea5f-5310-480f-96b7-97b4fdc1f28b", Offers(mapObj))











    @classmethod
    def getRedeemedOffers(cls,criteria):
        """
        Query objects of type Offers by id and optional criteria
        @param type criteria
        @return Offers object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("33f817b3-c538-4286-8dfd-9c298c563aca", Offers(criteria))






    @classmethod
    def getPointsExpiring(cls,criteria):
        """
        Query objects of type Offers by id and optional criteria
        @param type criteria
        @return Offers object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("ef8538b1-c137-46da-bb7a-a54a8064cbcd", Offers(criteria))






    @classmethod
    def getPoints(cls,criteria):
        """
        Query objects of type Offers by id and optional criteria
        @param type criteria
        @return Offers object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("71325c24-5083-45dc-9adc-44774ad2050a", Offers(criteria))






    @classmethod
    def userOffersRegistrationStatus(cls,criteria):
        """
        Query objects of type Offers by id and optional criteria
        @param type criteria
        @return Offers object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("cf01e37d-80e6-4779-b1e1-3f13b1d4346a", Offers(criteria))






    @classmethod
    def getVouchers(cls,criteria):
        """
        Query objects of type Offers by id and optional criteria
        @param type criteria
        @return Offers object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("58eeb20d-66b7-49b7-9200-5f39d8366e0b", Offers(criteria))






    @classmethod
    def getVoucherDetail(cls,criteria):
        """
        Query objects of type Offers by id and optional criteria
        @param type criteria
        @return Offers object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("1fd5912b-0e42-440e-b99c-67829f27aa6f", Offers(criteria))


