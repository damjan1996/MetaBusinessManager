# MetaBusinessManager Tools Repository

This repository is dedicated to managing and analyzing Facebook Ads campaign data. It contains a Python script that fetches campaign insights from the Facebook Business Manager and compiles an email report detailing the campaign's performance. This tool plays a crucial role in advertising performance analysis and strategic planning.

Facebook Ads Campaign Insights Reporting Tool

This Python script is designed to interact with the Facebook Ads API. It fetches key insights from an active campaign, such as the amount spent, number of clicks, and cost per click. The data is then compiled into a detailed report and sent via email to specified recipients.

The reporting tool generates reports for two timeframes:

The last 24 hours: This provides a snapshot of the campaign's most recent performance.
From the beginning of the campaign: This offers a comprehensive view of the campaign's performance since its launch.
This tool provides a convenient and automated way of tracking the performance of your Facebook Ad campaigns.

# How to Use
To use this script, clone the repository, navigate to the script, and follow these steps:

Install necessary dependencies.
Set your Facebook Ads API credentials in the main() function.
Define the IDs of the campaigns you wish to fetch data from.
Set your SMTP server settings to enable the script to send emails.
Run the script.
Please note that these scripts are developed with a certain version of the Facebook Ads API in mind. If you encounter any compatibility issues, please raise an issue for this repository.

# Contributions
Contributions are welcome! If you have improvements, bug fixes, or other changes you would like to make, please fork the repository, make your changes, and submit a pull request.
