from inspect import isclass
from ixnetwork_restpy.connection import Connection
from ixnetwork_restpy.errors import NotFoundError
from ixnetwork_restpy.multivalue import Multivalue
from ixnetwork_restpy.files import Files


try:
    basestring
except NameError:
    basestring = str


class Base(object):
    """Base"""
    def __init__(self, parent):
        self._properties = {}
        self._parent = parent
        if self._parent is not None:
            self._connection = parent._connection

    @property
    def parent(self):
        """The parent object of this object
        
        Returns:
            obj(Base): The parent object of this object

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._parent

    @property
    def href(self):
        """The hypertext reference of this object
        
        Returns: 
            str: The fully qualified hypertext reference of this object

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._properties['href']

    def _check_arg_type(self, object_to_test, arg_type):
        if isinstance(object_to_test, arg_type) is not True:
            raise TypeError('the parameter supplied is of %s but must be of <type \'%s\'>' % (type(object_to_test), arg_type.__name__))

    def _get_attribute(self, name):
        """The main accessor for all sdm attributes"""
        if name in self._properties.keys():
            return self._properties[name]
        else:
            raise NotFoundError('The attribute %s is not supported with the current version of the test platform' % name)
  
    def _set_attribute(self, name, value):
        self._update({name: value})
        
    def _dump(self):
        dump = '%s: %s' % (self.__class__.__name__, self.href)
        methods = dir(self)
        for key in sorted(self._properties.keys()):
            property_name = '%s%s' % (key[0].upper(), key[1:])
            if key in ['href']:
                continue
            if property_name in methods:
                dump += '\n\t%s: %s' % (property_name, self._properties[key])
        return dump

    def __str__(self):
        return self._dump()

    def __repr__(self):
        return self._dump()

    def _build_payload(self, locals_dict, ignore_internal_properties=False):
        """Build and return a payload dictionary

        Ignore the following:
            key of self
            any key not in the internal dictionary
            value of None or Multivalue
        
        Returns: 
            dict: if there are items in the payload after processing of the locals_dict is complete
            None: if there are no items in the payload
        """
        payload = {}
        if locals_dict is not None:
            for key, value in locals_dict.items():
                if key == 'self' or value is None or isinstance(value, Multivalue):
                    continue
                if isclass(value) is True:
                    continue
                if ignore_internal_properties is True:
                    attribute_name = key
                else:
                    attribute_name = '%s%s' % (key[0].lower(), key[1:])
                payload_value = self._build_value(value)
                if payload_value is not None:
                    payload[attribute_name] = payload_value
        if bool(payload) is True:
            return payload
        else:
            return None

    def _build_value(self, value):
        if isinstance(value, Files):
            if value.is_local_file:
                upload_url = '%s/files?filename=%s' % (self.href[0:self.href.find('ixnetwork') + len('ixnetwork')], value.file_name)
                self._connection._execute(upload_url, payload=value)
            return value.file_name
        elif isinstance(value, Base):
            return value.href
        elif isinstance(value, list):
            list_values = []
            for list_item in value:
                list_value = self._build_value(list_item)
                if list_value is not None:
                    list_values.append(list_value)
            return list_values
        else:
            return value

    def _create(self, child_instance, locals_dict):
        payload = self._build_payload(locals_dict)
        url = '%s/%s' % (self._properties['href'], child_instance._SDM_NAME)
        properties = self._connection._create(url, payload)
        self._set_properties(url, child_instance, properties)
        return child_instance

    def _read(self, child_instance, rest_id):
        url = '%s/%s' % (self._properties['href'], child_instance._SDM_NAME)
        if rest_id is not None:
            url = '%s/%s/%s' % (self._properties['href'], child_instance._SDM_NAME, rest_id)
        response = self._connection._read(url)
        if isinstance(response, list):
            sibling_list = []
            for item in response:
                sibling = child_instance._create_sibling()
                self._set_properties(url, sibling, item)
                sibling_list.append(sibling)
            return sibling_list
        else:
            self._set_properties(url, child_instance, response)
        return child_instance
    
    def _set_properties(self, url, child_instance, properties):
        if properties is None:
            return
        child_instance._properties = properties
        for key in child_instance._properties.keys():
            value = child_instance._properties[key]
            if value is not None and isinstance(value, basestring) and value.find('/ixnetwork/multivalue') != -1:
                child_instance._properties[key] = Multivalue(self._connection, child_instance._properties[key])
        if 'href' not in child_instance._properties.keys():
            if 'links' in child_instance._properties.keys():
                child_instance._properties['href'] = child_instance._properties['links'][0]['href']
                child_instance._properties.pop('links') 
            elif 'id' in child_instance._properties.keys():
                child_instance._properties['href'] = '%s/%s' % (url, child_instance._properties['id'])        

    def _create_sibling(self):
        sibling = self.__class__(self._parent)
        return sibling

    def _update(self, locals_dict):
        payload = self._build_payload(locals_dict)
        if bool(payload) is True:
            self._connection._update(self._properties['href'], payload)
            properties = self._connection._read(self.href)
            self._set_properties(self.href, self, properties)
        return self
    
    def _delete(self):
        self._connection._delete(self._properties['href'])

    def _execute(self, operation, payload=None, response_object=None):
        url = self._properties['href']

        if operation is not None:
            url = '%s/operations/%s' % (url, operation)

        payload = self._build_payload(payload, ignore_internal_properties=True)
        response = self._connection._execute(url, payload)
        if response_object is None:
            return response

    def refresh(self):
        """Refresh the contents of this object

        Returns: 
            None

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        response = self._connection._read(self.href)
        self._set_properties(self.href, self, response)

    def _select(self, child_instance, locals_dict):
        payload = {
            'selects': [
                {
                    'from': child_instance.parent.href,
                    'properties': [],
                    'children': [
                        {
                            'child': child_instance._SDM_NAME,
                            'properties': ['*'],
                            'filters': []
                        }
                    ],
                    'inlines': []
                }
            ]
        }
        for key in locals_dict.keys():
            if key == 'self' or locals_dict[key] is None or isclass(locals_dict[key]):
                continue
            child_filter = {
                'property': '%s%s' % (key[0].lower(), key[1:]),
                'regex': locals_dict[key]
            }
            payload['selects'][0]['children'][0]['filters'].append(child_filter)
        end = child_instance.parent.href.index('ixnetwork') + len('ixnetwork')
        url = '%s/operations/select' % child_instance.parent.href[0:end]
        response = self._connection._execute(url, payload)
        sibling_list = []
        if child_instance._SDM_NAME in response[0].keys():
            for item in response[0][child_instance._SDM_NAME]:
                sibling = child_instance._create_sibling()
                self._set_properties(url, sibling, item)
                sibling_list.append(sibling)
        return sibling_list
