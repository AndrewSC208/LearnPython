<radio 
  label="NS1"
  averages="cols"
  shuffle="rows"
  values="order">
  <title>Please use a scale from 1 to 10, where 1 means “not important at all” and 10 means “extremely important”.<br /><br />It is very important to me that the store(s) I visit when shopping for apparel, footwear, accessories and personal care/cosmetics...</title>
  <col label="c1" value="1">Not important at all 1</col>
  <col label="c2" value="2">2</col>
  <col label="c3" value="3">3</col>
  <col label="c4" value="4">4</col>
  <col label="c5" value="5">5</col>
  <col label="c6" value="6">6</col>
  <col label="c7" value="7">7</col>
  <col label="c8" value="8">8</col>
  <col label="c9" value="9">9</col>
  <col label="c10" value="10">Extremely Important 10</col>
  <row label="r1">Is a store that offers the latest trends</row>
  <row label="r2">Has a wide range of brands from mainstream to high-end designer names</row>
  <row label="r3">Has staff that doesn’t bother me while I shop</row>
  <row label="r4">Has helpful customer service</row>
  <row label="r5">Is a one-stop-shop where I can find everything I need at the same time</row>
  <row label="r6">Has a website that is easy to shop</row>
  <row label="r7">Has a compelling loyalty/rewards program</row>
  <row label="r8">Has frequent sales and promotions</row>
</radio>

<suspend/>

<radio 
  label="NS2"
  shuffle="rows">
  <title>The following statements describe how some people think about fashion and shopping in general. Please indicate how much you agree or disagree with each statement.</title>
  <col label="c1">Totally Agree 1</col>
  <col label="c2">Somewhat Agree 2</col>
  <col label="c3">Neither Agree nor Disagree 3</col>
  <col label="c4">Somewhat Disagree 4</col>
  <col label="c5">Totally Disagree 5</col>
  <row label="r1">I'm too busy to shop for clothes</row>
  <row label="r2">I want my shopping experience to be simple and quick</row>
  <row label="r3">It’s important for me to stand out from others</row>
  <row label="r4">If money was not an issue, I would only buy designer brands/brand names</row>
  <row label="r5">When shopping, I have a fixed budget and I need to stretch my dollars as much as possible</row>
  <row label="r6">I am willing to pay more for high quality</row>
  <row label="r7">I would shop at off-price stores more frequently if the staff was more helpful</row>
  <row label="r8">I hate to shop for clothes online</row>
</radio>

<suspend/>

<exec>
def mean(data):
    #Return the sample arithmetic mean of data.
    n = len(data)
    if n lt 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/float(len(data))

def sumOfSquareDev(data):
  #Return sum of square deviations of sequence data.
  c = mean(data)
  ss = sum((x-c)**2 for x in data)
  return ss

def stDev(data):
  #Calculates the population standard deviation.
  n = len(data)-1
  if n lt 2:
      raise ValueError('variance requires at least two data points')
  ss = sumOfSquareDev(data)
  pvar = ss/n 
  return pvar**0.5

#get the values from dat file:
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

		#create segment: [coefficent+constant]
		for s in range(len(algObj)):
			algorithmObj[s+1] = algObj[s][1:]

		print algorithmObj

	except IOError:
		algorithmObj = {}
	return algorithmObj

def algorithmCalculation(resp_answers, segment_coeff):
	return sum(i*j for i,j in zip(resp_answers, segment_coeff)) + segment_coeff[-1]

def algorithmRaw(answers, algorithmObj):
	computation = [ algorithmCalculation(answers, algorithmObj[c+1]) for c in range(1, algorithmObj['segments'] + 1)]

def algorithmCompute(answers, algorithmObj):
    computation = [ algorithmCalculation(answers, algorithmObj[c+1]) for c in range(1, algorithmObj['segments'] + 1) ]
    maxValue = max(computation)
    return computation.index(maxValue) + 1

