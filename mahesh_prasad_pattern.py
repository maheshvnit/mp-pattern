import sys,csv,re

class MP_Pattern:

	dt 		= []
	
	def __init__(self):
		self.dt = []	

	def readCSV(self,file,de_limiter):
		try:
			self.dt = csv.reader(open(file),delimiter=de_limiter)
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			raise
		except ValueError:
			print "Could not convert data to an integer."
			raise
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise	
		
	def searchReplace(self):
		sdt=[]
		csvFile     = 'output.csv'
		wtr = csv.writer( open(csvFile,"wb") )
		try:
			for r in self.dt:				
				del r[2]
				#re.sub(\a?a\, , r[0])
				#re.sub(regex, replacement, r[1])
				wtr.writerow( r )
					
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			raise
		except ValueError:
			print "Could not convert data to an integer."
			raise
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise	
		return sdt
		
# end of MP_Pattern class

if __name__ == '__main__':

	csvFile = 'test_example.csv'
	
	mpPattern = MP_Pattern()
	
	mpPattern.readCSV(csvFile,',')
	
	mpPattern.searchReplace()

	
	
		
