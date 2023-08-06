from Evtx.Evtx import Evtx
from Evtx.Views import evtx_file_xml_view
from lxml import etree
import click
import json


def to_lxml(raw_xml):
    """
        Convert raw xml string into an lxml object so we can more easily navigate it.
    """

    utf8_parser = etree.XMLParser(encoding='utf-8')
    clean_xml = raw_xml.replace("xmlns=\"http://schemas.microsoft.com/win/2004/08/events/event\"", "")
    return etree.fromstring(clean_xml, parser=utf8_parser)

def extract_xml(evtx_file):
    """
        Parse the evtx file and extract just the xml parts of each event.
        If the function throws an error, we'll catch it and just return the value we have with the error.
    """
    with Evtx(evtx_file) as evtx:
        for xml, record in evtx_file_xml_view(evtx.get_file_header()):
            try:
                # Successfully parsed! Return the lxml object
                
                yield to_lxml(xml), None
            except etree.XMLSyntaxError as e:
                # Parse failed, return what we have and an exception object
                
                yield xml, e

def evtx_to_json(evtx_file):
    """
        Convert an evtx file from native format to JSON objects.
    """
    
    json_out = []
    for evt, err in extract_xml(evtx_file):
        evt_json = {}
        if err is not None:
            # This record failed to parse, print out the error here in console
            print(err.text())

            # Read the next record
            continue
        
        # Form the structure of the object with top level tags
        for top_node in evt.getchildren():
            # Here we have the top level tags like System and EventData for example
            evt_json[top_node.tag] = {}
        
            # Loop through each top level tag section to get the contents and add to the json object
            for node in top_node.getchildren():
                # create node in json
            
                # EventData uses the same tag name ("DATA") for every tag, 
                # so we'll just use the attribute name here instead
                if node.tag == "Data":
                    tag_name = node.attrib["Name"]
                else:
                    tag_name = node.tag
                
                evt_json[top_node.tag][tag_name] = {}
            
                # Does this node have any content?
                node_content = ""
                if node.text is not None:
                    node_content = node.text.rstrip()
                if len(node_content) > 0:
                    # The tag has some content
                    evt_json[top_node.tag][tag_name]["value"] = node_content           
            
                # check to see if there are any attributes
                if len(node.attrib) > 0:
                    for a in node.attrib:
                        evt_json[top_node.tag][tag_name][a] = node.attrib[a]

        json_out.append(evt_json)
                    
    return json_out


# Setup commandline options
@click.command()
@click.argument('input_file',
            type=click.Path(exists=True))
@click.argument('output_file', 
            type=click.Path())
def main_entry(input_file, output_file):
    """
        WinevtJSON utility - used to convert Microsoft Windows system event logs into JSON format.
        
        \b
        F_IN = A Microsoft Windows system event log (.evtx) file exported from Event Viewer or Sysmon.

        \b
        F_OUT = Path to a file for output of data.
    """
    # Convert evtx to json format
    json_output = evtx_to_json(input_file)

    # Write the output to file
    with open(output_file, "a+") as out_f:
        out_f.writelines(json.dumps(json_output, indent=4))

if __name__ == '__main__':
    main_entry()
