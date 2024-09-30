# Virtual Machine VDI

_WB ITS sometimes updates their processes,
so if you see something in this document that seems incorrect, out of date or missing,
then please notify DIME Analytics.
If your addition/correction is not too big you can notify DIME Analytics by
making an edit directly to this document on GitHub and submit a pull request.
If you are not familiar with GitHub or the issue you noted is substantial,
then you can send an email to dimeanalytics@worldbank.org describing the issue._

Content of this page:

* What are VDIs?
* Logging in and out from a VDI
* Installing software on a VDI


## What are VDIs?

VDI (virtual desktop interface) is a computer on the World Bank's servers you log in to remotely.
The remote desktop you get by default if you are staff, ETC or tier 3 STC
(ask your TTL if you are an STC and not sure which tier you are) is also a VDI.
However, that is called a _regular_ or _pooled_ VDI.
All data stored on a pooled VDI is deleted between usages as
someone else will be using that specific hardware after you log off.
If you sync data to OneDrive or in any other way save data somewhere else,
then that data is not deleted.
That is why you cannot install any extra software on a pooled VDI.

The rest of this guide is only about _dedicated_ VDIs.
A dedicated VDI has a dedicated piece of hardware on the WB servers only you will use.
Any data you save or any software you install will be there the next time you log in,
just the same way it would on a WB laptop.
Since some hardware is reserved for only you, a dedicated VDI comes with a charge.
This charge starts at $39/month and may be increased if you request
a hardware upgrade of your VDI to make it more powerful.

You can leave a dedicated VDI running a big task even when you are not connected.
See instructions below for how to do that.
A dedicated VDI can be shared among several users, but only one user can use it at any given time.

A dedicated VDI a great first alternative for computing needs as the learning curve is very low.
If you can use any WB computer then you have the prerequisite skills to use this solution.

### Common pros and cons with VDIs

To help you understand if this solution fits your needs,
here is a list of pros and cons.

**Pros:**
* VDIs look and behave like regular World Bank computers - but they can be made very powerful
* VDIs seamlessly access World Bank systems such as WB intranet, WB OneDrive, AWS/Azure servers on the WB Cloudportal etc.
* VDIs offer extremely high internet speed, ergo downloading large datasets is relatively fast
* VDIs restart your session from where you left and wait for 5 minutes to reconnect
in case you are facing difficulties in connecting with the VDI from your local computer
* Cost is fixed and not variable to how much you use it
* The VDI team will work with you to increase RAM, processing power, storage, and add GPU processing.
They will work with you to identify the bottleneck you are experiencing
and increase the power and/or resources added to your VDI as needed.

**Cons:**
* You may only install software approved for installation on WB computer
* Currently no support for some common cloud computing tools like _docker_ and _spark_
* Cannot be used to host web applications accessible from the web
* One can face latency issues based on the internet status of one's local computer. This does not make the computation slower, but a user with a slow connection to the server in DC might experience some lag. Meaning that it takes a split second for the key strokes or mouse movements to register.
* We have had issues with very slow sync (or not working at all)
when intensively using sync software like OneDrive and DropBox (very large files or a very large number of files).

## Logging in and out from a VDI

Logging in on a VDI is straight forward by following the guide below.
There are multiple ways you can log out from a VDI and the different methods
has different use cases.

For example, if you want a task to run on your VDI after you log out,
then you should use one method.
If you use a shared VDI and you want to let someone else use the VDI,
then it is important that you log out using another method
as only one person can have an active session at the time on a VDI.
This is all explained below.

Please contact IT If you run into any technical difficulties
at +1 202-473-2121 or ithelp@worldbankgroup.org.
You get a quicker response if calling but email tend to be quite fast as well.
If you call, you can as the IT officer to call you back on any global phone number
so you do not have to pay for the call.
If you email from a personal email as you do not yet have access to your WB email,
make sure to include your name and UPI so they can verify that you are on a WB contract.

