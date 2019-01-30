#!/usr/bin/python
#
# Filename:  
#
# Version: 1.0.0
#
# Author:  Emmanuel Ferran (FullMidnight) based off the work by Joe Gervais (TryCatchHCF)
#
# Summary:
#
#	Part of the DumpsterFire Toolset. See documentation at https://github.com/TryCatchHCF/DumpsterFire
#
#
# Description:
#
#
# Example:
#
#

import os, sys

from FireModules.fire_module_base_class import *

class nmap_database_probes( FireModule ):

	def __init__(self):
		self.commentsStr = "NetworkScans/nmap_database_probes"
		return

	def __init__(self, moofStr):
		self.moofStr = moofStr
		self.commentsStr = "NetworkScans/nmap_database_probes"
		return

	def Description( self ):
		self.Description = "Runs nmap, probing common database ports and services on all hosts of target network"
		return self.Description


        def Configure( self ):
		print ("Standard nmap targets accepted, e.g.  192.168.0.1  or  192.168.1-254 or comma-separated IP addresses")
		print ("")
                self.networkAddrStr = input( "Enter Target Network IP Address (W.X.Y.Z): " )
                return

        def GetParameters( self ):
                return( self.networkAddrStr )

        def SetParameters( self, parametersStr ):
                self.networkAddrStr = parametersStr
                return

        def ActivateLogging( self, logFlag ):
                print (self.commentsStr + ": Setting Logging flag!")
                print (logFlag)
                return

        def Ignite( self ):
                if ( self.networkAddrStr == "" ):
                        print ("## ", self.commentsStr, ": Error - Network address string is blank")
                        return
		else:
			self.commandStr = "nmap -Pn -n --open -sT -sV -p1433,1521,3306,27017,27018,27019,28017,5000,5001 " + self.networkAddrStr
			print (self.commentsStr + ": Scanning with " + self.commandStr)
			os.system( self.commandStr )

		return