myalg = algorithmSetup("segmentInfo.dat")


#segment coefficients:
# seg_1 =[0.101322,0,-1.715052,-0.060401,-1.280058,0.062572,-0.956105,-0.837508,-0.521245,0,0.563135,1.275031,-0.272093,0.882339,0.201215,-1.291542]
# seg_2 =[-0.077569,0,0.535774,-0.258613,-1.980569,-0.091129,-0.395697,-0.047093,-1.363170,0,-0.081016,0.502602,-1.184038,0.742198,-0.561030,-2.271814]
# seg_3 =[0.151921,0,1.451859,-0.050437,1.828808,0.312052,0.397386,1.001373,-1.068578,0,-0.760888,-0.361353,-0.355747,-0.186869,-1.141889,-2.619294]
# seg_4 =[0.168792,0,0.572238,1.116282,0.040748,1.140649,1.533182,2.554301,-1.152071,0,-1.138939,-1.234744,1.241290,-0.334972,-1.258608,-2.089153]
# seg_5 =[-0.450624,0,-0.708117,1.051890,-0.846211,0.968055,-0.710499,-0.300018,-1.514951,0,-1.611399,-2.320401,-0.264664,-0.195070,-1.098839,-2.358533]
# seg_6 =[-0.319655,0,0.324693,0.434167,-0.066608,-0.581512,-0.141763,0.838836,-0.851161,0,-0.774811,-0.390540,-0.137593,-0.416060,-0.484545,2.377288]
# seg_7 =[0.177830,0,-0.776093,-0.160299,-1.468344,0.236141,-0.358500,0.174766,-1.146714,0,0.126262,0.850051,0.858151,0.593090,-0.133689,-2.228763]



# #segment constant:
# seg_1_const = -4.708427
# seg_2_const = -5.582999
# seg_3_const = -4.391359
# seg_4_const = -5.839225
# seg_5_const = -5.049548
# seg_6_const = -4.246064
# seg_7_const = -5.034017

#original question values:
q1_org = [NS1.r1.val + 1, NS1.r2.val + 1, NS1.r3.val + 1, NS1.r4.val + 1, NS1.r5.val + 1, NS1.r6.val + 1, NS1.r7.val + 1, NS1.r8.val + 1]
q2_org = [NS2.r1.val + 1, NS2.r2.val + 1, NS2.r3.val + 1, NS2.r4.val + 1, NS2.r5.val + 1, NS2.r6.val + 1, NS2.r7.val + 1, NS2.r8.val + 1]


# rescale the question values:
q1_maped = [ row.map(c1=1, c2=1, c3=2, c4=2, c5=3, c6=3, c7=4, c8=6, c9=8, c10=10) for row in NS1.rows]
q2_maped = [ row.map(c1=7, c2=5, c3=3, c4=2, c5=1) for row in NS2.rows]


#rz_score_1 = []
#rz_score_2 = []

# for i in range(len(q1_maped)):
#   me = mean(q1_maped)
#   x = q1_maped[i] - me
#   if stDev(q1_maped)==0:
#     y = 0
#   else:
#     y = x/float(stDev(q1_maped))
#   rz_score_1.append(y)
  
# for i in range(len(q2_maped)):
#   me = mean(q2_maped)
#   x = q2_maped[i] - me
#   if stDev(q2_org)==0:
#     y = 0
#   else: 
#     y = x/float(stDev(q2_maped))
#   rz_score_2.append(y)

# rz_score_1 = rzCalc(q1_maped)
# rz_score_2 = rzCalc(q2_maped)

#concat rz_scores array:
#rz_scores = rz_score_1 + rz_score_2

def rzCalc(i):
	for z in range(len(i))
		me = mean(i)
		x = i[z] - me
		if stDev(i)==0:
			y = 0
		else:
			y = x / float(stDev(i))
		q.append(y)
	return q



rz_scores = rzCalc(q1_maped) + rzCalc(q2_maped)

