from idautils import *
from idaapi import *
from idc import *

class BBCounter(idaapi.plugin_t):
	flags = idaapi.PLUGIN_UNL
	comment = "Count the number of basic blocks in this binary file."

	wanted_name = "BBCounter"
	wanted_hotkey = "Alt-F6"
	help = "help"

	def init(self):
		idaapi.msg("init BBCounter.\n")
		idaapi.require("bbcounter")
		idaapi.require("bbcounter.bbcounterImpl")
		return idaapi.PLUGIN_OK

	def run(self, arg):
		bbcounter.bbcounterImpl.main()

	def term(self):
		idaapi.msg("term function\n")

def PLUGIN_ENTRY():
	return BBCounter()