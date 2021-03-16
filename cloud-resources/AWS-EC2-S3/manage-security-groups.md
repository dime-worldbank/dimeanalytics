# Manage and maintain security groups

_WB ITS sometimes updates their processes,
so if you see something in this document that seems incorrect, out of date or missing,
then please notify DIME Analytics.
If your addition/correction is not too big you can notify DIME Analytics by
making an edit directly to this document on GitHub and submit a pull request.
If you are not familiar with GitHub or your the issue you notified is substantial,
then you can send an email to dimeanalytics@worldbank.org describing the issue._

## Getting started with the groups portal

All WB users have access to the `http://groups/`,
but to manage a security group you need access to the "_Security Groups (SGs)_" section.
If you do not see this section - see image below - then you need to submit
[this eServices](https://worldbankgroup.service-now.com/wbg?id=wbg_sc_catalog&sys_id=4b4ce496dbe9f300c4813a1b7c96195f) request. In "_Type of Service_" select "_Group Management_" and in "_Description_" write "_I need access to Security Groups (SG) in the http://groups/ portal as I will manage a security group used in the "WBG AWS DIME PDMZ" AWS account_"

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/document-cloud-resources/cloud-resources/AWS-EC2-S3/img/aws-securitygroup0.png" width="50%"><!--- Image is read from master branch or use full URL-->

## Starting a new group

DIME Analytics will help you initially set up the security group.
You do not need to follow these steps her,
they are included for our reference.
First we will give one of us in Analytics ownership of the group,
but then we will add one person in the project team to be co-owner.
See instruction for "Adding owner" below.

To create a new security group go to `http://groups/` on the WB intranet.
Then click "My SGs" in the menu to the left in the section "_Security Groups (SGs)_".
See instructions above if you do not see the section "_Security Groups (SGs)_".
Then click "New" in the menu at the top.

In the first menu, fill in the form like in the image below.
You need to update the info in form items that has a red box around them.
For "_Display Name_" copy the name `WBGMaster-DIME-XX-Admin` and
make sure to update `XX` to a two-letter abbreviation of the team name.
Examples of abbreviations already in use are
IC for ieConnect, DA for DIME Analytics and DJ for DeJure.
Whatever you pick, copy the same full name to "_Account Name_".
In the "_Description_" form item, copy the text:
`AWS resources for TEAMNAME team in unit UNIT. Will give access to start and stop instances`.
Make sure to update `TEAMNAME` and `UNIT`.
You may list multiple units but one unit must be a DIME unit on the DIME AWS account.

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/document-cloud-resources/cloud-resources/AWS-EC2-S3/img/aws-securitygroup1.png" width="50%"><!--- Image is read from master branch or use full URL-->

Then you click `Next`.
You may add members at this point but the default is
that the project team co-owner of the group will do so.
Either add members according to the instructions below,
or click `next` again to get to the owner tab
and add owner according to the instructions below.

# Adding owner

Only owners can add owners to a group.

The process of adding a new owner is similar regardless if this is a brand new group
or a group that has existed for a while.
If this is an already existing group you need to click the name of the group
in the "_Security Group (SGs)_" section in the `http://groups/` portal.
See the getting started section above if you do not see the "_Security Group (SGs)_" section.
If you are in the process of creating a new group, you are already in that menu.
Regardless how you got to that menu,
make sure that you are in the `Owners` tab - see image below.

Add the names of the owners of this security group.
It should be one DIME Analytics member and one project team member.
The project team member should be the Displayed owner.
Use the address book tool (highlighted in a red box) to search for people names
for them to be included correctly.
Then click `Finish`.
This change may take up to 4 hours to take effect.

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/document-cloud-resources/cloud-resources/AWS-EC2-S3/img/aws-securitygroup2.png" width="50%"><!--- Image is read from master branch or use full URL-->

# Adding member

Only owners can add members to a group.
You will only be able to add WB users that already have a C-account.
You can request a C-account using
[this eServices request](https://worldbankgroup.service-now.com/wbg?id=wbg_sc_catalog&sys_id=00101b2fdbd00c10f6ae90b3db9619e6).
This eServices request will tell you if the user you are requesting for already have a C-account.
C stands for cloud and is needed to access WB cloud resources.
So if you are not sure if a user has a C-account,
you can start the eService request for that person and
the system will notify you if the user already have a C-account.

To add members to a security group you need to click the name of the group
in the "_Security Group (SGs)_" section in the `http://groups/` portal.
See the getting started section above if you do not see the "_Security Group (SGs)_" section.

In the field "_Member To Add_" you write `c<UPI>` for the users you want to add.
See image below for and example.
Then you need to click the validate button (highlighted in a red box),
and if you have entered the value corrected you will see that
the last name of the person you are adding will appear next to the `c<UPI>` value.
Otherwise you will get squiggly lines as if you have a typo in Microsoft Word.

When you have validated the names you can press `OK`.
This change may take up to 4 hours to take effect.

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/document-cloud-resources/cloud-resources/AWS-EC2-S3/img/aws-securitygroup3.png" width="50%"><!--- Image is read from master branch or use full URL-->


# Removing member

Only owners can add members to a group.
This is almost identical to adding a new member.
Follow the instructions for adding a new member,
but use the field "Members To Remove" instead.
Remember to identify members using their C-account.
This change may take up to 4 hours to take effect.
