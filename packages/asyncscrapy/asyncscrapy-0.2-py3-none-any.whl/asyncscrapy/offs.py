

async def async_iterate_check(result, spider, Request, should_follow, urlparse_cached, domains_seen, logger, stats):
        async for x in result:
            if isinstance(x, Request):
                if x.dont_filter or should_follow(x, spider):
                    yield x
                else:
                    domain = urlparse_cached(x).hostname
                    if domain and domain not in domains_seen:
                        domains_seen.add(domain)
                        logger.debug("Filtered offsite request to %(domain)r: %(request)s",
                                     {'domain': domain, 'request': x}, extra={'spider': spider})
                        stats.inc_value('offsite/domains', spider=spider)
                    stats.inc_value('offsite/filtered', spider=spider)
            else:
                yield x
