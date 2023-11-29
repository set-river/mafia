#import time

#for i in range(24):
    #for j in range(60):
        #for k in range(60):
            #print("Время: "+ str(i)+":"+str(j)+':'+str(k))
            #time.sleep(1)
#g = 2
#s = input(f"")
#for i in range(len(s)):
#    print(f"{i} - {s[-i-1]}")
name = input()
last_name = input()
correct_name = 'Иван'
correct_last_name = 'Иванов'
if name.title() == correct_name and last_name.title() == correct_last_name:
    print(f'Привет {name.title()} {last_name.title()}')
