# signalsciences
Export the requests
Main script forked from https://docs.signalsciences.net/developer/extract-your-data/#example-usage

The recommended way to use this endpoint is to set up a cron that runs at 5 minutes past each hour and fetches the previous full hour’s worth of data.
In the example below, we calculate the previous full hour’s start and end timestamps and use them to call the API.

example setting the environment variables for the password script:
export SIGSCI_EMAIL='email@domain.com'
export SIGSCI_PASSWORD='***********'

example setting the environment variables for the token script:
export SIGSCI_EMAIL='email@domain.com'
export SIGSCI_TOKEN='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
