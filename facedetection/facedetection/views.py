from django.shortcuts import render,HttpResponse
import cv2
from fd.models import registation,faceAtt

def main(request):

    regobj = registation.objects.all()
    faceAt = faceAtt.objects.all()
    mylist = []
    images = []
    for r in regobj:
        mylist.append(r.st_img)
        print(r.st_img)
    print(mylist)

    for cl in mylist:
        curimg = cv2.imread(f"{cl}")
        images.append(curimg)








    return HttpResponse(f'''
    {regobj[0].st_img.url}
    <img src="{regobj[0].st_img.url}">
    
    ''')




    # return render(request,"index.html")

def reg(request):

    if request.POST:
        name = request.POST['name']
        enrol =request.POST['enrol']
        img = request.FILES['img']
        print(name,enrol,img)

        savedata = registation(st_name=name,st_enrollment=enrol,st_img=img)
        savedata.save()
        print("save in database")

    return render(request,"reg.html")