import os
import zipfile
import shutil
import traceback
import cv2
import time
import micral

def zipdir(dirPath, zipPath):
    zip_ref = zipfile.ZipFile("../"+zipPath, 'w')
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            zip_ref.write(os.path.join(root, file))
    zip_ref.close()
    
def unzipdir(zipPath, dirPath):
    zip_ref = zipfile.ZipFile(zipPath, 'r')
    zip_ref.extractall(dirPath)
    zip_ref.close()

def replace(filePath, dictRemplace):
    with open(filePath, 'r') as file :
      filedata = file.read()
    
    for i, j in dictRemplace.items():
        filedata = filedata.replace(i, j)
    
    with open(filePath, 'w') as file:
      file.write(filedata)

def alter(outputName, dictRemplaceText, dictRemplaceImages):
    inputName = os.path.dirname(os.path.realpath(__file__)) + "/template"
    tmpDirName = outputName+"_tmp"
    unzipdir(inputName+".docx", tmpDirName)
    replace(tmpDirName+'/word/document.xml', dictRemplaceText)
    replace(tmpDirName+'/word/charts/chart1.xml', dictRemplaceText)
    replace(tmpDirName+'/word/charts/chart2.xml', dictRemplaceText)
    replace(tmpDirName+'/word/charts/chart3.xml', dictRemplaceText)
    
    for numExcel in ["1", "2", "3"]:
        try:
            tmpNameExcel = tmpDirName+"_excel"+numExcel
            unzipdir(tmpDirName+"/word/embeddings/Microsoft_Excel_Worksheet"+numExcel+".xlsx", tmpNameExcel)
            
            replace(tmpNameExcel+"/xl/worksheets/sheet1.xml", dictRemplaceText)
            
            oldDir = os.getcwd()
            os.chdir(tmpNameExcel)
            zipdir(".", tmpDirName+"/word/embeddings/Microsoft_Excel_Worksheet"+numExcel+".xlsx")
            os.chdir(oldDir)
            shutil.rmtree(tmpNameExcel, ignore_errors=True)
        except Exception as e:
            traceback.print_exc()
            print("Error when plotting graph : %s" % e.__doc__)

    for i, j in dictRemplaceImages.items():
        try:
            if isinstance(j, str):
                shutil.copyfile(os.path.dirname(os.path.realpath(__file__))+"/examples/"+j.replace(" ","_"), tmpDirName+"/word/media/"+i)
            else:
                cv2.imwrite(tmpDirName+"/word/media/"+i, j)
        except Exception as e:
            traceback.print_exc()
            print("Error when writing image : %s" % e.__doc__)
    
    os.chdir(tmpDirName)
    zipdir(".", outputName+".docx")
    os.chdir("..")
    shutil.rmtree(tmpDirName, ignore_errors=True)

def summaryImage(data):
    for nameImage,dictImage in data.items():
        dictRemplaceText = dict()
        dictRemplaceImages = dict()
        
        dictRemplaceText["__version__"] = micral.version()
        dictRemplaceText["__dranl__"] = time.strftime("%Y-%m-%d")
        dictRemplaceText["__tranl__"] = time.strftime("%H:%M:%S")
        dictRemplaceText["__pic_name__"] = nameImage
        
        im = cv2.imread(nameImage)
        dictRemplaceImages["image1.png"] = im
        dictRemplaceText["__width__"] = "%d" % im.shape[1]
        dictRemplaceText["__height__"] = "%d" % im.shape[0]
        
        if "grain" in dictImage:
            d = dictImage["grain"]
            if "ratio" in d:
                dictRemplaceText["__ratio__"] = "%.2f" % d["ratio"]
            if "coarse" in d:
                dictRemplaceText["__coarse__"] = "%.2f" % d["coarse"]
            if "coarse" in d:
                dictRemplaceText["__ultrafine__"] = "%.2f" % d["ultrafine"]
            if "overlay" in d:
                dictRemplaceImages["image2.png"] = d["overlay"]
        if "harmonicity" in dictImage:
            d = dictImage["harmonicity"]
            if "harmonicity" in d:
                dictRemplaceText["__harmo__"] = "%.2f" % d["harmonicity"]
            if "argmax" in d:
                dictRemplaceText["__max_freq__"] = "%.2f" % d["argmax"]
            if "process" in d and isinstance(d["process"],dict):
                if "spectrum1d" in d["process"]:
                    t = d["process"]["spectrum1d"]
                    for i in range(len(t)):
                        dictRemplaceText[str(30000000+i+1)] = "%.3f" % t[i]
                    if len(t)<=200:
                        for i in range(len(t), 201):
                            dictRemplaceText[str(30000000+i+1)] = "0"
                    dictRemplaceText["32000010"] = "%.4f" % max(t)
                if "left" in d["process"] and "right" in d["process"]:
                    dictRemplaceText["__bandwidth__"] = "%.2f" % (abs(d["process"]["right"]-d["process"]["left"]))
                    dictRemplaceText["32000001"] = "%.4f" % d["process"]["left"]
                    dictRemplaceText["32000002"] = "%.4f" % d["process"]["right"]
                if "limit" in d["process"]:
                    dictRemplaceText["31000001"] = "%.4f" % d["process"]["limit"]
        if "classify" in dictImage:
            d = dictImage["classify"]
            if "category" in d:
                dictRemplaceText["__category__"] = d["category"]
                dictRemplaceImages["image3.png"] = d["category"]+".jpg"
            if "prediction_histogram" in d:
                t = d["prediction_histogram"]
                for i in range(len(t)):
                    dictRemplaceText[str(10000000+i+1)] = "%.2f" % t[i]
                if "category_number" in d:
                    dictRemplaceText["__cat_accuracy__"] = "%.2f" % t[d["category_number"]]
        if "name" in dictImage:
            d = dictImage["name"]
            if "name" in d:
                dictRemplaceText["__name__"] = d["name"]
                dictRemplaceImages["image4.png"] = d["name"]+".jpg"
            if "prediction_histogram" in d:
                t = d["prediction_histogram"]
                for i in range(len(t)):
                    dictRemplaceText[str(20000000+i+1)] = "%.2f" % t[i]
                if "name_number" in d:
                    dictRemplaceText["__name_accuracy__"] = "%.2f" % t[d["name_number"]]
        alter(os.path.splitext(nameImage)[0]+"_summary", dictRemplaceText, dictRemplaceImages)