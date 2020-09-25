# Guide to requesting cloud resources

## Intro - Please read

DIME Analytics will help you request the cloud resources that you need.
Requesting cloud sources at the WB is a very manual process that
will require you and your team to provide answers to a lot of questions.
Unfortunately, this process is slow.
Expect a processing time of about a month for a simple cloud resource,
and several months for a more complex cloud setup.
Understanding the dynamics of this process before you start it
will help you avoid any additional delays.


Cloud resources paid for by WB funding must be created by the WB's IT Services unit (**ITS**).
If you create your own AWS account and create resources you simply will not be reimbursed.
WB ITS will not create anything
until the WB's Office of Information Security (**OIS**)
has reviewed and approved your request.
OIS will have many questions that you and your team will have to answer.
DIME Analytics will support your team in answering these questions,
but will not be able to answer them for you.

OIS and ITS will look primarily at the requirements you need for your cloud service.
They will take into account if you have a specific preference,
but the requirement will always be more important to them.
For example, you can say
"_I would need a server with 32GB RAM (for example AWS EC2) and storage for 200GB data (for example AWS S3)_".
But it will not be sufficient to say "_I want an EC2 server and an S3 bucket_".
It is perfectly fine to not know the name of the product you want,
and you can say "I would need a server with 32GB RAM and storage for 200GB data".

## Process for requesting cloud resources

There is not a single place to request cloud resources at the WB.
DIME Analytics will help you find out where to start but
to do so we need to understand what you need.
The form below includes questions that, in our experience,
is the first things ITS and OIS will ask about,
unless we include that information in our first communication.
The more thoroughly you fill in this information,
the less likely it will be that OIS/ITS
starts this process down the wrong path.
When this happens, these processes can be delayed by weeks
and we will have additional calls
answering the same questions again to a different team at OIS.

Please fill in the form below as well as you can
and send it to dimeanalytics@worldbank.org.
We will then copy this information to a Word document
that we will put on OneDrive and share with you.
We will likely have follow up questions and we need you to answer those comments in the Word document.
This document will be the basis of our request when we contact OIS/ITS.

___

### Basic Info:

* Name of project:
* Contact person in project:
* Name of TTL:
* Unit of TTL:
* Manager of unit of TTL:
* Charge code _(not requeired yet, but will delay process if it is not ready when requested)_:

### Use-case:

_ITS/OIS always want to know the usecase.
They are less interested in economic theory and justification for the study,
and more interested in what function the cloud resource will have in your workflow._

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

"_Who needs access to this system?
This should include everyone that needs access to run code,
access to upload and download data,
access to view any dashboards etc._

_Are all people that need any type of access WB Staff/ETC/STC?
Will they all at least have WB UPIs?
If anyone who does not have a WB UPI will access this system,
then describe who they are,
and if they will have any type of authentication._"

### Access - code:

"_What access does the code need to have to the internet?
For example, if you are scraping the internet,
describe the pages you will scrape and provide the URLs.
If you need to add more URLs in the future,
you can but it will require another request.
You usually only need to give the domain an not the full URL.
For example, if you intend to scrape a few twitter accounts,
then you only need to provide the URL_ `https://twitter.com`
_and not one for each full URL with twitter handles._"

"_You also need to provide details if the systems needs to:
access data from the internet,
install libraries from a non-standard repository etc.
You also need to specify if the resource needs to
be able to receive requests from the internet.
For example, if data will be pushed to this system from another resource._"
