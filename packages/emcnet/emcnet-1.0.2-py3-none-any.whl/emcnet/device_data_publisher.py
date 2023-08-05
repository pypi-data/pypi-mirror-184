import argparse
import paho.mqtt.client as mqtt
import json
import time
from _collections import OrderedDict
import sys
import logging
from dotenv import load_dotenv
import os

log = logging.getLogger(__name__)


class MQTTDeviceDataPublisher:

    def __init__(self, site_id="defaultsite", mqttbrokeraddress='localhost', mqttbrokerport=1883,
                 device_id="defaultdeviceid"):
        """ Instantiate an MQTT client and start it

        Args:
            site_id (str): Site ID
            mqttbrokeraddress (str): MQTT broker address
            mqttbrokerport (int): MQTT broker port
            device_id (str): Device ID
        """
        self.site_id = site_id.lstrip('/').rstrip('/')
        self.client = mqtt.Client()
        self.client.connect(mqttbrokeraddress, mqttbrokerport, 60)
        self.client.loop_start()
        self.topic = "emcnet/devicedata/" + site_id + "/" + device_id
        log.info(f"MQTT Device Data Publisher to {mqttbrokeraddress}:{mqttbrokerport}, Topic: {self.topic}")


    def publish(self, payload):
        """
        Publish device data to MQTT broker on self.topic.
        This method publishes a record that conforms to the EMCNet standard, payload should be a JSON-formatted string.
        The name-value pairs will be published in the following format.
            "ts": (optional) timestamp in seconds since epoch
            "data: a separate JSON object containing a list of field-name value pairs

        Args:
            payload: data record to publish (see above)
        """
        log.debug(f"Received: {payload}")
        if isinstance(payload, str):
            line = payload.strip()
            try:
                payload = json.loads(line)
            except json.decoder.JSONDecodeError:
                log.error("JSON decode error.")
                return
        if isinstance(payload, dict):
            ts = payload.pop('ts', time.time())
            subtopic = payload.pop('table', None)
            payload_ordered = OrderedDict([('ts', ts), ('data', payload)])
            payload_str = json.dumps(payload_ordered)
            topic = self.topic.rstrip('/')
            if subtopic is not None:
                topic = topic + '/' + str(subtopic)
            self.client.publish(topic, payload_str)
            log.debug(f"Sent on topic {topic}: {payload_str}")
        else:
            log.error(f"Unsupported payload type: {payload!r}")

    def run(self):
        """ Continuously read data records from stdin in JSON format and publish to MQTT broker
        """
        while True:
            # See see https://stackoverflow.com/questions/26677389/python-stdin-readline-blocks
            line = sys.stdin.readline()  # blocking
            if line is not None:
                if line:
                    self.publish(line)
            time.sleep(0.1)


def main():
    # set the default path to the EMCNET directory - from the environment if set
    emcnetdir = os.getenv("EMCNETDIR", './').rstrip('/')
    load_dotenv(emcnetdir + '/config.env', override=True)
    # read command-line arguments and override environment variables if given
    parser = argparse.ArgumentParser(description=(
        'MPPT Publisher - listens for device messages (lines) on stdin and sends them to the MQTT broker'))
    parser.add_argument('--site_id', type=str, default=os.getenv("SITE_ID", 'defaultsiteid'), help='Site ID')
    parser.add_argument('--mqttbrokeraddress', help='MQTT broker address', type=str,
                        default=os.getenv("MQTT_BROKER_ADDRESS", 'localhost'))
    parser.add_argument('--mqttbrokerport', help='MQTT broker port', type=int,
                        default=os.getenv("MQTT_BROKER_PORT", 1883))
    parser.add_argument('--loglevel', help='logging level one of [DEBUG, INFO, WARNING, ERROR, CRITICAL]',
                        default=os.getenv("LOG_LEVEL", 'INFO'))
    parser.add_argument('--device_id', help='Device ID', type=str, default='defaultdeviceid')

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper())
    log.info("MPPT Publisher - listens for messages (lines) on stdin and sends them to the MQTT broker")
    log.info(f"EMCNet directory: {emcnetdir}")
    log.info(f"Broker: {args.mqttbrokeraddress}:{args.mqttbrokerport}")
    log.info(f"Site ID: {args.site_id}, Device ID: {args.device_id}")
    ddp = MQTTDeviceDataPublisher(site_id=args.site_id, mqttbrokeraddress=args.mqttbrokeraddress, mqttbrokerport=args.mqttbrokerport,
                                  device_id=args.device_id)
    ddp.run()


if __name__ == '__main__':
    main()
