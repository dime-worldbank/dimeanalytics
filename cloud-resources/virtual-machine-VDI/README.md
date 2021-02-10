# Virtual Machine VDI

This solution is a often a great first alternative as the learning curve is very low.
If you can use any WB computer then you have the prerequisite skills to use this solution.

### Common pros and cons with VDIs

To help you understand if this solution fits your needs,
here is a list of pros and cons.

**Pros:**
* VDIs look and behave like regular World Bank computers - but they can be made very powerful
* VDIs seamlessly access World Bank systems such as WB intranet, WB OneDrive etc.
* Cost is fixed and not variable to how much you use it
* The VDI team at WB ITS is more hands-on compare to other ITS teams,
and will help you investigate when a big job takes to much time,
or if you can tell that your code is not using the full power.
They will not fix your code,
but might be able to give you the input you need to fix your code,
or they might increase the RAM or processing power.

**Cons:**
* You may only install software approved for installation on WB computer
* No support for some common cloud computing tools like _docker_ and _spark_
* Cannot be used to host web applications accessible from the web

## Access resource

You access this resource in the same portal as you access any World Bank virtual machine.
See [DIME's onboarding guide](https://paper.dropbox.com/doc/New-hire-onboarding-guide--BE7DT35OLeRO9HGJMa_zgvONAg-obzjcDCW8HyXPFwzSd5nb#:h2=Remote-Access-to-World-Bank-Co) for instructions.
These powerful VDIs is a type of dedicated VDI,
even when they are shared between multiple people.

## Install software

As default, the VDI comes with all software that any World Bank computer have
(Word, Excel, Outlook etc.)
but it does not come with any statistical or data science software.
Such software will have to be installed manually or
to be requested to be installed by Local IT
(note that Local IT is not the same as the VDI team - do not ask them for software).

#### Self-install

Many software you can install by yourself.
To do that, go to the windows menu and search for "Software center".
In "Software Center" search for the software you want to install.
If you find the software you want to install,
just click the "Install" button and follow any instructions
If you do not find the software you are looking for
you have to request Local IT to install your software.

#### Request installation

Follow these steps to install any software not available for self-install.

**Approved Software**.
You can only request installation of software that are
pre-approved for installation on World Bank Windows machines.
Before requesting a software make sure it is listed in the
[WBG Software Catalog](https://worldbankgroup.service-now.com/wbg?id=wbg_software_catalog)
(WB intranet only) first.
Common software like R, Stata, Anaconda, Git Bash, GitHub Desktop etc.
are there at the time of writing.
If you do not see your software there, then email dimeanalytics@worldbank.org
and we can discuss what your best option are.
Requesting that a new software is approved can be a long and laborsome process.

**Licensed Software**.
Software that are approved for installation might still require a license.
If the software you want to install is a licensed software,
for example Stata,
then you need to discuss with your TTL how that can be financed.
The World Bank has negotiated organization wide licenses for some licensed software,
and for those your team does not have to pay.
The example most commonly used by DIME is ArcGIS.

**Making the request**
You can make the request yourself,
but if you are not sure of any detail,
it is better that you ask dimeanalytics@worldbank.org
before submitting something that is incorrect.
Make sure that the ID of your VDI is indicated somewhere in this form.
If you are not able to select it you can explain that
this request if for an VDI in the comments box,
and include the ID there.
