import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
