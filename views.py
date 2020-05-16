from django.core.files.storage import FileSystemStorage
import http.client
from django.http import JsonResponse
from http.client import HTTPResponse
from django.shortcuts import *
from pymysql import *
from django.views.decorators.csrf import *
from datetime import *
from random import *
import smtplib

# C:\Users\Komal\AppData\Local\Programs\Python\Python35\python C:\packingkings\manage.py runserver

states = ["Punjab", "Delhi", "Haryana", "Uttar Pradesh", "Jammu and Kashmir", "Maharashtra", "Madhya Pradesh",
          "Karnataka", "Kerala", "Tamil Nadu", "West Bengal", "Andhra Pradesh", "Rajasthan", "Gujarat", "Assam",
          "Uttarakhand"]
cities = {"Punjab": ["Tarn-Taran", "Amritsar", "Ludhiana", "Jalandhar", "Bathinda", "Ferozpur", "Faridkot", "Ajnala",
                     "Gurdaspur", "Moga", "Attari", "Chandigarh", "Pathankot", "Abhor"],
          "Delhi": ["Agra", "Mehrauli", "Tughlaqabad", "Firozabad", "Shergarh", "Shajahnabad"],
          "Haryana": ["Gurugram", "Rohtak", "Sirsa", "Panchkula", "Panipat", "Karnal", "Ambala", "Sonepat",
                      "Yamuna Nagar"],
          "Uttar Pradesh": ["Kanpur", "Lucknow", "Varanasi", "Bareilly", "Ayodhya", "Jhansi", "Meerut", "Aligarh"],
          "Jammu and Kashmir": ["Leh", "Rajauri", "Doda", "Duru", "Akhnoor", "Kulgam", "Srinagar", "Anantnag", "Punch"]}


def addadmin(request):
    return render(request, "addadmin.html")


