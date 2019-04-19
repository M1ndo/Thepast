#!/usr/bin/env python
# date : 19/04/2019
# Created By ybenel

class past():
 def encodeSTR(self,text): # Convert string to binary
     if type(text) is str:
         return ' '.join(format(ord(i),'b').zfill(8) for i in text).replace(" ","")
     elif type(text) is list or type(text) is tuple:
        return [' '.join(formay(ord(i),'b').zfill(8) for i in x).replace(" ","") for x in text if type(x) is str]
     else :
          return "[!]Invalid Data[] !!!".format(type(text))

 def encodeINT(self,num): # Convert Number To Binary
        if type(num) is str:
            if num.isdigit():
                num = int(num)
                return "{0:b}".format(num)
            else:
                return "[!] Invalid Number !!!"
        elif type(num) is int:
            return "{0:b}".format(num)
        elif type(num) is list or type(num) is tuple:
            return ["{0:b}".format(int(x)) for x in num if type(x) is int or x.isdigit()]
        else:
            return "[!] Invalid Data {} !!!".format(type(num))
 def decodeINT(self,bnum): # Convert Binary Bits Number To Decimal
        if type(bnum) is str:
            if bnum.isdigit():
            	check = set(bnum)
            	if check =={'1','0'} or check =={'1'} or check =={'0'}:
            		dcode = int(bnum, 2)
            		return dcode
            	else:
            		return "[!] Invalid Binary bits Number !!!"
            else:
            	return "[!] Invalid Binary bits Number !!!"
        elif type(bnum) is int:
        	bnum = str(bnum)
        	check = set(bnum)
        	if check =={'1','0'} or check =={'1'} or check =={'0'}:
        		return int(bnum, 2)
        	else:
        		return "[!] Invalid Binary Bits Number !!!"
        elif type(bnum) is list or type(bnum) is tuple:
        	bnums = []
        	for bnm in bnum:
        		bnm = str(bnm)
        		if bnm.isdigit():
        			check = set(bnm)
        			if check =={'1','0'} or check =={'1'} or check =={'0'}:
        				bnums.append(bnm)
        	if len(bnums) >0:
        		return [int(x, 2) for x in bnums]
        	else:
        		return "[!] Invalid Binary Bits Number !!!"
        else:
            return "[!] Invalid Data {} !!!".format(type(bnum))
 def decodeSTR(self,bcode): # convert binary bits string to decimal
    	if type(bcode) is str:
    		if bcode.isdigit():
    			check = set(bcode)
    			if check =={'1','0'} or check =={'1'} or check =={'0'}:
    				result = ''.join(chr(int(bcode[i*8:i*8+8],2)) for i in range(len(bcode)//8))
    				if result =="":
    					return "[!] Invalid Binary Bits String[ {} ]".format(bcode)
    				else:
    					return result
    			else:
    				return "[!] Invalid Binary Bits String[ {} ]".format(bcode)
    		else:
    			return "[!] Invalid Binary Bits String[ {} ]".format(bcode)
    	elif type(bcode) is list or type(bcode) is tuple:
    		bcodes = []
    		for bc in bcode:
    			if str(bc).isdigit():
    				if type(bc) is str:
    					check = set(bc)
    					if check =={'1','0'} or check =={'1'} or check =={'0'}:
    						bcodes.append(bc)
    		if len(bcodes) > 0:
    			return [''.join(chr(int(bcode[i*8:i*8+8],2)) for i in range(len(bcode)//8)) for bcode in bcodes]
    		else:
    			return "[!] Invalid Binary Bits Strings"
    	else:
    		"[!] Invalid Data {} !!!".format(type(bcode))
 def encodeIP(self,IP): # Convert IPv4 To Binary
        if type(IP) is str:
            if IP.count(".") ==3:
                return ".".join(map(str,["{0:08b}".format(int(x)) for x in IP.split(".")]))
            else:
                return "[!] Invalid IPv4[{}]".format(IP)
        elif type(IP) is list or type(IP) is tuple:
            return [".".join(map(str,["{0:08b}".format(int(x)) for x in IP.split(".")])) for IP in IP if str(IP).count(".") == 3]
        else:
            return "[!] Invalid Data {} !!!".format(type(IP))
 def decodeIP(self,bIP): #Convert Binary Bits IP To Decimal
        if type(bIP) is str:
            if bIP.count(".") ==3:
                check = set(bIP)
                check.remove(".")
                if check =={'1','0'} or check =={'1'} or check =={'0'}:
                    return ".".join(map(str, [ int(x, 2) for x in bIP.split(".")]))
                else:
                    return "[!] Invalid IPv4 Binary Bits"
            else:
                return "[!] Invalid IPv4 Address"
        elif type(bIP) is list or type(bIP) is tuple:
            bIPS = []
            for ip in bIP:
            	if type(ip) is str:
            		if str(ip).count(".") ==3:
            			check = set(ip)
            			check.remove('.')
            			if check =={'1','0'} or check =={'1'} or check =={'0'}:
            				bIPS.append(ip)
            if len(bIPS) > 0:
                return [".".join(map(str, [ int(x, 2) for x in bIP.split(".")])) for bIP in bIPS]
            else:
                return "[!] Invalid IPv4 Binary Bits ips"
        else:
        	return "[!] Invalid Data {} !!!".format(type(bIP))

#Now We going to make it works!!!!!!
encodeSTR,decodeSTR = past().encodeSTR,past().decodeSTR
encodeINT,decodeINT = past().encodeINT,past().decodeINT
encodeIP,decodeIP = past().encodeIP,past().decodeIP
