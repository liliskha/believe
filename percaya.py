# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import *
import glob
from LINETCR.Api import Channel
from LINETCR.lib.curve.ttypes import Message
from threading import Thread
from io import StringIO
from imgurpython import ImgurClient
import time, random, sys, re, os, json, subprocess, threading, datetime, string, codecs, requests, tweepy, ctypes, multiprocessing 
import urllib2
import urllib
import urbandictionary as ud

cl = LINETCR.LINE()
cl.login(token='El50LJVcYcapmHQ1Ktrf.wcKT3lNClJNWKWz3SYD3NW.lT4Juby532p+REDWqQqo9Tufly/SqNDYGQ+wGlWSlXo=')
cl.loginResult()

ki = LINETCR.LINE() 
ki.login(token='EmdpMtI7LTgnkL7tU7L9.ascU7pKGWRV3sNLHX8366q./6tF2HKxVHgJAtCHp+/Ujiv3PDbqOCtROf1l31DldyM=')
ki.loginResult()

kk = LINETCR.LINE() 
kk.login(token='Em6vTKQzz13ZvHyQxDO5.B/u0zQii9RWpKoS5mQeOLq.rAlNONTaeC9fZ6SnMKdRbDOIck5A0V0eqeUvKRg5uA0=')
kk.loginResult()

kc = LINETCR.LINE() 
kc.login(token='EmOSg8CEXV48FobO1Zve.9D4AKJdAxWzC3Q0GAIIX3G.7sXJjZwjwjgX3R9OMGGMf6q91kvqDtd7kq66KvMi9RM=')
kc.loginResult()


print "login all success"
reload(sys)
sys.setdefaultencoding('utf-8')

album = None
image_path = 'tmp/tmp.jpg'

helpMessage =""" [RFO] Self Bot

Me
Mid
Cek
Gift
Cancel
Ginfo
Link on
Fx1 link on
link off
Fx1 link off
Gn (group name)
Fx1 gn
Fx1/2/3cn [anu]
Ban @
Unban @
Fx ban
Fx unban
Looking up
Looking result
Tagall
Fx join
Fx bye
Spam add
Spam add1
Spam: number spam
Fx1 spam:
"""
KAC=[ki,kk,kc]
INV=[kk,ki,kc]
p1=[ki,kk,kc]
p2=[kk,kc]
p3=[ki,kc]
p4=[ki,kk]
wuk=random.choice(KAC)
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid]
global Switch1
Switch1 = 1
controlall=["u67bfe927898b722d7c3e7645be88b2e9",mid,Amid,Bmid,Cmid]
creator='u58292ddcb9dc2e39f0930677b327779f'
admin=["u58292ddcb9dc2e39f0930677b327779f", "ua6cc2bfe8e9808aabff052aaeb98d5cd"]
global staff
staff = [""]
bolehin=[""]
global accesed
accesed = list(controlall) + bolehin
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"My Real name is juan, thanks for add me in your life :)",
    "lang":"JP",
    "comment":"Thanks for add me in your life :)",
    "spam":"None spam",
    "spam1":"None spam",
    "spam2":"None spam",
    "spam3":"None spam",
    "spam4":"None spam",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "pesanlike":"",    
    "wmark":"Auto Like by Raidentz Flame Offical\n\nwww.instagram.com/juan_pradana\n",    
    "cName":"‮ABR inazraF",
    "clock":False,
#   "maling":False,
    "autokik":False,
    "protectqr":False,
    "backup":True,
    "cancel":False,
    'whitelist':{},
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "wlcmsg":False,
    "wlctxt":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

wait3 = {
    "copy":False,
    "copybot":False,
    "copy2":"target",
    "target":{}
    }
    
setTime = {}
setTime = wait2['setTime']

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False

def upload_tempimage(self):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = cl.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    print nm
    for nm in nm:
        akh = akh + 3
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(nm)+"},"""
        strt = strt + 4
        akh = akh + 1
        bb += "@x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print error
        
def sendContact(to,mid):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = None
    mes.contentType = 13
    mes.contentMetadata = {'mid': mid}
    cl.sendMessage(mes)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
#                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
 #                   if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
  #                  if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
   #                 if op.param2 in mid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                 G = cl.getGroup(op.param1)
                 if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                 elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
                 Y = cl.getGroup(op.param1)
                 ginfo = cl.getGroup(op.param1)
                 Y.preventJoinByTicket = False
                 cl.updateGroup(Y)
                 invsend = 0
                 Ticket = cl.reissueGroupTicket(op.param1)
                 ki.acceptGroupInvitationByTicket(op.param1,Ticket)
		 #ki.sendText(msg.to, "siap")
                 time.sleep(0.02)
                 kk.acceptGroupInvitationByTicket(op.param1,Ticket)
		 #kk.sendText(msg.to, "otw")
                 time.sleep(0.02)
                 kc.acceptGroupInvitationByTicket(op.param1,Ticket)
		 #kc.sendText(msg.to, "ready")
                 time.sleep(0.02)
                 Y = cl.getGroup(op.param1)
                 Y.preventJoinByTicket = True
                 ki.updateGroup(Y)
                 print "kicker ok"
                 G.preventJoinByTicket(Y)
                 ki.updateGroup(Y)
            if Amid in op.param3:
                 G = ki.getGroup(op.param1)
                 if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                 elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            if Bmid in op.param3:
                 G = kk.getGroup(op.param1)
                 if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                 elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            if Cmid in op.param3:
                 G = kc.getGroup(op.param1)
                 if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                 elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kc.rejectGroupInvitation(op.param1)
                    
