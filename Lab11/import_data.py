import csv
company_count = dict()
email_list = set()
# mo file = with open
with open('./Lab11/data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader :
        name = row[0]
        company = row[1]
        email = row[2]
        #email ko trung lap => them vao danh sach
        if email not in email_list:
            email_list.add(email)
#dem so luong nguoi trong cty
            if company not in company_count:
            #chua co cty trong danh sach
                company_count[company] = 1
            else:
                #da co ten trong cty =>cong don
                company_count[company] +=1
#output: danh sach cty: so luong nguoi (dict)
print(f"so luong dai bieu : {len(email_list)}")
for company, count in company_count.items():
    print(f"{company}: {count}")