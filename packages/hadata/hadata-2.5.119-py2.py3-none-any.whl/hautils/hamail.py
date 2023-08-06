import datetime
import json
import re
import sys, os
import boto3
import jwt
from hautils.aws import get_client
from hadata.user import MongoUser
from hareqres.jwtbearer import JWT_SECRET, JWT_ALGORITHM
from hareqres.jwtbearer import encode_jwt
from hautils.logger import logger


def email_token(receiver):
    """
    The email_token function takes a receiver email address as an argument and returns a token.
    The token is created by encoding the receiver email address in a JWT payload, which expires after 48 hours.

    :param receiver: Send the email to the user
    :return: A token that is a jwt
    :doc-author: Trelent
    """
    logger.info("email token called with %s" % (receiver,))
    payload = {
        "email": receiver,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=2)
    }
    logger.info("token creation %s" % (payload,))
    token = encode_jwt(payload)
    logger.info("token created %s" % (token,))
    return token


####
# @params user = instance of mongo user, only used (email, firstname, lastname)
# @kwargs origin = (needs to match the site that the template should be
# marked as base) default to localhost:3000
####
def send_registration_confirmation(user, **kwargs):
    hostname = kwargs.get("origin", "http://localhost:3000")
    hostname = re.sub(r"\/$", "", hostname)
    logger.info(f"hostname is {hostname}")
    token = email_token(user.email)
    template_data = json.dumps(
        {"first_name": user.first_name, "last_name": user.last_name, "hostname": hostname, "token": token})
    ses = get_client('ses')
    response = ses.send_templated_email(
        Source="HiAcuity Support <support@hiacuity.com>",
        Template="Registration",
        ConfigurationSetName="hiacuity",
        Destination={"ToAddresses": [user.email]},
        SourceArn='arn:aws:ses:ap-southeast-1:898389633641:identity/hiacuity.com',
        TemplateData=template_data
    )
    logger.info(f"{response}")
    return response


async def send_assessment_invitation(user: MongoUser, **kwargs):
    ses = get_client('ses')
    token = email_token(user.email)
    hostname = kwargs.get("origin", "http://localhost:3000")
    hostname = re.sub(r"\/$", "", hostname)
    logger.info(f"hostname is {hostname}")
    template_data = json.dumps(
        {"first_name": user.first_name, "company_name": "Hiacuity", "password": user.clear_password,
         "hostname": hostname,
         "token": token, "email": user.email, "last_name": user.last_name})
    new_user = kwargs.get("new_user", False)
    template_name = "InviteOld"
    if new_user is True:
        template_name = "Invitation"
    ses.send_templated_email(
        Source="HiAcuity Support <support@hiacuity.com>",
        Template=template_name,
        ConfigurationSetName="hiacuity",
        Destination={"ToAddresses": [user.email]},
        SourceArn='arn:aws:ses:ap-southeast-1:898389633641:identity/hiacuity.com',
        TemplateData=template_data
    )


async def verify_token(token: str):
    """
    The verify_token function takes a token as an argument and returns the user object associated with that token.
    The function uses the jwt library to decode the token, then loads it into a json object. The json object is then
    used to query MongoDB for the user's document, which is returned.

    :param token:str: Pass the token that is being verified
    :return: A dictionary of the user's information
    :doc-author: Trelent
    """
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    user = json.loads(MongoUser.objects(email=payload.get("email")).to_json())
    selected_user = user[0]
    return selected_user