#cal each segment:
alg_raw_1 = [ sum(i*j for i,j in zip(rz_scores, seg_1)) + seg_1_const ]
alg_raw_2 = [ sum(i*j for i,j in zip(rz_scores, seg_2)) + seg_2_const ]
alg_raw_3 = [ sum(i*j for i,j in zip(rz_scores, seg_3)) + seg_3_const ]
alg_raw_4 = [ sum(i*j for i,j in zip(rz_scores, seg_4)) + seg_4_const ]
alg_raw_5 = [ sum(i*j for i,j in zip(rz_scores, seg_5)) + seg_5_const ]
alg_raw_6 = [ sum(i*j for i,j in zip(rz_scores, seg_6)) + seg_6_const ]
alg_raw_7 = [ sum(i*j for i,j in zip(rz_scores, seg_7)) + seg_7_const ]

# combine arrays:
algRawArray = alg_raw_1 + alg_raw_2 + alg_raw_3 + alg_raw_4 + alg_raw_5 + alg_raw_6 + alg_raw_7

#the punch
bla = (algRawArray.index(max(algRawArray)))

if sum(algRawArray) == 0:
  QALG_SEG.val = 8
else:
  QALG_SEG.val = bla

# print out the raw values:
for i in range(len(algRawArray)):
  QALG_RAW.rows[i].val = str(algRawArray[i])
</exec>

<text 
  label="QALG_RAW"
  optional="0"
  size="150"
  where="execute,survey,report">
  <title>Raw Segment Value: **HIDDEN**</title>
  <row label="r1">One</row>
  <row label="r2">Two</row>
  <row label="r3">Three</row>
  <row label="r4">Four</row>
  <row label="r5">Five</row>
  <row label="r6">Six</row>
  <row label="r7">Seven</row>
</text>

<radio 
  label="QALG_SEG"
  where="execute,survey,report">
  <title>Segment Value: **HIDDEN**</title>
  <row label="r1">Segment-1 High Touch Enthusiasts</row>
  <row label="r2">Segment-2 Self-Directed Enthusiasts</row>
  <row label="r3">Segment-3 Time Starved</row>
  <row label="r4">Segment-4 Budget Constrained Sale Stalkers</row>
  <row label="r5">Segment-5 Mainstream Basics</row>
  <row label="r6">Segment-6 Disengaged</row>
  <row label="r7">Segment-7 Fashion and Quality at a Pricde</row>
  <row label="r8">Low Standard Deviation</row>
</radio>

# #q_vals = [S5.r1.val, S5.r2.val, S5.r3.val, S5.r4.val, S5.r5.val, S5.r6.val, S5.r7.val, S5.r8.val, S5.r9.val, S5.r10.val, S5.r11.val, S5.r12.val, S6.r1.val, S6.r2.val, S6.r3.val, S6.r4.val, S6.r5.val, S6.r6.val, S6.r7.val, S6.r8.val, S6.r9.val, S6.r10.val, S6.r11.val, S7.r1.val, S7.r2.val, S7.r3.val]
# q_vals = [S5.r1.val+1,  S5.r2.val+1,  S5.r3.val+1,  S5.r4.val+1,  S5.r5.val+1,  S5.r6.val+1,  S5.r7.val+1,  S5.r8.val+1,  S5.r9.val+1,  S5.r10.val+1,  S5.r11.val+1,  S5.r12.val+1,  S6.r1.val+1,  S6.r2.val+1,  S6.r3.val+1,  S6.r4.val+1,  S6.r5.val+1,  S6.r6.val+1,  S6.r7.val+1,  S6.r8.val+1,  S6.r9.val+1,  S6.r10.val+1,  S6.r11.val+1,  S7.r1.val+1,  S7.r2.val+1,  S7.r3.val+1]
# #q_vals = [2, 3, 5, 6, 7, 3, 1, 3, 4, 5, 2, 1, 6, 6, 3, 4, 5, 6, 2, 2, 3, 5, 6, 7, 7, 3]

