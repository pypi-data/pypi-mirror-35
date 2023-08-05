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
class AddUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ims', '2017-04-30', 'AddUser','ims')

	def get_EmployeeType(self):
		return self.get_query_params().get('EmployeeType')

	def set_EmployeeType(self,EmployeeType):
		self.add_query_param('EmployeeType',EmployeeType)

	def get_Comments(self):
		return self.get_query_params().get('Comments')

	def set_Comments(self,Comments):
		self.add_query_param('Comments',Comments)

	def get_JobTitle(self):
		return self.get_query_params().get('JobTitle')

	def set_JobTitle(self,JobTitle):
		self.add_query_param('JobTitle',JobTitle)

	def get_HomeAddress(self):
		return self.get_query_params().get('HomeAddress')

	def set_HomeAddress(self,HomeAddress):
		self.add_query_param('HomeAddress',HomeAddress)

	def get_EmployeeId(self):
		return self.get_query_params().get('EmployeeId')

	def set_EmployeeId(self,EmployeeId):
		self.add_query_param('EmployeeId',EmployeeId)

	def get_Enabled(self):
		return self.get_query_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_query_param('Enabled',Enabled)

	def get_UserPrincipalName(self):
		return self.get_query_params().get('UserPrincipalName')

	def set_UserPrincipalName(self,UserPrincipalName):
		self.add_query_param('UserPrincipalName',UserPrincipalName)

	def get_WorkAddress(self):
		return self.get_query_params().get('WorkAddress')

	def set_WorkAddress(self,WorkAddress):
		self.add_query_param('WorkAddress',WorkAddress)

	def get_DisplayName(self):
		return self.get_query_params().get('DisplayName')

	def set_DisplayName(self,DisplayName):
		self.add_query_param('DisplayName',DisplayName)

	def get_MobilePhone(self):
		return self.get_query_params().get('MobilePhone')

	def set_MobilePhone(self,MobilePhone):
		self.add_query_param('MobilePhone',MobilePhone)

	def get_WorkPhone(self):
		return self.get_query_params().get('WorkPhone')

	def set_WorkPhone(self,WorkPhone):
		self.add_query_param('WorkPhone',WorkPhone)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_Email(self):
		return self.get_query_params().get('Email')

	def set_Email(self,Email):
		self.add_query_param('Email',Email)