"""
Rotate dicom image
"""

import SimpleITK as sitk
import imutils
import os
import sys
import numpy as np
import cv2

__author__ = "Dibya Raj Ghosh"

try:
    def RotateImage(inputDirectory,outputDiretory,degOfRotation):
    """
    Input-Dicom image
    Output-Dicom image
    It will rotate image by a specific angle provided by user
    This function will accept 3 mandatory parameter- source folder, destination folder, 
    rotation-angle(positive  value means -anticlowise and negative value means clockwise rotation)
    """
    dcmList=os.listdir(inputDirectory)
    for imgName in dcmList:
        path=inputDirectory+'\\'+imgName
        dcm = sitk.ReadImage(path)
        array = sitk.GetArrayFromImage(dcm)
        imgarray = array[0] #sitk reads image as volume adding z-dimension
        rotate = imutils.rotate(imgarray,int(degOfRotation))
        filtered_image = sitk.GetImageFromArray(rotate)
        for key in dcm.GetMetaDataKeys():
            filtered_image.SetMetaData(key, dcm.GetMetaData(key))

        filtered_image.SetSpacing(dcm.GetSpacing())
        writer = sitk.ImageFileWriter()
        writer.KeepOriginalImageUIDOn()
        #writer
        writer.SetFileName(outputDiretory+'//'+imgName)
        writer.Execute(filtered_image)
        print(imgName+' saved successfully')
except Exception as e:
    print('Error occured during execution-'+e)


