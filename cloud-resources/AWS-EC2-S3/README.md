# AWS - EC2/S3 setup

_WB ITS sometimes updates their processes,
so if you see something in this document that seems incorrect, out of date or missing,
then please notify DIME Analytics.
If your addition/correction is not too big you can notify DIME Analytics by
making an edit directly to this document on GitHub and submit a pull request.
If you are not familiar with GitHub or your the issue you notified is substantial,
then you can send an email to dimeanalytics@worldbank.org describing the issue._

We can use AWS for many use cases at DIME. We will divide this use cases in two categories that we call _computation_ and _application_. The first things you need to decide which use case your

Most of DIME's use cases falls under _computation_ and examples include running python or R scripts.
_Computation_ use cases does not need installation of non-standard software
and do not need to be open to the public internet.
Non-standard software in this context means anything not included
in RedHat's (the operating system used on all our EC2 instances) official repository.

While we have use cases at DIME that falls under _application_
we have yet to successfully finalize the approval process for any such case.
Installing any non-standard software or opening it up incoming web traffic
requires OIS (Office of Information Security) approval.
Examples of _application_ use cases in DIME is
hosting a shiny server open to the public internet or
web scraping that require non-standard software like a Chrome driver.

## AWS Accounts and Security Groups

We have two AWS Account for all of DIME,
but we use Security Groups to control who has access to which resource.

### DIME's two AWS Accounts

The two AWS accounts are called `WBG AWS DIME PDMZ` and `WBG AWS DIME DEV PDMZ`.
If your resources is for a _computation_ use case,
then your resources will be created only in `WBG AWS DIME PDMZ`.
If your resources is for a _application_ use case,
then your resources will first be created in `WBG AWS DIME DEV PDMZ` and
only after they are tested there will they also be created on `WBG AWS DIME PDMZ`.
Resources in `WBG AWS DIME DEV PDMZ` might have restricted access
to create a safe testing environment,
but this is decided on case-by-case basis.

### How we use Security Groups

We can create as many or as few security groups that we want.
However, the project teams are responsible to manage and keep these groups up to date,
so there is a trade-off between how many groups we have
and how much time the project teams needs to spend on administrating the groups.
There is also a trade-off in access granularity,
as everyone in the same security group
will have access to the same resources.
It is up to the team what is the balance for them.
DIME Analytics will help you set up the security group,
but then it is up to the team to follow these guidelines to maintain it.

By default, ITS expects a one-to-one relationship between one security group and one charge code.
Although we can work with ITS if this does not match your reality.
If we want to use different charge codes within one security group,
then ITS will create tags for each charge code and tag resources accordingly.
In this case it is important that you mention this tag each time
you request new resources or request changes to your current resources.
One charge code for many security groups is easier.
We just tell ITS this when we apply the same charge code to a new security group,
and then all resources created for this security group will be charged to that code.

DIME Analytics has set up a security group that will by default be applied to all DIME AWS resources.
This will allow us to help you troubleshoot and work with ITS on your behalf.
However, you are free to opt out of this, but then we might not be able to assist you as efficiently.
