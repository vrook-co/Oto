"""

When an video file is passed along with the name of an output file, exrtact the meta data information of the passed video and write it out to the file.

"""

from pymdeco import services
srv = services.FileMetadataService()
def extract_meta_data(video_file_name, output_file=meta.txt, *args, **kwargs):
    
    """

    #TODO
    
    - Fill this with the documentation of the code. i.e. the docstring.
    - Accomadate for the different video file types such as mp4, mkv, raw, etc.

    - Add arguments to accomadate, if needed.

    - Add requirements to requirements.txt usign "pip freeze > requirements"

    - Make sure the meta data output file is human readable. 

    """
    video_file_extensions = (".mp4", ".mkv", ".raw", ".mov", ".flv", ".wmv", ".avi", ".webm")
    if video_file_name.endswith((video_file_extensions)):
        meta = srv.get_metadata(video_file_name)
        print(meta.to_json(indent=2))
        
    else:
        print("Video file format not supported")