#	if op.type == 19:
 #               if not op.param2 in Bots:
  #                  try:
   #                     gs = ki.getGroup(op.param1)
    #                    gs = kk.getGroup(op.param1)
     #                   gs = cl.getGroup(op.param1)
      #                  targets = [op.param2]
       #                 for target in targets:
        #                   try:
         #                       wait["blacklist"][target] = True
          #                      f=codecs.open('st2__b.json','w','utf-8')
           #                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            #               except:
             #               return
#
 #                   except Exception, e:
  #                     print e
	if op.type == 17:
	  group = kc.getGroup(op.param1)
	  if wait["wlcmsg"] == True:
    	    try:
        	wuk.sendText(op.param1, wuk.getContact(op.param2).displayName + " Selamat datang di " + group.name + "\n" + wait["wlctxt"])
            except Exception as error:
	        print error        
        if op.type == 11:
            try:
                if not op.param2 in Bots and not op.param2 in wait["whitelist"]:
                   if op.param3 == "1":
                       group = random.choice(KAC).getGroup(op.param1)
                       try:
                           D = open(op.param1 + "lockname.txt","r")
                           name = D.read()
                           D.close()
                           group.name = name
                           random.choice(KAC).updateGroup(group)
                           random.choice(KAC).sendText(op.param1, "Jangan ubah2 nama group")
                       except Exception as e:
                           print e
                           pass
                   else:
                       pass
            except:
                print "Udah"
        if op.type == 19:
                if mid in op.param3:
                  if op.param2 not in accesed:
                    try:
                        random.choice(p1).kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    	X = random.choice(p1).getGroup(op.param1)
                    	X.preventJoinByTicket = False
                    	random.choice(p1).updateGroup(X)
                    	Ti = random.choice(p1).reissueGroupTicket(op.param1)
                    	cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    	kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    	kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    	ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    	G = random.choice(KAC).getGroup(op.param1)
                    	G.preventJoinByTicket = True
                    	random.choice(KAC).updateGroup(G)
                    	Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                    except:
                        try:
                            
			    wait["blacklist"][op.param2] = True
	                    X = random.choice(p1).getGroup(op.param1)
	                    X.preventJoinByTicket = False
	                    random.choice(p1).updateGroup(X)
	                    Ti = random.choice(p1).reissueGroupTicket(op.param1)
	                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
	                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
	                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
	                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
	                    G = random.choice(KAC).getGroup(op.param1)
	                    G.preventJoinByTicket = True
	                    random.choice(KAC).updateGroup(G)
	                    Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                if Amid in op.param3:
                  if op.param2 not in accesed:
                    try:
                        random.choice(p2).kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    	X = random.choice(p2).getGroup(op.param1)
                    	X.preventJoinByTicket = False
                    	random.choice(p2).updateGroup(X)
                    	Ti = random.choice(p2).reissueGroupTicket(op.param1)
                    	ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    	kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    	kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    	cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    	G = random.choice(KAC).getGroup(op.param1)
                    	G.preventJoinByTicket = True
                    	random.choice(KAC).updateGroup(G)
                    	Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                    except:
                        try:
                            
			    wait["blacklist"][op.param2] = True
	                    X = random.choice(p2).getGroup(op.param1)
	                    X.preventJoinByTicket = False
	                    random.choice(p2).updateGroup(X)
	                    Ti = random.choice(p2).reissueGroupTicket(op.param1)
	                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
	                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
	                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
	                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
	                    G = random.choice(KAC).getGroup(op.param1)
	                    G.preventJoinByTicket = True
	                    random.choice(KAC).updateGroup(G)
	                    Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                  if op.param2 not in accesed:
                    try:
                        random.choice(p3).kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    	X = random.choice(p3).getGroup(op.param1)
                    	X.preventJoinByTicket = False
                    	random.choice(p3).updateGroup(X)
                    	Ti = random.choice(p3).reissueGroupTicket(op.param1)
                    	kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    	cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    	kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    	ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    	G = random.choice(KAC).getGroup(op.param1)
                    	G.preventJoinByTicket = True
                    	random.choice(KAC).updateGroup(G)
                    	Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                    except:
                        try:

			    wait["blacklist"][op.param2] = True
	                    X = random.choice(p3).getGroup(op.param1)
	                    X.preventJoinByTicket = False
	                    random.choice(p3).updateGroup(X)
	                    Ti = random.choice(p3).reissueGroupTicket(op.param1)
	                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
	                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
	                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
	                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
	                    G = random.choice(KAC).getGroup(op.param1)
	                    G.preventJoinByTicket = True
	                    random.choice(KAC).updateGroup(G)
	                    Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                if Cmid in op.param3:
                  if op.param2 in accesed:
                    try:
                        random.choice(p4).kickoutFromGroup(op.param1,[op.param2])
			wait["blacklist"][op.param2] = True
                    	X = random.choice(p4).getGroup(op.param1)
                    	X.preventJoinByTicket = False
                    	random.choice(p4).updateGroup(X)
                    	Ti = random.choice(p4).reissueGroupTicket(op.param1)
                    	kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    	kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    	cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    	ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    	G = random.choice(KAC).getGroup(op.param1)
                    	G.preventJoinByTicket = True
                    	random.choice(KAC).updateGroup(G)
                    	Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                    except:
                        try:

			    wait["blacklist"][op.param2] = True
	                    X = random.choice(p4).getGroup(op.param1)
	                    X.preventJoinByTicket = False
	                    random.choice(p4).updateGroup(X)
	                    Ti = random.choice(p4).reissueGroupTicket(op.param1)
	                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
	                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
	                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
	                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
    	                    G = random.choice(KAC).getGroup(op.param1)
	                    G.preventJoinByTicket = True
	                    random.choice(KAC).updateGroup(G)
	                    Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
	if op.type == 17:
	  group = kc.getGroup(op.param1)
	  if wait["autokik"] == True:
	   if op.param2 in wait["blacklist"]:
    	    try:
        	kc.kickoutFromGroup(op.param1,[op.param2])
            except Exception as error:
	        print error
	if op.type == 19:
	    if op.param2 not in accesed:
	      if wait["autokik"] == True:
		try:
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		except:
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
	if op.type == 19:
	    if wait["backup"] == True:
                if op.param3 in accesed:
                  if op.param2 not in accesed:                    
		    try:
		        ki.inviteIntoGroup(op.param1,[op.param3])
		        ki.kickoutFromGroup(op.param1,[op.param2])
                        wait ["blacklist"][op.param2] = True
		    except:
		      try:
		        ki.kickoutFromGroup(op.param1,[op.param2])
			ki.inviteIntoGroup(op.param1,[op.param3])
                        wait ["blacklist"][op.param2] = True
                      except:
                        wuk.sendText(op.param1,"limit")
