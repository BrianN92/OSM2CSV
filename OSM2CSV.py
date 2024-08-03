import sys
from xml.etree import ElementTree as ET
import pandas as pd
import os

def message_output(line):
    """Outputs a message to stdout and flushes the buffer."""
    sys.stdout.write(line)
    sys.stdout.flush()

def load_nodes(root):
    """Loads nodes from the XML tree and returns a dictionary of node coordinates."""
    node_coords = {}
    for node in root.iter('node'):
        node_id = node.get('id')
        lat = node.get('lat')
        lon = node.get('lon')
        node_coords[node_id] = (lat, lon)
    return node_coords

def store_ways(nodes, root, keywords):
    """Stores ways containing specified keywords and returns a list of way information."""
    ways = []
    for way in root.iter('way'):
        if any(keyword.lower() in tag.get('v', '').lower() for tag in way.iter('tag') for keyword in keywords):
            way_info = {
                'way_id': way.get('id'),
                'nodes': [],
                'way_name': None,
            }

            for tag in way.iter('tag'):
                if tag.get('k') == 'name':
                    way_info['way_name'] = tag.get('v')

            for nd in way.iter('nd'):
                node_ref = nd.get('ref')
                if node_ref in nodes:
                    way_info['nodes'].append({
                        'node_id': node_ref,
                        'latitude': nodes[node_ref][0],
                        'longitude': nodes[node_ref][1],
                    })
            ways.append(way_info)
    return ways

def main():
    message_output("\nGenerate CSV file from OSM\n")

    if len(sys.argv) < 2:
        message_output(".osm filename missing\n")
        sys.exit(1)

    filename = sys.argv[1]
    print(f"Trying to open file: {filename}")

    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        sys.exit(1)

    csv_name = sys.argv[2] if len(sys.argv) > 2 else filename.replace(".osm", ".csv")
    keywords = sys.argv[3:] if len(sys.argv) > 3 else ' '

    message_output(f"  OSM file       : {filename}\n")
    message_output(f"  CSV file       : {csv_name}\n")
    message_output(f"  Keywords       : {keywords}\n")

    message_output("\nLoading OSM file...\n")
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing file: {e}")
        sys.exit(1)

    nodes = load_nodes(root)
    ways = store_ways(nodes, root, keywords)

    message_output(f"Saving CSV to file {csv_name}\n")
    data = [
        {
            'way_id': way['way_id'],
            'way_name': way['way_name'],
            'node_id': node['node_id'],
            'Latitude': node['latitude'],
            'Longitude': node['longitude']
        }
        for way in ways for node in way['nodes']
    ]

    df_nodes = pd.DataFrame(data)
    df_nodes.to_csv(csv_name, index=False)

    message_output("CSV file saved\n\n")

if __name__ == '__main__':
    main()
