#! /home/python35/bin/python
"""
-------------------------------------------------
   File Name：     versionChange
   Description :   Python3版本号变更
   Author :       lvchenggang
   date：          2018/8/14
-------------------------------------------------
   Change Activity:
                   2018/8/14
-------------------------------------------------
"""
__author__ = 'lvchenggang'

baseDir = None  # 文件搜索根路径
groupId = None  # pom.xml中匹配的groupId值
artifactPattern = None  # pom.xml中匹配的artifactId模式
propertyTag = None  # pom.xml中properties标签内匹配的变量
oriVersionCheck = True  # 是否交验原先的版本号

import re
from xml.etree import ElementTree as ET

class CommentedTreeBuilder(ET.TreeBuilder):
  '''
  保留xml文件中的注释
  '''

  def __init__(self, *args, **kwargs):
    super(CommentedTreeBuilder, self).__init__(*args, **kwargs)

  def comment(self, data):
    self.start(ET.Comment, {})
    self.data(data)
    self.end(ET.Comment)


from abc import ABCMeta, abstractmethod


class PomVersion(object):
  __metaclass__ = ABCMeta

  ns = "http://maven.apache.org/POM/4.0.0"
  ET.register_namespace('', ns)
  tree = ET.ElementTree()

  def __init__(self, pomFile, groupId, artifactPattern, propertyTag, oriVersion, destVersion):
    self.pomFile = pomFile
    self.groupId = groupId
    self.artifactPattern = artifactPattern
    self.propertyTag = propertyTag
    self.oriVersion = oriVersion
    self.destVersion = destVersion
    self.found = False
    xmlParser = ET.XMLParser(target=CommentedTreeBuilder())
    PomVersion.tree.parse(pomFile, parser=xmlParser)

  def handler(self):
    self.internalHandler()
    if self.found:
      print("{%s}匹配{%s}" % (self.pomFile, self.__class__.__name__))

  @abstractmethod
  def internalHandler(self):
    pass


class RootPomVersion(PomVersion):
  '''
  根标签内版本号修改
  '''

  def __init__(self, pomFile, groupId, artifactPattern, propertyTag, oriVersion, destVersion):
    super().__init__(pomFile, groupId, artifactPattern, None, oriVersion, destVersion)

  def internalHandler(self):
    root = PomVersion.tree.getroot()
    groupId = root.find("{%s}groupId" % PomVersion.ns)
    artifactId = root.find("{%s}artifactId" % PomVersion.ns)
    version = root.find("{%s}version" % PomVersion.ns)

    if groupId is not None and self.groupId == groupId.text and \
        artifactId is not None and re.match(self.artifactPattern, artifactId.text) and \
        version is not None:
      versionMatch = True
      if oriVersionCheck:
        versionMatch = self.oriVersion == version.text

      if versionMatch:
        version.text = self.destVersion
        PomVersion.tree.write(self.pomFile, encoding='UTF-8', xml_declaration=True)
        self.found = True
    return self.found


class ParentPomVersion(PomVersion):
  '''
  parent标签内版本号修改
  '''

  def __init__(self, pomFile, groupId, artifactPattern, propertyTag, oriVersion, destVersion):
    super().__init__(pomFile, groupId, artifactPattern, None, oriVersion, destVersion)

  def internalHandler(self):
    root = PomVersion.tree.getroot()
    for parent in root.iter("{%s}parent" % PomVersion.ns):
      groupId = parent.find("{%s}groupId" % PomVersion.ns)
      artifactId = parent.find("{%s}artifactId" % PomVersion.ns)
      version = parent.find("{%s}version" % PomVersion.ns)

      if groupId is not None and self.groupId == groupId.text and \
          artifactId is not None and re.match(self.artifactPattern, artifactId.text) and \
          version is not None:
        versionMatch = True
        if oriVersionCheck:
          versionMatch = self.oriVersion == version.text

        if versionMatch:
          version.text = self.destVersion
          PomVersion.tree.write(self.pomFile, encoding='UTF-8', xml_declaration=True)
          self.found = True
    return self.found


class PropertiesPomVersion(PomVersion):
  '''
  properties标签内版本号修改
  '''

  def __init__(self, pomFile, groupId, artifactPattern, propertyTag, oriVersion, destVersion):
    super().__init__(pomFile, groupId, artifactPattern, propertyTag, oriVersion, destVersion)

  def internalHandler(self):
    root = PomVersion.tree.getroot()
    for property in root.iter("{%s}properties" % PomVersion.ns):
      tag = property.find("{%s}%s" % (PomVersion.ns, self.propertyTag))

      if tag is not None and self.oriVersion == tag.text:
        tag.text = self.destVersion
        PomVersion.tree.write(self.pomFile, encoding='UTF-8', xml_declaration=True)
        self.found = True
    return self.found

import os
import fnmatch
def findAllPoms(baseDir):
  '''
  递归查找baseDir目录下所有的pom.xml文件
  :param baseDir: 根目录
  :return: pom路径集合
  '''
  allPoms = []
  fileMap = {root: files for root, _, files in os.walk(baseDir) if 'pom.xml' in files}
  for root, files in fileMap.items():
    root = os.path.normpath(root) if root.endswith(os.sep) else os.path.normpath(root) + os.sep
    pomFiles = fnmatch.filter(files, 'pom.xml')
    for pomFile in pomFiles:
      allPoms.append(root + pomFile)
  if allPoms:
    allPoms.sort(key=lambda k: len(k))
  return allPoms