@csrf_exempt
def addadmin1(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    q = "select * from admins where email='" + request.POST["email"] + "'"
    cr = conn.cursor()
    cr.execute(q)
    result = cr.fetchone()
    if result:
        return HttpResponse("fail")
    else:
        s = "insert into admins values('" + request.POST["email"] + "','" + request.POST["password"] + "','" + \
            request.POST[
                "type"] + "','" + request.POST["mobile"] + "')"
        cr.execute(s)
        conn.commit()
        return HttpResponse("success")


def viewadmin(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from admins"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        query = "select type from admins where email='" + request.session["adminemail"] + "'"
        cr.execute(query)
        result1 = cr.fetchone()
        for row in result:
            d = {}
            d["email"] = row[0]
            d["password"] = row[1]
            d["type"] = row[2]
            d["mobile"] = row[3]
            x.append(d)
        return render(request, "viewadmin.html", {"ar": x, "type": result1[0]})
    else:
        return HttpResponseRedirect('adminlogin')


def editadmin(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from admins where email='" + request.GET["q"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        d = {"email": result[0], "type": result[2], "mobile": result[3]}
        # return render(request, "editadmin.html", {"ar"/: d})
        return JsonResponse(d, safe=False)
    else:
        return HttpResponseRedirect('adminlogin')


@csrf_exempt
def updateadmin(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "update admins set type='" + request.POST["type"] + "',mobile='" + \
            request.POST["mobile"] + "' where email='" + request.POST["email"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        return HttpResponse("success")
    else:
        return HttpResponseRedirect('adminlogin')


def removeadmin(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "delete from admins where email='" + request.GET["q"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        return HttpResponseRedirect("viewadmin")
    else:
        return HttpResponseRedirect('adminlogin')


def adminlogin(request):
    return render(request, "adminlogin.html")


@csrf_exempt
def adminlogin1(request):
    email = request.POST["email"]
    password = request.POST["password"]
    conn = connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from admins where email='" + email + "' and password='" + password + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    if result:
        request.session['adminemail'] = email
        return HttpResponse('success')
    else:
        return HttpResponse('fail')


@csrf_exempt
def admindashboard(request):
    return render(request, "admindashboard.html")


def home(request):
    if "adminemail" in request.session:
        return render(request, "admindashboard.html")
    else:
        return HttpResponseRedirect('adminlogin')


# @csrf_exempt
# def changepassword(request):
#     if "adminemail" in request.session:
#         return render(request, "changepassword.html")
#     else:
#           return HttpResponseRedirect('adminlogin')


@csrf_exempt
def adminchangepassword(request):
    if "adminemail" in request.session:
        oldpassword = request.POST["oldpassword"]
        newpassword = request.POST["newpassword"]
        confirmpassword = request.POST["confirmpassword"]
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from admins where email='" + request.session['adminemail'] + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        if oldpassword == result[1]:
            query = "update admins set password='" + newpassword + "' where email='" + request.session[
                'adminemail'] + "'"
            cr.execute(query)
            conn.commit()
            return HttpResponse("success")
        else:
            return HttpResponse("failed due to wrong old password")
    else:
        return HttpResponseRedirect("adminlogin")


@csrf_exempt
def adminforgetpassword(request):
    conn = connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from admins where mobile='" + request.POST["mobile"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    if result:
        password = result[1]
        conn = http.client.HTTPConnection("server1.vmm.education")
        conn.request('GET',
                     '/VMMCloudMessaging/AWS_SMS_Sender?username=anmolpreetkaur&password=05N8K83E&message=' + password + '&phone_numbers='
                     + str(request.POST["mobile"]))
        response = conn.getresponse()
        return HttpResponse('success')
        # print(response)
        # return HttpResponseRedirect("userlogin")
    else:
        return HttpResponse('fail')


def addnews(request):
    if "adminemail" in request.session:
        return render(request, "addnews.html")
    else:
        return HttpResponseRedirect('adminlogin')


@csrf_exempt
def addnews1(request):
    if "adminemail" in request.session:
        dateofnews = date.today()
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from news where title='" + request.POST["title"] + "' and description='" + request.POST[
            "description"] + "' and dateofnews='" + str(dateofnews) + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        if result:
            return HttpResponse("fail")
        else:
            q = "insert into news values(NULL,'" + request.POST["title"] + "','" + request.POST[
                "description"] + "','" + str(dateofnews) + "')"
            cr = conn.cursor()
            cr.execute(q)
            conn.commit()
            # return HttpResponseRedirect("viewnews")
            return HttpResponse("success")
    else:
        return HttpResponseRedirect('adminlogin')


def viewnews(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from news"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            d = {"newsid": row[0], "title": row[1], "description": row[2], "dateofnews": row[3]}
            x.append(d)
        return render(request, "viewnews.html", {"ar": x})
    else:
        return HttpResponseRedirect('adminlogin')


def deletenews(request):
    if "adminemail" in request.session:
        conn = connect("127.0.0.1", "root", "", "moversandpackers")
        s = "delete from news where newsid=" + request.GET["q"]
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        return HttpResponseRedirect("viewnews")
    else:
        return HttpResponseRedirect('adminlogin')


def addpackages(request):
    if "adminemail" in request.session:
        global states
        return render(request, "addpackages.html", {"states": states})
    else:
        return HttpResponseRedirect('adminlogin')


@csrf_exempt
def addpackages1(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        q = "select * from packages where packagename='" + request.POST["packagename"] + "'"
        cr = conn.cursor()
        cr.execute(q)
        result = cr.fetchone()
        print(result)
        if result:
            return HttpResponse('fail')
            # return render(request,"addpackages.html",{"message":""})
        else:
            s = "insert into packages values('" + request.POST["packagename"] + "','" + request.POST[
                "description"] + "','" + request.POST["state"] + "','" + request.POST["sourcecity"] + "','" + \
                request.POST["state1"] + "','" + request.POST["destinationcity"] + "'," + request.POST["price"] + ")"
            cr.execute(s)
            conn.commit()
            # return HttpResponseRedirect("viewpackages")
            return HttpResponse('success')
    else:
        return HttpResponseRedirect('adminlogin')


def viewpackages(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from packages"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            d = {"packagename": row[0], "description": row[1], "state": row[2], "sourcecity": row[3], "state1": row[4],
                 "destinationcity": row[5], "price": row[6]}
            x.append(d)
        return render(request, "viewpackages.html", {"ar": x})
    else:
        return HttpResponseRedirect('adminlogin')


def getlistofpackages(request):
    state = request.GET["state"]
    city = request.GET["city"]
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from packages where sourcecity='" + city + "' or destinationcity='" + city + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []
    for row in result:
        d = {"packagename": row[0], "description": row[1], "state": row[2], "sourcecity": row[3], "state1": row[4],
             "destinationcity": row[5], "price": row[6]}
        x.append(d)
    return JsonResponse(x, safe=False)


def editpackages(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from packages where packagename='" + request.GET["q"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        conn.commit()
        d = {"packagename": result[0], "description": result[1], "price": result[6]}
        # return render(request, "editpackages.html", {"ar": d})
        return JsonResponse(d, safe=False)
    else:
        return HttpResponseRedirect('adminlogin')


@csrf_exempt
def updatepackages(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "update packages set description='" + request.POST["description"] + "',price=" + request.POST[
            "price"] + " where packagename='" + request.POST["packagename"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        return HttpResponse("success")
    else:
        return HttpResponseRedirect('adminlogin')


def deletepackages(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "delete from packages where packagename='" + request.GET["q"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        return HttpResponseRedirect("viewpackages")
    else:
        return HttpResponseRedirect('adminlogin')


def servicingstations(request):
    global states
    if "adminemail" in request.session:
        return render(request, "servicingstations.html", {"states": states})
    else:
        return HttpResponseRedirect('adminlogin')


@csrf_exempt
def servicingstations1(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        print(request.POST["servicecityname"])
        print(request.POST["description"])
        print(request.POST["state"])
        q = "select * from servicingstations where service_city_name='" + request.POST["servicecityname"] + "'"
        cr = conn.cursor()
        cr.execute(q)
        result = cr.fetchone()
        print(result)
        if result:
            return HttpResponse("fail")
        else:
            s = "insert into servicingstations values('" + request.POST["servicecityname"] + "','" + request.POST[
                "description"] + "','" + request.POST["state"] + "')"
            cr = conn.cursor()
            cr.execute(s)
            conn.commit()
            return HttpResponse("success")
    # return HttpResponseRedirect("viewservicingstations")
    else:
        return HttpResponseRedirect('adminlogin')


# def showcity(request):
#     global cities
#     state = request.GET['state']
#     print(state)
#     listofcities = cities[state]
#     print(listofcities)
#     return JsonResponse(listofcities, safe=False)

def showcity(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select service_city_name from servicingstations where state='" + request.GET["state"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    listofcities = result
    conn.commit()
    print(listofcities)
    return JsonResponse(listofcities, safe=False)


def viewservicingstations(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from servicingstations"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        x = []
        for row in result:
            d = {"servicecityname": row[0], "description": row[1], "state": row[2]}
            x.append(d)
        return render(request, "viewservicingstations.html", {"ar": x})
    else:
        return HttpResponseRedirect('adminlogin')


def editservicestations(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from servicingstations where service_city_name='" + request.GET["q"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        conn.commit()
        d = {"servicecityname": result[0], "description": result[1], "state": result[2]}
        # return render(request, "editpackages.html", {"ar": d})
        return JsonResponse(d, safe=False)
    else:
        return HttpResponseRedirect('adminlogin')


@csrf_exempt
def updateservicestations(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "update servicingstations set description='" + request.POST["description"] + "' where service_city_name='" + \
            request.POST["servicecityname"] + "'"
        print(request.POST["servicecityname"])
        print(request.POST["description"])
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        return HttpResponse("success")
    else:
        return HttpResponseRedirect('adminlogin')


def deleteservicingstations(request):
    if "adminemail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "delete from servicingstations where service_city_name='" + request.GET["q"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        conn.commit()
        return HttpResponseRedirect("viewservicingstations")
    else:
        return HttpResponseRedirect('adminlogin')


def choosestate(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from servicingstations where state='" + request.GET["state"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []
    for row in result:
        d = {"servicecityname": row[0], "description": row[1], "state": row[2]}
        x.append(d)
    return JsonResponse(x, safe=False)


def usersignup(request):
    return render(request, "usersignup.html")


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def sendotp(request):
    mobile = request.GET["mobile"]
    print('test', mobile)
    n = random_with_N_digits(6)
    request.session["userotp"] = str(n)
    msg = "your otp is " + str(n)
    print(msg)
    msg = msg.replace(" ", "%20")
    conn = http.client.HTTPConnection("server1.vmm.education")
    conn.request('GET',
                 '/VMMCloudMessaging/AWS_SMS_Sender?username=anmolpreetkaur&password=05N8K83E&message=' + msg + '&phone_numbers=' + str(
                     mobile))
    response = conn.getresponse()
    print(response)
    return HttpResponse("success")


def verifyotp(request):
    actualotp = request.session['userotp']
    otp = request.GET['otp']
    if actualotp == otp:
        return HttpResponse("success")
    else:
        return HttpResponse("fail")


def usersignup1(request):
    mobile = request.GET['mobile']
    return render(request, "usersignup1.html", {"mobile": mobile})


@csrf_exempt
def usersignup2(request):
    import random
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    q = "select * from users where email='" + request.POST["email"] + "'and mobile=" + request.POST["mobile"]
    cr = conn.cursor()
    cr.execute(q)
    result = cr.fetchone()
    if result:
        return HttpResponse("fail")
    else:
        file = request.FILES["photo"]
        uploadname = "userphotos/" + str(random.randint(1, 100000)) + file.name
        s = "insert into users values('" + request.POST["email"] + "'," + request.POST["mobile"] + ",'" + request.POST[
            "password"] + "','" + request.POST["name"] + "','" + request.POST["address"] + "','" + uploadname + "')"
        fs = FileSystemStorage()
        fs.save(uploadname, file)
        cr.execute(s)
        conn.commit()
        # d = {"message": "User Added Successfully !!"}
        # return render(request, "usersignup1.html", {"ar": d})
        return HttpResponse("success")


def userlogin(request):
    return render(request, "userlogin.html")


@csrf_exempt
def userlogin1(request):
    email = request.POST["email"]
    password = request.POST["password"]
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from users where email='" + email + "'and password='" + password + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()

    if result:
        # request.session['mobile'] = request.POST["mobile"]
        # return render(request,"userdashboard.html",{"d":result[3]})
        request.session['useremail'] = email
        return HttpResponse("success")
    else:
        return HttpResponse("fail")


def userlogout(request):
    try:
        del request.session['useremail']
    except:
        pass
    return HttpResponseRedirect('/')


def logout(request):
    try:
        del request.session['adminemail']
    except:
        pass
    return HttpResponseRedirect('adminlogin')


@csrf_exempt
def forgetpassword(request):
    conn = connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from users where mobile=" + request.POST["mobile"]
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    if result:
        password = result[2]
        conn = http.client.HTTPConnection("server1.vmm.education")
        conn.request('GET',
                     '/VMMCloudMessaging/AWS_SMS_Sender?username=anmolpreetkaur&password=05N8K83E&message=' + password + '&phone_numbers='
                     + str(request.POST["mobile"]))
        response = conn.getresponse()
        return HttpResponse('success')
        # print(response)
        # return HttpResponseRedirect("userlogin")
    else:
        return HttpResponse('fail')
        # return render(request,"userlogin.html",{"message1":"Invalid Mobile Number"})


@csrf_exempt
def userchangepassword(request):
    if "useremail" in request.session:
        oldpassword = request.POST["oldpassword"]
        newpassword = request.POST["newpassword"]
        confirmpassword = request.POST["confirmpassword"]
        conn = Connect("127.0.0.1", "root", "system", "moversandpackers")
        s = "select * from users where email='" + request.session['useremail'] + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        if oldpassword == result[2]:
            query = "update users set password='" + newpassword + "' where email='" + request.session[
                'useremail'] + "'"
            cr.execute(query)
            conn.commit()
            return HttpResponse("success")
        else:
            return HttpResponse("failed due to wrong old password")
    else:
        return HttpResponseRedirect("login")


def booking(request):
    if "useremail" in request.session:
        conn = Connect("127.0.0.1", "root", "", "moversandpackers")
        s = "select * from users where email='" + request.session["useremail"] + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        d = {"name": result[3], "mobile": result[1]}
        return render(request, "booking.html", {"data": d})
    else:
        return HttpResponseRedirect("login")


@csrf_exempt
def userbooking1(request):
    dateofbooking = date.today()
    pickupstate = request.POST['pickupstate']
    pickupcity = request.POST['pickupcity']
    pickupaddress = request.POST['pickupaddress']
    droppingstate = request.POST['droppingstate']
    droppingcity = request.POST['droppingcity']
    droppingaddress = request.POST['droppingaddress']
    packagename = request.POST['packagename']
    dateofpickup = request.POST['dateofpickup']
    dateofdropping = request.POST['dateofdropping']
    price = request.POST['price']
    paymentmode = request.POST['paymentmode']
    paymentstatus = "success"
    dispatchstatus = "pending"
    emailstatus = "pending"

    status = "pending"
    if paymentmode == "Cash":
        price = 0.0
        paymentstatus = "pending"

    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from users where email='" + request.session["useremail"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    mobile = result[1]
    email = request.session["useremail"]
    bookername = result[3]
    q = "insert into booking values(NULL,'" + bookername + "','" + email + "','" + mobile + "','" + pickupstate + "','" + pickupcity + "','" + pickupaddress + "','" + droppingstate + "','" + droppingcity + "','" + droppingaddress + "','" + packagename + "','" + str(
        dateofbooking) + "','" + dateofpickup + "','" + dateofdropping + "','" + paymentmode + "','" + str(
        price) + "','" + paymentstatus + "','" + status + "','" + dispatchstatus + "','" + emailstatus + "')"
    print(q)
    cr.execute(q)
    bookingid = cr.lastrowid
    conn.commit()
    # id = cr.fetchone()[0]
    print(id)
    msg = "Your booking is successfully Done!!"
    print(msg)
    # msg = msg.replace(" ", "%20")
    # conn = http.client.HTTPConnection("server1.vmm.education")
    # conn.request('GET',
    #              '/VMMCloudMessaging/AWS_SMS_Sender?username=anmolpreetkaur&password=05N8K83E&message=' + msg + '&phone_numbers=' + str(
    #                  mobile))
    # response = conn.getresponse()
    # print(response)
    #
    # sender = 'python.vmm@gmail.com'
    # receiver = email
    # password = 'vmmpython'
    # try:
    #     smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    #     smtpserver.ehlo()
    #     smtpserver.starttls()
    #     smtpserver.ehlo()
    #     smtpserver.login(sender, password)
    #     body = msg
    #     subject = "Subject:confirm booking "
    #     msg = subject + body
    #     # msg='Subject:Demo <h1>This is a test e-mail message.</h1>'
    #     smtpserver.sendmail(sender, receiver, msg)
    #     print('Sent')
    #     smtpserver.close()
    # except smtplib.SMTPException:
    #     print("Not Sent")

    return JsonResponse({"bookingid": bookingid}, safe=False)


def index(request):
    # conn = Connect("127.0.0.1", "root", "system", "moversandpackers")
    # s = "select * from review ORDER BY rand() LIMIT 0,4"
    # cr = conn.cursor()
    # cr.execute(s)
    # result = cr.fetchall()
    # print(result)
    # x=[]
    # for row in result:
    #     d = {}
    #     d["rating"]=row[2]
    #     d["review"]=row[3]
    #     d["bookername"]=row[5]
    #     d["photo"]=row[6]
    #     x.append(d)
    # print(x)
    # return render(request, "index.html",{'x':x})
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from review ORDER BY rand() LIMIT 0,4"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    print(result)
    x = []
    for row in result:
        d = {}
        d["rating"] = row[2]
        d["review"] = row[3]
        d["bookername"] = row[5]
        d["photo"] = row[6]
        x.append(d)
    print(x)
    q = "select * from news"
    cr.execute(q)
    result1 = cr.fetchall()
    x1 = []
    for row in result1:
        d1 = {"description": row[2], "title": row[1]}
        x1.append(d1)
    lst = []
    lst.append(x)
    lst.append(x1)
    return render(request, "index.html", {'x': lst})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")


def searchpackages(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select packagename,description from packages where (sourcecity='" + request.GET[
        "pickupcity"] + "' and destinationcity='" + request.GET["droppingcity"] + "') or (sourcecity='" + request.GET[
            "droppingcity"] + "' and destinationcity='" + request.GET["pickupcity"] + "')"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    print(result)
    x = []
    for row in result:
        x.append(row[0])
    print(x)
    if result:
        return JsonResponse(x, safe=False)
    else:
        return HttpResponse('fail')
        # return render(request,"booking.html",{"msg":"NO Service Available for above Stations "})


def getdescription(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select description,price from packages where packagename='" + request.GET["packagename"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    print(result)

    x = []
    for row in result:
        d = {"description": row[0], "price": row[1]}
        x.append(d)
    if result:
        return JsonResponse(x, safe=False)
    # x =[]
    # for row in result:
    #     x.append(row[0])
    # print(x)
    # if result:
    #     return JsonResponse(x, safe=False)


def thankspage(request):
    bookingid = request.GET["bookingid"]
    amount = request.GET["amount"]
    status = request.GET["status"]
    return render(request, "thankspage.html", {"amount": amount, "bookingid": bookingid, "status": status})


def viewbookings(request):
    paymentstatus = request.GET["paymentstatus"]
    # if paymentstatus =='pending':
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from booking where paymentstatus='" + paymentstatus + "' and status!='rejected'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []
    for row in result:
        d = {"bookingid": row[0], "bookername": row[1], "email": row[2], "mobile": row[3], "status": row[17],
             "dispatchstatus": row[18], "emailstatus": row[19]}
        x.append(d)
    return render(request, "viewbookings.html", {"ar": x})


# elif paymentstatus =='success':
#     conn = Connect("127.0.0.1", "root", "system", "moversandpackers")
#     s = "select * from booking where paymentstatus='" + paymentstatus +"' and status='pending'"
#     cr = conn.cursor()
#     cr.execute(s)
#     result = cr.fetchall()
#     x = []
#     for row in result:
#         d = {"bookingid": row[0], "bookername": row[1], "email": row[2], "mobile": row[3]}
#         x.append(d)
#     return render(request, "viewbookings.html", {"ar": x})

def viewbookingdetails(request):
    bookingid = request.GET["q"]
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from booking where bookingid='" + str(bookingid) + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()

    d = {"bookingid": result[0], "pickupstate": result[4], "pickupcity": result[5], "pickupaddress": result[6],
         "droppingstate": result[7], "droppingcity": result[8], "droppingaddress": result[9],
         "packagename": result[10], "dateofbooking": result[11], "dateofpickup": result[12],
         "dateofdropping": result[13], "paymentmode": result[14], "amountreceived": result[15],
         "paymentstatus": result[16], "status": result[17]}

    return render(request, "viewbookingdetails.html", {"d": d})


# def updatestatus(request):
#     if request.GET["status"] == 'dispatched':
#         conn = Connect("127.0.0.1", "root", "system", "moversandpackers")
#         s = "update booking set status='dispatched' where bookingid='" + str(request.GET['bookingid']) + "'"
#         cr = conn.cursor()
#         cr.execute(s)
# 
#         q = "select * from booking where bookingid='"+str(request.GET["bookingid"])+"'"
#         cr = conn.cursor()
#         cr.execute(q)
#         result = cr.fetchone()
#         mobile = result[3]
#         msg = "Your dispatching have been successfully done!!"
#         conn = http.client.HTTPConnection("server1.vmm.education")
#         conn.request('GET',
#                      '/VMMCloudMessaging/AWS_SMS_Sender?username=anmolpreetkaur&password=05N8K83E&message=' + msg + '&phone_numbers=' + str(
#                          mobile))
#         response = conn.getresponse()
#         print(response)
# 
# 
#     elif request.GET["status"] == 'accepted':
#         conn = Connect("127.0.0.1", "root", "system", "moversandpackers")
#         # s = f"update booking set paymentstatus='success' where bookingid='" + str(request.GET['bookingid']) + "'"
#         s = "update booking set status='accepted' where bookingid='" + str(request.GET['bookingid']) + "'"
#         cr = conn.cursor()
#         cr.execute(s)
#         conn.commit()
# 
#     elif request.GET["status"] == 'rejected':
#         conn = Connect("127.0.0.1", "root", "system", "moversandpackers")
#         s = "update booking set status='rejected' where bookingid='" + str(request.GET['bookingid']) + "'"
#         cr = conn.cursor()
#         cr.execute(s)
#         conn.commit()
#     # else:
#     #
#     #     conn = Connect("127.0.0.1", "root", "system", "moversandpackers")
#     #     s = "update booking set status=" + request.GET["status"] + " where bookingid='" + str(
#     #         request.GET['bookingid']) + "'"
#     #     cr = conn.cursor()
#     #     cr.execute(s)
#     #     conn.commit()
#     return HttpResponseRedirect("admindashboard")

def acceptbooking(request):
    conn = connect("127.0.0.1", "root", "", "moversandpackers")
    cr = conn.cursor()
    bookingid = request.GET['bookingid']
    status = request.GET['status']
    query = "UPDATE booking SET status='" + status + "' where bookingid='" + str(bookingid) + "'"
    cr.execute(query)
    conn.commit()
    # query1 = "select * from billdetails where billid={billid} and status='pending'"
    # cr.execute(query1)
    # result = cr.fetchall()
    # print(result)
    # if not result:
    #     query2 = f"UPDATE bills set status='accepted' where billid={billid}"
    #     cr.execute(query2)
    #     conn.commit()
    return HttpResponseRedirect('admindashboard')


def rejectbooking(request):
    conn = connect("127.0.0.1", "root", "", "furlenco")
    cr = conn.cursor()
    bookingid = request.GET['bookingid']
    status = request.GET['status']
    query = "UPDATE booking SET status='" + status + "' where bookingid='" + str(bookingid) + "'"
    cr.execute(query)
    conn.commit()
    # query1 = f"select * from billdetails where billid={billid} and status='pending'"
    # cr.execute(query1)
    # result = cr.fetchall()
    # print(result)
    # if not result:
    #     query2 = f"UPDATE bills set status='rejected' where billid={billid}"
    #     cr.execute(query2)
    #     conn.commit()
    return HttpResponseRedirect('admindashboard')


def dispatch(request):
    conn = connect("127.0.0.1", "root", "", "moversandpackers")
    cr = conn.cursor()
    bookingid = request.GET['bookingid']
    mobile = request.GET['mobile']
    # paystatus = request.GET['paystatus']
    query1 = "select * from booking where bookingid='" + str(bookingid) + "' and paymentstatus='pending'"
    cr.execute(query1)
    result = cr.fetchall()
    print(result)
    query2 = "UPDATE booking set paymentstatus='success',dispatchstatus='success' where bookingid='" + str(
        bookingid) + "'"
    cr.execute(query2)
    conn.commit()
    msg = "Your Product has been dispatched on your bookingid:" + str(bookingid)
    msg = msg.replace(" ", "%20")
    conn = http.client.HTTPConnection("server1.vmm.education")
    conn.request('GET',
                 '/VMMCloudMessaging/AWS_SMS_Sender?username=anmolpreetkaur&password=05N8K83E&message=' + msg + '&phone_numbers=' + str(
                     mobile))

    response = conn.getresponse()
    # res = "SMS sent successfully"
    print(response)
    # return HttpResponseRedirect('viewbookingtoadminsuccess')

    return HttpResponseRedirect('admindashboard')


def userviewbookindetails(request):
    paymentstatus = request.GET["paymentstatus"]
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select * from booking where email='" + request.session['useremail'] + "' and paymentstatus='" + paymentstatus+"'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    if result:
        x = []
        for row in result:
            d = {"bookingid": row[0], "pickupstate": row[4], "pickupcity": row[5], "pickupaddress": row[6],
                 "droppingstate": row[7], "droppingcity": row[8], "droppingaddress": row[9],
                 "packagename": row[10], "dateofbooking": row[11], "dateofpickup": row[12],
                 "dateofdropping": row[13], "paymentmode": row[14], "amountpaid": row[15],
                 "paymentstatus": row[16], "status": row[17]}
            x.append(d)
            # print(x)
        return render(request, "userviewbookingdetails.html", {"d": x})
    else:
        msg = "You have no " + request.GET["paymentstatus"] + " Bookings Yet"
        return render(request, "userviewbookingdetails.html", {"d": msg})


def reviews(request):
    bookingid = request.GET["bookingid"]
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    # s = "select * from booking where bookingid='"+str(bookingid)+"'"
    s = "select * from booking where bookingid='" + str(bookingid) + "'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    bookername = result[1]
    sourcecity = result[5]
    destinationcity = result[8]
    return render(request, "reviews.html", {"bookingid": bookingid, "bookername": bookername, "sourcecity": sourcecity,
                                            "destinationcity": destinationcity})


@csrf_exempt
def addreviews(request):
    import random
    dateofsubmit = date.today()
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    bookingid = request.POST["bookingid"]
    bookername = request.POST["bookername"]
    rating = request.POST["rating"]
    review = request.POST["review"]
    file = request.FILES["photo"]
    uploadname = "userphotos/" + str(random.randint(1, 100000)) + file.name
    fs = FileSystemStorage()
    fs.save(uploadname, file)
    s = "insert into review values(NULL,'" + str(bookingid) + "','" + str(rating) + "','" + review + "','" + str(
        dateofsubmit) + "','" + bookername + "','" + uploadname + "')"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect('/')


def sendratingmsgandemail(request):
    bookingid = request.GET['bookingid']
    email = request.GET['email']
    mobile = request.GET['mobile']
    msg = "http://127.0.0.1:8000/reviews?bookingid=" + bookingid

    conn = http.client.HTTPConnection("server1.vmm.education")
    conn.request('GET',
                 '/VMMCloudMessaging/AWS_SMS_Sender?username=anmolpreetkaur&password=05N8K83E&message=' + msg + '&phone_numbers=' + str(
                     mobile))
    response = conn.getresponse()
    print(response)

    # sender = 'python.vmm@gmail.com'
    sender = 'python.vmm@gmail.com'
    receiver = email
    password = 'vmmpython'
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(sender, password)
        # body = msg
        subject = "Rating "
        from email.mime.text import MIMEText
        msg = MIMEText(msg)

        msg['Subject'] = subject
        # msg='Subject:Demo <h1>This is a test e-mail message.</h1>'
        smtpserver.sendmail(sender, receiver, msg.as_string())
        print('Sent')
        smtpserver.close()
    except smtplib.SMTPException:
        print("Not Sent")
    conn = connect("127.0.0.1", "root", "", "moversandpackers")
    cr = conn.cursor()
    bookingid = request.GET['bookingid']
    mobile = request.GET['mobile']
    # paystatus = request.GET['paystatus']
    query1 = "update booking  set emailstatus='success'  where bookingid='" + str(bookingid) + "'"
    cr.execute(query1)
    conn.commit()

    return HttpResponse("success")


@csrf_exempt
def updatetracking(request):
    dateofupdate = date.today()
    bookingid = request.POST["bookingid"]
    remarks = request.POST['remarks']
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    cr = conn.cursor()
    s = "select * from booking_track where bookingid='" + str(bookingid) + "'"
    cr.execute(s)
    result = cr.fetchone()
    if result:
        q = "update booking_track set remarks='" + remarks + "' and dateofupdate='" + str(
            dateofupdate) + "' where bookingid='" + str(bookingid) + "'"
        cr.execute(q)
    else:
        d = "insert into booking_track values(NULL,'" + str(bookingid) + "','" + remarks + "','" + str(
            dateofupdate) + "')"
        cr.execute(d)
        conn.commit()

    return HttpResponse("success")


@csrf_exempt
def trackbooking(request):
    bookingid = request.POST["bookingid"]
    print(bookingid)
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    cr = conn.cursor()
    s = "select * from booking_track where bookingid=" + str(bookingid)
    cr.execute(s)
    result = cr.fetchone()
    print(result)
    d = {}
    d["remarks"] = result[2]
    d["dateofupdate"] = result[3]
    return JsonResponse(d, safe=False)

    # mobile ="9592231891"
    # msg = "Track Request for Booking ID "+str(bookingid)
    # msg = msg.replace(" ","%20")
    # conn = http.client.HTTPConnection("server1.vmm.education")
    # conn.request('GET',
    #              "/VMMCloudMessaging/AWS_SMS_Sender?username=anmolpreetkaur&password=05N8K83E&message=" + msg + "&phone_numbers=9592231891")
    # response = conn.getresponse()
    # print(response)
    #
    # sender = 'python.vmm@gmail.com'
    # receiver = "hundal.anmol96@gmail.com"
    # password = 'vmmpython'
    # try:
    #     smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    #     smtpserver.ehlo()
    #     smtpserver.starttls()
    #     smtpserver.ehlo()
    #     smtpserver.login(sender, password)
    #     # body = msg
    #     subject = "Tracking Request "
    #     from email.mime.text import MIMEText
    #     msg = MIMEText(msg)
    #
    #     msg['Subject'] = subject
    #     # msg='Subject:Demo <h1>This is a test e-mail message.</h1>'
    #     smtpserver.sendmail(sender, receiver, msg.as_string())
    #     print('Sent')
    #     smtpserver.close()
    # except smtplib.SMTPException:
    #     print("Not Sent")
    #
    # return HttpResponseRedirect("/")


def searchforpackages(request):
    return render(request, "searchforpackages.html")


def searchforpackages1(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    s = "select packagename,description,price from packages where (sourcecity='" + request.GET[
        "pickupcity"] + "' and destinationcity='" + request.GET["droppingcity"] + "') or (sourcecity='" + request.GET[
            "droppingcity"] + "' and destinationcity='" + request.GET["pickupcity"] + "')"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    print(result)
    x = []
    d = {}
    for row in result:
        d = {"packagename": row[0], "description": row[1], "price": row[2]}
        x.append(d)
    print(x)
    if result:
        return JsonResponse(x, safe=False)
    else:
        return HttpResponse('fail')
        # return render(request,"booking.html",{"msg":"NO Service Available for above Stations "})


def viewschedulevisit(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    cr = conn.cursor()
    s = "select * from booking order by dateofpickup"
    cr.execute(s)
    result = cr.fetchall()
    x = []
    for row in result:
        d = {"bookingid": row[0], "bookername": row[1], "pickupstate": row[4], "pickupcity": row[5],
             "pickupaddress": row[6],
             "droppingstate": row[7], "droppingcity": row[8], "droppingaddress": row[9],
             "packagename": row[10], "dateofbooking": row[11], "dateofpickup": row[12],
             "dateofdropping": row[13]}
        x.append(d)
        print(x)
    return render(request, "viewschedulevisit.html", {"ar": x})


def fetchnews(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    cr = conn.cursor()
    s = "select * from news"
    cr.execute(s)
    result = cr.fetchall()
    for row in result:
        d = {"description": row[2]}


def findaveragerating(request):
    conn = Connect("127.0.0.1", "root", "", "moversandpackers")
    cr = conn.cursor()
    s = "select avg(rating) from review"
    cr.execute(s)
    rs = cr.fetchone()
    avg = rs[0]
    print(avg)
    return HttpResponse(str(avg))
