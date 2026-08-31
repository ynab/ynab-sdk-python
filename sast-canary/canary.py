# Deliberate SAST canary fixture for testing the ynab-sast-scanner migration end to end.
# Not real code path — exercises TLS verification being disabled on an outbound request,
# a genuine, unsuppressed finding, to confirm the new workflow actually blocks a PR.
import requests


def fetch_user_avatar(user_supplied_url):
    return requests.get(user_supplied_url, verify=False)
