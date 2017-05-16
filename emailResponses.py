#! /usr/bin/env python3
# emailResponse.py - Easy way to copy/paste responses to work emails.

RESPONSES = {

'EBDA' : 
'''Hello, we received a report about the malicious domain "" coming through one of your creatives (ext.CRID ""). We've already blocked the creative, but can you please ensure that the flagged URL is blacklisted on your end? Unfortunately, this is all the information that Google is willing to provide, but I appreciate your cooperation on request.

Thanks,
Marc | Rubicon Project, Malware Support'''

,

'beacon' : 
'beacon-us-iad2.rubiconproject.com/beacon/d/4426bce5-e2d9-40e3-9b95-69cb79bb6c0b?accountId=11648&siteId=36320&zoneId=150592&e=…'

,

'TMT' : 
'''Hello, we received a TMT report about the malicious domain "" coming through one of your creatives (ext.CRID ""). We've already blocked the creative, but can you please ensure that the flagged URL is blacklisted on your end? 

Below is the link to the original report:

Thanks,
Marc | Rubicon Project, Malware Support'''

,

'DFP' :
'''Hello, 

The URL has been added to our scanners - I'll let you know if we see any hits. In the meantime, would you mind asking Google to see if our Rubicon beacon was included in the ad call for this URL? For reference, you can send them this: 
beacon-us-iad2.rubiconproject.com/beacon/d/4426bce5-e2d9-40e3-9b95-69cb79bb6c0b?accountId=11648&siteId=36320&zoneId=150592&e=… 

Thanks,
Marc | Rubicon Project, Malware Support '''

,

'DFPs' :
'''Hello, 

The URLs have been added to our scanners - I'll let you know if we see any hits. In the meantime, would you mind asking Google to see if our Rubicon beacon was included in the ad call for these URLs? For reference, you can send them this: 
beacon-us-iad2.rubiconproject.com/beacon/d/4426bce5-e2d9-40e3-9b95-69cb79bb6c0b?accountId=11648&siteId=36320&zoneId=150592&e=… 

Thanks, 
Marc | Rubicon Project, Malware Support '''


}


import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python emailResponse.py [situation] - copy situation response')
	sys.exit()
 
situation = sys.argv[1]	# first command line arg is the account name

if situation in RESPONSES:
	pyperclip.copy(RESPONSES[situation])
	print('Response for ' + situation + ' copied to clipboard.')
else:
	print('There is no response for ' + situation + ".")