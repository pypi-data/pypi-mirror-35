/*!
  * Copyright 2017,  Digital Reasoning
  * 
  * Licensed under the Apache License, Version 2.0 (the "License");
  * you may not use this file except in compliance with the License.
  * You may obtain a copy of the License at
  * 
  *     http://www.apache.org/licenses/LICENSE-2.0
  * 
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  * 
*/

define(["generics/pagination","models/cloud-image"],function(e,i){"use strict";return e.extend({breadcrumbs:[{active:!1,title:"Cloud Accounts",href:"/accounts/"},{active:!1,title:window.stackdio.accountTitle,href:"/accounts/"+window.stackdio.accountId+"/"},{active:!0,title:"Images"}],model:i,baseUrl:"/images/",initialUrl:"/api/cloud/accounts/"+window.stackdio.accountId+"/images/",sortableFields:[{name:"name",displayName:"Name",width:"35%"},{name:"description",displayName:"Description",width:"40%"},{name:"imageId",displayName:"Image ID",width:"15%"}]})});