#-----------------------------------------------------------
        if op.type == 11:
            if not op.param2 in accesed:
              if wait["protectqr"] == True:
                try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
            		G.preventJoinByTicket = True
     			random.choice(KAC).updateGroup(G)
                except Exception, e:
                    print e
#----------------------------------------------------------------
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
		  if wait["autokik"] == True:
                    kk.cancelGroupInvitation(op.param1, matched_list)
	if op.type == 55:
            try:
        	if op.param1 in wait2['readPoint']:
            	    Name = cl.getContact(op.param2).displayName
            	    if Name in wait2['readMember'][op.param1]:
                	pass
            	    else:
                	wait2['readMember'][op.param1] += "\n・" + Name
                	wait2['ROM'][op.param1][op.param2] = "・" + Name
            	else:
            	    pass
    	    except:
        	pass
	if op.type == 26:
    	    msg = op.message
    	    try:
        	if msg.contentType == 0:
            	    try:
                	if msg.to in wait['readPoint']:
                    	    if msg.from_ in wait["ROM"][msg.to]:
                        	del wait["ROM"][msg.to][msg.from_]
                	else:
                    	    pass
            	    except:
                    	pass
        	else:
            	    pass
    	    except:
		pass
	if op.type == 13:
	    if not op.param2 in accesed:
	      if wait["cancel"] == True:
		try:
                    X = random.choice(KAC).getGroup(op.param1)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
		    else:
			pass
		except Exception, e:
		    print e
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                    msg.to = msg.from_
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)                            
            elif msg.from_ in wait3["target"] and wait3["copy"] == True and wait3["copy2"] == "target":
                    klist = [ki,kk,kc,cl]
                    po = random.choice(klist)
                    for i in range(1):
                        cl.sendText(msg.to,msg.text)
                        wait3["copy"] = False
                    wait3["copy"] = True 
            elif msg.from_ in wait3["target"] and wait3["copybot"] == True and wait3["copy2"] == "target":
                    klist = [ki,kk,kc]
                    po = random.choice(klist)
                    for i in range(1):
                        po.sendText(msg.to,msg.text)
                        wait3["copybot"] = False
                    wait3["copy"] = True                                                
            elif msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            elif msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
#            elif "join " in msg.text.lower():
#		rplace=msg.text.lower().replace("join ")
#		if rplace == "on":
#			wait["atjointicket"]=True
#		elif rplace == "off":
#			wait["atjointicket"]=False
#		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
 #           elif '/ti/g/' in msg.text.lower():
