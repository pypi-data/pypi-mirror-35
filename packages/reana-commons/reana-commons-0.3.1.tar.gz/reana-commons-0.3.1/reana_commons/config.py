# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# REANA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# REANA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.

"""REANA Commons configuration."""

import os

BROKER_URL = os.getenv('RABBIT_MQ_URL',
                       'message-broker.default.svc.cluster.local')
"""RabbitMQ server host name."""

BROKER_USER = os.getenv('RABBIT_MQ_USER', 'test')
"""RabbitMQ user name."""

BROKER_PASS = os.getenv('RABBIT_MQ_PASS', '1234')
"""RabbitMQ password."""

BROKER_PORT = os.getenv('RABBIT_MQ_PORT', 5672)
"""RabbitMQ service port."""

BROKER = os.getenv('RABBIT_MQ', 'amqp://{0}:{1}@{2}//'.format(BROKER_USER,
                                                              BROKER_PASS,
                                                              BROKER_URL))
"""RabbitMQ connection string."""

STATUS_QUEUE = 'jobs-status'
"""Name of the queue where to publish/consume from."""

EXCHANGE = ''
"""RabbitMQ exchange."""

ROUTING_KEY = 'jobs-status'
"""RabbitMQ routing key."""
