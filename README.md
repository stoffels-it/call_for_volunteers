# call_for_volunteers
This django app was programmed during the COVID-19 crisis for calling for volunteers for the DRK Kreisverband Bonn e.V. The topic itself was planned some time ago, to enable volunteers, who are not a member of this association, to take part in urgent requests for help anyway.

## prerequisites
* django 2.2
* python3-yaml (for example data fixtures)
* django-phone-field
* django-user-accounts
* django-modeladmin-reorder
* django-registration

## installation
* add the app folders to the project and add the app to settings.py
* assume the desired options from settings.py and urls.py in the django-project-folder of this repo
* load initial data with python3 manage.py loaddata initial_data/qualification.yaml and all other yaml-Files
