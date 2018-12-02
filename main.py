from random import *
import time

main1_1 = int(randint(1, 6))
main2_1 = int(randint(1, 6))
main3_1 = int(randint(1, 6))

mainmain1 = int(main1_1 + main2_1 + main3_1)

#----------------------------------------------

main1_2 = int(randint(1, 6))
main2_2 = int(randint(1, 6))
main3_2 = int(randint(1, 6))

mainmain2 = int(main1_2 + main2_2 + main3_2)

#----------------------------------------------

main1_3 = int(randint(1, 6))
main2_3 = int(randint(1, 6))
main3_3 = int(randint(1, 6))

mainmain3 = int(main1_3 + main2_3 + main3_3)

#----------------------------------------------

main1_4 = int(randint(1, 6))
main2_4 = int(randint(1, 6))
main3_4 = int(randint(1, 6))

mainmain4 = int(main1_4 + main2_4 + main3_4)

#----------------------------------------------

main1_5 = int(randint(1, 6))
main2_5 = int(randint(1, 6))
main3_5 = int(randint(1, 6))

mainmain5 = int(main1_5 + main2_5 + main3_5)

#----------------------------------------------

main1_6 = int(randint(1, 6))
main2_6 = int(randint(1, 6))
main3_6 = int(randint(1, 6))

mainmain6 = int(main1_6 + main2_6 + main3_6)

#----------------------------------------------


mainmains = mainmain1, mainmain2, mainmain3, mainmain4, mainmain5, mainmain6
print(mainmains)
f = open("dndCharFile.txt", "w")
f.write(str(mainmains))

time.sleep(3)