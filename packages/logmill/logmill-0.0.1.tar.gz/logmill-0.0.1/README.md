# Logmill

A single-library logging and eventing service.

# Notes (more current than below)

+ Could you statistically calculate query specificity based on the entire available dataset? I think you almost certainly could. You'd have to be careful to take the entire query -- including the input -- into account, so you couldn't, for example, do one query at a time to enumerate an entire userID. You'd probably also need to designate where specificity is important (examples: a 5-person dataset with each person from a unique country; a 100k loging.log() list with 2 instances of a particular critical message)
+ Percent formatting cpython source: _PyUnicode_Format https://github.com/python/cpython/blob/master/Objects/unicodeobject.c
+ Percent formatting pypy source: mod_format https://bitbucket.org/pypy/pypy/src/7967a85cf805f0258118591978a1ecbea1d10f0b/pypy/objspace/std/formatting.py?at=py3.5&fileviewer=file-view-default
+ https://blog.sentry.io/2018/03/14/gdpr-sentry-and-you
+ I'm almost positive (but not 100%) that the API I want is really a decorator. So if you wanted to replicate the logging API, in your project using logmill, you'd have something like:
@logmill.log
def debug(msg, *args, **kwargs):
pass
+ But how does that play with having a class -- more specifically, having something like automatic injection of kwargs into the logging call based on the module? You want, for example, to be able to have the module='foo.bar.baz' to be present in all of the module's logging statements, without needing to explicitly add them to each logging call
+ Need a generalized form of context variables -- not just stack traces! Think experiments. You want to be able to assign both a stack context **and** an experiment value, so that subsequent calls from that context still apply that experiment to the individual events that are actually logged
+ https://goaccess.io/faq
+ https://rt.goaccess.io/?20170228214800
+ https://docs.aws.amazon.com/AmazonS3/latest/dev/ListingKeysHierarchy.html
+ https://medium.com/@enjalot/the-hitchhikers-guide-to-d3-js-a8552174733a
+ https://oracleaide.wordpress.com/2015/08/21/dynamo-db-local-a-missing-tutorial-in-python/
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
+ https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control
+ https://www.html5rocks.com/en/tutorials/cors/#toc-adding-cors-support-to-the-server
+ https://stackoverflow.com/questions/581383/adding-custom-http-headers-using-javascript
+ https://blog.logrocket.com/rethinking-front-end-error-reporting-659db3950db3
+ https://bravenewgeek.com/building-a-distributed-log-from-scratch-part-3-scaling-message-delivery/
+ https://about.gitlab.com/2017/10/02/scaling-the-gitlab-database/
+ https://labs.spotify.com/2016/02/25/spotifys-event-delivery-the-road-to-the-cloud-part-i/

# Misc thoughts

+   Standardized terminology is important too
+   Uptime and health metrics are definitely important

From a business perspective:

+   What reliability requirements?
+   Better for duplicated events vs dropped events (better duplicated)

Joining on eg. user_id is important; other queries are great

Funnels are great too (that's a join on user_id)


Would it be possible to use AST manipulation to automatically instrument
every coroutine? You could automatically add a context variable into stuff.
This would, of course, be a lot easier to do if PEP 550/555 lands, and we
can just use context variables directly.

That would also make it more or less trivial to handle multiple different
kinds of event loop runners. HOWEVER, it's only going to work if you are
directly going up or down the call stack.

You could automatically do something like these replacements:

```python
async def foo(*args, **kwargs):
    await sleep(30)
```

converted to:

```python
async def foo(*args, _logrunner_context=None, **kwargs):
    if _logrunner_context is None:
        _logrunner_context = LogrunnerContext(foo)

    await sleep(30, _logrunner_context=_logrunner_context)
```

The difficulty here is going to be, hey, what if this is a C function call
or something, where we can't change the call signature.
