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

define(["generics/permissions"],function(i){"use strict";return i.extend({permsUrl:"/api/cloud/images/"+window.stackdio.objectId+"/permissions/",saveUrl:"/images/"+window.stackdio.objectId+"/",init:function(){this._super(),this.breadcrumbs=[{active:!1,title:"Cloud Images",href:"/images/"},{active:!1,title:window.stackdio.imageTitle,href:this.saveUrl},{active:!0,title:"Permissions"}]}})});