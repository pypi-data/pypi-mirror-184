# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteFacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'face_set_name': 'str',
        'body': 'DeleteFacesBatchReq'
    }

    attribute_map = {
        'face_set_name': 'face_set_name',
        'body': 'body'
    }

    def __init__(self, face_set_name=None, body=None):
        """BatchDeleteFacesRequest

        The model defined in huaweicloud sdk

        :param face_set_name: 人脸库名称。
        :type face_set_name: str
        :param body: Body of the BatchDeleteFacesRequest
        :type body: :class:`huaweicloudsdkfrs.v2.DeleteFacesBatchReq`
        """
        
        

        self._face_set_name = None
        self._body = None
        self.discriminator = None

        self.face_set_name = face_set_name
        if body is not None:
            self.body = body

    @property
    def face_set_name(self):
        """Gets the face_set_name of this BatchDeleteFacesRequest.

        人脸库名称。

        :return: The face_set_name of this BatchDeleteFacesRequest.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        """Sets the face_set_name of this BatchDeleteFacesRequest.

        人脸库名称。

        :param face_set_name: The face_set_name of this BatchDeleteFacesRequest.
        :type face_set_name: str
        """
        self._face_set_name = face_set_name

    @property
    def body(self):
        """Gets the body of this BatchDeleteFacesRequest.

        :return: The body of this BatchDeleteFacesRequest.
        :rtype: :class:`huaweicloudsdkfrs.v2.DeleteFacesBatchReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchDeleteFacesRequest.

        :param body: The body of this BatchDeleteFacesRequest.
        :type body: :class:`huaweicloudsdkfrs.v2.DeleteFacesBatchReq`
        """
        self._body = body

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchDeleteFacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
