from __future__ import absolute_import
from flask import current_app, request
from flask_rq import job


def request_event_wrapper(on_event):
    def wrapper(fn):
        if request:
            @on_event
            def handler(response):
                fn()
                return response
            return handler
        return fn
    return wrapper


def _bool_callable(v):
    return v if callable(v) else lambda: v


def smart_job(func_or_queue='default', should_noop=False, allow_sync=True, on_event=None, **smart_job_kwargs):
    should_noop = _bool_callable(should_noop)
    allow_sync = _bool_callable(allow_sync)

    def inner(original_fn):
        wrapper = job(func_or_queue)
        if not callable(func_or_queue):
            wrapper = wrapper(original_fn)

        # We're going to replace this with a new function, but internally call the original one.
        real_delay = wrapper.delay

        def delay(*args, **kwargs):
            # Decide if we should run this job at all
            if should_noop():
                return

            def delay_fn():
                # We need these later on for RQ, but they shouldn't be passed to the function that's
                # being delayed when we're doing a synchronous call
                rq_kwargs = kwargs.pop('rq_kwargs', {})

                # Bypass RQ when appropriate
                if allow_sync() and current_app.config.get('RQ_SYNC_SMART_JOB', current_app.debug or current_app.testing):
                    return lambda: original_fn(*args, **kwargs)

                # Smart job kwargs first
                # Updated with the fn kwargs
                # Updated with rq_kwargs
                delay_kwargs = {}
                delay_kwargs.update(smart_job_kwargs)
                delay_kwargs.update(kwargs)
                delay_kwargs.update(rq_kwargs)

                return lambda: real_delay(*args, **delay_kwargs)

            fn = delay_fn()
            return on_event(fn) if on_event else fn()

        wrapper.delay = delay

        return wrapper

    # No decorator arguments (use the default behavior)
    if callable(func_or_queue):
        return inner(func_or_queue)

    return inner
