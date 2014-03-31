*** Settings ***
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/selenium.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Suite Setup
Suite Teardown  Close all browsers


*** Test Cases ***
Cktemplate folder is never indexed
    Go to  ${PLONE_URL}
    Page should contain  Powered by Plone
    Go to  ${PLONE_URL}/ckeditortemplates/edit
    Input Text  id=form-widgets-IDublinCore-title  edited_cktemplate
    Click button  id=form-buttons-save
    Go to  ${PLONE_URL}/folder_contents
    Element Should Not Be Visible  css=tr#folder-contents-item-ckeditortemplates

Add and use cktemplate
    ${cktemplate_name} =  set variable  my_cktemplate_name
    Go to  ${PLONE_URL}/ckeditortemplates
    Open add new menu
    Click Link  id=cktemplate

    Input Text  id=form-widgets-IDublinCore-title  ${cktemplate_name}
    Execute JavaScript  CKEDITOR.instances['form.widgets.content'].insertHtml('<h1>My title</h1>')
    Submit Form  form
    Click button  id=form-buttons-save
    Page Should Contain  Item created
    Page should contain  ${cktemplate_name}
    Open Menu  plone-contentmenu-workflow
    Click link  id=workflow-transition-enable

    Go to  ${PLONE_URL}
    Open add new menu
    Click Link  id=document

    Input Text  title  My doc with template
    Execute JavaScript  CKEDITOR.instances['text'].commands.templates.exec()
    Page should contain  ${cktemplate_name}


*** Keywords ***
Suite Setup
    Open test browser
    Enable autologin as  Manager
