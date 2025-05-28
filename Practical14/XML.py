import xml.dom.minidom
import xml.sax
from datetime import datetime

# DOM 
def process_dom(file_path):
    start_time = datetime.now()
    dom_doc = xml.dom.minidom.parse(file_path)
    terms = dom_doc.getElementsByTagName('term')
    
    max_counts = {
        'molecular_function': {'count': 0, 'id': ''},
        'biological_process': {'count': 0, 'id': ''},
        'cellular_component': {'count': 0, 'id': ''}
    }
    
    for term in terms:
        namespace_elements = term.getElementsByTagName('namespace')
        if not namespace_elements:
            continue
        namespace = namespace_elements[0].firstChild.data.strip()
        if namespace not in max_counts:
            continue
        
        is_a_count = len(term.getElementsByTagName('is_a'))
        current_max = max_counts[namespace]
        if is_a_count > current_max['count']:
            id_element = term.getElementsByTagName('id')[0]
            current_max['count'] = is_a_count
            current_max['id'] = id_element.firstChild.data.strip()
    
    dom_time = datetime.now() - start_time
    return max_counts, dom_time

# SAX 
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.max_counts = {
            'molecular_function': {'count': 0, 'id': ''},
            'biological_process': {'count': 0, 'id': ''},
            'cellular_component': {'count': 0, 'id': ''}
        }
        self.current_term = None
        self.current_content = ''
        self.in_namespace = False
        self.in_id = False
    
    def startElement(self, tag, attrs):
        if tag == 'term':
            self.current_term = {'id': '', 'namespace': '', 'is_a_count': 0}
        elif tag == 'is_a' and self.current_term is not None:
            self.current_term['is_a_count'] += 1
        elif tag == 'namespace':
            self.in_namespace = True
            self.current_content = ''
        elif tag == 'id':
            self.in_id = True
            self.current_content = ''
    
    def characters(self, content):
        if self.in_namespace or self.in_id:
            self.current_content += content
    
    def endElement(self, tag):
        if tag == 'term':
            if self.current_term['namespace'] in self.max_counts:
                ns = self.current_term['namespace']
                current_max = self.max_counts[ns]
                if self.current_term['is_a_count'] > current_max['count']:
                    current_max['count'] = self.current_term['is_a_count']
                    current_max['id'] = self.current_term['id']
            self.current_term = None
        elif tag == 'namespace':
            self.in_namespace = False
            if self.current_term is not None:
                self.current_term['namespace'] = self.current_content.strip()
        elif tag == 'id':
            self.in_id = False
            if self.current_term is not None:
                self.current_term['id'] = self.current_content.strip()

def process_sax(file_path):
    start_time = datetime.now()
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    sax_time = datetime.now() - start_time
    return handler.max_counts, sax_time

# global
def main():
    file_path = '/Users/pro/Desktop/IBI1_2024-25/Practical14/go_obo.xml'
    
    # DOM 
    dom_results, dom_time = process_dom(file_path)
    print("DOM Results:")
    for ns in dom_results:
        print(f"{ns}: {dom_results[ns]['id']} (count: {dom_results[ns]['count']})")
    print(f"DOM Time: {dom_time}\n")
    
    # SAX 
    sax_results, sax_time = process_sax(file_path)
    print("SAX Results:")
    for ns in sax_results:
        print(f"{ns}: {sax_results[ns]['id']} (count: {sax_results[ns]['count']})")
    print(f"SAX Time: {sax_time}\n")
    
    # compare time
    if dom_time < sax_time:
        print("# DOM was faster")
    else:
        print("# SAX was faster")

if __name__ == "__main__":
    main()