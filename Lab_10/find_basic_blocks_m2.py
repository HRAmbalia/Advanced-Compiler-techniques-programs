import re

address_code = ['i=m-1', 'j=n', 't1=4*n', 'v=a[t1]', 'i=i+1', 't2=4*i', 't3=a[t2]', 'if t3<v goto (5)',
                'j=j-1', 't4=4*j', 't5=a[t4]', 'if t5>v goto (9)', 'if i>=j goto (23)', 't6=4*i',
                'x=a[t6]', 't7=4*i', 't8=4*j', 't9=a[t8]', 'a[t7]=t9', 't10=4*j', 'a[10]=x', 'goto (5)',
                't11=4*i', 'x=a[t11]', 't12=4*i', 't13=4*n', 't14=a[t13]', 'a[t12]=t14', 't15=4*n', 'a[t15]=x']

def find_leaders(address_code):
    pattern = r'goto\s*\(\s*(\d+)\s*\)'
    leaders = [1]
    for i, stt in enumerate(address_code):
        if "goto" in stt:
            leaders.append(i+2)
            match = re.search(pattern, stt)
            extracted_text = match.group(1) if match else None
            extracted_text = extracted_text.replace('(', '').replace(')', '')
            leaders.append(int(extracted_text))

    leaders = sorted(set(leaders))
    return leaders

leaders = find_leaders(address_code)
for i, led in enumerate(leaders):
    print("Leader-" + str(i+1) + " : " + address_code[led-1])