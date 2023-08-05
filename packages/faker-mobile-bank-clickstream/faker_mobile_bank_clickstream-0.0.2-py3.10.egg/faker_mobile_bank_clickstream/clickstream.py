import hashlib
import random
import string
from datetime import datetime, timedelta
from random import choice, randint

from faker.providers import BaseProvider

from faker_mobile_bank_clickstream.event_constants import weighted_events, events
from faker_mobile_bank_clickstream.ip import ip_list
from faker_mobile_bank_clickstream.user_agents import user_agents


class ClickstreamProvider(BaseProvider):
    """
        A Provider for clickstream related test data.

        >>> from faker import Faker
        >>> from faker_mobile_bank_clickstream import ClickstreamProvider
        >>> fake = Faker()
        >>> fake.add_provider(ClickstreamProvider)
        >>> fake.session_clickstream()
    """

    def user_agent(self):
        """
        Generate random user agent.

        :return: User agent string
        """
        return choice(user_agents)

    def event(self):
        """
        Generate random event type name for mobile banking app.

        :return: Event type string
        """
        return choice(events)

    def weighted_event(self):
        """
        Generate a random event object according to popularity weight. Higher popularity increases the
        chances of occurrence.

        :return: Event object (JSON)
        """
        return random.choices(weighted_events, weights=[e['popularity'] for e in weighted_events], k=1)[0]

    def session_clickstream(self, rand_session_max_size: int = 25):
        """
        Generate session clickstream events.

        :param rand_session_max_size: Max number of possible events in session. Defaults to 25.
        :return: List of session events
        """

        # Initialize static session values
        session_events = []
        user_id = _get_user_id()
        user_agent = self.user_agent()
        session_id = _get_session_id()
        ip = _get_ip()
        random_session_size = randint(1, rand_session_max_size)
        incremental_delta_delay = randint(1, 60)
        first_events = [e['name'] for e in weighted_events if e['dependsOn']==['Login']]

        print("Weighted events: ", weighted_events)
        print("First events: ", first_events)

        # Keep track of unique values in a session
        unique_session_events = set()

        for s in range(random_session_size):
            # Mock time delay between events
            incremental_delta_delay = incremental_delta_delay + (s * randint(1, 60))
            event_time = _format_time(_get_event_time(delta=incremental_delta_delay))

            # Fetch weighted event
            event = self.weighted_event()
            # First event should be Login event
            if len(unique_session_events)==0:
                event['name'] = 'Login'            

            if (event['name'] == 'Login' and event['name'] in unique_session_events):
                # or Login exists in session, discard Login event
                # Add a mock ViewHome event
                event['name'] = 'ViewHome'

            if event['name'] == 'Login' and user_id == 0:
                # If user id is -1 and Login event, regenerate user ID.
                user_id = _get_user_id(start=1)

            if (event['name'] == 'Login' and user_id != 0) or (event['name'] == 'Logout' and user_id == 0):
                # Add a mock ViewHome event
                event['name'] = 'ViewHome'

            # Keep track of unique events in session
            unique_session_events.add(event['name'])

            # Handle event dependencies
            if len(event['dependsOn']):
                list_check = [d in unique_session_events for d in event['dependsOn']]
                if event['dependencyFilter'] == 'all':
                    f = all(list_check)
                else:
                    f = any(list_check)
                if not f:
                    # Add a mock first_events event
                    event['name'] = random.choice(first_events)

            # Construct final event object
            r = {
                "ip": ip,
                "user_id": user_id,
                "user_agent": user_agent,
                "session_id": session_id,
                "event_time": event_time,
                "event_name": event['name']
            }
            session_events.append(r)
        return session_events


def _get_session_id():
    """
    Generate session ID

    :return: Session ID string
    """
    return hashlib.sha256(
        ('%s%s%s' % (
            datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f"),
            (''.join(random.choice(string.ascii_lowercase)) for _ in range(10)),
            'faker_clickstream'
        )).encode('utf-8')
    ).hexdigest()


def _get_user_id(start: int = 0, end: int = 999999):
    """
    Generate random user id from range 0 to 999999. Zero value may identify null user.

    :param start: Index start (Default: 0)
    :param end: Index end (Default: 999999)
    :return:
    """
    return randint(start, end)


def _get_event_time(delta):
    """
    Generate current event time, added by some delta value.

    :param delta: Delta time value in seconds
    :return: Event time
    """
    return datetime.now() + timedelta(seconds=delta)


def _format_time(t):
    """
    Format time to string.

    :param t: Time object
    :return: Time string in format like 28/03/2022 23:22:15.360252
    """
    return t.strftime("%d/%m/%Y %H:%M:%S.%f")


def _get_ip():
    """
    Get random IP address from list.

    :return: IP address string
    """
    return choice(ip_list)
