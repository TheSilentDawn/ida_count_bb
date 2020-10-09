import idautils
import idaapi
import idc
from idc import GetFunctionName

def main():
	bbsum = 0
	for fva in idautils.Functions():
		function = idaapi.get_func(fva)
		flowchart = idaapi.FlowChart(function)
		print("Function %s starting at 0x%x consists of %d basic blocks\n" % (GetFunctionName(function.startEA), function.startEA, flowchart.size))
		bbsum += flowchart.size
	print("Total BB number is %d\n" % bbsum)		

if __name__ == '__main__':
    main()