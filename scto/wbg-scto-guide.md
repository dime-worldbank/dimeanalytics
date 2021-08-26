# World Bank SurveyCTO

## Introduction

The World Bank Group’s SurveyCTO Enterprise server is an on-site installation of the SurveyCTO data collection platform,
managed by ITS SurveyCTO Administration team ([contact](mailto:itssurveyctoadministration@worldbank.org)).
DIME Analytics manages an SurveyCTO Enterprise server where a team can create a "group",
which is a space where you can run your survey.

To start a group on the WBG SurveyCTO server,
visit eServices and submit a request for
“[SurveyCTO Data Collection Platform](https://worldbankgroup.service-now.com/wbg?id=wbg_sc_catalog&sys_id=7d1e71b86f16d340db112d232e3ee4aa)”.
Requests are fulfilled within 2 business day.


## Cost and Group Limits
The cost is $179 per month per group.
Each group is allowed up to 30 forms (i.e. questionnaires),
10,000 mobile submissions, 10,000 web submissions, and 2GB of storage.
In eServices, the requestor will designate a ‘Survey Administrator’ for their group.
This person must have a World Bank Group email address for authentication purposes.
The Survey Administrator will receive an email as soon as their group is live on the server,
at which point they will be able to log on and add all other team members and assign them the appropriate profile.

The additional team members can be WBG staff and consultants or trusted external partners,
who will then receive an invitation to the group on the WBG server.
WBG users will be automatically authenticated;
externals will be asked to create a password on their first visit.

## Access and Roles
The Survey Administrator will be able to manage (add/delete) users, forms, and data for their group.
New users can be added using the “Configure” tab.
Each new user must be assigned a role,
which will determine what access the user has to the groups data and forms on the server.
The following standard roles are available for all groups:

- Admin: can upload, move, and remove survey forms; can view and export data. Can manage users.
- Form and Data Managers: can upload, move, and remove survey forms; can view and export data. Cannot manage users.
- Data Managers: can view and export data. Cannot manage forms or users.
- Enumerators: can view forms and submit questionnaires. Cannot manage users or forms, or access data.

Custom roles are available on request.
## Important Notes
Because this is an enterprise installation, you are sharing server space with many other WBG teams.
For the enterprise installation to work smoothly, please make sure to follow these rules; they will be enforced by the WBG server administrators.

1.	**Anything you add to the server (forms, datasets, etc) must use your server prefix.**
For example, the “DIME_Ghana_Ag” group should use “DIME_Ghana_Ag_” for all dataset and surveys to avoid naming conflicts.
The appropriate prefix will appear in user roles.
2.	**Any datasets and survey forms added to the server should be encrypted.**
If this is not done, your confidential data will be visible to the Enterprise Administrators,
which may violate your ethical approval agreements. See DIME Analytic's [SurveyCTO Encryption guidelines](https://osf.io/gh4y8/).

## Pausing your Group
When you create your group, you will indicate an anticipated end date for the server in the eServices request.
You will receive a reminder email 5 business days before the selected end date. 
At the end date for the group, you can decide to end the group or pause the group.
Pausing a group means that the data and forms will be kept secure on the server but will not be accessible until the group is resumed.
To pause a SurveyCTO survey for $20 per month, visit eServices and submit a request for
“[SurveyCTO - Pause Server](https://worldbankgroup.service-now.com/wbg?id=wbg_sc_catalog&sys_id=87ebb44ddbc1dc10d37979668c961931)”.
Requests are fulfilled within 2 business day.

When you are ready to resume your group, you must submit a new eServices request for 
"[SurveyCTO - Request Server](https://worldbankgroup.service-now.com/wbg?id=wbg_sc_catalog&sys_id=7d1e71b86f16d340db112d232e3ee4aa)" 
with the same survey name,
starting on the planned resume date and extending to the desired new end date.
Your group will then continue with no interruption.

## Ending your Group
When you create your group, you will indicate an anticipated end date for the server in the eServices request.
You will receive a reminder email 5 business days before the selected end date. 
At the end date for the group,  If you are ready to terminate the server, 
you must remove all forms and data and store that in a different secure location _before the end date_.
If you have any forms or data remaining on the server on the end date,
your group will not be deleted and you will be charged a penalty (equivalent to 1 additional month).

If the data collection is lasting longer than you initially expected and you instead would like to keep your server past the end date,
you must submit a new eServices request for "[SurveyCTO - Request Server](https://worldbankgroup.service-now.com/wbg?id=wbg_sc_catalog&sys_id=7d1e71b86f16d340db112d232e3ee4aa)" with the same survey name, starting on the planned end date and extending to the desired new end date.
Your group will then continue with no interruption.

## Help and Customer Support
Extensive documentation and resources are available through the “Help” menu on the server.
Questions regarding how to use SurveyCTO (e.g. programming challenges, questions on particular features)
should be addressed to SurveyCTO through the Support Center.
Please make Support Center requests through the WBG SurveyCTO server to benfit from the premium support agreement we have with SurveyCTO.
Questions regarding the WBG Enterprise set-up specifically (start a new survey, request custom roles, etc)
can be addressed to [itssurveyctoadministration@worldbank.org](mailto:itssurveyctoadministration@worldbank.org).

#### Anonymous access

Anonymous access is common when you run Web Data collection so that the respondents
does not have to create a account with password authentication when submitting answers.
If you plan on using anonymous access we strongly recommend you to read
[this guide](https://github.com/dime-worldbank/dimeanalytics/blob/master/scto/scto-anonymous-access-guide.md) first.

## Installing SurveyCTO Desktop
SurveyCTO Desktop is the most flexible and powerful way to use SurveyCTO.
Once installed on your desktop or laptop computer,
Desktop will help you to synchronize data between your computer and one or more SurveyCTO servers –
and even between your computer and other computers, or between your computer and mobile devices.
It provides a wide range of data export formats and options,
plus: powerful tools for working offline; convenient access to the server console, Support Center, and other online resources; and more.
You can directly install SurveyCTO Desktop on your device using [this installation file](https://docs.surveycto.com/desktop/).
