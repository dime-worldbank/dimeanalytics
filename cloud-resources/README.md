# Guide to requesting cloud resources

## Intro - Please read

DIME Analytics can help DIME teams request necessary cloud resources.
Requesting cloud sources will require you and your team to provide answers to a lot of questions.
Unfortunately, this process is slow:
in our experience, it takes about a month for a simple cloud resource,
and several months for a more complex cloud setup.
Understanding the dynamics of this process before you start it
will help you avoid any additional delays.

Cloud resources paid for by WB funding must be created by the WB's IT Services unit (**ITS**).
If you create your own AWS account and create resources you simply will not be reimbursed.
The first step of the process is for WB's Office of Information Security (**OIS**)
to review and approve your request. 
OIS approval must be granted before any cloud resource can be set up.
OIS will have many questions about your project needs and set-up;
DIME Analytics will support in answering these questions,
but will not be able to answer them for you.

OIS and ITS will look at the requirements you need for your cloud service.
and recommend a WB-approved solution.
You may note specific preferences in the request, 
but the recommended solution will ultimately be based on your project's needs. 
For example, you can say
"_I would need a server with 32GB RAM (for example AWS EC2) and storage for 200GB data (for example AWS S3)_".
But it will not be sufficient to say "_I want an EC2 server and an S3 bucket_".
It is perfectly fine to not know the name of the product you want,
and you can say "I would need a server with 32GB RAM and storage for 200GB data".

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
We will then copy this information to a Word document
that we will put on OneDrive and share with you for further collaboration.
We will likely have follow up questions, which we will flag to you in the Word document.
This document will be the basis of the request when we contact OIS/ITS.

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

_ITS/OIS always want to know the usecase. 
They are less interested in economic theory and justification for the study,
and more interested in what function the cloud resource will have in your workflow.
Such as storage of large or sensitive data, 
running regressions that can't run on your currently availible machines, etc._

_This is also a great place to give an overview on where the data will come from,
how it will be ingested in the system,
how it will be analyzed and
if any data (not just results) will be exported from the system._

### Data storage:

_What type of data will be stored in this system?
By "type" we want to know how sensitive the data is.
Is it confidential? Does it include name or other PII information
(regardless if the data is public or not)?_

_What is the size of the data?
Give a rough estimate in terms of MB, GB, TB.
Remember that if you save both
the original data and intermediate datasets in this cloud resource
you should include the size of all that data in your estimate.
We can usually scale the size of the data storage easily,
but a rough estimate is needed to decide for which type of storage is needed.
Data storage is cheap and it is better to err
on the side of overestimating the storage size._

### Processing power:

_What type of processing power is needed?
Processing power tends to be the main driver of cost,
so it is usually better to underestimate the processing power need
and scale it up later._

_You can express the processing power in terms of "GB of RAM",
by saying "about as fast as a powerful laptop",
by saying "about 100GB will be analyzed at a single time","
or express your requirement in any other way._

### Software requirements:

_What software needs to be installed on the cloud service?
This should include:
the software needed to run the code that you intend to use,
any specific libraries needed for your code,
git clients etc.
Omitting required software is a big source of delays._

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

_Who needs access to this system?
This should include everyone that needs access to run code,
access to upload and download data,
access to view any dashboards etc._

_Are all people that need any type of access WB Staff/ETC/STC?
Will they all at least have WB UPIs?
If anyone who does not have a WB UPI will access this system,
then describe who they are,
and if they will have any type of authentication._

_If you know the exact list of people already,
then you can mention them.
Include the UPI for each person (if applicable),
as well as whether they have access to
a WB laptop, remote access to a physical WB desktop,
access to a dedicated virtual machine (called VDI) and/or
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
