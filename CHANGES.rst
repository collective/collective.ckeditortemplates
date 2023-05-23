Changelog
=========

0.9.0 (2023-05-23)
------------------

- Made compatible Plone 4.3 and Plone 6.0
  [sgeulette]

0.3.3 (2021-04-20)
------------------

- Add Transifex.net service integration to manage the translation process.
  [macagua]
- Add Spanish translation
  [macagua]
- Corrected bad import step requirement
  [sgeulette]
- Added features param on BeautifulSoup init
  [sgeulette]
- Degroked package
  [sgeulette]
- Made the enabled state criteria a class variable, so it can be overrided.
  [sgeulette]
- Sorted templates by title
  [sgeulette]

0.3.2 (2015-10-06)
------------------

- Member can see ckeditortemplates, so it possible to use local roles and adding a ckeditortemplate.
  [bsuttor]
- Adding upgradesteps for workflow changes.
  [bsuttor]

0.3.1 (2015-02-09)
------------------

- Remove plone.multilingualbehavior because of to many bugs.

0.3.0 (2015-01-15)
------------------

- Add plone.multilingualbehavior behavior, cktemplate is translable now.
  [bsuttor]

0.2.4 (2014-11-05)
------------------

- Move unindex ckeditorfolder to setup installation instead of upgrade step.
  [bsuttor]

0.2.3 (2014-06-06)
------------------

- Allow content type Image for cktemplatefolder/
  [bsuttor]

0.2.2 (2014-05-23)
------------------

- Add upgrade steps.
  [bsuttor]

0.2.1 (2014-04-18)
------------------

- Fix accents errors, decode content to utf-8.
  [bsuttor]

0.2 (2014-03-31)
----------------

- Remove the group restriction on CK Template
  [mpeeters]
- Improve the parsing of html
  [mpeeters]
- ckeditor template folder is no more allow globally, this container is
  installed with package
  [bsuttor]

0.1 (2014-03-10)
----------------

- Initial release
  [mpeeters, bsuttor]
