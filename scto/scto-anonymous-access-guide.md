# SurveyCTO Anonymous Survey Workflow

## Summary
- This guide relates **_only_** to SurveyCTO data collection using browsers and not data collection on tablets
- This guide covers the following:
    - **Educate the WB teams using SurveyCTO of the**
    [risks of “anonymous access”](https://github.com/dime-worldbank/dimeanalytics/blob/master/scto/scto-anonymous-access-guide.md#understanding-risk-with-anonymous-access)
    when collecting data using the browser.
    While the risk is small,
    we want teams to actively consider it before launching web based data collection.
    - **Provide guidelines on**
    [different methods to mitigate the risk](https://github.com/dime-worldbank/dimeanalytics/blob/master/scto/scto-anonymous-access-guide.md#methods-to-mitigate-risk-with-anonymous-access)
    without compromising on functionality or ease of use


## Background

In SurveyCTO, we can collect data using tablets or using
[Web data collection](https://docs.surveycto.com/03-collecting-data/02-web-data-collection/01.web-forms.html).
**When using Web data collection,
we can either require the respondent to first create an account with email/password authentication,
or enable “_anonymous access_”**.

**We strongly recommend using authentication when possible.**
It is more secure and prevents unauthorized people from submitting data.
You should, for example,
always use it when the enumerators in your team use web browsers to submit data from interviews with respondents.

However, we understand that there are many cases where email/password authentication is not feasible.
Many surveys would have low completion rate if respondents would have to set up accounts before submitting data,
and some data collection needs to be fully anonymous and not associated with someone’s email.
We can see that many surveys on the World Bank server (survey.wb.surveycto.com) do indeed allow anonymous access.

## Understanding risk with anonymous access

What is anonymous access?
To fill in a form using Web data collection,
the SurveyCTO server dashboard generates a URL on this format for your server:

`https://<server_name>.surveycto.com/collect/<form_name>`

- `<server_name>` is the name of your server.
If you are using the World Bank administered SurveyCTO server, then this name is survey.wb.
- `<form_name>` is the name you have given to your form

If you would click the web data collection URL for a form that does not have anonymous access enabled,
then you are asked to log in.
If anonymous access is enabled,
then you get to the beginning of the form and can start filling in data.

**What are the risks with anonymous access?**

- There are risks of receiving made up data,
or real data from a respondent not included in your sample.
- There are risks of being unable to identify,
ex-post, which survey forms represent responses from the expected sample,
as anonymous access leaves no trace regarding who submitted it.
- It in **_no way_** risks exposing data submitted to your server.

**How can someone get unauthorized access to a form with anonymous access?**

It is difficult to completely prevent unauthorized access in a fully anonymous survey.
We recommend you to actively consider:

- How likely it is that someone would use the two methods below to unauthorized submit data?
- What could the consequences be for your data collection activity if someone unauthorized submitted data.

These are the two methods we have identified that someone could use to unauthorized submit data:

1. **Passing on the URL** - Someone that you have shared the URL with passes it on to someone else who is not supposed to submit data
2. **Guessing the URL** - Someone guesses the submission URL (we will show that this is easier than you think)

It is difficult to prevent case 1 where someone **passes on the URL** in a fully anonymous survey.
If you run a fully anonymous survey, you should consider how likely it is that someone would forward the URL to someone else,
and what consequences that would have for the purpose of the data collection.
You might find it very unlikely and there might not be any consequences,
but we recommend you to actively consider it this scenario before you launch your survey.

### Guessing a URL

All Web data collection forms in Survey CTO are filled by accessing a link with the format

`https://<server_name>.surveycto.com/collect/<form_name>`

An there are two unknowns in this URL that needs to be guessed: <server_name> and <form_name>.

While the server name is easier to guess, especially on shared servers like survey.wb,
form names are usually less public as they are based on what you define in each survey form.
However, for every Survey CTO server,
there is a public page that lists all forms on that server with anonymous access.
That URL to that page is:

`https://<server_name>.surveycto.com/collect/forms.html`

Anyone who has figured out how to access this page by using the public URL now has access to all anonymous forms on the server.  

Remember that, if you were to click on the web data collection URL
for a form that does _not_ have anonymous access enabled you will be asked to log in.
On that log in page there is a link to this page listing all forms with anonymous access.

**We are not saying it is likely that this will happen,
we only want the teams using this server to make an informed decision for their data collection activities regarding how likely this would be abused,
and how severe would the consequences be if it did.**

## Methods to mitigate risk with anonymous access

If you’re running a survey which uses web based data collection,
consider incorporating one or several of the following suggestions to mitigate the risks with _anonymous access_.

_Note that not all methods might be applicable to your use case._

### 1. Unique URL for each respondent/sub-groups of respondents

SurveyCTO allows you to include a “Case ID” in the URL.
The URL SurveyCTO generates for web based data collection actually have that parameter prepared for you.
The default is that the parameter is there,
but there is no thing after the equality sign,
so the value passed to the form is by default missing.

`https://survey.wb.surveycto.com/collect/<form_name>/?caseid=`

Anything that you would write after `?caseid=` is accessible anywhere in the form using `${caseid}`.
For example, if the URL ends with `?caseid=a234c2` then `${caseid}` will be equal to `a234c2`.
This value can for example be used in the relevance column or a the constraint column.
It will also be included in your data when you download it from the server.
See more on case IDs in SurveyCTOs documentation [here](https://docs.surveycto.com/03-collecting-data/02-web-data-collection/03.custom-urls.html).

If you were to generate a unique case ID for each respondents,
then you can use that case ID and create unique URLs for each respondent.
Anyone accessing the form from the page listing all forms would easily be identified as this value would be missing.
You would also be able to identify which URL has been passed on to people not included in your sample as that case ID would be duplicated,
and you can easily remove those submissions from your data.
This work flow is described in detail in this
[SurveyCTO blog post](https://support.surveycto.com/hc/en-us/articles/360046325374-Guide-to-unique-links-for-web-forms).

While this is a good practice,
it is a non-trivial exercise to administer the creation of unique case IDs for each respondents
 and the sharing all of them with the right respondent.
 Also, if you were to use this method, then the submissions are not longer fully anonymous.

If you were to chose this method we recommend the following best practices:

1. Make sure that your form has a test that the case ID was not missing.
This can be done by having a required note field that is required with the relevance expression: `empty(${caseid})`
This prevents anyone who went to https://survey.wb.surveycto.com/collect/forms.html and
start submitting data to progress past that required note.
This way you do not have to remove these submissions afterwards.
And the note field can include helpful information,
like and email address, if the respondent has question why they cannot proceed.

2. Even if you use `empty(${caseid})`, make sure that only IDs you created are used,
as someone can simply make up their own case ID and add to the URL.
To prevent someone from guessing a case ID you are actually using,
make sure that all your case IDs are long (8 characters) random strings.

3. When you create case IDs, do not create case IDs where it is easy to guess the other IDs if you know one ID.
For example, if your IDs are id1, id2, id3, then if I see a URL with `?caseid=id12`,
then I can guess that id11, id13 etc. are also valid case IDs.

4. Do not use special characters like “`=`”, “`?`”, “`&`” etc.
They are prone to cause errors in the URL or in your form.

### 2. Put a password in the URL that is applied automatically

This is a simplification of Method 1, so please make sure that you have read Method 1 first.
In order to avoid having to create unique URLs for all respondents (and thereby making it non-anonymous),
like in Method 1, you can create a single case ID that is a long random string used for all respondents.
This could look like this: `?caseid=eVyAgoH7Ep43WxuKjqHcQ75p2o`

This long random string is impossible to guess (even for a powerful computer),
and you will have the same URL for all respondents.
Just like in Method 1, you would have a required note but instead of testing whether the case ID is empty,
you can test that it is exactly the value of the long random string.

`${caseid} != 'eVyAgoH7Ep43WxuKjqHcQ75p2o'`

This is easier to implement compared to Method 1 as you can send the same URL to the all respondents.
One draw back with that is that we do not longer protect the URL from being forwarded by respondents to people not in the sample.
If that is an acceptable risk for your data collection, then this is a good solution.

Similarly to Method 1, do not use any special characters like “`=`”, “`?`”, “`&`” in your case ID.
They are prone to errors in your URL and/or in your form.


### 3. Add a password in the survey form

This method is very similar to Method 2, but instead of passing a case ID in the URL,
you simply share a code that the respondent will have to fill in in the form.
This code can be shared separately.
For example, the link to the form is put on a website but the code is sent in an sms to the respondents.

Just like in Method 1 and 2,
you would have a required note but instead of testing the case ID you would test if the value the used just filled in is equal to the correct code.
A code entered by the responded needs to be shorter and easier to type without errors compared to the case IDs in method 1 and 2.

`${code} != 'AB6784'`

## 4. Adjust the data download and monitoring workflow to look for incorrect entries

While all of these three methods drastically reduces the risk of data submissions from people you do not want to submit data,
there is always a risk that is happens.
Therefore we strongly recommend that all data collections are followed by a monitoring work flow where cased like this can be identified.

Data checks like this should test for many other aspects of data quality,
and not just unwanted submissions.
But we will not cover those in this guide.
Here are 2 ways in which you can monitor the data collection activity to catch unwanted submissions:

1. _Update the High Frequency checks_:
You can download the data as you usually do (through SurveyCTO Desktop or the console) and
then use your high frequency checks to look for unexpected entries.
These checks will be based on the information you’ve regarding the respondents.
For instance, if you know the names of your respondents,
you can check that the names entered in the survey match the list of respondents you have.

2. _Change the review workflow on the SurveyCTO_:
Under default settings, SurveyCTO auto-approves every incoming submission as soon as it comes.
SurveyCTO allows you to enable the review and correction workflow for a form,
in which case new submissions can be initially held awaiting review.
During review, you can examine submissions, comment on them, and make corrections to the data;
when ready, you either approve or reject each submission.
Only approved submissions can be downloaded.
You can find more details about the review workflow [here](https://docs.surveycto.com/04-monitoring-and-management/01-the-basics/04.reviewing-and-correcting.html).
