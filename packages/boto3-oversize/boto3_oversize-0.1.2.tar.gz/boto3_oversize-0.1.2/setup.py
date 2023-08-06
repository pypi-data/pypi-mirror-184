# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boto3_oversize', 'boto3_oversize.tests']

package_data = \
{'': ['*']}

install_requires = \
['boto3-stubs[s3,sns,sqs]>=1.20.30', 'boto3>=1.20.30']

setup_kwargs = {
    'name': 'boto3-oversize',
    'version': '0.1.2',
    'description': 'Transparently stores oversize SNS messages in S3 and retrieves them when receiving messages using SQS.',
    'long_description': "boto3-oversize\n==============\n\nMessages published using Amazon SNS have a [maximum size of 256KiB](https://aws.amazon.com/about-aws/whats-new/2013/06/18/amazon-sqs-announces-256KB-large-payloads/),\nwhich can be a limitation for certain use cases. AWS provides an\n[extended client library for Java](https://aws.amazon.com/about-aws/whats-new/2020/08/amazon-sns-launches-client-library-supporting-message-payloads-of-up-to-2-gb/)\nthat transparently uploads messages exceeding this threshold to S3 and restores them when the\nmessages are received. This Python package provides the same functionality for\n[boto3](https://aws.amazon.com/sdk-for-python/).\n\n## Installation\n\n1. Create an Amazon S3 bucket that will store message payloads that exceed the maximum size.\n   * While the Java library deletes payloads from S3 when they are retrieved, this is not\n     appropriate when there are multiple subscribers to the topic. Instead, apply a\n     [S3 lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)\n     to expire the message payloads after a reasonable length of time, e.g., 14 days.\n2. Install this package, e.g., `pip install boto3-oversize`.\n3. Define the `OVERSIZE_PAYLOAD_BUCKET_NAME` environment variable as the name of the bucket you created;\n   ensure your AWS access credentials have permission to call `PutObject` and `GetObject` in the\n   root of the bucket.\n\n## Usage\n\nThe library provides replacement implementations of the core boto3 entry points that transparently\napply the necessary changes to the SNS and SQS clients, both for the low-level client and service\nresource. Simply reference `boto3_oversize` instead of `boto3`.\n\n### Low-level client example\n\n```python\nimport boto3_oversize\n\nsns_client = boto3_oversize.client('sns')\nresponse = sns_client.create_topic(Name='example-large-payload-topic')\nsns_client.publish(TopicArn=response['TopicArn'], Message='example-message')\n```\n\n### Service resource example\n\n```python\nimport boto3_oversize\n\nsqs_client = boto3_oversize.resource('sqs')\nqueue = sqs_client.create_queue(QueueName='example-large-payload-queue')\nmessages = queue.receive_messages()\n```\n\n## Implementation\n\nCalls to publish messages are intercepted and the message body sized check against the limit,\nreduced by a small percentage to consider SNS message envelope overhead if raw message delivery is\nnot enabled. If the message exceeds this threshold, it is uploaded to an S3 bucket and the SNS\nmessage replaced with the object ARN.\n\nWhen receiving messages, the SQS client checks if the entire message body appears to be an S3 object\nARN. If it is, the object is retrieved from S3 and returned to the caller as the message body.\n",
    'author': 'roberthl',
    'author_email': 'roberthl@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
