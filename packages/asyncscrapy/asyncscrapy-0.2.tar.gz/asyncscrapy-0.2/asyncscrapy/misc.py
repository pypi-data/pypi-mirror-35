import asyncio

def async_comprehension(func=None, iterator, func2=None):
	if not func:
		if not func2:
			return (None)
		else:
			return (r async for r in iterator or () if func2)
	elif not func2:
		return(func(r) async for r in iterator or ())
	else:
		return(r async for r in iterator)