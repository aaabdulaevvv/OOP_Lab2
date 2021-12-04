import xml.etree.ElementTree as eTree
import lxml.etree as ET
import xml.sax


class XML:
    fileName: str

    def __init__(self, fileName):
        self.fileName = fileName
        try:
            self.file = open(self.fileName, "r")
        except FileNotFoundError:
            print("File not found")


def search(fileName, ISearcher, filter):
    return (ISearcher.search(fileName, filter))


class ISearcher:
    def search(self, fileName, filter):
        pass


class SAX_Searcher(ISearcher):
    def search(self, fileName, filter):
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        Handler = teachersHandler(filter)
        parser.setContentHandler(Handler)
        parser.parse(fileName)
        return Handler.result


class DOM_Searcher(ISearcher):
    def search(self, fileName, filter):
        tree = eTree.parse(fileName)

        rootXML = tree.getroot()
        result = []
        for child in rootXML:
            teacher = teacher()
            is_Valid = True
            for key, value in child.attrib.items():
                if (key == 'Name'):
                    if ('Name' not in filter or filter['Name'] == value):
                        teacher.Name = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Faculty'):
                    if ('Faculty' not in filter or filter['Faculty'] == value):
                        teacher.Faculty = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Department'):
                    if ('Department' not in filter or filter['Department'] == value):
                        teacher.Department = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Material'):
                    if ('Material' not in filter or filter['Material'] == value):
                        teacher.Material = value
                    else:
                        is_Valid = False
                        break
                if (key == 'MaterialT'):
                    if ('MaterialT' not in filter or filter['MaterialT'] == value):
                        teacher.MaterialT = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Extent'):
                    if ('Extent' not in filter or (filter['Extent'][0].isnumeric() and filter['Extent'][1].isnumeric() and int(filter['Extent'][0]) <= int(value) and int(filter['Extent'][1]) >= int(value))):
                    #if ('Extent' not in filter or (filter['Extent'][0] <= value and filter['Extent'][1] >= value)):
                        teacher.Extent = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Date'):
                    if ('Date' not in filter or filter['Date'] == value):
                        teacher.Date = value
                    else:
                        is_Valid = False
                        break
            if (is_Valid):
                result.append(teacher)
        return result


class teacher:
    Name: str
    Faculty: str
    Department: str
    Material: str
    MaterialT: str
    Extent: str
    Date: str

    def __init__(self):
        self.Name = ''
        self.Faculty = ''
        self.Department = ''
        self.Material = ''
        self.MaterialT = ''
        self.Extent = ''
        self.Date = ''


class teachersHandler(xml.sax.ContentHandler):
    def __init__(self, filter):
        self.filter = filter
        self.result = []

    def startElement(self, tag, attributes):
        if tag == "teacher":
            teacher1 = teacher()
            if 'Name' not in self.filter or self.filter['Name'] == attributes["Name"]:
                teacher1.Name = attributes["Name"]
            else:
                return
            if ('Faculty' not in self.filter or self.filter['Faculty'] == attributes["Faculty"]):
                teacher1.Faculty = attributes["Faculty"]
            else:
                return

            if ('Department' not in self.filter or self.filter['Department'] == attributes["Department"]):
                teacher1.Department = attributes["Department"]
            else:
                return

            if ('Material' not in self.filter or self.filter['Material'] == attributes["Material"]):
                teacher1.Material = attributes["Material"]
            else:
                return
            if ('MaterialT' not in self.filter or self.filter['MaterialT'] == attributes["MaterialT"]):
                teacher1.MaterialT= attributes["MaterialT"]
            else:
                return
            if ('Extent' not in self.filter or (self.filter['Extent'][0].isnumeric() and self.filter['Extent'][1].isnumeric() and int(self.filter['Extent'][0]) <= int(attributes["Extent"]) and int(self.filter['Extent'][1]) >= int(attributes["Extent"]))):
                teacher1.Extent= attributes["Extent"]
            else:
                return
            if ('Date' not in self.filter or self.filter['Date'] == attributes["Date"]):
                teacher1.Date= attributes["Date"]
            else:
                return

            self.result.append(teacher1)



def transform():
    mydata = ET.parse('mydata.xml')
    teachers = ET.parse('teachers.xsl')
    transformation = ET.XSLT(teachers)
    newfile = transformation(mydata)
    newfile.write("output-toc.html", pretty_print=True)
