import os
import json
from random import randint
from subprocess import Popen, PIPE

from .aws_config_file import AWSConfig

class GetS3Handler(AWSConfig):
    """Returns an object with methods to interact with aws S3 storage service.
    
    This module allows the user to interact with S3 storage service.

    The module contains the following functions:

    - `list_buckets()` - Returns List of all S3 buckets of an aws account.
    - `list_objects()` - Returns List of all the objects in the bucket/bucket_path recursively.
    - `upload_objects()` - Upload files/folders to s3 bucket.
    - `download_objects()` - Download files/folders from s3 bucket.
    
    Example : 
        ```
        >> from satsure_cloud_utils import GetS3Handler
        >> s3_handler = GetS3Handler( 
                        access_key_id = "*****",
                        secret_access_key="*****"
                        )
        >> output = s3_handler.get_buckets()
        >> print(output)
        ```

    """
    AWS_PROFILE_NAME = ""
    def __init__(self,config_file_path:str):
        AWSConfig.__init__(self,config_file_path)
    
    def _list_buckets(self):
        command = f'aws s3api list-buckets --profile {self.AWS_PROFILE_NAME} --query "Buckets[].Name" --output text'

        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        
        command_output_str = stdout.decode("utf-8")

        try:
            bucket_names_list = command_output_str.strip("\n").strip("\r").split("\t")
            return bucket_names_list
            
        except Exception as E:
            print("No output found")
            return [command_output_str]
             
    def list_buckets(self):
        """Lists all s3 buckets of an aws account
          
        Returns:
            list: output/error list
        """
        return self._list_buckets()
        
    def _list_objects(self,
                      bucket_name: str,
                      obj_path: str = "",
                      include_filters: list = [],
                      exclude_filters: list = []):

        include_pattern_str = ""
        exclude_pattern_str = ""
        
        if len(include_filters) > 0:
            include_filters_str =  "&&".join( [f"contains(Key,'{include_filter}')" for include_filter in include_filters ] )
            
            include_pattern_str = f""" --query "Contents[? {include_filters_str} ].Key" """
        
        if len(exclude_filters) > 0: 
            exclude_filters_str = "&&".join( [f"!contains(Key,'{exclude_filter}')" for exclude_filter in exclude_filters ] )
            
            exclude_pattern_str = f""" --query "Contents[? {exclude_filters_str} ].Key" """
        
        
        command = f"""aws s3api list-objects --bucket "{bucket_name}" --prefix "{obj_path}" {include_pattern_str} {exclude_pattern_str} --profile {self.AWS_PROFILE_NAME} --output text"""

        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        
        command_output_str =  stdout.decode("utf-8")
        try:
            object_names_list = command_output_str.strip("\n").strip("\r").split("\t")
            
            return object_names_list
            
        except Exception as E:
            print("No output found")
            return []
    
    def list_objects(self,
                    bucket_name: str,
                    obj_path: str = "",
                    include_filters: list = [],
                    exclude_filters: list = []):
        
        """Lists all the objects in the bucket/bucket_path recursively

        Args:
            bucket_name (string): Name of the bucket
            obj_path (string): Path of files in bucket (Default: '')
            include_filters (list): list of strings to include in filtering
            exclude_filters (list): list of strings to exclude in filtering
        Returns:
            list: output/error list
        """
        
        return self._list_objects(bucket_name,obj_path,include_filters,exclude_filters)
        
    def upload_objects(self,
                     bucket_name: str,
                     s3_obj_path: str,
                     local_obj_path: str):
        """Upload files/folders to s3 bucket
        
        Args:
            bucket_name (string): Name of bucket
            s3_obj_path (string): Path on s3 bucket
            local_obj_path (string): Local path on your machine
        Returns:
            string: output/error string
        """
        
        s3_obj_path = s3_obj_path.strip("/")

        if os.path.isdir(local_obj_path):
            command = f"""aws s3 sync "{local_obj_path}" "s3://{bucket_name}/{s3_obj_path}" --profile {self.AWS_PROFILE_NAME} --output json"""
        else:
            command = f"""aws s3 cp "{local_obj_path}" "s3://{bucket_name}/{s3_obj_path}" --profile {self.AWS_PROFILE_NAME} --output json"""
        
        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        return stdout.decode("utf-8")
    
    def _download_objects(self,
                         bucket_name: str,
                         s3_obj_path: str ,
                         local_obj_path: str,
                         include_filters: list = [],
                         exclude_filters:list = ["*"],
                         dryrun: bool = False):
        
        include_filter_pattern = ""
        exclude_filter_pattern = ""
        dryrun_pattern = ""
        
        if len(include_filters) > 0:
            include_filter_pattern +=  " ".join( [f'--include "*{include_filter}*"' for include_filter in include_filters ] )
        
        if len(exclude_filters) > 0: 
            exclude_filter_pattern +=  " ".join( [f'--exclude "*{exclude_filter}*"' for exclude_filter in exclude_filters ] )
            
        if dryrun:
            dryrun_pattern = f"--dryrun"
        
        command = f"""aws s3 sync {dryrun_pattern} "s3://{bucket_name}/{s3_obj_path}" "{local_obj_path}" {exclude_filter_pattern} {include_filter_pattern} --profile {self.AWS_PROFILE_NAME} --output json"""

        process = Popen(command,shell=True,stdout=PIPE)
        stdout, _ = process.communicate()
        return stdout.decode("utf-8")
    
    def download_objects(self,
                         bucket_name: str,
                         s3_obj_path: str ,
                         local_obj_path: str=".",
                         include_filters: list = [],
                         exclude_filters:list = ["*"],
                         dryrun: bool = False):
        """Download files/folders from s3 bucket
        
        Args:
            bucket_name (string): Name of bucket
            s3_obj_path (string): path on s3 bucket
            local_obj_path (string): Path on your machine
            include_filters (list): list of strings to include in filtering
            exclude_filters (list): list of strings to exclude in filtering
            dryrun (bool): Displays the operations that would be performed using the specified command without actually running them
        Returns:
            string: output/error string
        """
        
        return self._download_objects(bucket_name,
                               s3_obj_path,
                               local_obj_path,
                               include_filters,
                               exclude_filters,
                               dryrun)
       
