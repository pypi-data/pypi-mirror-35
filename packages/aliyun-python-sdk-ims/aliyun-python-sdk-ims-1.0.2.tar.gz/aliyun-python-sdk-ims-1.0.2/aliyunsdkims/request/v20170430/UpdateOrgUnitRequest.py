# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class UpdateOrgUnitRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ims', '2017-04-30', 'UpdateOrgUnit','ims')

	def get_NewComments(self):
		return self.get_query_params().get('NewComments')

	def set_NewComments(self,NewComments):
		self.add_query_param('NewComments',NewComments)

	def get_NewOrgUnitName(self):
		return self.get_query_params().get('NewOrgUnitName')

	def set_NewOrgUnitName(self,NewOrgUnitName):
		self.add_query_param('NewOrgUnitName',NewOrgUnitName)

	def get_NewParentOrgUnitId(self):
		return self.get_query_params().get('NewParentOrgUnitId')

	def set_NewParentOrgUnitId(self,NewParentOrgUnitId):
		self.add_query_param('NewParentOrgUnitId',NewParentOrgUnitId)

	def get_NewParentOrgUnitPath(self):
		return self.get_query_params().get('NewParentOrgUnitPath')

	def set_NewParentOrgUnitPath(self,NewParentOrgUnitPath):
		self.add_query_param('NewParentOrgUnitPath',NewParentOrgUnitPath)

	def get_OrgUnitId(self):
		return self.get_query_params().get('OrgUnitId')

	def set_OrgUnitId(self,OrgUnitId):
		self.add_query_param('OrgUnitId',OrgUnitId)

	def get_OrgUnitPath(self):
		return self.get_query_params().get('OrgUnitPath')

	def set_OrgUnitPath(self,OrgUnitPath):
		self.add_query_param('OrgUnitPath',OrgUnitPath)

	def get_NewManagerId(self):
		return self.get_query_params().get('NewManagerId')

	def set_NewManagerId(self,NewManagerId):
		self.add_query_param('NewManagerId',NewManagerId)