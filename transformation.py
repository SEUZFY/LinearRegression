# this is for data transformation from 4258 to 28992.

from pyproj import Transformer


def writefile(filename, list1):
    with open(filename, 'w') as fh:
        for item in list1:
            fh.write('{}{}'.format(item, '\n'))


def readfile(filename):
    list1 = []
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        for line in lines:
            #if 'id' in line:
            #    continue
            x = float(line.split(',')[4])*0.01
            y = float(line.split(',')[2])*0.01
            #z = 0

            transformer = Transformer.from_crs("EPSG:4326", "EPSG:28992", always_xy=True)
            result = transformer.transform(x, y)
            list1.append(result)
    return list1

def main():
    # name of metadata file
    list1 = readfile('SmartPhoneGPGGA.csv')
    # output file name
    writefile('outputSmartPhone.csv', list1)

if __name__ == '__main__':
    main()
