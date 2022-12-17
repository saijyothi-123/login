import json
def register():
    enter=input("enter login/signup:")
    d={}
    d1={}
    dic={}
    if enter=="signup":
        user_name=input("enter the user_name:")
        p=input("enter the password:")
        if len(p)>=6:
            if "0" in p or "1" in p or "2" in p or "3" in p or "4" in p or "5" in p or"6" in p or "7" in p or "8" in p or "9" in p:
                if "A" in p or "B" in p or "C" in p or "D" in p or "E" in p or "F" in p or"G" in p or "H" in p or "I" in p or "J" in p or "K" in p or "L" in p or "M" in p or "N" in p or "O" in p or "P" in p or "Q" in p or "R" in p or "S" in p or "T" in p or "U" in p or "V" in p or "W" in p or "X" in p or "Y" in p or "Z" in p:
                    if "a" in p or "b" in p or "c" in p or "d" in p or "e" in p or "f" in p or"g" in p or "h" in p or "i" in p or "j" in p or "k" in p or "l" in p or "m" in p or "n" in p or "o" in p or "p" in p or "q" in p or "r" in p or "s" in p or "t" in p or "u" in p or "v" in p or "w" in p or "x" in p or "y" in p or "z" in p:
                        if "@" in p or "#" in p or "$" in p or "&" in p or "*" in p :
                            conform_password=input("enter the conform password")
                            if p==conform_password:
                                print("both passwords are same")
                                des=input("enter the description:")
                                birth=int(input("enter the birth date"))
                                hobbies=input("enter the hobies")
                                gender=input('enter the gender')
                                d1["description"]=des
                                d1["date of birth"]=birth
                                d1["hobbies"]=hobbies
                                d1["gender"]=gender
                                d["username"]=user_name
                                d["password"]=p
                                d["profile"]=d1
                                dic["user"]=[d]
                                
                                print(dic)
                                file= open("signup.json","w")
                                json.dump(dic,file,indent=4)
                                file.close()
                                print("congrats",user_name,"signup successful")
        
                            else:
                                print("both passwords are not same")
                          
                        else:
                            print("password should contain special_char")
                    else:
                        print("password should contain lower_case")
                else:
                    print("password should contain upper_case")
            else:
                print("password should contain number")
        else:
                print("password should contain atleast 6 charecters")
    elif enter=="login":
        login_user_name=input("enter the user_name:")
        login_password=input("enter the password:")
        a=open("signup.json","r")
        f=json.load(a)
         
        if f["user"][0]["username"]==login_user_name:
            if f["user"][0]["password"]==login_password:
                print("congrats.......successfully login")
            else:
                print("password is wrong try again...")
        else:
            print("username is not matching.....")
                
register()             


