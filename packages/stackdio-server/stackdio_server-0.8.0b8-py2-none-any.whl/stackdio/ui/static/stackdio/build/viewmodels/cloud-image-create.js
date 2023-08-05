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

define(["jquery","knockout","ladda","bootbox","select2"],function(e,t,a,r){"use strict";return function(){var s=this;s.breadcrumbs=[{active:!1,title:"Cloud Images",href:"/images/"},{active:!0,title:"New"}],s.accountSelector=e("#imageAccount"),s.sizeSelector=e("#imageDefaultInstanceSize"),s.accountSelector.select2({ajax:{url:"/api/cloud/accounts/",dataType:"json",delay:100,data:function(e){return{title:e.term}},processResults:function(e){return e.results.forEach(function(e){e.text=e.title}),e},cache:!0},theme:"bootstrap",placeholder:"Select an account...",templateResult:function(e){return e.loading?e.text:e.title+"  --  "+e.description},minimumInputLength:0}),s.accountSelector.on("select2:select",function(e){var t=e.params.data;s.accountId(t.id),s.sizeSelector.select2({ajax:{url:"/api/cloud/providers/"+t.provider+"/instance_sizes/",dataType:"json",delay:100,data:function(e){return{instance_id:e.term}},processResults:function(e){return e.results.forEach(function(e){e.id=e.instance_id,e.text=e.instance_id}),e},cache:!0},disabled:!1,theme:"bootstrap",placeholder:"Select an instance size...",minimumInputLength:0})}),s.sizeSelector.select2({data:[],theme:"bootstrap",placeholder:"Select an account first",disabled:!0}),s.sizeSelector.on("select2:select",function(e){var t=e.params.data;s.defaultInstanceSize(t.instance_id)}),s.accountId=t.observable(),s.title=t.observable(),s.description=t.observable(),s.imageId=t.observable(),s.defaultInstanceSize=t.observable(),s.sshUser=t.observable(),s.reset=function(){s.accountId(null),s.title(""),s.description(""),s.imageId(""),s.defaultInstanceSize(""),s.sshUser("")},s.removeErrors=function(t){t.forEach(function(t){var a=e("#"+t);a.removeClass("has-error"),a.find(".help-block").remove()})},s.createCloudImage=function(){var t=["account","title","description","image_id","default_instance_size","ssh_user"];s.removeErrors(t);var n=a.create(document.querySelector("#create-button"));n.start(),e.ajax({method:"POST",url:"/api/cloud/images/",data:JSON.stringify({account:s.accountId(),title:s.title(),description:s.description(),image_id:s.imageId(),default_instance_size:s.defaultInstanceSize(),ssh_user:s.sshUser()})}).always(function(){n.stop()}).done(function(){window.location="/images/"}).fail(function(a){var s="";try{var n=JSON.parse(a.responseText);for(var i in n)if(n.hasOwnProperty(i))if(t.indexOf(i)>=0){var c=e("#"+i);c.addClass("has-error"),n[i].forEach(function(e){c.append('<span class="help-block">'+e+"</span>")})}else if("non_field_errors"===i)n[i].forEach(function(t){if(t.indexOf("title")>=0){var a=e("#title");a.addClass("has-error"),a.append('<span class="help-block">A image with this title already exists.</span>')}});else{var o=i.replace("_"," ");n[i].forEach(function(e){s+="<dt>"+o+"</dt><dd>"+e+"</dd>"})}s&&(s='<dl class="dl-horizontal">'+s+"</dl>")}catch(e){s="Oops... there was a server error.  This has been reported to your administrators."}s&&r.alert({title:"Error creating image",message:s})})},s.reset()}});