# # need the batt vals: 
# q_vals_batt_1 = q_vals[0:12]
# q_vals_batt_2 = q_vals[12:23]

# def sumOfSquareDev(data):
#   #Return sum of square deviations of sequence data.
#   c = mean(data)
#   ss = sum((x-c)**2 for x in data)
#   return ss

# def stDev(data):
#   #Calculates the population standard deviation.
#   n = len(data)-1
#   if n lt 2:
#       raise ValueError('variance requires at least two data points')
#   ss = sumOfSquareDev(data)
#   pvar = ss/n 
#   return pvar**0.5

# def standardisedScores(data):
#   n = len(data)
#   x = mean(data)
#   if stDev(data) &gt; 0:
#     y = stDev(data)
#   else:
#     y = 1
#   stScore = [(data[i] - x)/y for i in range(len(data)-1)]
#   return stScore

# def concatArray(x, y):
#   return x + y

# # this is the last method:
# def algRawCalc(seg, seg_std, vals, b_vals_1, b_vals_2, const):
#   if sum(standardisedScores(b_vals_1)) == 0:
#     return 0
#   if sum(standardisedScores(b_vals_2)) == 0:
#     return 0
#   left_x = vals + standardisedScores(b_vals_1) + standardisedScores(b_vals_2)
#   right_x = concatArray(seg, seg_std)
#   return sum(i*j for i,j in zip(left_x, right_x)) + const

# alg_raw_1 = [algRawCalc(seg_1, seg_1_std, q_vals, q_vals_batt_1, q_vals_batt_2, seg_1_const)]
# alg_raw_2 = [algRawCalc(seg_2, seg_2_std, q_vals, q_vals_batt_1, q_vals_batt_2, seg_2_const)]
# alg_raw_3 = [algRawCalc(seg_3, seg_3_std, q_vals, q_vals_batt_1, q_vals_batt_2, seg_3_const)]
# alg_raw_4 = [algRawCalc(seg_4, seg_4_std, q_vals, q_vals_batt_1, q_vals_batt_2, seg_4_const)]
# alg_raw_5 = [algRawCalc(seg_5, seg_5_std, q_vals, q_vals_batt_1, q_vals_batt_2, seg_5_const)]
# alg_raw_6 = [algRawCalc(seg_6, seg_6_std, q_vals, q_vals_batt_1, q_vals_batt_2, seg_6_const)]

# #raw value:
# algRawArray = alg_raw_1 + alg_raw_2 + alg_raw_3 + alg_raw_4 + alg_raw_5 + alg_raw_6

# #the punch
# bla = (algRawArray.index(max(algRawArray)))

# if sum(algRawArray) == 0:
#   QALG_SEG.val = 6
# else:
#   QALG_SEG.val = bla  

# # print out the raw values:
# for i in range(len(algRawArray)):
#   QALG_RAW.rows[i].val = str(algRawArray[i])
# # </exec>

# <text 
#   label="QALG_RAW"
#   optional="0"
#   size="150"
#   where="execute,survey,report">
#   <title>Raw Segment Value: **HIDDEN**</title>
#   <row label="r1">One</row>
#   <row label="r2">Two</row>
#   <row label="r3">Three</row>
#   <row label="r4">Four</row>
#   <row label="r5">Five</row>
#   <row label="r6">Six</row>
# </text>

# <radio 
#   label="QALG_SEG"
#   where="execute,survey,report">
#   <title>Segment Value: **HIDDEN**</title>
#   <row label="r1">Primary Electrolux</row>
#   <row label="r2">Secondary Electrolux</row>
#   <row label="r3">Three</row>
#   <row label="r4">Four</row>
#   <row label="r5">Secondary Frigidaire</row>
#   <row label="r6">Primary Frigidaire</row>
#   <row label="r7">Low Standard Deviation</row>
# </radio>

# <suspend/>
