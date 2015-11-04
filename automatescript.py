

import openpyxl   #Import OpenPyxl module
wb = openpyxl.load_workbook('LOC54.xlsx')   
sheet = wb.get_sheet_by_name('Report')
listpo = []
listps = []
listqty = []
i = 3
while(1==1):
    i = i + 1
    
    cellvalueqad = sheet['W'+str(i)].value
    cellvaluevss = sheet['A'+str(i)].value
    if(sheet['R'+str(i)].value == None):
        break
    if(cellvalueqad !=cellvaluevss):
        if(cellvaluevss != None):
            print cellvaluevss
            print "Packing Slip: " + sheet['E'+str(i)].value
            print "Quantity :"+str(sheet['F'+str(i)].value)
            print "\n"
            listpo.append(str(cellvaluevss))
            listps.append(str(sheet['E'+str(i)].value))
            listqty.append(str(sheet['F'+str(i)].value))
    if listpo:
        for j in range(0,len(listpo)):
           
            if listpo[j]==str(cellvalueqad) and listqty[j]==str(sheet['AB'+str(i)].value):   #and listps[j]==str(sheet['AA'+str(i)].value)
                print listpo[j] + ' found in QAD with Packing Slip :' +  str(sheet['AA'+str(i)].value) + ' and Qty :' +str(sheet['AB'+str(i)].value)+'\n'
                listpo.remove(listpo[j])
                listps.remove(listps[j])
                listqty.remove(listqty[j])          
                break




for j in range(0,len(listpo)):
    print 'PO ' +listpo[j]+' with Packing Slip: '+listps[j]+' and qty: '+listqty[j]+' not found in qad' + '\n'

             
nb = openpyxl.load_workbook('recon.xlsx')




def removedupli(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

povssdata = []
poqaddata = []
ponum = ''
pops = ''
poqty = 0
if listpo:
    listpo1 = removedupli(listpo)
    for value in listpo1:
        i = 3
        while(1==1):
            
            i = i + 1
            cellvalueqad = str(sheet['W'+str(i)].value)
            cellvaluevss = str(sheet['A'+str(i)].value)
            
            if(sheet['R'+str(i)].value == None):
                break
            if cellvaluevss==value:
                
                pops = str(sheet['E'+str(i)].value)
                poqty = sheet['F'+str(i)].value
                povssdata.append([value,[pops,poqty]])
                pops = str(sheet['AA'+str(i)].value)
                poqty = sheet['AB'+str(i)].value
                poqaddata.append([value,[pops,poqty]])
            elif cellvalueqad==value:
                
                pops = str(sheet['E'+str(i)].value)
                poqty = sheet['F'+str(i)].value
                povssdata.append([value,[pops,poqty]])
                pops = str(sheet['AA'+str(i)].value)
                poqty = sheet['AB'+str(i)].value
                poqaddata.append([value,[pops,poqty]])


        


nb.create_sheet(index=0, title='LOC54')
sheetnew = nb.get_sheet_by_name('LOC54')

sheetnew['A1'] = 'PO Missing in QAD'
sheetnew['A1'].font = openpyxl.styles.Font(size=12,bold=True)

for i in range(0,len(povssdata)):
    sheetnew['A'+str(i+2)] = povssdata[i][0]
    

sheetnew['B1'] = 'Qty missing in QAD'
sheetnew['B1'].font = openpyxl.styles.Font(size=12,bold=True)

for i in range(0,len(povssdata)):
    if(poqaddata[i][1][1] == None):
        sheetnew['B'+str(i+2)] = povssdata[i][1][1]
    else:
        sheetnew['B'+str(i+2)] = povssdata[i][1][1]-poqaddata[i][1][1]
    
sheetnew['C1'] = 'Packaging Slip Number in VSS'
sheetnew['C1'].font = openpyxl.styles.Font(size=12,bold=True)

for i in range(0,len(povssdata)):
    sheetnew['C'+str(i+2)] = povssdata[i][1][0]
    
sheetnew['D1'] = 'QTY In vSS'
sheetnew['D1'].font = openpyxl.styles.Font(size=12,bold=True)

for i in range(0,len(povssdata)):
    sheetnew['D'+str(i+2)] = povssdata[i][1][1]
    
sheetnew['E1'] = 'Packaging Slip Number in QAD'
sheetnew['E1'].font = openpyxl.styles.Font(size=12,bold=True)

for i in range(0,len(poqaddata)):
    sheetnew['E'+str(i+2)] = poqaddata[i][1][0]

sheetnew['F1'] = 'QTY in QAD'
sheetnew['F1'].font = openpyxl.styles.Font(size=12,bold=True)

for i in range(0,len(poqaddata)):
    sheetnew['F'+str(i+2)] = poqaddata[i][1][1]
    
sheetnew['G1'] = 'Total in VSS'
sheetnew['G1'].font = openpyxl.styles.Font(size=12,bold=True)
sheetnew['H1'] = 'Total in QAD'
sheetnew['H1'].font = openpyxl.styles.Font(size=12,bold=True)

nb.save('recon.xlsx')
