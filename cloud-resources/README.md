# Guide to requesting cloud resources

## Intro - Please read

DIME Analytics can help DIME teams request necessary cloud resources.
Requesting cloud resources will require you and your team to provide answers to a lot of specific technical questions.
Unfortunately, this process is slow:
in our experience, it takes about a month for a simple cloud resource to be approved and activated after being requested,
and several months for a more complex or custom cloud resource setup.
Understanding the dynamics of this process before you start it
will help you avoid any additional delays.

Cloud resources paid for by WB funding must be created by the WB's IT Services unit (**ITS**).
If you create your own AWS account and create resources you simply will not be reimbursed.
The first step of the process is for the WB Office of Information Security (**OIS**)
to review and approve your request.
OIS approval must be granted before any cloud resource can be set up.
OIS will have many questions about your project needs and setup.
DIME Analytics will support you in structuring your answers to questions from ITS and OIS,
but we will not be able to answer them for you without significant time investment understanding your project.

OIS and ITS will look at the requirements you need for your cloud service.
and recommend a WB-approved solution.
You may note specific preferences in the request,
but the recommended solution will ultimately be based on your project's needs.
For example, you can say
"_I would need a server with 32GB RAM (for example AWS EC2) and storage for 200GB data (for example AWS S3)_".
It will **not** be sufficient to request a product without specifications, such as: "_I want an EC2 server and an S3 bucket_".
It is, by contrast, perfectly fine to not know the name of the exact product you want,
so you can say, "I would need a server with 32GB RAM and storage for 200GB data".

## Process for requesting cloud resources

There is not yet a streamlined process for requesting cloud resources at the WB.
DIME Analytics will help you find out where to start, but
to do so we need to understand what you need.
The form below includes the information that ITS and OIS typically ask for when starting the request process.
The more thoroughly you fill in this information,
the more likely it will be that the OIS/ITS process starts in the right direction.
Insufficient information at the start of a request process will cause additional delays
and requires providing the same information to multiple OIS teams.

Please fill in the form below as well as you can
and send it to dimeanalytics@worldbank.org.
We will then review your request to make sure it
includes everything that OIS typically asks for,
and that it is expressed in a way that will make sense to them.
We will likely have at least some follow-up questions.
If there are a lot of items you want our help with, then
we can copy this information to a Word document on OneDrive
where we can collaborate until it is ready for submission.
Then we will forward this request to our ITS contact and copy you
so that you can provide additional information if they have questions.

_NOTE: PLEASE DELETE ALL THE ITALICIZED COMMENTS WHEN COMPLETING AND RETURNING THE FORM BELOW._

___

### Basic Info:

* Full name of project:
* Short name of project _(will be used by ITS to create a tag for the project's resources. For example: "dimeieconnectkenya)_:
* Contact person in project:
* Name of TTL:
* Unit of TTL:
* Manager of unit of TTL:
* Charge code _(not requeired yet, but will delay process if it is not ready when requested)_:

### Use-case:

_ITS/OIS always want to know the use case.
They are less interested in economic theory and justification for the study,
and more interested in what function the cloud resource will have in your workflow.
For example, you may need a solution for storage of large or sensitive data,
for running regressions that can't run on your currently availible machines, etc._

_This is also a great place to give an overview on where the data will come from,
how it will be ingested or input in the system,
how it will be analyzed, and
if any data (not just results) will be exported from the system._

### Data storage:

_What type of data will be stored in this system?
By "type" we want to you to use one of the four levels in the WB's data classification,
see the [World Bank Group Classification Handbook for Restricted Iinformation](https://spawin.worldbank.org/sites/corporate/A2I/Knowledge%20Base%20Documents/Classification_online.pdf).
It is mandatory from OIS to select one of these classifications,
corresponding to the most sensitive data that will be stored, and
you could be held accountable if
you use your resource for data more sensitive than
what your resource will be classified for.
This classification will determine who may access data
and what security controls will be put in place (such as 2FA/RSA login)._

_What is the size of the data?
Give a rough estimate in terms of MB, GB, TB.
Remember that if you save both
the original data and intermediate datasets in this cloud resource
you should include the size of all that data in your estimate.
We can usually increase the size of the data storage easily,
but a rough estimate is needed to decide for which type of storage product should be set up.
Moving data to a different storage type later is very cumbersome.
Data storage is relatively inexpensive, 
and storage products will be chosen depending on orders of magnitude,
not small linear differences.
Therefore it is almost always better to err
on the side of somewhat generously overestimating the required storage size._

### Processing power:

_What type of processing power is needed?
Processing power tends to be the main driver of cost,
so it is usually better to underestimate the processing power need
and scale it up later if it is too slow.
The bare minimum requirement is approximately
the amount of data that you will process in one computational operation.
If you can split data into smaller pieces or remove excess information,
or compress the data you have (by changing variable storage types for example)
you might consider doing that before calculating this minimum._

_You can express the processing power in terms of "GB of RAM"
(a typical high-performance Mac desktop has 8 or 16 GB,
and a typical high-powered graphics desktop has 32 or 64 GB).
You can use descriptions such as saying "about as fast as a powerful laptop",
by saying "about 100GB will be analyzed at a single time","
or express your requirement in any other way
and we will help approximate your needs._

### Software requirements:

_What software needs to be installed on the cloud service?
This should include:
the software needed to run the code that you intend to use,
any non-standard libraries needed for your code,
git clients etc.
In this context, by "non-standard libraries" we mean libraries
that require something else to be installed or downloaded. 
For example, chromedriver to selenium, NLP corpus for NLP libraries etc.
You do not need to list libraries that can sufficiently be installed 
by only using a standard package manager.
Omitting any required software is a big source of delays
as new software products can require re-approval of the entire system._

### Code development:

_Where will code be developed?
On local computer(s) (laptop/desktop) or in this cloud resource?
Cloud resources are expensive to use as code editors
so, if possible, we recommend developing the code
on a sample of the data on a local computer.
If developing locally,
how will the code be transferred to the cloud resource?
(GitHub is usually a great solution for this.)_

_Where will the code be backed up?
Cloud data storage is backed up
(unless OIS/ITS makes it very clear that it won't be),
but we do not tend to store our code in the data storage.
(GitHub is usually a great solution for this.)_

### Access - humans:

_**Who needs access to this system?**
This should include everyone that needs access to run code,
access to upload and download data,
access to view any dashboards etc._

_**Are all people that need any type of access WB Staff/ETC/STC?**
Will they all at least have WB UPIs?
If anyone who does not have a WB UPI will access this system,
then describe who they are,
and if they will have any type of authentication._

_**If you know the exact list of people already,
then you can enumerate them.**
Include the UPI for each person (if applicable),
as well as whether they currently have access to
a WB laptop, remote access to a physical WB desktop,
access to a dedicated virtual machine (called VDI), and/or
access to a regular virtual machine._

### Access - code:

_What access does the code need to have to the internet?
For example, if you are scraping the internet,
describe the pages you will scrape and provide the URLs.
If you need to add more URLs in the future,
you can but it will require another request.
You usually only need to give the domain an not the full URL.
For example, if you intend to scrape a few twitter accounts,
then you only need to provide the URL_ `https://twitter.com`
_and not one for each full URL with twitter handles._

_You also need to provide details if the systems needs to:
access data from the internet,
install libraries from a non-standard repository etc.
You also need to specify if the resource needs to
be able to receive requests from the internet.
For example, if data will be pushed to this system from another resource._
