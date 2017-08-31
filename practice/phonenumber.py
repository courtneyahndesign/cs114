#Write a small app that asks the user for an all-digits ten or seven digit phone number. Then pretty prints it out in both XXX-XXX-XXXX and (XXX) XXX-XXXX format. If there isn't an area code, drop that part.

#Phone number? All digits. 5035551234

#503-555-1234

#(503) 555-1234

#Phone number? All digits. 5551234

#555-1234

#555-1234

print("What's your phone number")
phone = input()

areacode = len(phone) == 10

if areacode:
    phoneparts = [phone[:4], phone[4:7], phone[7;]]
else:
    phoneparts = [phone[:4], phone [4:]]

dashed_phone
