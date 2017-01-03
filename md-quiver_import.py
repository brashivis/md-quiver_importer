import os, json, collections, uuid
from time import time

# Path to directory containing .md files to be imported
src_dir = ''
# Moves .md files to dst_dir after import
dst_dir = ''
# Path to .qvlibrary
qvr_dir = ''

# Only gets .md files
def getFiles():
    md_files = []
    for entry in os.scandir(src_dir):
        if entry.is_file() and entry.name.endswith('.md'):
            md_files.append(entry)

    return md_files

def importFiles(in_files):
    os.chdir(dst_dir)

    # Iterate through files
    for current_file in files:
        file_obj = open(current_file.path)
        contents = file_obj.read()

        # Create JSON structure
        cell_dict = collections.OrderedDict()
        cell_dict["type"] = "markdown"
        cell_dict["data"] = contents
        
        cell_array = [cell_dict]
        
        json_dict = collections.OrderedDict()
        json_dict["title"] = "test"
        json_dict["cells"] = cell_array

        # Serialize JSON
        json_str = json.dumps(json_dict)

        # Write contents.json file to disk
        cur_uuid = uuid.uuid4().urn[9:]
        path_newfile = './' + cur_uuid + '.qvnote'
        os.mkdir(path_newfile)
        
        path_note = path_newfile + '/content.json'
        new_fileobj = open(path_note, 'w')
        new_fileobj.write(json_str)
        
        # Setup note meta information
        time_ms = int(round(int(time())))
        current_filename = os.path.splitext(current_file.name)[0]
        title = current_filename
        tags = []

        meta_dict = collections.OrderedDict()
        meta_dict["created_at"] = time_ms
        meta_dict["tags"] = tags
        meta_dict['title'] = title
        meta_dict['updated_at'] = time_ms
        meta_dict['uuid'] = cur_uuid

        meta_json = json.dumps(meta_dict)

        # Write meta.json file to disk
        path_meta = path_newfile + '/meta.json'
        print(path_meta)
        print(meta_json)
        new_metaobj = open(path_meta, 'w')
        new_metaobj.write(meta_json)
        
        new_metaobj.close()
        new_fileobj.close()

        # Move files to dst_dir
        os.rename(src_dir + current_filename + '.md', dst_dir + current_filename + '.md')
        file_obj.close()


files = getFiles()