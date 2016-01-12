
def findProtein(dna):
    dna = dna.lower()
    start = dna.find('atg')

    if (start == -1):
        return ""
    endTag = ["tag", "tga","taa"]
    for i in endTag:
        if i in dna:
            stop = dna.find(i, (start + 3))
            if ((stop - start) % 3 == 0 ):
                return dna[start:(stop+3)]
            else:
                return ""

def endCodon(protein):
    answer = findProtein(protein)
    if (answer != 0):
        return answer + "   " + answer[-3:]


print endCodon("ADDggghghhjAtgaaaxxxtaa")
print "***********"
print endCodon("ADDggghghhjAataaaa")
print "************"
print endCodon("ADDggghghhjAataaaa")
print "************"
print endCodon("ADDggghghhjAtgaaaxxxtgaaa")


print findProtein("AAATGCCCTAACTAGATTGAAACC")
#print "***********"
#print findProtein("ADDggghghhjAtgaaaxxxtaa")
#print "************"
#print findProtein("ADDggghghhjAataaaa")
#print "************"
#print findProtein("ADDggghghhjAtgaaaxxxtgaaa")
