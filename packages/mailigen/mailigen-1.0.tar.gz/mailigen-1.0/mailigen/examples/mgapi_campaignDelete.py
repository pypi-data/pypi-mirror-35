from mailigen.lib.config import * #contains apikey
from mailigen.lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId


retval = api.campaignDelete(cid)
if api.errorCode:
	print "Unable to load campaignDelete()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Campaign Deleted!"
