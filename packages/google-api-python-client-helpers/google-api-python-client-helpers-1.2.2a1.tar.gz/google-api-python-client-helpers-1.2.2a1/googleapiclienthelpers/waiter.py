import json
import time

import googleapiclient

__all__ = [
    'Waiter',
]


class Waiter(object):
    '''Wait for a resource to reach a desired state.

    This class implements a generic way to wait for an operation to
    reach a desired state.

    To use: create a new instance by providing a callable and the
    arguments that it requires.  Then, call wait() and the Waiter will
    poll the callable until the desired status is reached.

    The callable you pass must have a .execute() method, like the
    Resource objects returned by googleapiclient.

    For example, you might start an instance and wait until it reaches
    the RUNNING status:
    >>> instances = build_subresource('compute.instances', 'v1')
    >>> instances.insert(...)
    >>> waiter = Waiter(instances.get, project=..., zone=..., instance=...)
    >>> waiter.wait('status', 'RUNNING')

    '''
    def __init__(self, func, *args, **kargs):
        '''Construct a new Waiter

        Args:
          func: callable, the callable that returns the status.  Most
                of the time this will be a googleapiclient Resource method.
          *args: positional arguments to be passed to func.
          **kargs: keyword arguments to be passed to func.

        '''
        self.func = func
        self.args = args
        self.kargs = kargs

    def wait(self, field, value, retries=60, interval=2, not_found='fail'):
        '''Wait until an object reached the desired status

        When called, the Waiter will invoke the callable provided at
        construction and capture its return.  The Waiter extracts
        field, and checks if it's equal to value.  If it is, the full
        response from the callable is returned.

        In different circumstances, a 404 Not Found response from GCP
        can indicate different things.  The not_found parameter allows
        control over this.  For example:

          * By default, a 404 is treated as a failure.  If you expect
            a resource to exist before and after your waiting, this
            default is correct.  not_found should be set to 'fail'.

          * If you are waiting on a new resource to be created, you
            might get 404 before the resource can reach the desired
            state.  not_found should be set to 'ignore'.

          * If you are deleting a resource, a 404 might indicate that
            the removal is complete.  Since the resource is gone, a
            caller cannot receive a response.  In this case, not_found
            should be set to 'done'.

        wait() handles three kinds of field parameter:
          * dict-like return where field is a string that specified a key.
          * object-like return where field is a string naming an attribute.
          * any kind of return where field is a one-place callable that extracts
            the needed data to compare.

        Args:
          field: string or callable, the data to extract.
          value: varies, the value indicating the desired state.
          retries: int, maximum number of times to poll.
          interval: float, time to sleep between polls.

          not_found: string, specifies how to treat a 404 response
            from the Google API.  Acceptable values:
            * fail: allow the exception to be raised
            * ignore: assumes 404 is an okay response, suppresses the exception
              and continues waiting.
            * done: interprets 404 as a completion indicator, suppresses the
              exception and returns success.

        '''
        count = 0

        while count < retries:
            try:
                response = self.func(*self.args, **self.kargs).execute()
            except googleapiclient.errors.HttpError as e:
                if e.args[0]['status'] != '404' or not_found == 'fail':
                    raise

                # if control hits here, this is a 404 and the caller
                # asked for special handling
                if not_found == 'ignore':
                    time.sleep(interval)
                    count += 1
                    continue

                elif not_found == 'done':
                    return

            # field might be a dict key
            try:
                if response[field] == value:
                    return response
            except KeyError:
                pass

            # field might be an object attribute
            try:
                if getattr(response, field) == value:
                    return response
            except (AttributeError, TypeError):
                pass

            # field might be a callable that finds the right thing
            try:
                if field(response) == value:
                    return response
            except TypeError:
                pass

            # either the desired status hasn't been reached, or the
            # user passed something nonsensical as field/value
            time.sleep(interval)
            count += 1

        raise ValueError('Never received desired value %s' % value)
