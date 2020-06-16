class AbsMilvus:

    def client_version(self):
        """
        Returns the version of the client.

        :return: Version of the client.

        :rtype: (str)
        """
        pass

    def server_status(self, timeout=30):
        """
        Returns the status of the Milvus server.

        :return:
            Status: Whether the operation is successful.

            str : Status of the Milvus server.

        :rtype: (Status, str)
        """
        pass

    def server_version(self, timeout=30):
        """
        Returns the version of the Milvus server.

        :return:
           Status: Whether the operation is successful.

           str : Version of the Milvus server.

        :rtype: (Status, str)
        """
        pass

    def _cmd(self, cmd, timeout=30):
        pass

    def create_collection(self, collection_name, fields, timeout=30):
        """
        Creates a collection.

        :type  collection_name: str
        :param collection_name: collection name.

        :param fields: field params.
        :type  fields: dict
            ` [
                    {"field_name": "A", "data_type": DataType.INT64},
                    {"field_name": "B", "data_type": DataType.INT64},
                    {"field_name": "C", "data_type": DataType.INT64},
                    {"field_name": "Vec", "data_type": DataType.BINARY_VECTOR, "dimension": 128, "extra_params": {"index_file_size": 100, "metric_type": MetricType.L2}}
            ]`

        :return: N/A

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
        """
        pass

    def has_collection(self, collection_name, timeout=30):
        """

        Checks whether a collection exists.

        :param collection_name: Name of the collection to check.
        :type  collection_name: str

        :return:
            bool

        :raises:
            IllegalCollectionNameException(BaseException)

        """
        pass

    def get_collection_info(self, collection_name, timeout=30):
        """
        Returns information of a collection.

        :type  collection_name: str
        :param collection_name: Name of the collection to describe.

        :returns: TableSchema

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
        """
        pass

    def count_entities(self, collection_name, timeout=30):
        """
        Returns the number of vectors in a collection.

        :type  collection_name: str
        :param collection_name: target table name.

        :returns:
            count: int, table row count

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
        """
        pass

    def list_collections(self, timeout=30):
        """
        Returns collection list.

        :return:
            collections: list of collection names, return when operation
                    is successful

        :raises:

        """
        pass

    def get_collection_stats(self, collection_name, timeout=30):
        """
        Returns collection statistics information.

        This API not define return values and exceptions

        :return:

            statistics: statistics information

        :raises:
        
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)


        """
        pass

    def load_collection(self, collection_name, timeout=None):
        """
        Loads a collection for cache.

        :type collection_name: str
        :param collection_name: collection to load

        :return: N/A

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def reload_segments(self, collection_name, segment_ids):
        """
            Load segment delete docs to cache

            This API not define return values and exceptions

        : return:
            Status

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def drop_collection(self, collection_name, timeout=30):
        """
        Deletes a collection by name.

        :type  collection_name: str
        :param collection_name: Name of the collection being deleted

        :returns:
            Status, indicate if operation is successful
                - SUCCESS_BUT_NOT_DROP_COLLECTION
                - DROPPED

        :raises:
            IllegalCollectionNameException(BaseException)
        """
        pass

    def insert(self, collection_name, entities, ids=None, partition_tag=None, params=None):
        """
        Insert vectors to a collection.

        :param collection_name:
        :type  collection_name: str

        :param entities:
        :type  entities: dict
        `{
            "Attributes":  [
                {"field": "A", "values": A_list},
                {"field": "B", "field_values": A_list},
                {"field": "C", "field_values": A_list, "datatype": datatype:},
                {"field": "Vec", "field_values": vec}
            ]
        }`

        :type  collection_name: str
        :param collection_name: Name of the collection to insert vectors to.

        :type partition_tag: str or None.
            If partition_tag is None, vectors will be inserted to the collection rather than partitions.

        :param partition_tag: Tag of a partition.

       :return: N/A

       :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
            InvalidRowRecordException(BaseException)
            InvalidVectorIdException(BaseException)
            PartitionTagNotExistException(BaseException)
            InvalidPartitionTagException(BaseException)
        """
        pass

    def get_entity_by_id(self, collection_name, ids, timeout=None):
        """
        Returns raw vectors according to ids.

        :param collection_name: Name of the collection
        :type collection_name: str

        :param ids: list of vector id
        :type ids: list

        :return:
            Vectors: list[list[float]]

        :raises:
            CollectionNotExistException(BaseException)
            InvalidVectorIdException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def list_id_in_segment(self, collection_name, segment_name, timeout=None):
        """
        This API not define return values and exceptions

        :returns:
            ids: list[int]

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def create_index(self, collection_name, params=None, timeout=None, **kwargs):
        """
        Creates index for a collection.

        :param collection_name: Collection used to create index.
        :type collection_name: str

        :param params: index params
        :type params: 

        :return:
            Status:
                - SUCCESS_BUT_NOT_CREATE_INDEX
                - CREATED

        :raises:
            CollectionNotExistException(BaseException)
            InvalidIndexParamsException(BaseException)
            InvalidIndexTypeException(BaseException)
            IllegalCollectionNameException(BaseException)
        """
        pass

    def get_index_info(self, collection_name, params, timeout=30):
        """
        Show index information of a collection.

        :type collection_name: str
        :param collection_name: table name been queried

        :returns:
            IndexSchema:

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def drop_index(self, collection_name, params, timeout=30):
        """
        Removes an index.

        :param collection_name: target collection name.
        :type collection_name: str

        :return:
            Status:
                - SUCCESS_BUT_NOT_DROP_INDEX
                - DROPPED

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def create_partition(self, collection_name, partition_tag, timeout=30):
        """
        create a partition for a collection.

        :param collection_name: Name of the collection.
        :type  collection_name: str

        :param partition_name: Name of the partition.
        :type  partition_name: str

        :param partition_tag: Name of the partition tag.
        :type  partition_tag: str

        :return:
            Status: Whether the operation is successful.
                - SUCCESS_BUT_NOT_CREATE_PARTITION
                - CREATED

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
            IllegalPartitionNameException(BaseException)
            ExceedPartitionMaxLimitException(BaseException)

        """
        pass

    def has_partition(self, collection_name, partition_tag):
        """
        Check if specified partition exists.

        This API not define return values and exceptions

        :param collection_name: target table name.
        :type  collection_name: str

        :param partition_tag: partition tag.
        :type  partition_tag: str

        :return:
            Status: Whether the operation is successful.
            exists: If specified partition exists

        :raises:


        """
        pass

    def list_partitions(self, collection_name, timeout=30):
        """
        Show all partitions in a collection.

        :param collection_name: target table name.
        :type  collection_name: str

        :param timeout: time waiting for response.
        :type  timeout: int

        :return:
            partition_list: list[str]

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def drop_partition(self, collection_name, partition_tag, timeout=30):
        """
        Deletes a partition in a collection.

        :param collection_name: Collection name.
        :type  collection_name: str

        :param partition_tag: Partition name.
        :type  partition_tag: str

        :return:
            Status: Whether the operation is successful.
                - SUCCESS_BUT_NOT_DROP_PARTITION
                - DROPPED

        :raises:
            CollectionNotExistException(BaseException)
            PartitionTagNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass
    
    @deprecated
    def search(self, collection_name, vector_params, dsl, partition_tags=None, params=None, **kwargs):
        """
        Search vectors in a collection.

        :param collection_name: Name of the collection.
        :type  collection_name: str

        :param vector_params:
        :type  vector_params: dict
            `[
                {"ph_1": {"field_name": "Vec", "topk": 10, "params": {"nprobe": 10},},
                 "vector": vec[:10]},
            ]`

        :param dsl:
        :type  dsl: dict
            `{
                "bool": {
                    "must": [
                        {"term": {"field_name": "A", "values": [1, 2, 5]}},
                        {"range": {"field_name": "B", "values": {"gt": "1", "lt": "100"}}},
                        {"vector": "ph_1"}
                    ],
                },
            }`

        :param params:
        :type  params: dict

        :param partition_tags: tags to search
        :type  partition_tags: list

        :return
            result: query result

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
            InvalidTopkException(BaseException)
            InvalidSearchParamException(BaseException)
            PartitionTagNotExistException(BaseException)
            InvalidPartitionTagException(BaseException)

        """
        pass

    def search(self, collection_name, query_entities, partition_tags=None, params=None, **kwargs):
        """
        :param collection_name:
        :type  collection_name: str

        :param query_entities:
        :type  query_entities: dict
             `{
                 "bool": {
                     "must": [
                         {"term": {"A": {"values": [1, 2, 5]}}},
                         {"range": {"B": {"ranges": {RangeType.GT: 1, RangeType.LT: 100}}}},
                         {"vector": {"Vec": {"topk": 10, "query": vec[: 1], "params": {"nprobe": 10}}}}
                     ],
                 },
             }`
             
             `{
                 "bool": {
                     "must": [
                         {"vector": {"Vec": {"topk": 10, "query": vec[: 1], "params": {"nprobe": 10}}}}
                     ],
                 },
             }`

        :param params: extra params.
        :type prams: dict

        :return
            result: query result

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
            InvalidTopkException(BaseException)
            InvalidSearchParamException(BaseException)
            PartitionTagNotExistException(BaseException)
            InvalidPartitionTagException(BaseException)

        """
        pass

    def search_in_segment(self, collection_name, segment_ids, query_entities, params=None, timeout=None):
        """
        :param collection_name:
        :type  collection_name: str

        :param file_ids:
        :type  file_ids: list[int]

        :param query_entities:
        :type  query_entities: dict

        :param params: extra params.
        :type prams: dict

        :return
            result: query result

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
            InvalidTopkException(BaseException)
            InvalidSearchParamException(BaseException)
            PartitionTagNotExistException(BaseException)
            InvalidPartitionTagException(BaseException)

        """
        pass

    def delete_entity_by_id(self, collection_name, ids, timeout=None):
        """
        Deletes vectors in a collection by vector ID.

        :param collection_name: Name of the collection.
        :type  collection_name: str

        :param id_array: list of vector id
        :type  id_array: list[int]

        :return:
            Status: Whether the operation is successful.
                - ID_NOT_EXIST
                - DELETED

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)
            InvalidVectorIdException(BaseException)

        """
        pass

    def flush(self, collection_names=None, timeout=None, **kwargs):
        """
        Flushes vector data in one collection or multiple collections to disk.

        :type  collection_name_array: list
        :param collection_name: Name of one or multiple collections to flush.

        :return: N/A

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def compact(self, collection_name, timeout=None, **kwargs):
        """
        Compacts segments in a collection. This function is recommended after deleting vectors.

        :type  collection_name: str
        :param collection_name: Name of the collections to compact.

        :return:
            Status:
                - SUCCESS_BUT_NOT_COMPACT
                - COMPACTED

        :raises:
            CollectionNotExistException(BaseException)
            IllegalCollectionNameException(BaseException)

        """
        pass

    def get_config(self, parent_key, child_key):
        """
        Gets Milvus configurations.

        """
        pass

    def set_config(self, parent_key, child_key, value):
        """
        Sets Milvus configurations.

        """
        pass

