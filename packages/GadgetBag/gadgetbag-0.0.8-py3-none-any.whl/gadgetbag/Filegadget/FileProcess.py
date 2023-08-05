#!/usr/bin/env python
# coding:utf-8

import os
import json
import shutil
import threading
import time


class FileProcessUtilityTool:
    fileLock = threading.Lock()

    @staticmethod
    def mkdir(path):
        """create a path by input parameters, if path already exist do nothing
        :param str path: want to create
        :return void : void
        """

        path = path.strip()
        path = path.rstrip("\\")
        FileProcessUtilityTool.fileLock.acquire()
        isExists = os.path.exists(path)
        isSuccess = True
        if not isExists:
            #print(path + ' create success')
            os.makedirs(path)
        else:
            #print(path + 'dir already existed')
            isSuccess = False
        FileProcessUtilityTool.fileLock.release()
        return isSuccess


    @staticmethod
    def readFullPathFile2Json(fileNameWithPath):
        """read file by specified path and filename,if strRelPath and strAbsPath specified at the same time strAbsPath will take effect

        :param str strFileName: which file need to be read
        :param str strRelPath: relative file path
        :param str strAbsPath: absolute file path
        :return jsonloads object: read file to a Python object.
        """
        with open(fileNameWithPath, 'r') as readToJson:
            data = json.load(readToJson)

        return data

    @staticmethod
    def readFile2Json(strFileName, strRelPath = None, strAbsPath = None):
        """read file by specified path and filename,if strRelPath and strAbsPath specified at the same time strAbsPath will take effect

        :param str strFileName: which file need to be read
        :param str strRelPath: relative file path
        :param str strAbsPath: absolute file path
        :return jsonloads object: read file to a Python object.
        """

        fileStorePath = FileProcessUtilityTool.createFullPath(strAbsPath, strRelPath)
        fileNameWithPath = fileStorePath + strFileName
        with open(fileNameWithPath, 'r') as readToJson:
            data = json.load(readToJson)

        return data

    @staticmethod
    def write2SpecifiedFile(data, strFileName, strRelPath = None, strAbsPath = None, coverOldData=False):
        """write data to file by specified file name and path, if strRelPath and strAbsPath specified at the same time strAbsPath will take effect

        :param JSONEncoder data: will write to file
        :param str strFileName: stored file name
        :param str strRelPath: relative file path
        :param str strAbsPath: absolute file path
        :return void: void
        """

        fileStorePath = FileProcessUtilityTool.createFullPath(strAbsPath, strRelPath)
        fileNameWithPath = os.path.join(fileStorePath, strFileName)

        if not coverOldData:
            if os.path.exists(fileNameWithPath):
                return

        FileProcessUtilityTool.mkdir(fileStorePath)

        FileProcessUtilityTool.fileLock.acquire()
        with open(fileNameWithPath, 'w') as writeToFile:
            writeToFile.write(data)
        FileProcessUtilityTool.fileLock.release()


    @staticmethod
    def createFullPath(strAbsPath, strRelPath):
        """create a path by specified path ,if strRelPath and strAbsPath specified at the same time strAbsPath will take effect

        :param str strRelPath: relative file path
        :param str strAbsPath: absolute file path
        :return void: void
        """
        if None != strAbsPath:
            fileStorePath = strAbsPath

        elif None != strRelPath:
            fileStorePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), strRelPath)

        return fileStorePath


    @staticmethod
    def append2SpecifiedFile(data, strFileName, strRelPath = None, strAbsPath = None):
        """append data to file by specified file name and path, if strRelPath and strAbsPath specified at the same time strAbsPath will take effect

        :param JSONEncoder data: will write to file
        :param str strFileName: stored file name
        :param str strRelPath: relative file path
        :param str strAbsPath: absolute file path
        :return void: void
        """
        fileStorePath = FileProcessUtilityTool.createFullPath(strAbsPath, strRelPath)

        FileProcessUtilityTool.mkdir(fileStorePath)

        fileNameWithPath = os.path.join(fileStorePath, strFileName)
        FileProcessUtilityTool.fileLock.acquire()
        with open(fileNameWithPath, 'a') as writeToFile:
            writeToFile.write(data)
        FileProcessUtilityTool.fileLock.release()


    @staticmethod
    def copyDir(src, dst):
        ''' copy whole content from src to dst

        :param str src: The directory that you want to copy
        :param str dst: The directory that you want to move files into
        :return None:
        '''
        if os.path.exists(dst):
            print("the dir already exist, please check if they are you want")
        elif not os.path.exists(src):
            print(f'{src} not exist')
        else:
            print(f'start to copy {src} to {dst}')
            shutil.copytree(src, dst)
            print('finished dir copy')


    @staticmethod
    def copySpecifiedDir2TimeSuffixDir(src):
        ''' copy 'src' directory to 'src' to 'src-Y-M-D'

        :param str src: The directory that you want to copy
        :return:
        '''
        timeSuffix = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        dst = f'{src}-{timeSuffix}'
        FileProcessUtilityTool.copyDir(src,dst)

    @staticmethod
    def delSpecifiedFile(srcWithFullPath):
        if os.path.exists(srcWithFullPath):
            os.remove(srcWithFullPath)

    @staticmethod
    def file_name(file_dir):
        """
        get all file with a full path that in specified file directory
        :param file_dir:
        :return:
        """
        filesList = []
        for root, dirs, files in os.walk(file_dir):
            # print(root)  # 当前目录路径
            # print(dirs)  # 当前路径下所有子目录
            # print(files)  # 当前路径下所有非目录子文件
            for fileName in files:
                filesList.append(os.path.join(root, fileName))

            for dir in dirs:
                filesList = filesList + FileProcessUtilityTool.file_name(os.path.join(root, dir))
        return filesList


if __name__ == "__main__":
    print("os.path.dirname(os.path.realpath(__file__))=%s" %  os.path.dirname(os.path.realpath(__file__)))




