# Virtual Machine VDI

_WB ITS sometimes updates their processes,
so if you see something in this document that seems incorrect, out of date or missing,
then please notify DIME Analytics.
If your addition/correction is not too big you can notify DIME Analytics by
making an edit directly to this document on GitHub and submit a pull request.
If you are not familiar with GitHub or your the issue you notified is substantial,
then you can send an email to dimeanalytics@worldbank.org describing the issue._

This solution is a often a great first alternative as the learning curve is very low.
If you can use any WB computer then you have the prerequisite skills to use this solution.

## Common pros and cons with VDIs

To help you understand if this solution fits your needs,
here is a list of pros and cons.

**Pros:**
* VDIs look and behave like regular World Bank computers - but they can be made very powerful
* VDIs seamlessly access World Bank systems such as WB intranet, WB OneDrive, AWS/Azure servers on the WB Cloudportal etc.
* VDIs offer extremely high internet speed, ergo downloading large datasets is relatively quite fast
* VDIs restart your session from where you left and wait for 5 minutes to reconnect
in case you are facing difficulties in connecting with the VDI from your local computer
* Cost is fixed and not variable to how much you use it
* The VDI team will work with you to increase RAM, processing power, storage and add GPU processing.
They will work with you to identify the bottleneck you are experience
and increase the power and/or resources added to your VDI as needed.

**Cons:**
* You may only install software approved for installation on WB computer
* No support for some common cloud computing tools like _docker_ and _spark_
* Cannot be used to host web applications accessible from the web
* One can face latency issues based on the internet status of one's local computer, this slows down the VDI and one might experience some lag

## Access resource

You access this resource in the same portal as you access any World Bank virtual machine.
See [DIME's onboarding guide](https://paper.dropbox.com/doc/New-hire-onboarding-guide--BE7DT35OLeRO9HGJMa_zgvONAg-obzjcDCW8HyXPFwzSd5nb#:h2=Remote-Access-to-World-Bank-Co) for instructions.
These powerful VDIs is a type of dedicated VDI,
even when they are shared between multiple people.
If multiple people share a resource,
remember that only one person can be logged in at the time.
Each person who has been given access to a VDI
log in to the VDI using their own WB credentials.

## Logging out from a VDI

How you log out from your VDI matters much more if you are using a shared VDI.
If your VDI is not shared,
then the only important thing is that you occasionally restart the VDI.
Optimally once per week (if you use it frequently)
but always at least once per month.
This both improves performance and make sure that the OS on your VDI is up to date.

#### Best practices for shared VDIs

Each time you log in on to a VDI a _session_ is created.
No other user cannot log in to the same VDI until this session is terminated.
If you want to run a big job overnight, then you must not terminate your session.
However, no one else will be able to use the VDI until you log back in
and terminate your session after your job is completed.

**Logging out with session preserved.**
You have two options if you want to log out from the VDI
and preserve your session
so that any task you are currently running will keep running.
You can either just close the Citrix window on your local computer,
or you can click the "_Disconnect_" button in the top of the Citrix window.
See image below.
Note that no other user can use the VDI until you log back in and use any of the logging out methods listed below that terminates your session.

<img src="https://github.com/dime-worldbank/dimeanalytics/tree/document-cloud-resources/cloud-resources/virtual-machine-VDI/img/vdi-disconnect.png" width="50%"><!--- Image is read from master branch or use full URL-->

**Logging out with session terminated.**
You can either sign out of the VDI or restart the VDI to terminate the session. When you sign out the VDI is immediately available for another user,
but restarting usually takes 5 min
and it can take up to 30 min if there is a pending update.
We strongly recommend that you restart as often as once per week.
If you know that no one else will use the machine,
you can even do this each time you log out
if it is unlikely that someone is waiting to use the VDI.
You should restart at least once per month.
Both for performance reasons,
but also because ITS will force a restart
if you have updates pending for too long
and you do not want that to happen in the middle of a job running.

Here is how you **_sign out_** from the VDI.
This terminates your session and any tasks currently running.
Another user will be able to log in immediately.
See the image below for how to sign out.
Click first in the blue circle and then in the red circle.

<img src="https://github.com/dime-worldbank/dimeanalytics/tree/document-cloud-resources/cloud-resources/virtual-machine-VDI/img/vdi-disconnect.png" width="50%"><!--- Image is read from master branch or use full URL-->

Here is how you **_restart_** the VDI.
This terminates your session and any tasks currently running.
Another user will typically be able to log in after 5 min,
but it could take up to 30 min if an update is pending.
See the image below for how to sign out.
Click first in the blue circle and then in the red circle.

<img src="https://github.com/dime-worldbank/dimeanalytics/tree/document-cloud-resources/cloud-resources/virtual-machine-VDI/img/vdi-disconnect.png" width="50%"><!--- Image is read from master branch or use full URL-->


## Install software

As default, the VDI comes with all software that any World Bank computer have
(Word, Excel, Outlook etc.)
but it does not come with any statistical or data science software.
Such software will have to be installed manually or
to be requested to be installed by Local IT
(note that Local IT is not the same as the VDI team
- do not ask them for software).

### Self-installation of software

Many software you can install by yourself.
To do that, go to the windows menu and search for "Software center".
In "Software Center" search for the software you want to install.
If you find the software you want to install,
just click the "Install" button and follow any instructions
If you do not find the software you are looking for
you have to request Local IT to install your software.
R/RStudio is for example available in "Software center".
If you are not able to open "Software center",
please contact dimeanalytics@worldbank.org
and we can help you raise that issue with an ITS officer.

### Request installation of software from Local IT

Follow these steps to install any software not available for self-install.

#### Approved Software

You can only request installation of software that are
pre-approved for installation on World Bank Windows machines.
Before requesting a software make sure it is listed in the
[WBG Software Catalog](https://worldbankgroup.service-now.com/wbg?id=wbg_software_catalog)
(WB intranet only) first.
Common software like R, Stata, Anaconda, Git Bash, GitHub Desktop etc.
are there at the time of writing.
If you do not see your software there, then email dimeanalytics@worldbank.org
and we can discuss what your best options are.
Requesting that a new software is approved can be a long and laborsome process.

DropBox is not approved for installation on World Bank Windows machines
but DIME has an dispensation conditional on
the user taking a very brief training and signing a waiver.
Email dimeanalytics@worldbank.org for details on this process.
Include the ID of your VDI in this email.

#### Licensed Software

Software that are approved for installation might still require a license.
If the software you want to install is a licensed software,
for example Stata,
then you need to discuss with your TTL how that can be financed.
The World Bank has negotiated organization wide licenses for some licensed software,
and for those your team does not have to pay.
The example of this most commonly used by DIME is ArcGIS.

#### Making the request

You can make the request yourself,
but if you are not sure of any detail,
it is better that you ask dimeanalytics@worldbank.org
before submitting something that is incorrect.
Make sure that the ID of your VDI is indicated somewhere in this form.
If you are not able to select it you can explain that
this request if for an VDI in the comments box,
and include the ID there.
