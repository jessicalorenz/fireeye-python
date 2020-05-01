# coding: utf-8

"""
    Helix API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fireeye.helix.configuration import Configuration


class InlineObject29(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'distinguisher_key': 'str',
        'classification': 'int',
        'closed_state': 'str',
        'kill_chain': 'list[str]',
        'message': 'str',
        'risk': 'str',
        'confidence': 'str',
        'alert_type': 'str',
        'last_event_at': 'str',
        'severity': 'str',
        'info_links': 'list[str]',
        'state': 'str',
        'events_threshold': 'int',
        'external_id': 'str',
        'is_tuned': 'bool',
        'trigger_revision': 'int',
        'customer_id': 'str',
        'is_hidden': 'bool',
        'origin_id': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'first_event_at': 'str',
        'threat_type': 'int',
        'distinguishers': 'str',
        'seconds_threshold': 'int',
        'trigger_id': 'str',
        'revision_notes': 'str',
        'emailed_at': 'int',
        'search': 'str',
        'last_sync_ms': 'int',
        'alert_threat': 'str',
        'tuning_search': 'str',
        'queues': 'list[str]',
        'source_revision': 'int'
    }

    attribute_map = {
        'distinguisher_key': 'distinguisherKey',
        'classification': 'classification',
        'closed_state': 'closedState',
        'kill_chain': 'killChain',
        'message': 'message',
        'risk': 'risk',
        'confidence': 'confidence',
        'alert_type': 'alertType',
        'last_event_at': 'lastEventAt',
        'severity': 'severity',
        'info_links': 'infoLinks',
        'state': 'state',
        'events_threshold': 'eventsThreshold',
        'external_id': 'externalId',
        'is_tuned': 'isTuned',
        'trigger_revision': 'triggerRevision',
        'customer_id': 'customer_id',
        'is_hidden': 'isHidden',
        'origin_id': 'originId',
        'description': 'description',
        'tags': 'tags',
        'first_event_at': 'firstEventAt',
        'threat_type': 'threatType',
        'distinguishers': 'distinguishers',
        'seconds_threshold': 'secondsThreshold',
        'trigger_id': 'triggerId',
        'revision_notes': 'revisionNotes',
        'emailed_at': 'emailedAt',
        'search': 'search',
        'last_sync_ms': 'lastSyncMs',
        'alert_threat': 'alertThreat',
        'tuning_search': 'tuningSearch',
        'queues': 'queues',
        'source_revision': 'sourceRevision'
    }

    def __init__(self, distinguisher_key=None, classification=None, closed_state=None, kill_chain=None, message=None, risk=None, confidence=None, alert_type=None, last_event_at=None, severity=None, info_links=None, state=None, events_threshold=None, external_id=None, is_tuned=None, trigger_revision=None, customer_id=None, is_hidden=None, origin_id=None, description=None, tags=None, first_event_at=None, threat_type=None, distinguishers=None, seconds_threshold=None, trigger_id=None, revision_notes=None, emailed_at=None, search=None, last_sync_ms=None, alert_threat=None, tuning_search=None, queues=None, source_revision=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject29 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._distinguisher_key = None
        self._classification = None
        self._closed_state = None
        self._kill_chain = None
        self._message = None
        self._risk = None
        self._confidence = None
        self._alert_type = None
        self._last_event_at = None
        self._severity = None
        self._info_links = None
        self._state = None
        self._events_threshold = None
        self._external_id = None
        self._is_tuned = None
        self._trigger_revision = None
        self._customer_id = None
        self._is_hidden = None
        self._origin_id = None
        self._description = None
        self._tags = None
        self._first_event_at = None
        self._threat_type = None
        self._distinguishers = None
        self._seconds_threshold = None
        self._trigger_id = None
        self._revision_notes = None
        self._emailed_at = None
        self._search = None
        self._last_sync_ms = None
        self._alert_threat = None
        self._tuning_search = None
        self._queues = None
        self._source_revision = None
        self.discriminator = None

        if distinguisher_key is not None:
            self.distinguisher_key = distinguisher_key
        if classification is not None:
            self.classification = classification
        if closed_state is not None:
            self.closed_state = closed_state
        if kill_chain is not None:
            self.kill_chain = kill_chain
        if message is not None:
            self.message = message
        if risk is not None:
            self.risk = risk
        if confidence is not None:
            self.confidence = confidence
        if alert_type is not None:
            self.alert_type = alert_type
        if last_event_at is not None:
            self.last_event_at = last_event_at
        if severity is not None:
            self.severity = severity
        if info_links is not None:
            self.info_links = info_links
        if state is not None:
            self.state = state
        if events_threshold is not None:
            self.events_threshold = events_threshold
        if external_id is not None:
            self.external_id = external_id
        if is_tuned is not None:
            self.is_tuned = is_tuned
        if trigger_revision is not None:
            self.trigger_revision = trigger_revision
        if customer_id is not None:
            self.customer_id = customer_id
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if origin_id is not None:
            self.origin_id = origin_id
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if first_event_at is not None:
            self.first_event_at = first_event_at
        if threat_type is not None:
            self.threat_type = threat_type
        if distinguishers is not None:
            self.distinguishers = distinguishers
        if seconds_threshold is not None:
            self.seconds_threshold = seconds_threshold
        if trigger_id is not None:
            self.trigger_id = trigger_id
        if revision_notes is not None:
            self.revision_notes = revision_notes
        if emailed_at is not None:
            self.emailed_at = emailed_at
        if search is not None:
            self.search = search
        if last_sync_ms is not None:
            self.last_sync_ms = last_sync_ms
        if alert_threat is not None:
            self.alert_threat = alert_threat
        if tuning_search is not None:
            self.tuning_search = tuning_search
        if queues is not None:
            self.queues = queues
        if source_revision is not None:
            self.source_revision = source_revision

    @property
    def distinguisher_key(self):
        """Gets the distinguisher_key of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The distinguisher_key of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._distinguisher_key

    @distinguisher_key.setter
    def distinguisher_key(self, distinguisher_key):
        """Sets the distinguisher_key of this InlineObject29.

          # noqa: E501

        :param distinguisher_key: The distinguisher_key of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._distinguisher_key = distinguisher_key

    @property
    def classification(self):
        """Gets the classification of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The classification of this InlineObject29.  # noqa: E501
        :rtype: int
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this InlineObject29.

          # noqa: E501

        :param classification: The classification of this InlineObject29.  # noqa: E501
        :type: int
        """

        self._classification = classification

    @property
    def closed_state(self):
        """Gets the closed_state of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The closed_state of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._closed_state

    @closed_state.setter
    def closed_state(self, closed_state):
        """Sets the closed_state of this InlineObject29.

          # noqa: E501

        :param closed_state: The closed_state of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._closed_state = closed_state

    @property
    def kill_chain(self):
        """Gets the kill_chain of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The kill_chain of this InlineObject29.  # noqa: E501
        :rtype: list[str]
        """
        return self._kill_chain

    @kill_chain.setter
    def kill_chain(self, kill_chain):
        """Sets the kill_chain of this InlineObject29.

          # noqa: E501

        :param kill_chain: The kill_chain of this InlineObject29.  # noqa: E501
        :type: list[str]
        """

        self._kill_chain = kill_chain

    @property
    def message(self):
        """Gets the message of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The message of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineObject29.

          # noqa: E501

        :param message: The message of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def risk(self):
        """Gets the risk of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The risk of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this InlineObject29.

          # noqa: E501

        :param risk: The risk of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._risk = risk

    @property
    def confidence(self):
        """Gets the confidence of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The confidence of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this InlineObject29.

          # noqa: E501

        :param confidence: The confidence of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._confidence = confidence

    @property
    def alert_type(self):
        """Gets the alert_type of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The alert_type of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this InlineObject29.

          # noqa: E501

        :param alert_type: The alert_type of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._alert_type = alert_type

    @property
    def last_event_at(self):
        """Gets the last_event_at of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The last_event_at of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._last_event_at

    @last_event_at.setter
    def last_event_at(self, last_event_at):
        """Sets the last_event_at of this InlineObject29.

          # noqa: E501

        :param last_event_at: The last_event_at of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._last_event_at = last_event_at

    @property
    def severity(self):
        """Gets the severity of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The severity of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this InlineObject29.

          # noqa: E501

        :param severity: The severity of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def info_links(self):
        """Gets the info_links of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The info_links of this InlineObject29.  # noqa: E501
        :rtype: list[str]
        """
        return self._info_links

    @info_links.setter
    def info_links(self, info_links):
        """Sets the info_links of this InlineObject29.

          # noqa: E501

        :param info_links: The info_links of this InlineObject29.  # noqa: E501
        :type: list[str]
        """

        self._info_links = info_links

    @property
    def state(self):
        """Gets the state of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The state of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineObject29.

          # noqa: E501

        :param state: The state of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def events_threshold(self):
        """Gets the events_threshold of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The events_threshold of this InlineObject29.  # noqa: E501
        :rtype: int
        """
        return self._events_threshold

    @events_threshold.setter
    def events_threshold(self, events_threshold):
        """Sets the events_threshold of this InlineObject29.

          # noqa: E501

        :param events_threshold: The events_threshold of this InlineObject29.  # noqa: E501
        :type: int
        """

        self._events_threshold = events_threshold

    @property
    def external_id(self):
        """Gets the external_id of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The external_id of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this InlineObject29.

          # noqa: E501

        :param external_id: The external_id of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def is_tuned(self):
        """Gets the is_tuned of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The is_tuned of this InlineObject29.  # noqa: E501
        :rtype: bool
        """
        return self._is_tuned

    @is_tuned.setter
    def is_tuned(self, is_tuned):
        """Sets the is_tuned of this InlineObject29.

          # noqa: E501

        :param is_tuned: The is_tuned of this InlineObject29.  # noqa: E501
        :type: bool
        """

        self._is_tuned = is_tuned

    @property
    def trigger_revision(self):
        """Gets the trigger_revision of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The trigger_revision of this InlineObject29.  # noqa: E501
        :rtype: int
        """
        return self._trigger_revision

    @trigger_revision.setter
    def trigger_revision(self, trigger_revision):
        """Sets the trigger_revision of this InlineObject29.

          # noqa: E501

        :param trigger_revision: The trigger_revision of this InlineObject29.  # noqa: E501
        :type: int
        """

        self._trigger_revision = trigger_revision

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject29.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject29.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject29.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject29.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def origin_id(self):
        """Gets the origin_id of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The origin_id of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._origin_id

    @origin_id.setter
    def origin_id(self, origin_id):
        """Sets the origin_id of this InlineObject29.

          # noqa: E501

        :param origin_id: The origin_id of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._origin_id = origin_id

    @property
    def description(self):
        """Gets the description of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject29.

          # noqa: E501

        :param description: The description of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The tags of this InlineObject29.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject29.

          # noqa: E501

        :param tags: The tags of this InlineObject29.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def first_event_at(self):
        """Gets the first_event_at of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The first_event_at of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._first_event_at

    @first_event_at.setter
    def first_event_at(self, first_event_at):
        """Sets the first_event_at of this InlineObject29.

          # noqa: E501

        :param first_event_at: The first_event_at of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._first_event_at = first_event_at

    @property
    def threat_type(self):
        """Gets the threat_type of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The threat_type of this InlineObject29.  # noqa: E501
        :rtype: int
        """
        return self._threat_type

    @threat_type.setter
    def threat_type(self, threat_type):
        """Sets the threat_type of this InlineObject29.

          # noqa: E501

        :param threat_type: The threat_type of this InlineObject29.  # noqa: E501
        :type: int
        """

        self._threat_type = threat_type

    @property
    def distinguishers(self):
        """Gets the distinguishers of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The distinguishers of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._distinguishers

    @distinguishers.setter
    def distinguishers(self, distinguishers):
        """Sets the distinguishers of this InlineObject29.

          # noqa: E501

        :param distinguishers: The distinguishers of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._distinguishers = distinguishers

    @property
    def seconds_threshold(self):
        """Gets the seconds_threshold of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The seconds_threshold of this InlineObject29.  # noqa: E501
        :rtype: int
        """
        return self._seconds_threshold

    @seconds_threshold.setter
    def seconds_threshold(self, seconds_threshold):
        """Sets the seconds_threshold of this InlineObject29.

          # noqa: E501

        :param seconds_threshold: The seconds_threshold of this InlineObject29.  # noqa: E501
        :type: int
        """

        self._seconds_threshold = seconds_threshold

    @property
    def trigger_id(self):
        """Gets the trigger_id of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The trigger_id of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this InlineObject29.

          # noqa: E501

        :param trigger_id: The trigger_id of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._trigger_id = trigger_id

    @property
    def revision_notes(self):
        """Gets the revision_notes of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The revision_notes of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._revision_notes

    @revision_notes.setter
    def revision_notes(self, revision_notes):
        """Sets the revision_notes of this InlineObject29.

          # noqa: E501

        :param revision_notes: The revision_notes of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._revision_notes = revision_notes

    @property
    def emailed_at(self):
        """Gets the emailed_at of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The emailed_at of this InlineObject29.  # noqa: E501
        :rtype: int
        """
        return self._emailed_at

    @emailed_at.setter
    def emailed_at(self, emailed_at):
        """Sets the emailed_at of this InlineObject29.

          # noqa: E501

        :param emailed_at: The emailed_at of this InlineObject29.  # noqa: E501
        :type: int
        """

        self._emailed_at = emailed_at

    @property
    def search(self):
        """Gets the search of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The search of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this InlineObject29.

          # noqa: E501

        :param search: The search of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._search = search

    @property
    def last_sync_ms(self):
        """Gets the last_sync_ms of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The last_sync_ms of this InlineObject29.  # noqa: E501
        :rtype: int
        """
        return self._last_sync_ms

    @last_sync_ms.setter
    def last_sync_ms(self, last_sync_ms):
        """Sets the last_sync_ms of this InlineObject29.

          # noqa: E501

        :param last_sync_ms: The last_sync_ms of this InlineObject29.  # noqa: E501
        :type: int
        """

        self._last_sync_ms = last_sync_ms

    @property
    def alert_threat(self):
        """Gets the alert_threat of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The alert_threat of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._alert_threat

    @alert_threat.setter
    def alert_threat(self, alert_threat):
        """Sets the alert_threat of this InlineObject29.

          # noqa: E501

        :param alert_threat: The alert_threat of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._alert_threat = alert_threat

    @property
    def tuning_search(self):
        """Gets the tuning_search of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The tuning_search of this InlineObject29.  # noqa: E501
        :rtype: str
        """
        return self._tuning_search

    @tuning_search.setter
    def tuning_search(self, tuning_search):
        """Sets the tuning_search of this InlineObject29.

          # noqa: E501

        :param tuning_search: The tuning_search of this InlineObject29.  # noqa: E501
        :type: str
        """

        self._tuning_search = tuning_search

    @property
    def queues(self):
        """Gets the queues of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The queues of this InlineObject29.  # noqa: E501
        :rtype: list[str]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this InlineObject29.

          # noqa: E501

        :param queues: The queues of this InlineObject29.  # noqa: E501
        :type: list[str]
        """

        self._queues = queues

    @property
    def source_revision(self):
        """Gets the source_revision of this InlineObject29.  # noqa: E501

          # noqa: E501

        :return: The source_revision of this InlineObject29.  # noqa: E501
        :rtype: int
        """
        return self._source_revision

    @source_revision.setter
    def source_revision(self, source_revision):
        """Sets the source_revision of this InlineObject29.

          # noqa: E501

        :param source_revision: The source_revision of this InlineObject29.  # noqa: E501
        :type: int
        """

        self._source_revision = source_revision

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject29):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject29):
            return True

        return self.to_dict() != other.to_dict()