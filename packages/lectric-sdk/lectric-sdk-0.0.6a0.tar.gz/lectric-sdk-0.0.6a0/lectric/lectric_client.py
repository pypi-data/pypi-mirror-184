from typing import Dict, List, Union, Any
import json
from requests import Response
from functools import wraps

from .models.input_data import InputData
from .models.index_in_spec import IndexInSpec
from .models.collection import Collection
from .models.collection_in_spec import CollectionInSpec
from .models.query_spec import QuerySpec
from .models.vector_query_spec import VectorQuerySpec
from .models.query_response import QueryResponse

from .helpers import *
from .client import AuthenticatedClient


# defaults
from .api.default import  root_get, root_auth_auth_get, list_connections_connections_get

# collections
from .api.collection import (
    create_collection_collection_create_post,
    exists_collection_collection_exists_name_get,
    is_empty_collection_collection_empty_name_get,
    get_collection_collection_get_name_get,
    list_collections_collection_list_get,
    get_indexes_collection_indexes_name_get,
    drop_collection_collection_delete,
    sizeof_collection_collection_size_name_get,
    delete_entities_collection_entities_delete,
)

# ingest
from .api.ingest import ingest_ingest_post

# index
from .api.index import create_index_create_post, delete_index_collection_name_field_name_delete

# query
from .api.query import query_query_fields_post, query_query_vectors_post


def propagate_exception(func):
    @wraps(func)
    def propagator(*args, **kwargs):

        response = func(*args, **kwargs)

        if response.status_code == HTTPStatus.OK:
            return response.parsed
        else:
            raise RuntimeError(f"HTTP Code: {response.status_code}, {response}")

    return propagator


