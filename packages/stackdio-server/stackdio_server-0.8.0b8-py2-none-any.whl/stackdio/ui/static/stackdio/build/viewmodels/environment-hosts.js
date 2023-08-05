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

define(["jquery","knockout","bootbox","generics/pagination","models/environment"],function(e,n,i,t,s){"use strict";return t.extend({breadcrumbs:[{active:!1,title:"Environments",href:"/environments/"},{active:!1,title:window.stackdio.environmentName,href:"/environments/"+window.stackdio.environmentName+"/"},{active:!0,title:"Hosts"}],environment:n.observable(),autoRefresh:!0,model:Object,baseUrl:"/environments/",initialUrl:"/api/environments/"+window.stackdio.environmentName+"/hosts/",sortableFields:[{name:"hostname",displayName:"Hostname",width:"35%"},{name:"roles",displayName:"Roles",width:"40%"},{name:"ip_addresses",displayName:"IP Addresses",width:"25%"}],init:function(){this._super(),this.environment(new s(window.stackdio.environmentName,this))}})});