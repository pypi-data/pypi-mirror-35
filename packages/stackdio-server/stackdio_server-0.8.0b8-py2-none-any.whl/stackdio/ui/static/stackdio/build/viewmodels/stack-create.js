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

define(["jquery","knockout","ladda","bootbox","utils/formula-versions","models/formula-version","fuelux","select2"],function(e,r,t,s,o,n){"use strict";return function(){var a=this;a.breadcrumbs=[{active:!1,title:"Stacks",href:"/stacks/"},{active:!0,title:"New"}],a.blueprintSelector=e("#stackBlueprint"),window.stackdio.blueprintId&&a.blueprintSelector.append('<option value="'+window.stackdio.blueprintId+'" title="'+window.stackdio.blueprintText+'">'+window.stackdio.blueprintText+"</option>"),a.blueprintSelector.select2({ajax:{url:"/api/blueprints/",dataType:"json",delay:100,data:function(e){return{q:e.term}},processResults:function(e){return e.results.forEach(function(e){e.text=e.title}),e},cache:!0},theme:"bootstrap",placeholder:"Select a blueprint...",templateResult:function(e){return e.loading?e.text:e.title+"  --  "+e.description},minimumInputLength:0}),a.selectBlueprint=function(r){function t(r){e.ajax({method:"GET",url:r}).done(function(e){i.push.apply(i,e.results.map(function(e){return new n(e,a)})),null===e.next?(a.formulaVersions(i),a.formulas?a.createSelectors():o.getAllFormulas(function(e){a.formulas=e,a.createSelectors()})):t(e.next)})}a.createUsers(r.create_users),a.blueprintId(r.id);var s=["blueprint","title","description","create_users","namespace","properties"];a.removeErrors(s),e.ajax({method:"GET",url:r.properties}).done(function(e){a.properties(e)});var i=[];t(r.formula_versions)},a.blueprintSelector.on("select2:select",function(e){var r=e.params.data;a.selectBlueprint(r)}),a.blueprintId=r.observable(),a.title=r.observable(),a.description=r.observable(),a.createUsers=r.observable(),a.namespace=r.observable(),a.properties=r.observable({}),a.formulaVersions=r.observableArray([]),a.formulas=null,a.versionsReady=r.observable(),a.validProperties=!0,a.createButton=null,a.propertiesJSON=r.pureComputed({read:function(){return r.toJSON(a.properties(),null,3)},write:function(e){try{a.properties(JSON.parse(e)),a.validProperties=!0}catch(e){a.validProperties=!1}}}),a.subscription=null,a.reset=function(){a.subscription&&a.subscription.dispose();var r=e(".checkbox-custom");a.subscription=a.createUsers.subscribe(function(e){e?r.checkbox("check"):r.checkbox("uncheck")}),a.blueprintId(null),a.title(""),a.description(""),a.createUsers(!1),a.namespace(""),a.properties({}),a.formulaVersions([]),a.versionsReady(!1),window.stackdio.blueprintId&&(a.blueprintSelector.val(window.stackdio.blueprintId).trigger("change"),e.ajax({method:"GET",url:"/api/blueprints/"+window.stackdio.blueprintId+"/"}).done(function(e){a.selectBlueprint(e)}))},a.createSelectors=function(){var e=[];a.formulaVersions().forEach(function(r){o.createVersionSelector(r,a.formulas)||e.push(r)}),e.forEach(function(e){a.formulaVersions.remove(e)}),a.versionsReady(!0)},a.removeErrors=function(r){r.forEach(function(r){var t=e("#"+r);t.removeClass("has-error"),t.find(".help-block").remove()})},a.getVersionsData=function(){return a.formulaVersions().map(function(e){return{formula:e.formula(),version:e.version()}})},a.createStack=function(){var r=["blueprint","title","description","create_users","namespace","properties"];if(a.removeErrors(r),!a.validProperties){var o=e("#properties");return o.addClass("has-error"),void o.append('<span class="help-block">Invalid JSON.</span>')}var n=t.create(document.querySelector("#create-button"));n.start(),e.ajax({method:"POST",url:"/api/stacks/",data:JSON.stringify({blueprint:a.blueprintId(),title:a.title(),description:a.description(),create_users:a.createUsers(),namespace:a.namespace(),properties:a.properties(),formula_versions:a.getVersionsData()})}).always(function(){n.stop()}).done(function(){window.location="/stacks/"}).fail(function(t){var o="";try{var n=JSON.parse(t.responseText);for(var a in n)if(n.hasOwnProperty(a))if(r.indexOf(a)>=0){var i=e("#"+a);i.addClass("has-error"),n[a].forEach(function(e){i.append('<span class="help-block">'+e+"</span>")})}else if("non_field_errors"===a)n[a].forEach(function(r){if(r.indexOf("title")>=0){var t=e("#title");t.addClass("has-error"),t.append('<span class="help-block">A stack with this title already exists.</span>')}});else{var l=a.replace("_"," ");n[a].forEach(function(e){o+="<dt>"+l+"</dt><dd>"+e+"</dd>"})}o&&(o='<dl class="dl-horizontal">'+o+"</dl>")}catch(e){o="Oops... there was a server error.  This has been reported to your administrators."}o&&s.alert({title:"Error creating stack",message:o})})},a.reset()}});