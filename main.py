ren_samples = 0

def chkpdf (num_inpt: int, list_inpt: list):
	prob = num_inpt
	pdf = list_inpt

	for index in range(len(pdf) + 1 ):
		if prob < sum (pdf[0:index]):
			return index-1

def mkpdf (inpt: list):
	pdf_samples = inpt
	midlist = [ 0 for i in range(max(pdf_samples)+1) ]
	for i in range(len(samples)):
		midlist[pdf_samples[i-1]] += 1
	normf = sum(midlist)
	print (midlist)
	outlist = [ item/normf for item in midlist  ]
	return outlist

testList = [0,1,0,1,1,1,2,2,2,4,5,6,2]

print(mkpdf(testList))

