from lxml import etree
import xgbxml

if __name__ == '__main__':
    parser=xgbxml.get_parser('0.37')

    tree=etree.parse('xml/block-10-10-6.xml', parser)
    gbxml=tree.getroot()

    # edit an attribute
    gbxml.temperatureUnit='F'
    print(gbxml.temperatureUnit)
    # prints "F"

    # add a child node
    new_node=gbxml.add_Construction()
    new_node.add_Name()
    new_node.Name.text = 'test'
    print(new_node.tag)
    # prints "{http://www.gbxml.org/schema}Construction"

    # edit node text
    print(gbxml.Campus.Location.Name)
    gbxml.Campus.Location.Name.text = 'my_new_station_id'
    # prints "my_new_station_id"

    print(gbxml.Campus.Surfaces)

    # save the edited file
    tree.write('xml/edited_gbxml_file.xml', pretty_print=True)