class LectricClient:

    def __init__(self, api_url: str, api_key: str=None,
                    cookies: Dict[str, str]={}, timeout:int=60000) -> None:
        """The Lectric client class

        Args:
            api_url (str): The base url for the api service
            api_key (str, optional): The API key for the service. Defaults to None.
            cookies (Dict[str, str], optional): Optional cookies to be maintained. Defaults to {}.
            timeout (int, optional): Request timeout. Defaults to 60000.
        """
        self.api_url = api_url

        self.client = AuthenticatedClient(base_url=self.api_url,
                                    token=api_key, cookies=cookies,
                                    headers={"X-API-KEY": api_key} if api_key else {},
                                    timeout=timeout)

        response_dict = json.loads(self.verify_connection(api_key is not None).content)

        self.api_build_id = response_dict.get("lectric-build-id")
        self.backend_db = response_dict.get("lectric-vdb-backend")

    def verify_connection(self, is_authenticated: bool=False) -> Response:
        """Test the connection to the Lectric server

        Returns:
            bool|RuntimeError: Either True for success or failure
        """

        if is_authenticated:
            response = root_auth_auth_get.sync_detailed(client=self.client)
        else:
            response = root_get.sync_detailed(client=self.client)

        if response.status_code != HTTPStatus.OK.value:
            raise RuntimeError(f"HTTP Code: {response.status_code}, {response}")

        return response

    @propagate_exception
    def list_connections(self) -> List[str]:
        """List the connections created within the vector db

        Returns:
            List[str]: A list of the connection names
        """
        return list_connections_connections_get.sync_detailed(client=self.client)


    ########################## collections ###############################

    @propagate_exception
    def create_collection(self, coll_in_spec: CollectionInSpec) -> Collection:
        """Create a vector collection

        Args:
            coll_in_spec (CollectionInSpec): The collection specification to be created

        Returns:
            Collection: An object representing the created collection
        """
        return create_collection_collection_create_post.sync_detailed(client=self.client, json_body=coll_in_spec)


    @propagate_exception
    def collection_exists(self, name: str) -> bool:
        """Check if a collection exists

        Args:
            name (str): The name of the collection

        Returns:
            bool: True if the collection exist, else False
        """
        return exists_collection_collection_exists_name_get.sync_detailed(client=self.client, name=name)


    @propagate_exception
    def is_collection_empty(self, name: str) -> bool:
        """Check if the collection has data or is empty

        Args:
            name (str): The name of the collection

        Returns:
            bool: True if the collection is empty, else False
        """
        return is_empty_collection_collection_empty_name_get.sync_detailed(client=self.client, name=name)


    @propagate_exception
    def get_collection(self, name: str) -> Collection:
        """Get a collection by name. Each collection has a unique, user defined name

        Args:
            name (str): The name of the collection.

        Returns:
            Collection: A representation of the collection
        """
        return get_collection_collection_get_name_get.sync_detailed(client=self.client, name=name)


    @propagate_exception
    def get_indexes(self, collection_name: str) -> List[str]:
        """Get a list of the field names for which indexes are defined

        Args:
            collection_name (str): The name of the collection for which indexes are queried

        Returns:
            List[str]: A list of the field names for which indexes are defined
        """
        return get_indexes_collection_indexes_name_get.sync_detailed(client=self.client, name=collection_name)


    @propagate_exception
    def list_collections(self) -> List[str]:
        """List the names of the collections

        Returns:
            List[str]: The collection names
        """
        return list_collections_collection_list_get.sync_detailed(client=self.client)


    @propagate_exception
    def drop_collection(self, name: str) -> None:
        """Drop (delete) a collection by name

        Args:
            name (str): The name of the collection to be dropped

        Returns:
            _type_: None
        """
        return drop_collection_collection_delete.sync_detailed(client=self.client, name=name)


    @propagate_exception
    def delete_entities(self, collection_name: str,
                ids: Union[List[str], List[int]]) -> None:
        """Delete entities by Primary key ID

        Args:
            collection_name (str): The collection name
            ids (Union[List[str], List[int]], optional): The list of IDs for which is to happen

        Returns:
            _type_: None
        """
        return delete_entities_collection_entities_delete.sync_detailed(
                client=self.client, name=collection_name, json_body=ids)


    @propagate_exception
    def sizeof(self, name: str) -> int:
        """Get the size of (number of entities) in a collection

        Args:
            name (str): The collection name

        Raises:
            RuntimeError: If collection does not exist

        Returns:
            int: The size of the collection
        """
        return sizeof_collection_collection_size_name_get.sync_detailed(client=self.client, name=name)


    @propagate_exception
    def ingest(self, data: InputData) -> None:
        """Ingest data into a collection

        Args:
            data (InputData): The data to be ingested

        Returns:
            _type_: None
        """
        return ingest_ingest_post.sync_detailed(client=self.client, json_body=data)

    @propagate_exception
    def create_index(self, index_spec: IndexInSpec) -> None:
        """Create an index for one field within the collection

        Args:
            index_spec (IndexInSpec): The creation spec of the index

        Returns:
            _type_: None
        """
        return create_index_create_post.sync_detailed(client=self.client, json_body=index_spec)


    @propagate_exception
    def drop_index(self, collection_name: str, field_name: str) -> None:
        """Drop (delete) a previously created index

        Args:
            collection_name (str): The collection name
            field_name (str): The field name on which the index is defined

        Returns:
            _type_: None
        """
        return delete_index_collection_name_field_name_delete.sync_detailed(client=self.client, collection_name=collection_name, field_name=field_name)

    @propagate_exception
    def query(self, query_spec: Union[QuerySpec, VectorQuerySpec]) -> Union[List[Dict], QueryResponse]:
        """Query a collection using either a vector, a batch of vectors or query on the fields

        Args:
            query_spec (Union[QuerySpec, VectorQuerySpec]): The specification of the query

        Raises:
            RuntimeError: If the query spec is non conformant, this is raised.

        Returns:
            Union[List[Dict], QueryResponse]: Either a list with the queried fields or a QueryResponse object from a vector query
        """

        if isinstance(query_spec, QuerySpec):
            return query_query_fields_post.sync_detailed(client=self.client, json_body=query_spec)
        elif isinstance(query_spec, VectorQuerySpec):
            return query_query_vectors_post.sync_detailed(client=self.client, json_body=query_spec)
        else:
            raise RuntimeError(f"Unable to query with given query spec of type {type(query_spec)}")

