import json, ast, base64
from urllib import parse

def lambda_handler(event, context):
    
    #Get test event if test run
    if "teststr" in event:
        event = ast.literal_eval(event["teststr"])
    
    #Get body and parmeter string from slack API call
    bodyEncStr = event["body"]
    paramsstr = str(base64.urlsafe_b64decode(bodyEncStr), "utf-8")

    #Create a mock url to make params work with urllib
    mock_url = "www.example.com/home?" + paramsstr
    params = dict(parse.parse_qsl(parse.urlsplit(mock_url).query))
    print(params)
    
    #Get username and create standard greeting
    user = params["user_name"]
    greeting = "Hello <@{}>, I am the *DIME Analytics* Slack bot :robot_face: - I reply faster than any human in DIME Analytics. :woman-running::man-running:".format(user)
    
    ###################
    # Parse subcommands
    
    #No subcommand used, show helpfile
    if "text" not in params:
        slack_message = """
        
        {} This is my helpfile. Here are the subcommands you can use:
          - `/da github` - info related to GitHub and links to all guidlines for all actions related to the DIME and WB account  
          - `/da scto` - info related to SurveyCTO.
          
        If you do not see a good option here, please email your question to dimeanalytics@worldbank.org.
        
        You can see this helpfile by either typing or `/dimeanalytics` or `/da`.

        """.format(greeting)
    
    #Subcommand github used
    elif params["text"] == "github":
        slack_message = """
        
        {} Here are some *DIME Analytics* GitHub resources:
          - Main page for all DIME Analytics GitHub guidelines: https://github.com/dime-worldbank/dime-account-admin
        """.format(greeting)

    #Subcommand github used
    elif params["text"] == "scto":
        slack_message = """
        
        {} Here are some *DIME Analytics* SurveyCTO resources:
            - Create a new SurveyCTO server in the WB account (WB intranet only): https://worldbankgroup.service-now.com/wbg?id=wbg_sc_catalog&sys_id=7d1e71b86f16d340db112d232e3ee4aa
            - Pause an existing SurveyCTO server in the WB account (WB intranet only): https://worldbankgroup.service-now.com/wbg?id=wbg_sc_catalog&sys_id=87ebb44ddbc1dc10d37979668c961931
        """.format(greeting)

    #No valid subcommand used
    else :
        slack_message = """
            {} The subcommand subcommand `{}` does unfortunately not exist. Type `/da` for valid subcommands.
        """.format(greeting,params["text"])

    response_body = {
        "response_type": "ephemeral",
        "text": slack_message
    }
    
    response_headers = {
        "Content-Type": "application/json"
    }

    return {
        "statusCode": 200,
        "headers" : response_headers,
        "body": json.dumps(response_body)
    }
