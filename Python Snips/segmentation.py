#Define algorithmSetup function:
def algorithmSetup(fname, fDelimiter="\t"):
	try:
		# open file that is saved in the dir:
		#f = open("%s/%s" % (gv.survey.path, fname))

		# below is for local testing only:
		f = open("%s" % (fname))

		# strip out "returns" and "new lines"
		# split off by fDelimiter for each line infile:
		algObj = [ line.strip("\r\n").split(fDelimiter) for line in f.readlines()]

		algorithmObj = {}

		# #number of Segments:
		algorithmObj['segments'] = len(algObj[0])
		# #number of values in each segment including segment number as first item and segment constant as final item
		algorithmObj['q_val'] = len(algObj)

		print algorithmObj

	except IOError:
		algorithmObj = {}
	return algorithmObj

# def algorithmCalculation(resp_answers, segment_coeff):
# 	return sum(i*j for i,j in zip(resp_answers, segment_coeff)) + segment_coeff[-1]

# def algorithmRaw(answers, algorithmObj):
# 	computation = [ algorithmCalculation(answers, algorithmObj[c+1]) for c in range(1, algorithmObj['segments'] + 1)]

# def algorithmCompute(answers, algorithmObj):
#     computation = [ algorithmCalculation(answers, algorithmObj[c+1]) for c in range(1, algorithmObj['segments'] + 1) ]
#     maxValue = max(computation)
#     return computation.index(maxValue) + 1

myalg = algorithmSetup("algorithm.dat")

# ==================================


# # # this is the other var:
# # #Respondent Answers Mapped
# p.resp_answers = [ row.map(c1=1, c2=2, c3=3, c4=4, c5=5) for row in QS5.rows ]
# print "Respondent Answers: %s" % p.resp_answers

# # #Populate the Raw Calculations
# for i,x in enumerate(algorithmRaw(p.resp_answers, myalg)):
#     QALG_RAW.rows[i].val = int(x)

# # #Populate the Segment Assigned
# QALG_SEG.val = algorithmCompute(p.resp_answers, myalg) - 1