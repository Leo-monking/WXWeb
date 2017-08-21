# -*- coding: utf-8-*-
import sys
sys.path.append('utils')
from django.shortcuts import render
from django.http import HttpResponse
import receive
import reply
import hashlib

def index(request):
	requestMethod = request.method
	try:
		if requestMethod == 'GET':
			signature = request.GET.get('signature')
			timestamp = request.GET.get('timestamp')
			nonce = request.GET.get('nonce')
			echostr = request.GET.get('echostr')
			token = "monking" 
			list = [token, timestamp, nonce]
			list.sort()
			sha1 = hashlib.sha1()
			map(sha1.update, list)
			hashcode = sha1.hexdigest()
			print "Handle/GET func: hashcode, signature: ", hashcode, signature
			if hashcode == signature:
				return HttpResponse(echostr, content_type="text/plain")
			else:
				return HttpResponse("")
			
		if requestMethod == 'POST':
			webData = str(request.body)
			print "handle/view.py	webData===>>>",webData
     		recMsg = receive.parse_xml(webData)
   			toUser = recMsg.FromUserName
   			fromUser = recMsg.ToUserName
   			msgType = recMsg.MsgType
   			if msgType == 'text':
   				content = "Welcome to monking`s house!"
   				replyMsg = reply.TextMsg(toUser, fromUser, content)
   				return HttpResponse(replyMsg.send())
   			if msgType == 'image':
   				mediaId = recMsg.MediaId
   				replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
   				return HttpResponse(replyMsg.send())
			if msgType == "voice":
				content = u"Welcome to monking`s house!But,What are you nong sha le , ting budong !"
				replyMsg = reply.TextMsg(toUser, fromUser, content)
				return HttpResponse(replyMsg.send())
          	else:
              		return HttpResponse(reply.Msg().send())
	except Exception, Argment:
		print Argment 
		return HttpResponse(Argment)
