passengers_transport={"car":{"no_of_passengers":"4" ,"AC_Type":["AC","NON_AC"]},
         "van":{"no_of_passengers":"4" ,"AC_Type":["AC","NON_AC"]},
         "three_wheeler":"3",
         }

heavy_transport={"truck":["7","12"],
             "lorry":["2500","3500"]}
             

print("Press \'a\' ,For Add the Passengers Transport Vechicle")
print("Press \'b\' ,For remove the Passengers Vechicle")
print("Press \'c\' ,For Add the Goods Transport Vechicle")
print("Press \'d\' ,For remove the Goods Vechicle")
print("Press \'e\' ,For hire the Vechicle")
print("Press \'f\' ,For see the available Vechicle")
print("Press \'end\' ,For Quite this Program")

while True:
  cab=input("Please Give Your Requirements: ")
  
  #add Passenger Vechicle
  if cab=="a":
     vechicle=input("Please Give the Vechicle: ")
     no=int(input("Please Enter No Passengers: "))
     actype=input("Please Enter Type of Ac: ")
     newtransport={"no_of_passengers":no,"AC_Type":actype}
     passengers_transport.update({vechicle:newtransport})
    

     print(passengers_transport)
     
  #remove Passenger Vechicle
  elif cab=="b":
       Vremove=input("Please remove: ")
       passengers_transport.pop(Vremove)
               
       print(passengers_transport)

  #add heavy Vechicle
  elif cab=="c":
       vechicle=input("Please Give the Vechicle: ")
       weight1=int(input("Please Enter Weight 1: "))
       weight2=int(input("Please Enter Weight 2: "))
       newtransport=[weight1,weight2]
       heavy_transport.update({vechicle:newtransport})
       print(heavy_transport)
       
  #remove heavy Vechicle
  elif cab=="d":
       Vremove=input("Please remove: ")
       heavy_transport.pop(Vremove)
       print(heavy_transport)
       
  #Hire Vechicle
  elif cab=="e":
       search=input("Hire Vechicle Name:")
       if search in passengers_transport.keys():
         print(passengers_transport[search])
         del passengers_transport[search]
         
       elif search in heavy_transport.keys():
         print(heavy_transport[search])
         del heavy_transport[search]

  #show Vechicle
  elif cab == "f":
       for show in passengers_transport.items():
          print(show)
       for show in heavy_transport.items():
          print(show)   

    
       
  #end the loop
  elif cab=="end":
      break

  else:
    print("Invalid Input.....")
        

