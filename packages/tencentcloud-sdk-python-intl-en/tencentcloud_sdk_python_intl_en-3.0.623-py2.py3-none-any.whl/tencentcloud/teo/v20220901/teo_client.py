# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.teo.v20220901 import models


class TeoClient(AbstractClient):
    _apiVersion = '2022-09-01'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'


    def BindZoneToPlan(self, request):
        """This API is used to bind a site to a plan.

        :param request: Request instance for BindZoneToPlan.
        :type request: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.BindZoneToPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindZoneToPlan", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindZoneToPlanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckCertificate(self, request):
        """This API is used to verify a certificate.

        :param request: Request instance for CheckCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.CheckCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CheckCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCertificate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAliasDomain(self, request):
        """This API is used to create an alias domain name.

        :param request: Request instance for CreateAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAliasDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAliasDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApplicationProxy(self, request):
        """This API is used to create an application proxy.

        :param request: Request instance for CreateApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationProxyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApplicationProxyRule(self, request):
        """This API is used to create an application proxy rule.

        :param request: Request instance for CreateApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationProxyRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCredential(self, request):
        """Creates a credential for COS origin-pull.

        :param request: Request instance for CreateCredential.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCredentialRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCredential", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCredentialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCustomErrorPage(self, request):
        """This API is used to create a custom error page.

        :param request: Request instance for CreateCustomErrorPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateCustomErrorPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateCustomErrorPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomErrorPage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustomErrorPageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIpTableList(self, request):
        """This API is used to create an IP blocklist/allowlist.

        :param request: Request instance for CreateIpTableList.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateIpTableListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateIpTableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIpTableList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIpTableListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLogSet(self, request):
        """This API is used to create a CLS logset.

        :param request: Request instance for CreateLogSet.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateLogSetRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateLogSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogSet", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLogSetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLogTopicTask(self, request):
        """This API is used to create a shipping task.

        :param request: Request instance for CreateLogTopicTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateLogTopicTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateLogTopicTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogTopicTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLogTopicTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOriginGroup(self, request):
        """This API is used to create an origin group.

        :param request: Request instance for CreateOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOriginGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOriginGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePlanForZone(self, request):
        """This API is used to purchase a plan for a new site.

        :param request: Request instance for CreatePlanForZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePlanForZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlanForZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePlanForZoneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrefetchTask(self, request):
        """This API is used to create a pre-warming task.

        :param request: Request instance for CreatePrefetchTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePrefetchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrefetchTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrefetchTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePurgeTask(self, request):
        """This API is used to create a cache purging task.

        :param request: Request instance for CreatePurgeTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreatePurgeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePurgeTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePurgeTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateReplayTask(self, request):
        """This API is used to create a replay task for purging or pre-warming URLs.

        :param request: Request instance for CreateReplayTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateReplayTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateReplayTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReplayTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReplayTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRule(self, request):
        """This API is used to create a rule in the rule engine.

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityDropPage(self, request):
        """This API is used to create a custom block page.

        :param request: Request instance for CreateSecurityDropPage.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSecurityDropPageRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSecurityDropPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityDropPage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityDropPageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSpeedTesting(self, request):
        """This API is used to create a site testing task for a specified domain name.

        :param request: Request instance for CreateSpeedTesting.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateSpeedTestingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateSpeedTestingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSpeedTesting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSpeedTestingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateZone(self, request):
        """This API is used to access a new site.

        :param request: Request instance for CreateZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.CreateZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.CreateZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateZoneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAliasDomain(self, request):
        """This API is used to delete an alias domain name.

        :param request: Request instance for DeleteAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAliasDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAliasDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApplicationProxy(self, request):
        """This API is used to delete an application proxy.

        :param request: Request instance for DeleteApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationProxyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApplicationProxyRule(self, request):
        """This API is used to delete an application proxy rule.

        :param request: Request instance for DeleteApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationProxyRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLogTopicTask(self, request):
        """This API is used to delete a shipping task.

        :param request: Request instance for DeleteLogTopicTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteLogTopicTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteLogTopicTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogTopicTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLogTopicTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteOriginGroup(self, request):
        """This API is used to delete an origin group.

        :param request: Request instance for DeleteOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOriginGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteOriginGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRules(self, request):
        """This API is used to batch delete rules from the rule engine.

        :param request: Request instance for DeleteRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteZone(self, request):
        """This API is used to delete a site.

        :param request: Request instance for DeleteZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.DeleteZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DeleteZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteZoneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddableEntityList(self, request):
        """This API is used to query available shipping entities.

        :param request: Request instance for DescribeAddableEntityList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAddableEntityListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAddableEntityListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddableEntityList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddableEntityListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAliasDomains(self, request):
        """This API is used to query the information of alias domain names.

        :param request: Request instance for DescribeAliasDomains.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAliasDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAliasDomains", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAliasDomainsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationProxies(self, request):
        """This API is used to query the list of application proxies.

        :param request: Request instance for DescribeApplicationProxies.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeApplicationProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationProxies", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationProxiesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAvailablePlans(self, request):
        """This API is used to query plan options available for purchase.

        :param request: Request instance for DescribeAvailablePlans.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeAvailablePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailablePlans", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailablePlansResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBotClientIpList(self, request):
        """This API is used to query the list of bot attackers.

        :param request: Request instance for DescribeBotClientIpList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotClientIpListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotClientIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotClientIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotClientIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBotData(self, request):
        """This API is used to query the bot attack data recorded over time.

        :param request: Request instance for DescribeBotData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBotHitRuleDetail(self, request):
        """This API is used to query the details of a hit bot security rule.

        :param request: Request instance for DescribeBotHitRuleDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotHitRuleDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotHitRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotHitRuleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotHitRuleDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBotLog(self, request):
        """This API is used to query bot attack logs.

        :param request: Request instance for DescribeBotLog.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotLog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBotManagedRules(self, request):
        """This API is used to query a bot managed rule.

        :param request: Request instance for DescribeBotManagedRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotManagedRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotManagedRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotManagedRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotManagedRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBotTopData(self, request):
        """This API is used to query the top-ranked bot attack data.

        :param request: Request instance for DescribeBotTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeBotTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeBotTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotTopData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBotTopDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClientRuleList(self, request):
        """This API is used to query the information of blocked clients.

        :param request: Request instance for DescribeClientRuleList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeClientRuleListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeClientRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientRuleList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientRuleListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeContentQuota(self, request):
        """This API is used to query content management quotas.

        :param request: Request instance for DescribeContentQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeContentQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContentQuota", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContentQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSAttackData(self, request):
        """This API is used to query the DDoS attack data recorded over time.

        :param request: Request instance for DescribeDDoSAttackData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSAttackEvent(self, request):
        """This API is used to query the list of DDoS attack events.

        :param request: Request instance for DescribeDDoSAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackEventResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSAttackEventDetail(self, request):
        """This API is used to query the details of a DDoS attack event.

        :param request: Request instance for DescribeDDoSAttackEventDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackEventDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackEventDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSAttackSourceEvent(self, request):
        """This API is used to query the list of DDoS attackers.

        :param request: Request instance for DescribeDDoSAttackSourceEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackSourceEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackSourceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackSourceEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackSourceEventResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSAttackTopData(self, request):
        """This API is used to query the top-ranked DDoS attack data.

        :param request: Request instance for DescribeDDoSAttackTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSAttackTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSAttackTopData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSAttackTopDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSBlockList(self, request):
        """This API is used to query the list of DDoS blocking data.

        :param request: Request instance for DescribeDDoSBlockList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSBlockListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSBlockListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSBlockList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSBlockListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSMajorAttackEvent(self, request):
        """This API is used to query the list of large attack events.

        :param request: Request instance for DescribeDDoSMajorAttackEvent.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSMajorAttackEventRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSMajorAttackEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSMajorAttackEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSMajorAttackEventResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSPolicy(self, request):
        """This API is used to query the DDoS protection configuration.

        :param request: Request instance for DescribeDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDefaultCertificates(self, request):
        """This API is used to query a list of default certificates.

        :param request: Request instance for DescribeDefaultCertificates.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDefaultCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultCertificates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDefaultCertificatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDistributionL4AccessData(self, request):
        """This API is used to query the data of L4 connection duration over time.

        :param request: Request instance for DescribeDistributionL4AccessData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDistributionL4AccessDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDistributionL4AccessDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDistributionL4AccessData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDistributionL4AccessDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDnsData(self, request):
        """This API is used to get DNS requests.

        :param request: Request instance for DescribeDnsData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDnsDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDnsDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnsData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDnsDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDnssec(self, request):
        """This API is used to query DNSSEC information.

        :param request: Request instance for DescribeDnssec.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeDnssecRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeDnssecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnssec", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDnssecResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHostsSetting(self, request):
        """This API is used to query detailed domain name configuration.

        :param request: Request instance for DescribeHostsSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeHostsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostsSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHostsSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIdentifications(self, request):
        """This API is used to query the verification information of a site.

        :param request: Request instance for DescribeIdentifications.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeIdentificationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdentifications", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIdentificationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogSets(self, request):
        """This API is used to get a list of logsets.

        :param request: Request instance for DescribeLogSets.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogSetsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogSetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogSets", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogSetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogTopicTaskDetail(self, request):
        """This API is used to get the details of a shipping task.

        :param request: Request instance for DescribeLogTopicTaskDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogTopicTaskDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogTopicTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogTopicTaskDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogTopicTaskDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogTopicTasks(self, request):
        """This API is used to get a list of shipping tasks.

        :param request: Request instance for DescribeLogTopicTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeLogTopicTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeLogTopicTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogTopicTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogTopicTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOriginGroup(self, request):
        """This API is used to obtain a list of origin groups.

        :param request: Request instance for DescribeOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOriginGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOriginGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOverviewL7Data(self, request):
        """This API is used to query the L7 traffic summary statistics recorded over time.

        :param request: Request instance for DescribeOverviewL7Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeOverviewL7DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewL7Data", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOverviewL7DataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrefetchTasks(self, request):
        """This API is used to query the pre-warming task status.

        :param request: Request instance for DescribePrefetchTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePrefetchTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrefetchTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrefetchTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePurgeTasks(self, request):
        """Querying the cache purging history

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurgeTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRateLimitIntelligenceRule(self, request):
        """This API is used to query an intelligent rate limiting rule.

        :param request: Request instance for DescribeRateLimitIntelligenceRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRateLimitIntelligenceRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRateLimitIntelligenceRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRateLimitIntelligenceRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRateLimitIntelligenceRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRules(self, request):
        """This API is used to query the rules in the rule engine.

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRulesSetting(self, request):
        """This API is used to return the list of the settings of the rule engine that can be used for request match and their detailed recommended configuration information.

        :param request: Request instance for DescribeRulesSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeRulesSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRulesSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupManagedRules(self, request):
        """This API is used to obtain a managed rule group.

        :param request: Request instance for DescribeSecurityGroupManagedRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityGroupManagedRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityGroupManagedRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupManagedRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupManagedRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityPolicy(self, request):
        """This API is used to query the security protection configuration. You must either specify "ZoneId+Entity" or "TemplateId".

        :param request: Request instance for DescribeSecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityPolicyList(self, request):
        """This API is used to query all protected subdomain names.

        :param request: Request instance for DescribeSecurityPolicyList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityPolicyRegions(self, request):
        """This API is used to query information of all regions.

        :param request: Request instance for DescribeSecurityPolicyRegions.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyRegionsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPolicyRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyRegions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityPortraitRules(self, request):
        """This API is used to query user profiling rules.

        :param request: Request instance for DescribeSecurityPortraitRules.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPortraitRulesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityPortraitRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPortraitRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPortraitRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityRuleId(self, request):
        """This API is used to query a security rule.

        :param request: Request instance for DescribeSecurityRuleId.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityRuleIdRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSecurityRuleIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityRuleId", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityRuleIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSingleL7AnalysisData(self, request):
        """This API is used to query the list of L7 dimensional data.

        :param request: Request instance for DescribeSingleL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSingleL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSingleL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSingleL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSingleL7AnalysisDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSpeedTestingDetails(self, request):
        """This API is used to query the site’s load speed across regions.

        :param request: Request instance for DescribeSpeedTestingDetails.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingDetailsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpeedTestingDetails", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpeedTestingDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSpeedTestingMetricData(self, request):
        """This API is used to query the result of a site test.

        :param request: Request instance for DescribeSpeedTestingMetricData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingMetricDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpeedTestingMetricData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpeedTestingMetricDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSpeedTestingQuota(self, request):
        """This API is used to query the quota limit on site tests.

        :param request: Request instance for DescribeSpeedTestingQuota.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingQuotaRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeSpeedTestingQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpeedTestingQuota", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpeedTestingQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTimingL4AccessData(self, request):
        """This API is used to query the number of L4 connections over time.

        :param request: Request instance for DescribeTimingL4AccessData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4AccessDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4AccessDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL4AccessData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimingL4AccessDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTimingL4Data(self, request):
        """This API is used to query the list of L4 traffic data recorded over time.

        :param request: Request instance for DescribeTimingL4Data.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL4DataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL4Data", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimingL4DataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTimingL7AnalysisData(self, request):
        """This API is used to query the L7 data recorded over time.

        :param request: Request instance for DescribeTimingL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimingL7AnalysisDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTimingL7CacheData(self, request):
        """This API is used to query the time-series L7 cached data.

        :param request: Request instance for DescribeTimingL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTimingL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimingL7CacheData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimingL7CacheDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTopL7AnalysisData(self, request):
        """This API is used to query the top-ranked L7 traffic data.

        :param request: Request instance for DescribeTopL7AnalysisData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7AnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7AnalysisData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopL7AnalysisDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTopL7CacheData(self, request):
        """This API is used to query the cached L7 top-ranked data.

        :param request: Request instance for DescribeTopL7CacheData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeTopL7CacheDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopL7CacheData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopL7CacheDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebManagedRulesData(self, request):
        """This API is used to query the WAF attack data recorded over time.

        :param request: Request instance for DescribeWebManagedRulesData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebManagedRulesDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebManagedRulesHitRuleDetail(self, request):
        """This API is used to query the details of a hit WAF security rule.

        :param request: Request instance for DescribeWebManagedRulesHitRuleDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesHitRuleDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesHitRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesHitRuleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebManagedRulesHitRuleDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebManagedRulesLog(self, request):
        """This API is used to query web attack logs.

        :param request: Request instance for DescribeWebManagedRulesLog.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesLogRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebManagedRulesLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebManagedRulesLog", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebManagedRulesLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebProtectionAttackEvents(self, request):
        """This API is used to query the list of CC attack events.

        :param request: Request instance for DescribeWebProtectionAttackEvents.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionAttackEventsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionAttackEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionAttackEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebProtectionClientIpList(self, request):
        """This API is used to query the information of CC attackers.

        :param request: Request instance for DescribeWebProtectionClientIpList.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionClientIpListRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionClientIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionClientIpList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionClientIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebProtectionData(self, request):
        """This API is used to query the CC protection data recorded over time.

        :param request: Request instance for DescribeWebProtectionData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebProtectionHitRuleDetail(self, request):
        """This API is used to query the details of a hit CC protection rule.

        :param request: Request instance for DescribeWebProtectionHitRuleDetail.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionHitRuleDetailRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionHitRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionHitRuleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionHitRuleDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebProtectionTopData(self, request):
        """This API is used to query the top-ranked CC protection data.

        :param request: Request instance for DescribeWebProtectionTopData.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionTopDataRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeWebProtectionTopDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebProtectionTopData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebProtectionTopDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneDDoSPolicy(self, request):
        """This API is used to query all DDoS mitigation configuration.

        :param request: Request instance for DescribeZoneDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneDDoSPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneSetting(self, request):
        """This API is used to query the site configuration.

        :param request: Request instance for DescribeZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZones(self, request):
        """This API is used to query the list of user sites.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.teo.v20220901.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadL4Logs(self, request):
        """This API is used to download L4 logs.

        :param request: Request instance for DownloadL4Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL4LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL4Logs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadL4LogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadL7Logs(self, request):
        """This API is used to download L7 logs.

        :param request: Request instance for DownloadL7Logs.
        :type request: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.DownloadL7LogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadL7Logs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadL7LogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IdentifyZone(self, request):
        """This API is used to verify ownership of the site.

        :param request: Request instance for IdentifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.IdentifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IdentifyZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IdentifyZoneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmConfig(self, request):
        """This API is used to modify alarm configuration.

        :param request: Request instance for ModifyAlarmConfig.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAlarmConfigRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAlarmConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmDefaultThreshold(self, request):
        """This API is used to modify the default alarm threshold.

        :param request: Request instance for ModifyAlarmDefaultThreshold.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAlarmDefaultThresholdRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAlarmDefaultThresholdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmDefaultThreshold", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmDefaultThresholdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAliasDomain(self, request):
        """This API is used to modify an alias domain name.

        :param request: Request instance for ModifyAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAliasDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAliasDomainStatus(self, request):
        """This API is used to modify the status of an alias domain name.

        :param request: Request instance for ModifyAliasDomainStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyAliasDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAliasDomainStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAliasDomainStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationProxy(self, request):
        """This API is used to modify an application proxy.

        :param request: Request instance for ModifyApplicationProxy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationProxyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationProxyRule(self, request):
        """This API is used to modify an application proxy rule.

        :param request: Request instance for ModifyApplicationProxyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationProxyRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationProxyRuleStatus(self, request):
        """This API is used to modify the status of an application proxy rule.

        :param request: Request instance for ModifyApplicationProxyRuleStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyRuleStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationProxyRuleStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationProxyStatus(self, request):
        """This API is used to modify the status of an application proxy.

        :param request: Request instance for ModifyApplicationProxyStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyApplicationProxyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationProxyStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationProxyStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDDoSPolicy(self, request):
        """This API is used to modify DDoS mitigation configuration.

        :param request: Request instance for ModifyDDoSPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDDoSPolicyHost(self, request):
        """This API is used to enable high availability for domain names.

        :param request: Request instance for ModifyDDoSPolicyHost.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSPolicyHostRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDDoSPolicyHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSPolicyHost", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyHostResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDefaultCertificate(self, request):
        """This example shows you how to modify the status of a default certificate.

        :param request: Request instance for ModifyDefaultCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDefaultCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDefaultCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultCertificate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDefaultCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDnssec(self, request):
        """This API is used to modify the DNSSEC status of a site.

        :param request: Request instance for ModifyDnssec.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyDnssecRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyDnssecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDnssec", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDnssecResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyHostsCertificate(self, request):
        """This API is used to modify the certificate of a domain name.

        :param request: Request instance for ModifyHostsCertificate.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyHostsCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostsCertificate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHostsCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLogTopicTask(self, request):
        """This API is used to modify a shipping task.

        :param request: Request instance for ModifyLogTopicTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyLogTopicTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyLogTopicTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogTopicTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLogTopicTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyOriginGroup(self, request):
        """This API is used to modify an origin group.

        :param request: Request instance for ModifyOriginGroup.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyOriginGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOriginGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyOriginGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRule(self, request):
        """This API is used to modify a rule in the rule engine.

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRulePriority(self, request):
        """This API is used to modify the priority of a rule in the rule engine.

        :param request: Request instance for ModifyRulePriority.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyRulePriorityRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyRulePriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRulePriority", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRulePriorityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityPolicy(self, request):
        """This API is used to modify the web and bot security configurations.

        :param request: Request instance for ModifySecurityPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityWafGroupPolicy(self, request):
        """This API is used to modify a managed rule.

        :param request: Request instance for ModifySecurityWafGroupPolicy.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifySecurityWafGroupPolicyRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifySecurityWafGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityWafGroupPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityWafGroupPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyZone(self, request):
        """This API is used to modify a site.

        :param request: Request instance for ModifyZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyZoneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyZoneCnameSpeedUp(self, request):
        """This API is used to modify the CNAME acceleration status.

        :param request: Request instance for ModifyZoneCnameSpeedUp.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneCnameSpeedUpRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneCnameSpeedUpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneCnameSpeedUp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyZoneCnameSpeedUpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyZoneSetting(self, request):
        """This API is used to modify the site configuration.

        :param request: Request instance for ModifyZoneSetting.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyZoneSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyZoneStatus(self, request):
        """This API is used to change the site status.

        :param request: Request instance for ModifyZoneStatus.
        :type request: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ModifyZoneStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyZoneStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyZoneStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReclaimAliasDomain(self, request):
        """To reclaim a site and its associated alias domain names, specify the "ZoneId" field; to reclaim an alias domain name that is already added, specify the "ZoneName" filed.

        :param request: Request instance for ReclaimAliasDomain.
        :type request: :class:`tencentcloud.teo.v20220901.models.ReclaimAliasDomainRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ReclaimAliasDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReclaimAliasDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReclaimAliasDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReclaimZone(self, request):
        """This API is used to reclaim a site from other users after its ownership is verified.

        :param request: Request instance for ReclaimZone.
        :type request: :class:`tencentcloud.teo.v20220901.models.ReclaimZoneRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.ReclaimZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReclaimZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReclaimZoneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchLogTopicTask(self, request):
        """This API is used to enable or disable a shipping task.

        :param request: Request instance for SwitchLogTopicTask.
        :type request: :class:`tencentcloud.teo.v20220901.models.SwitchLogTopicTaskRequest`
        :rtype: :class:`tencentcloud.teo.v20220901.models.SwitchLogTopicTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchLogTopicTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchLogTopicTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)