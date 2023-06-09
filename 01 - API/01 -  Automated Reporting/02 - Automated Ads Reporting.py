import datetime
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_campaign_insights(campaign_id: str, since_date: str, until_date: str):
    """
    Fetch insights for the given campaign ID and date range
    """
    campaign = Campaign(campaign_id)
    campaign.api_get(fields=[Campaign.Field.name])
    return campaign.get_insights(fields=['spend', 'clicks', 'cpc'],
                                 params={'time_range': {'since': since_date, 'until': until_date}})

def prepare_email(summary_text: str):
    """
    Prepare an email message with the given summary text
    """
    msg = MIMEMultipart()
    msg['From'] = 'sender@example.com'
    msg['To'] = 'receiver@example.com'
    msg['Subject'] = 'Current Reporting'
    msg.attach(MIMEText(summary_text, 'plain'))
    return msg.as_string()

def send_email(smtp_server: str, smtp_port: int, username: str, password: str, text: str):
    """
    Send an email via the provided SMTP server
    """
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail('sender@example.com', ['receiver1@example.com', 'receiver2@example.com', 'receiver3@example.com'], text)
    server.quit()

def main():
    """
    Main function that gets campaign insights and sends an email report
    """

    # Set credentials
    my_app_id = 'your_app_id'
    my_app_secret = 'your_app_secret'
    my_access_token = 'your_access_token'
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    # Set the ID of the Meta Ads campaign
    campaign_id = 'your_campaign_id'
    now = datetime.datetime.now()

    # For the last 24-hour report
    start_time_24h = (now - datetime.timedelta(hours=24)).strftime('%Y-%m-%d')
    stats_24h = get_campaign_insights(campaign_id, start_time_24h, now.strftime('%Y-%m-%d'))

    # For the report since the beginning of the campaign
    # Set the actual start date of your campaign here
    start_time_beginning = '2023-01-01'
    stats_beginning = get_campaign_insights(campaign_id, start_time_beginning, now.strftime('%Y-%m-%d'))

    # Create the summary text
    summary_text = 'Hello,\n\n'
    summary_text += 'Here is the current report regarding the ongoing campaigns:\n\n'
    summary_text += '= Reporting over the past 24 hours =\n'
    summary_text += f'Active campaign\n'
    summary_text += f'Spend: {float(stats_24h[0]["spend"]):.2f} Euro\n'
    summary_text += f'Visitors: {stats_24h[0]["clicks"]}\n'
    summary_text += f'Cost per visitor: {float(stats_24h[0]["cpc"]):.2f} Euro\n\n'
    summary_text += '= Reporting since the beginning of the campaign =\n'
    summary_text += f'Active campaign\n'
    summary_text += f'Spend: {float(stats_beginning[0]["spend"]):.2f} Euro\n'
    summary_text += f'Visitors: {stats_beginning[0]["clicks"]}\n'
    summary_text += f'Cost per visitor: {float(stats_beginning[0]["cpc"]):.2f} Euro\n\n'
    summary_text += 'Reporting time: ' + now.strftime("%d.%m.%Y at %H:%M.") + '\n\n'
    summary_text += 'Best regards,\nYour Name\nMarketing & E-Commerce Manager'
    email_text = prepare_email(summary_text)

    # Set your SMTP settings
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # This may vary depending on your SMTP server
    username = 'sender@example.com'
    password = 'your_password'
    send_email(smtp_server, smtp_port, username, password, email_text)

if __name__ == "__main__":
    main()