### Connecting from an non-WB computer

The first time you are connecting from a new personal computer
you must first install the [Citrix Workspace App](https://www.citrix.com/downloads/workspace-app/).
Download it and then follow the instructions below.

This software is already installed on all WB computers.

### Logging in to a VDI

If you are wondering if you are using a _dedicated_ or _pooled_ VDI,
you will notice the difference in Citrix Workspace by seeing which of these
guides match what you see.

### Logging in to a pooled VDI

_Note that any files not synced to OneDrive (or in any other way saved outside the VDI)
will be deleted when you log out from a pooled VDI_

Access a Regular VDI like this:
* Log in to Citrix Workspace app according to the instructions above
* Click on DESKTOPS
* Click any icon with Windows 10 (see image below). You might have one or multiple icons. They are all the same.

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/master/cloud-resources/virtual-machine-VDI/img/pooled-vdi-1.png" width="80%">

* If you do not see any ID immediately under “Windows 10” (compare with the instructions for Dedicated VDIs below) then you know that this is a Regular VDI.
* When you have confirmed that this is a Regular VDI, then click “Open” and follow instructions.

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/master/cloud-resources/virtual-machine-VDI/img/pooled-vdi-2.png" width="80%">

### Logging in to a dedicated VDI

Access a Dedicated VDI like this:
* Log in to Citrix Workspace app according to the instructions above
* Click DESKTOPS
* Click on the icon that does not say Windows 10. It is possible to have access to multiple Dedicated VDIs. Depending on type of Dedicated VDIs you have they might have the same name - see next step for how to tell them apart

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/master/cloud-resources/virtual-machine-VDI/img/dedicated-vdi-1.png" width="80%">

* Even when Dedicated VDIs have the same name, they will have a unique ID. If you have multiple Dedicated VDIs with the same name then you have to learn which ID is which.
    * Confirm that the ID in the grey text below under the VDI name is the correct VDI.
    * If you do not see this ID, then it is not a Dedicated VDI, but a regular VDI
* Click “Open” and follow instructions

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/master/cloud-resources/virtual-machine-VDI/img/dedicated-vdi-2.png" width="80%">

### Logging out from a VDI

How you log out from your VDI matters much more if you are using a shared VDI.
If your VDI is not shared,
then the only important thing is that you occasionally restart the VDI.
Optimally once per week (if you use it frequently)
but always at least once per month.
This both improves performance and make sure that the OS on your VDI is up to date.

#### Best practices for shared VDIs

Each time you log in on to a VDI a _session_ is created.
No other user can log in to the same VDI until this session is terminated.
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

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/master/cloud-resources/virtual-machine-VDI/img/vdi-disconnect.png" width="80%"><!--- Image is read from master branch or use full URL-->

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

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/master/cloud-resources/virtual-machine-VDI/img/vdi-signout.png" width="30%"><!--- Image is read from master branch or use full URL-->

Here is how you **_restart_** the VDI.
This terminates your session and any tasks currently running.
Another user will typically be able to log in after 5 min,
but it could take up to 30 min if an update is pending.
See the image below for how to sign out.
Click first in the blue circle and then in the red circle.

<img src="https://github.com/dime-worldbank/dimeanalytics/blob/master/cloud-resources/virtual-machine-VDI/img/vdi-restart.png" width="30%"><!--- Image is read from master branch or use full URL-->

## Install software on a VDI

As default, the VDI comes with all software that any World Bank computer have
(Word, Excel, Outlook, etc.)
but it does not come with any statistical or data science software.
Such software will have to be installed manually or
to be requested to be installed by Local IT
(note that Local IT is not the same as the VDI team -
do not ask the VDI team for software).

### Self-installation of software

Many software you can install by yourself.
To do that, go to the Windows menu and search for "Software center".
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
this request is for a VDI in the comments box,
and include the ID there.
