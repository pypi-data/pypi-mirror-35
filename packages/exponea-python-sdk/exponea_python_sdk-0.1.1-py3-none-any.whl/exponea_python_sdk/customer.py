class Customer:
    def __init__(self, client):
        self.client = client
        self.endpoint_base = "/data/v2/projects/{}/customers".format(client.project_token)
    
    def get_customer(self, ids):
        path = self.endpoint_base + "/export-one"
        payload = { "customer_ids": ids }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        return {
            "ids": response["ids"],
            "properties": response["properties"],
            "events": response["events"]
        }
    
    def get_customer_consents(self, ids, consents):
        path = self.endpoint_base + "/attributes"
        payload = { "customer_ids": ids, "attributes": [{"type": "consent", "category": consent_type} for consent_type in consents]}
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        result = {}
        for index, consent_type in enumerate(consents):
            # Check if user has permission to request data_type
            if not response["results"][index]["success"]:
                logger.warning("No permission to retrieve consent {}".format(consent_type))
                result[consent_type] = None
                continue
            result[consent_type] = response["results"][index]["value"]
        return result
    
    def get_customer_attributes(self, customer_ids, properties=[], segmentations=[], ids=[], expressions=[], aggregations=[], predictions=[]):
        path = self.endpoint_base + "/attributes"
        payload = {
            "customer_ids": customer_ids,
            "attributes": 
                [{"type": "property", "property": customer_property} for customer_property in properties] +
                [{"type": "segmentation", "id": segmentation} for segmentation in segmentations] +
                [{"type": "id", "id": id} for id in ids] +
                [{"type": "expression", "id": expression} for expression in expressions] +
                [{"type": "aggregate", "id": aggregate} for aggregate in aggregations] +
                [{"type": "prediction", "id": prediction} for prediction in predictions]
        }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        result = {}
        attributes_retrieved = 0
        for attribute_type in [("properties", properties), ("segmentations", segmentations), ("ids", ids), ("expressions", expressions), ("aggregations", aggregations), ("predictions", predictions)]:
            attribute_type_name = attribute_type[0]
            attribute_type_ids = attribute_type[1]
            if len(attribute_type_ids) == 0:
                continue
            result[attribute_type_name] = {}
            for id in attribute_type_ids:
                # Check if user has permission to request attribute_type
                if not response["results"][attributes_retrieved]["success"]:
                    logger.warning("No permission to retrieve {} {}".format(attribute_type_name, id))
                    result[attribute_type_name][id] = None
                    continue
                result[attribute_type_name][id] = response["results"][attributes_retrieved]["value"]
                attributes_retrieved += 1
        return result
    
    def get_customers(self):
        path = self.endpoint_base + "/export"
        payload = { "format": "native_json" }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        users = []
        ids = [ field["id"] for field in filter(lambda x: x["type"] == "id" ,response["fields"])]
        properties = [ field["property"] for field in filter(lambda x: x["type"] == "property" ,response["fields"])]
        for row in response["data"]:
            user = { "ids": {}, "properties": {} }
            for index, attribute in enumerate(row):
                if index < len(ids):
                    user["ids"][ids[index]] = attribute
                else:
                    user["properties"][properties[index - len(ids)]] = attribute
            users.append(user)
        return users

    
    def get_events(self, customer_ids, event_types):
        path = self.endpoint_base + "/events"
        payload = { "customer_ids": customer_ids, "event_types": event_types }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        return response["data"]
    
    def anonymize_customer(self, customer_ids):
        path = self.endpoint_base + "/anonymize"
        payload = { "customer_ids": customer_ids }
        response = self.client.request("POST", path, payload)
        if response is None:
            return None
        return response["success"]