#		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
#		links = link_re.findall(msg.text)
#		n_links=[]
#		for l in links:
#			if l not in n_links:
#				n_links.append(l)
#		for ticket_id in n_links:
#			if wait["atjointicket"] == True:
#				group=cl.findGroupByTicket(ticket_id)
#				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
#				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
    
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted Blacklist")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already in blacklist")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded to blacklist")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted to blacklist")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.text is None:
                return
            elif msg.text in ["Fx key","Help","Key","Juan help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Fx1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Fx1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Fx2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Fx2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif "Fx kick " in msg.text:
                midd = msg.text.replace("Fx kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Fx2 kick " in msg.text:
                midd = msg.text.replace("Fx2 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
	    elif "Fx3 kick " in msg.text:
                midd = msg.text.replace("Fx3 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "MyInvite " in msg.text:
                midd = msg.text.replace("MyInvite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                wuk.findAndAddContactsByMid(midd)
                wuk.inviteIntoGroup(msg.to,[midd])                
            elif "Fx1 invite " in msg.text:
                midd = msg.text.replace("Fx1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Fx2 invite " in msg.text:
                midd = msg.text.replace("Fx2 invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Fx3 invite " in msg.text:
                midd = msg.text.replace("Fx3 invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Bot contact"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
		msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
		msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
	    elif "Cek" in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    mi = cl.getContact(key1)
                    cl.sendText(msg.to,key1)
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': key1}
		    cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Fx1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Fx2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Fx3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Fx all gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Fx cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = wuk.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        wuk.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            wuk.sendText(msg.to,"No one is inviting")
                        else:
                            wuk.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        wuk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        wuk.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open qr","Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Fx1 open qr","Fx1 link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Open qr")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close qr","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Fx1 curl","Fx1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Chivas")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Gcreator":
             if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
			gCmid = ginfo.creator.mid
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
			gCmid = "Error"
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"group creator\n" + "@" + gCreator)
			msg.contentType = 13
			msg.contentMetadata = {'mid': gCmid}
			cl.sendMessage(msg)
                    else:
                        cl.sendText(msg.to,"group creator\n" + "@" + gCreator)
	     else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

#=========================================================================                        
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
            elif "Id" == msg.text:
                wuk.sendText(msg.to,msg.to)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Fx1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Fx2 mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "Fx3 mid" == msg.text:
                kc.sendText(msg.to,Cmid)
            elif msg.text in ["hahaha"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif ("Asst1cn " in msg.text):
              if msg.toType == 2:
                profile = ki.getProfile()
                X = msg.text.replace("Asst1cn ","")
                profile.displayName = X
                ki.updateProfile(profile)
                ki.sendText(msg.to,"name " + X + " done")
              else:
                ki.sendText(msg.to,"Failed")
            elif ("Asst2cn " in msg.text):
              if msg.toType == 2:
                profile = kk.getProfile()
                X = msg.text.replace("Asst2cn ","")
                profile.displayName = X
                kk.updateProfile(profile)
                kk.sendText(msg.to,"name " + X + " done")
              else:
                kk.sendText(msg.to,"Failed")
            elif ("Asst3cn " in msg.text):
              if msg.toType == 2:
                profile = kc.getProfile()
                X = msg.text.replace("Asst3cn ","")
		profile.displayName = X
                kc.updateProfile(profile)
                kc.sendText(msg.to,"name " + X + " done")
              else:
                kk.sendText(msg.to,"Failed")
	    elif ("Allcn " in msg.text):
              if msg.toType == 2:
                profile = kk.getProfile()
		profile = ki.getProfile()
		profile = kc.getProfile()
                X = msg.text.replace("Allcn ","")
                profile.displayName = X
                kk.updateProfile(profile)
		ki.updateProfile(profile)
		kc.updateProfile(profile)
                kk.sendText(msg.to,"name " + X + " done")
		ki.sendText(msg.to,"name " + X + " done")
		kc.sendText(msg.to,"name " + X + " done")
              else:
                kk.sendText(msg.to,"Failed")
	    elif ("MyCN " in msg.text):
              if msg.toType == 2:
                profile = cl.getProfile()
                X = msg.text.replace("MyCN ","")
                profile.displayName = X
                cl.updateProfile(profile)
                cl.sendText(msg.to,"name " + X + " done")
              else:
                cl.sendText(msg.to,"Failed")                
	    elif ("Mybio: " in msg.text):
              if msg.toType == 2:
                profile = cl.getProfile()
                X = msg.text.replace("Mybio: ","")
                profile.statusMessage = X
                cl.updateProfile(profile)
                cl.sendText(msg.to,"bio " + X + " done")
              else:
                cl.sendText(msg.to,"Failed")
	    elif ("Allbio: " in msg.text):
              if msg.toType == 2:
                profile = kk.getProfile()
		profile = ki.getProfile()
		profile = kc.getProfile()
                X = msg.text.replace("Allbio: ","")
                profile.statusMessage = X
                kk.updateProfile(profile)
		ki.updateProfile(profile)
		kc.updateProfile(profile)
                kk.sendText(msg.to,"bio " + X + " done")
		ki.sendText(msg.to,"bio " + X + " done")
		kc.sendText(msg.to,"bio " + X + " done")
              else:
                cl.sendText(msg.to,"Failed")       
            elif msg.text in ["Listgroup"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "(*)%s:{%s}\n" % (cl.getGroup(i).name,str(len(cl.getGroup(i).members)))
                cl.sendText(msg.to,h)                         
            elif "ByeGroup " in msg.text:
                    print "[keluar]ok"
                    _name = msg.text.replace("ByeGroup ","")
                    out = _name.rstrip('  ')
                    ginfo = cl.getGroup(out)
                    try:
                        ki.leaveGroup(out)
                        kk.leaveGroup(out)
                        kc.leaveGroup(out)
			cl.leaveGroup(out)
			cl.sendText(msg.to,"succes leave " + str(ginfo.name))
                    except:
                        cl.sendText(msg.to,"gagal")
            elif "Getpp " in msg.text:
                    print "[get]ok"
                    _name = msg.text.replace("Getpp ","")
                    pp = _name.rstrip('  ')
                    try:
		        cl.updateProfilePicture(pp)
		        cl.sendText(msg.to, "succes")
                    except:
                        cl.sendText(msg.to,"gagal")                                        
                #============================================================================================
            elif msg.text in ["Mimic on"]:
                if wait3["copy"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait3["copy"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mimic off"]:
                if wait3["copy"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait3["copy"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mimicbot on"]:
                if wait3["copybot"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait3["copybot"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mimicbot off"]:
                if wait3["copybot"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait3["copybot"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")                        
            elif "Pesanlike change: " in msg.text:
	       if msg.from_ in admin:
                wait["pesanlike"] = msg.text.replace("Pesanlike change: ","")
                cl.sendText(msg.to,"Pesanlike changed")                         
                        #===========================================================================================                
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Autojoin on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Autojoin off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Welcome message on"]:
                if wait["wlcmsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["wlcmsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Welcome message off"]:
                if wait["wlcmsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["wlcmsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Autoleave on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Autoleave off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Fx share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Fx share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
#            elif msg.text in ["maling:on","Fx maling:on"]:
 #               if wait["maling"] == True:
  #                  if wait["lang"] == "JP":
   #                     cl.sendText(msg.to,"Already on")
    #                else:
     #                   cl.sendText(msg.to,"Protec Maling On")
      #          else:
       #             wait["maling"] = True
        #            if wait["lang"] == "JP":
         #               cl.sendText(msg.to,"Protect Maling On")
          #          else:
           #             cl.sendText(msg.to,"already on")
#            elif msg.text in ["maling:off","Fx maling:off"]:
 #               if wait["maling"] == False:
  #                  if wait["lang"] == "JP":
   #                     cl.sendText(msg.to,"Already off")
    #                else:
     #                   cl.sendText(msg.to,"Protect Maling Off")
      #          else:
       #             wait["maling"] = False
        #            if wait["lang"] == "JP":
         #               cl.sendText(msg.to,"Protect Maling Off")
          #          else:
           #             cl.sendText(msg.to,"Already off")

            elif msg.text in ["Mlist"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target copy user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif msg.from_ in admin and wait3["copy"] == True and wait3["copy2"] == "me" and "Ccopy" not in msg.text:
                    klist = [kk,kc,ki,cl]
                    po = random.choice(klist)
                    for i in range(1):
                        po.sendText(msg.to,msg.text)
                        wait3["copy"] = False
                    wait3["copy"] = True

            elif "Mimic " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("MyMimic ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"MyMimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"MyMimic change to target")
                            else:
                                cl.sendText(msg.to,"Not Found -_-")
                               
            elif "Mtarget @" in msg.text:
                        target = msg.text.replace("Mtarget @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"MTarget added")
                               
            elif "Del mimic @" in msg.text:
                        target = msg.text.replace("Del mimic @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"MTarget deleted")
           #=======================================================================================
	    elif "Kepo " in msg.text:
                       nk0 = msg.text.replace("Kepo ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:		    
		            try:    
		        	print target
                            	contact = cl.getContact(target)
                        	try:
                            	    cu = cl.channel.getCover(target)
                        	except:
                            	    cu = ""
                        	cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + target + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
     			    except Exception as e:
     			     print e
     			     cl.sendText(msg.to, e)	
#================================================================================                    
            elif msg.text in "Backup my profile":
            	    wek = cl.getContact(mid)
                    k = wek.pictureStatus            	    
                    i = wek.displayName
                    j = wek.statusMessage
                    s = open('mydn.txt',"w")
                    s.write(i)
                    s.close()
                    t = open('mysm.txt',"w")
                    t.write(j)
                    t.close()
                    u = open('myps.txt',"w")
                    u.write(k)
                    u.close()                                        
                    cl.sendText(msg.to, "backup has been active")
                    print wek
                    print i
                    print j
                    print k
	    elif "Back profile" in msg.text:
		        try:
		            h = open('mydn.txt',"r")
		            name = h.read()
		            h.close()
		            x = name
		            profile = cl.getProfile()
		            profile.displayName = x
		            cl.updateProfile(profile)
		            i = open('mysm.txt',"r")
		            sm = i.read()
		            i.close()	            
		            y = sm
		            cak = cl.getProfile()
		            cak.statusMessage = y
		            cl.updateProfile(cak)
		            j = open('myps.txt',"r")
		            ps = j.read()
		            j.close()		            
		            p = ps
		            cl.updateProfilePicture(p)
		            cl.sendText(msg.to, "succes")
		            		            
		        except Exception as e:
		            cl.sendText(msg.to,"gagal")
		            print e                    
            elif msg.text in ["Back all profile run"]:
            	    wek = ki.getContact(Amid)
                    k = wek.pictureStatus            	    
                    i = wek.displayName
                    j = wek.statusMessage
                    s = open('botdn.txt',"w")
                    s.write(i)
                    s.close()
                    t = open('botsm.txt',"w")
                    t.write(j)
                    t.close()
                    u = open('botps.txt',"w")
                    u.write(k)
                    u.close()                                        
                    cl.sendText(msg.to, "backup bot has been active")
                    print wek
                    print i
                    print j
                    print k
	    elif "Back all profile" in msg.text:
		        try:
		            h = open('botdn.txt',"r")
		            name = h.read()
		            h.close()
		            x = name
		            profile = ki.getProfile()
		            profile1 = kk.getProfile()
		            profile2 = kc.getProfile()
		            profile.displayName = x
		            profile1.displayName = x
		            profile2.displayName = x
		            ki.updateProfile(profile)
		            kk.updateProfile(profile1)
		            kc.updateProfile(profile2)
		            i = open('botsm.txt',"r")
		            sm = i.read()
		            i.close()	            
		            y = sm
		            cak = ki.getProfile()
		            cak1 = kk.getProfile()
		            cak2 = kc.getProfile()
		            cak.statusMessage = y
		            cak1.statusMessage = y
		            cak2.statusMessage = y
		            ki.updateProfile(cak)
		            kk.updateProfile(cak1)
		            kc.updateProfile(cak2)
		            j = open('botps.txt',"r")
		            ps = j.read()
		            j.close()		            
		            p = ps
		            ki.updateProfilePicture(p)
		            kk.updateProfilePicture(p)
		            kc.updateProfilePicture(p)
		            kc.sendText(msg.to, "succes")
		            		            
		        except Exception as e:
		            kc.sendText(msg.to,"gagal")
		            print e                    		            
#==============================================================================        

            elif msg.text in ["Lockname off","Protect nama group off","Lock Gname off"]:
                        gid = msg.to
                        os.remove(gid + "lockname.txt")
                        random.choice(KAC).sendText(msg.to, "Lock name off")
            elif msg.text in ["Lockname on","Proteksi nama group on","Lock Gname on"]:
                    gid = msg.to
                    group = random.choice(KAC).getGroup(gid)
                    s = open(gid + 'lockname.txt',"w")
                    s.write(group.name)
                    s.close()
                    random.choice(KAC).sendText(msg.to, "Lockname has been active")

            elif "Create:" in msg.text:
                if msg.from_ in admin:
                   key = msg.text[7:]
		   klist = [ki,kk,kc,kl,cl]
                   tr = random.choice(klist)
                   try:
                       tr.findAndAddContactsByMid(key)
                       tr.createGroup("T.E.B LINE", [key])
                       tr.sendText(msg.to, "Done")
                       print "Success"
                   except:
                       tr.sendText(msg.to, "Eror")
                       print "Failed"
#            elif "join " in msg.text.lower():
#		rplace=msg.text.lower().replace("join ")
#		if rplace == "on":
#			wait["atjointicket"]=True
#		elif rplace == "off":
#			wait["atjointicket"]=False
#		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
 #           elif '/ti/g/' in msg.text.lower():
#		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
#		links = link_re.findall(msg.text)
#		n_links=[]
#		for l in links:
#			if l not in n_links:
#				n_links.append(l)
#		for ticket_id in n_links:
#			if wait["atjointicket"] == True:
#				group=cl.findGroupByTicket(ticket_id)
#				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
#				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))

	    elif "Copy " in msg.text:
		    targets = []
		    key = eval(msg.contentMetadata["MENTION"])
		    key["MENTIONEES"] [0] ["M"]
		    for x in key["MENTIONEES"]:
			targets.append(x["M"])
		    for target in targets:
		        try:
		            contact = cl.getContact(target)
		            x = contact.displayName
		            profile = cl.getProfile()
		            profile.displayName = x
		            cl.updateProfile(profile)
		            y = contact.statusMessage
		            cak = cl.getProfile()
		            cak.statusMessage = y
		            cl.updateProfile(cak)
		            p = contact.pictureStatus
		            cl.updateProfilePicture(p)
		            cl.sendText(msg.to, "succes")
		            		            
		        except Exception as e:
		            cl.sendText(msg.to,"gagal")
		            print e
	    elif "PP1copy " in msg.text:
		    targets = []
		    key = eval(msg.contentMetadata["MENTION"])
		    key["MENTIONEES"] [0] ["M"]
		    for x in key["MENTIONEES"]:
			targets.append(x["M"])
		    for target in targets:
		        try:
		            contact = ki.getContact(target)
		            p = contact.pictureStatus
		            ki.updateProfilePicture(p)
		            ki.sendText(msg.to, "succes")
		            		            
		        except Exception as e:
		            ki.sendText(msg.to,"gagal")
		            print e
	    elif "PP2copy " in msg.text:
		    targets = []
		    key = eval(msg.contentMetadata["MENTION"])
		    key["MENTIONEES"] [0] ["M"]
		    for x in key["MENTIONEES"]:
			targets.append(x["M"])
		    for target in targets:
		        try:
		            contact = kk.getContact(target)
		            p = contact.pictureStatus
		            kk.updateProfilePicture(p)
		            kk.sendText(msg.to, "succes")
		            		            
		        except Exception as e:
		            kk.sendText(msg.to,"gagal")
		            print e
	    elif "PP3copy " in msg.text:
		    targets = []
		    key = eval(msg.contentMetadata["MENTION"])
		    key["MENTIONEES"] [0] ["M"]
		    for x in key["MENTIONEES"]:
			targets.append(x["M"])
		    for target in targets:
		        try:
		            contact = kc.getContact(target)
		            p = contact.pictureStatus
		            kc.updateProfilePicture(p)
		            kc.sendText(msg.to, "succes")
		            		            
		        except Exception as e:
		            kc.sendText(msg.to,"gagal")
		            print e
	    elif "PPcopyall " in msg.text:
		    targets = []
		    key = eval(msg.contentMetadata["MENTION"])
		    key["MENTIONEES"] [0] ["M"]
		    for x in key["MENTIONEES"]:
			targets.append(x["M"])
		    for target in targets:
		        try:
		            contact = ki.getContact(target)
		            p = contact.pictureStatus
		            ki.updateProfilePicture(p)
		            contact1 = kk.getContact(target)
		            q = contact1.pictureStatus
		            kk.updateProfilePicture(q)
		            contact2 = kc.getContact(target)
		            r = contact2.pictureStatus
		            kc.updateProfilePicture(r)		            		            
		            kc.sendText(msg.to, "succes")
		            		            
		        except Exception as e:
		            kc.sendText(msg.to,"gagal")
		            print e		            		            
            elif msg.text in ["Protect on"]:
                if wait["autokik"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autokik"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Protect off"]:
                if wait["autokik"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autokik"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Pqr on"]:
                if wait["protectqr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protectqr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Pqr off"]:
                if wait["protectqr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protectqr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Pcancel on"]:
                if wait["cancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["cancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Pcancel off"]:
                if wait["cancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["cancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set"]:
                md = ""
                if wait["contact"] == True: md+="😈 Contact : on\n"
                else: md+="☺ Contact : off\n"
                if wait["autoJoin"] == True: md+="😈 Auto join : on\n"
                else: md +="☺ Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="😈 Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "☺ Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="😈 Auto leave : on\n"
                else: md+="☺ Auto leave : off\n"
                if wait["timeline"] == True: md+="😈 Share : on\n"
                else:md+="☺ Share : off\n"
                if wait["autoAdd"] == True: md+="😈 Auto add : on\n"
                else:md+="☺ Auto add : off\n"
                if wait["commentOn"] == True: md+="😈 Comment : on\n"
                else:md+="☺ Comment : off\n"
                if wait["backup"] == True: md+="😈 Backup : on\n"
                else:md+="☺ Backup : off\n"
		if wait["cancel"] == True: md+="😈 Protect Cancel : on\n"
                else:md+="☺ Protect Cancel : off\n"
                if wait["autokik"] == True: md+="😈 protect : on\n"
                else:md+="☺ protect : off\n"
                if wait["protectqr"] == True: md+="😈 Protect QR : on\n"
                else:md+="☺ Protect QR : off\n"
                if wait["wlcmsg"] == True: md+="😈 Welcome message : on\n"
                else:md+="☺ Welcome message : off\n"
#               if wait["maling"] == True: md+="😈 Protec Maling : on\n"
#               else:md+="☺ Protect Maling : off\n"
                cl.sendText(msg.to,md)
            elif msg.text in ["Backup on"]:
                if wait["backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["Backup off"]:
                if wait["backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Spam message: " in msg.text:
                wait["spam"] = msg.text.replace("Spam message: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Spam Change to:" + wait["spam"])
                else:
                    cl.sendText(msg.to,"doneã€‚")
	    elif "spam add1: " in msg.text:
		wait["spam1"] = msg.text.replace("Spam add1: ","")
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Spam Change to:" + wait["spam1"])
                else:
                    ki.sendText(msg.to,"doneã€‚")
	    elif "Welcome text: " in msg.text:
		wait["wlctxt"] = msg.text.replace("Welcome text: ","")
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Welcome message Change to:" + wait["spam1"])
                else:
                    ki.sendText(msg.to,"doneã€‚")                    
	    elif "Spam add2: " in msg.text:
		wait["spam2"] = msg.text.replace("Spam add2: ","")
                if wait["lang"] == "JP":
                    kk.sendText(msg.to,"Spam Change to:" + wait["spam2"])
                else:
                    kk.sendText(msg.to,"doneã€‚")
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Fx comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Fx comment:off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Send link"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Cknkgy"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

	    elif msg.text in ["Check"]:
                    cl.sendText(msg.to, "I have set a read point ♪\n「Read」I will show you who I have read ♪")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait2
	    elif msg.text in ["Read"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "Yang Baca %s\nthat's it\n\nCek sider dibuat pada:\n[%s]"  % (wait2['readMember'][msg.to],setTime[msg.to]))
#			cl.sendText(msg.to, "Yang Baca %s\nthat's it\n\nCek sider dibuat pada:\n[%s]"  % (wait2['readMember'],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「Check」you can send ♪ read point will be created ♪")


#-----------------------------------------------
#            elif msg.text in ["Kick on", "kick on", "Mayhem", "mayhem", "Kick all", "kick all", "Kickall", "Fuck", "Cleanse", "cleanse"]:
#	     if msg.from_ not in Bots:
 #               random.choice(KAC).kickoutFromGroup(op.param1,[msg.from_])
  #          elif "Mayhem" in msg.text:
#	     if msg.from_ not in Bots:
 #               l = msg.text.replace("Mayhem","")
  #              if wait["lang"] == "JP":
   #                 random.choice(KAC).kickoutFromGroup(op.param1,[msg.from_])
    #            else:
     #               random.choice(KAC).kickoutFromGroup(op.param1,[msg.from_])
            elif msg.text in ["List friend"]:
	     if msg.from_ in Bots:
	      try:
                if accesed == []:
			print "nothing"

                try:
                    ma = ""
                    for mi_d in accesed:
                        ma += "->" +cl.getContact(mi_d).displayName + "\n"
                    kk.sendText(msg.to,"-ϔFriend: \n" + ma)
		except Exception as a:
			print a
	      except Exception as e:
		print e
            elif "Friend add @" in msg.text:
		if msg.from_ in Bots:
                    print "[Friend]ok"
                    _name = msg.text.replace("Friend add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
		    print _name
		    print _nametarget
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
				accesed.append(target)
				cl.sendText(msg.to, "added to list")
                            except:
                                ki.sendText(msg.to,"Error")
            elif "Unfriend @" in msg.text:
		if msg.from_ in Bots:
                    print "[Unfriend]ok"
                    _name = msg.text.replace("Unfriend @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kc.sendText(msg.to,"Not found Coy")
                    else:
                        for target in targets:
                            try:
				accesed.remove(target)
				cl.sendText(msg.to,"succes unfriend")
                            except:
                                kc.sendText(msg.to,"Gagal pekok")
#-----------------------------------------------

            elif msg.text in ["Asst join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text in ["Asst 1 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Asst 2 in"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Asst 3 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
#-----------------------------------------------
	    elif "Shake " in msg.text:
		    targets = []
		    key = eval(msg.contentMetadata["MENTION"])
		    key["MENTIONEES"] [0] ["M"]
		    for x in key["MENTIONEES"]:
			targets.append(x["M"])
		    for target in targets:
                                try:
                                    klist=[ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    kicker.inviteIntoGroup(msg.to,[target])
                                    print (msg.to,[x["M"]])
                                except:
				    cl.sendText(msg.to,"error")
	    elif "poto" in msg.text:
		  try:
		    cl.sendImageWithURL(msg.to,"http://s1.picswalls.com/wallpapers/2015/09/20/wallpaper-2015_111528356_269.jpg")
		  except Exception as error:
		    print error
	    elif "potoh" in msg.text:
		  try:
		    cl.sendImage(msg.to,"/home/juan_pradana/Downloads/cat_girl_nekomimi_art_anime_girl_103991_1920x1080.jpg")
		  except Exception as error:
		    print error
            elif "Staff add @" in msg.text:
		if msg.from_ in admin:
                    print "[Staff]ok"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
		    print _name
		    print _nametarget
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
				staff.append(target)
				cl.sendText(msg.to, "added to list")
                            except:
                                ki.sendText(msg.to,"Error")
            elif "Unstaff @" in msg.text:
		if msg.from_ in admin:
                    print "[Unstaff]ok"
                    _name = msg.text.replace("Unstaff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kc.sendText(msg.to,"Not found Coy")
                    else:
                        for target in targets:
                            try:
				staff.remove(target)
				cl.sendText(msg.to,"succes unstaff")
                            except:
                                kk.sendText(msg.to,"Gagal pekok")
            elif msg.text in ["Asst bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye me"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
			kk.leaveGroup(msg.to)
			kc.leaveGroup(msg.to)
			cl.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Asst 1 bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Asst 2 bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Asst 3 bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Fx kill"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kc.sendText(msg.to,"Dasar munafik")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif msg.text in ["StartX"]:
                        cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
			kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        cl.getGroup(msg.to)
                        print "kicker ok"
            elif msg.text in ["Asst clean","JancokX"]:
		if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("JancokX","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"Crashing")
                    kk.sendText(msg.to,"Sorry dude")
                    kc.sendText(msg.to,"Love You All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                        kc.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
			  if not target in controlall:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
	    elif "Gigit " in msg.text:
		    targets = []
		    key = eval(msg.contentMetadata["MENTION"])
		    key["MENTIONEES"] [0] ["M"]
		    for x in key["MENTIONEES"]:
			targets.append(x["M"])
		    for target in targets:
                                try:
                                    klist=[ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[x["M"]])
                                except:
				    cl.sendText(msg.to,"error")
            elif "Kick " in msg.text:
                       nk0 = msg.text.replace("Kick ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kk.sendText(msg.to,"gagal")

            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki.sendText(msg.to,"Succes Fx")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
		    gs = cl.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes add to black list")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
		    gs = cl.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes delete to black list")
                            except:
                                ki.sendText(msg.to,"Succes")
#-----------------------------------------------
            elif msg.text in ["Fx respon","respon","AsstRespon"]:
                ki.sendText(msg.to," 1" + ki.getProfile().displayName)
                kk.sendText(msg.to," 2" + kk.getProfile().displayName)
                kc.sendText(msg.to," 3" + kc.getProfile().displayName)
#-----------------------------------------------
            elif msg.text in ["Speed","Respontime","Sp"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text in ["Fx1 speed","Fx1 respontime"]:
                start = time.time()
                ki.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text in ["Fx2 speed","Fx2 respontime"]:
                start = time.time()
                kk.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                kk.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text in ["Fx3 speed","Fx3 respontime"]:
                start = time.time()
                kc.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                kc.sendText(msg.to, "%sseconds" % (elapsed_time))

            elif msg.text in ["All Fx speed","All Fx respontime"]:
                start = time.time()
                ki.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
		start = time.time()
                kk.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                kk.sendText(msg.to, "%sseconds" % (elapsed_time))
		start = time.time()
                kc.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
		kc.sendText(msg.to, "%sseconds" % (elapsed_time))
		start = time.time()
#------------------------------------------------------------------
	    elif msg.text == "Gcreator join":
	      if msg.from_ in admin:
	       if msg.toType == 2:
		    ginfo = wuk.getGroup(msg.to)
		    print "gid" + msg.to
		    try:
			gcreatmid = ginfo.creator.mid
		    except:
			gcreatmid = "Error"
		    try:
                    	wuk.inviteIntoGroup(msg.to,[gcreatmid])
			wuk.sendText(msg.to,"succes masukin Creator Group" + str(ginfo.name))
		    except:
			wuk.sendText(msg.to,"gagal")
	       else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': creator}
                wuk.sendMessage(msg)
		wuk.sendText(msg.to, "Jika ada masalah pada bot harap hubungi Creator")
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to add blaclist")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to delete blacklist")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist munafik!")
	    elif "Spam:" in msg.text:
                    strnum = msg.text.replace("Spam:","")
		    num = int(strnum)
                    for var in range(0,num):
        		cl.sendText(msg.to, wait["spam"])
	    elif "Fx1 spam:" in msg.text:
                    strnum = msg.text.replace("Fx1 spam:","")
		    num = int(strnum)
                    for var in range(0,num):
                        cl.sendText(msg.to, wait["spam1"])
	    elif "Fx4 spam:" in msg.text:
                    strnum = msg.text.replace("Fx4 spam:","")
		    num = int(strnum)
                    for var in range(0,num):
                        kk.sendText(msg.to, wait["spam2"])
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
	    elif msg.text in ["Tagall"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(5)
                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                      strt = strt + int(6)
                      akh = akh + 1
                      cb2 += "@nrik\n"
                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
            if msg.text in ["Tag all"]:
                           group = cl.getGroup(msg.to)
                           nama = [contact.mid for contact in group.members]
                           nm1, nm2, nm3, nm4, nm5, nm6, jml = [], [], [], [], [], [], len(nama)
                           if jml <= 100:
                               mention(msg.to, nama)
                           if jml > 100 and jml < 600:
                               for i in range(0, 99):
                                   nm1 += [nama[i]]
                               mention(msg.to, nm1)
                               for j in range(100, len(nama)-1):
                                   nm2 += [nama[j]]
                               mention(msg.to, nm2)
                               for k in range(200, len(nama)-1):
                                   nm3 += [nama[k]]
                               mention(msg.to, nm3)
                               for l in range(300, len(nama)-1):
                                   nm4 += [nama[l]]
                               mention(msg.to, nm4)
                               for m in range(400, len(nama)-1):
                                   nm5 += [nama[m]]
                               mention(msg.to, nm5)
                               for n in range(500, len(nama)-1):
                                   nm6 += [nama[n]]
                               mention(msg.to, nm6)
                           if jml > 600:
                               print "Waduh 600 member"                       
        if op.type == 59:
            print op


    except Exception as error:
        print error
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
  while True:
    for zx in range(0,20):
	hasil = cl.activity(limit=20)
	if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
	    try:
		cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
		cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["wmark"] + wait["pesanlike"])
		ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
		ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["wmark"] + wait["pesanlike"])
		kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
		kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["wmark"] + wait["pesanlike"])
		kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
		kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["wmark"] + wait["pesanlike"])
		print "Like"
		
	    except:
		pass
	else:
	    print "Already liked"
    time.sleep(180)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
