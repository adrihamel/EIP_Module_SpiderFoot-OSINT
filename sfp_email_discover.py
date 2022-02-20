# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         sfp_email_discover
# Purpose:      SpiderFoot plug-in for discover email list through a domain.
#
# Author:      Adrián Guerrero Amelín <adrihamel@hotmail.com>
#
# Created:     29/01/2022
# Copyright:   (c) Adrián Guerrero Amelín 2022
# Licence:     GPL
# -------------------------------------------------------------------------------


from spiderfoot import SpiderFootEvent, SpiderFootPlugin

# Modules to import
from urllib.request import urlopen
import json

class sfp_email_discover(SpiderFootPlugin):

    meta = {
        'name': "Email Discover",
        'summary': "Obtein email list throught a domain",
        'flags': [],
        'useCases': ["Passive"],
        'categories': ["Footprint", "Investigate", "Passive"]
    }

    # Default options
    opts = {
    }

    # Option descriptions
    optdescs = {
    }

    results = None

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = self.tempStorage()

        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    # What events is this module interested in for input
    def watchedEvents(self):
        return ["DOMAIN_NAME"]

    # What events this module produces
    # This is to support the end user in selecting modules based on events
    # produced.
    def producedEvents(self):
        return ['DOMAIN_NAME']

    # Handle events sent to this module
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data

        if eventData in self.results:
            return

        self.results[eventData] = True

        self.sf.debug(f"Received event, {eventName}, from {srcModuleName}")

        vulnerabilites_without_duplicates = list()
            
        try:
            self.sf.debug(f"We use the data: {eventData}")
            print(f"We use the data: {eventData}")

            # List to store emails
            data_all = list()

            # Public apikey de hunter.io 
            apikey = 'c54c7e42a8911bdbe353dfbd143eeb4538359348'

            url = 'https://api.hunter.io/v2/domain-search?domain='+ eventData +'&api_key=' + apikey

            request = urlopen(url)
            response = json.loads(request.read().decode('utf-8'))

            # Maximum email size
            size = len(response["data"]["emails"]) - 1

            for i in range(size):
                email = response["data"]["emails"][i]["value"]
                data_all.append(email)
            
        except Exception as e:
            self.sf.error("Unable to perform the <ACTION MODULE> on " + eventData + ": " + str(e))
            return

        for email in data_all:
            evt = SpiderFootEvent('DOMAIN_NAME', email, self.__name__, event)
            self.notifyListeners(evt)

# End of sfp_email_discover class

