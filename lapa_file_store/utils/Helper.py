import os.path

from lapa_database_helper.main import LAPADatabaseHelper

from lapa_file_store.configuration import global_absolute_path_local_storage

local_object_lapa_database_helper = LAPADatabaseHelper()


def create_entry_in_file_store(
    file_name_with_extention: str,
    content_type: str,
    system_file_name_with_extension: str,
    file_storage_token: str,
    file_purpose: str,
    system_relative_path: str,
):
    try:
        database_name = "file_storage"
        schema_name = "public"
        table_name = "file"

        data = [
            {
                "file_name_with_extension": file_name_with_extention,
                "file_content_type": content_type,
                "file_system_file_name_with_extension": system_file_name_with_extension,
                "file_system_relative_path": system_relative_path,
                "file_storage_token": file_storage_token,
                "file_purpose": file_purpose,
            }
        ]

        response = local_object_lapa_database_helper.insert_rows(
            data, database_name, schema_name, table_name
        )

        return response
    except Exception as e:
        raise e


def download_file(file_storage_token):
    try:
        database_name = "file_storage"
        schema_name = "public"
        table_name = "file"

        filters = {"file_storage_token": file_storage_token}

        response = local_object_lapa_database_helper.get_rows(
            filters, database_name, schema_name, table_name
        )

        file_id = str(response[0]["file_id"])
        file_relative_path = response[0]["file_name_with_extension"]
        filepath = os.path.join(config_str_oss_folder_path, file_id, file_relative_path)

        return filepath

    except Exception as e:
        raise e
