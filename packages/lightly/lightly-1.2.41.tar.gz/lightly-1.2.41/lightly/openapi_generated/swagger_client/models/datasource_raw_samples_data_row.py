# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class DatasourceRawSamplesDataRow(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_name': 'str',
        'read_url': 'ReadUrl'
    }

    attribute_map = {
        'file_name': 'fileName',
        'read_url': 'readUrl'
    }

    def __init__(self, file_name=None, read_url=None, _configuration=None):  # noqa: E501
        """DatasourceRawSamplesDataRow - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_name = None
        self._read_url = None
        self.discriminator = None

        self.file_name = file_name
        self.read_url = read_url

    @property
    def file_name(self):
        """Gets the file_name of this DatasourceRawSamplesDataRow.  # noqa: E501


        :return: The file_name of this DatasourceRawSamplesDataRow.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DatasourceRawSamplesDataRow.


        :param file_name: The file_name of this DatasourceRawSamplesDataRow.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def read_url(self):
        """Gets the read_url of this DatasourceRawSamplesDataRow.  # noqa: E501


        :return: The read_url of this DatasourceRawSamplesDataRow.  # noqa: E501
        :rtype: ReadUrl
        """
        return self._read_url

    @read_url.setter
    def read_url(self, read_url):
        """Sets the read_url of this DatasourceRawSamplesDataRow.


        :param read_url: The read_url of this DatasourceRawSamplesDataRow.  # noqa: E501
        :type: ReadUrl
        """
        if self._configuration.client_side_validation and read_url is None:
            raise ValueError("Invalid value for `read_url`, must not be `None`")  # noqa: E501

        self._read_url = read_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DatasourceRawSamplesDataRow, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatasourceRawSamplesDataRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasourceRawSamplesDataRow):
            return True

        return self.to_dict() != other.to_dict()
